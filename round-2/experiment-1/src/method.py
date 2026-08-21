#!/usr/bin/env python3
"""
OSS Survival Experiment: Test Knowledge Redundancy Inverted-U Hypothesis

This experiment tests whether moderate knowledge redundancy (KR) optimizes
open-source project survival after founder departure, using survival analysis.

FALLBACK APPROACH: Using file_count as PROXY for knowledge redundancy since
dataset lacks file paths needed for Jaccard similarity. Computes 'pseudo-KR'
based on file count distribution patterns across contributors.

Methodology based on:
- Avelino et al. (2019) for founder departure (12-month threshold) and survival
- Pseudo-KR using cosine similarity of file_count distributions
- Cox proportional hazards model for survival analysis
"""

from loguru import logger
from pathlib import Path
import json
import sys
import gc
import os
import resource
import numpy as np
import pandas as pd
from itertools import combinations
from datetime import datetime, timedelta
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

# Configure logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Set memory limits (conservative: 8GB)
import psutil
_avail = psutil.virtual_memory().available
RAM_BUDGET = min(6 * 1024**3, _avail * 0.7)  # 6GB or 70% of available
resource.setrlimit(resource.RLIMIT_AS, (int(RAM_BUDGET * 1.5), int(RAM_BUDGET * 1.5)))


def setup_environment():
    """Setup output directories."""
    Path("logs").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)
    logger.info("Environment setup complete")


def load_dataset(file_paths):
    """Load and combine dataset from multiple JSON files."""
    all_examples = []

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            logger.warning(f"File not found: {file_path}")
            continue

        logger.info(f"Loading {file_path}")
        with open(path, 'r') as f:
            data = json.load(f)

        # Extract examples from datasets format
        if 'datasets' in data:
            for dataset in data['datasets']:
                if 'examples' in dataset:
                    all_examples.extend(dataset['examples'])
        elif 'examples' in data:
            all_examples.extend(data['examples'])

    logger.info(f"Loaded {len(all_examples)} total examples")
    return all_examples


def parse_examples(examples):
    """Parse examples into structured format."""
    parsed = []

    for ex in examples:
        try:
            # Parse input JSON
            input_data = json.loads(ex['input'])

            # Extract fields
            record = {
                'repo_id': input_data.get('repo_id', ''),
                'repo_name': input_data.get('repo_name', ''),
                'author_login': input_data.get('author_login', ''),
                'is_founder': input_data.get('is_founder', False),
                'file_count': input_data.get('file_count', 0),
                'commit_sequence_num': input_data.get('commit_sequence_num', 0),
                'author_total_commits': input_data.get('author_total_commits', 0),
                'repo_total_commits': input_data.get('repo_total_commits', 0),
                'commit_timestamp': input_data.get('commit_timestamp', ''),
                'commit_sha': ex.get('metadata_commit_sha', ''),
                'output': ex.get('output', ''),
            }

            # Parse timestamp
            if record['commit_timestamp']:
                try:
                    # Handle ISO format with timezone
                    ts = record['commit_timestamp'].replace('Z', '+00:00')
                    record['datetime'] = datetime.fromisoformat(ts)
                except:
                    record['datetime'] = None

            parsed.append(record)

        except Exception as e:
            logger.debug(f"Failed to parse example: {e}")
            continue

    logger.info(f"Parsed {len(parsed)} valid records")
    return parsed


def group_by_repo(records):
    """Group records by repository."""
    repos = defaultdict(list)
    for record in records:
        repos[record['repo_id']].append(record)

    # Sort each repo's records by timestamp
    for repo_id in repos:
        repos[repo_id] = sorted(
            [r for r in repos[repo_id] if r.get('datetime')],
            key=lambda x: x['datetime']
        )

    logger.info(f"Grouped into {len(repos)} repositories")
    return repos


def identify_founder(repo_records):
    """Identify founder using multiple methods."""
    if not repo_records:
        return None

    # Method 1: Use is_founder flag if available
    founders = [r for r in repo_records if r.get('is_founder')]
    if founders:
        return founders[0]['author_login']

    # Method 2: Earliest commit author (first commit)
    if repo_records:
        return repo_records[0]['author_login']

    return None


def detect_founder_departure(repo_records, founder, departure_threshold_months=12):
    """Detect founder departure using Avelino et al. threshold.
    
    Also checks if there's a significant gap in founder's contributions,
    not just complete stop.
    """
    if not founder or not repo_records:
        return None, None

    # Get founder's commits
    founder_commits = [r for r in repo_records if r['author_login'] == founder]
    if not founder_commits:
        return None, None

    # Sort by timestamp
    founder_commits = sorted(founder_commits, key=lambda x: x['datetime'])

    # Last commit by founder
    last_commit = founder_commits[-1]
    last_commit_date = last_commit['datetime']

    # Check if 12+ months since last founder commit
    departure_threshold = last_commit_date + timedelta(days=departure_threshold_months * 30)

    # Get repo's last commit date
    repo_last_commit = max(r['datetime'] for r in repo_records)

    # Also check: is there a 6+ month gap in founder's contributions before the last commit?
    # This captures "reduced activity" departures
    if len(founder_commits) >= 2:
        gaps = []
        for i in range(1, len(founder_commits)):
            gap_days = (founder_commits[i]['datetime'] - founder_commits[i-1]['datetime']).days
            gaps.append(gap_days)
        
        max_gap = max(gaps)
        if max_gap >= 180:  # 6+ month gap
            # Find the date of the gap
            for i in range(1, len(founder_commits)):
                if (founder_commits[i]['datetime'] - founder_commits[i-1]['datetime']).days >= 180:
                    gap_date = founder_commits[i-1]['datetime']
                    # Use gap date as departure if it's earlier than last commit
                    if gap_date < last_commit_date:
                        logger.info(f"Founder gap departure detected: {gap_date}")
                        return founder, gap_date

    if repo_last_commit > departure_threshold:
        # Founder has been gone for 12+ months
        return founder, last_commit_date
    else:
        # Founder still active or recently active
        return None, None


def compute_pseudo_kr(repo_records, founder, departure_date, time_window_months=24, max_commits=5000):
    """Compute pseudo-Knowledge Redundancy using file_count patterns.

    Since we don't have file paths for Jaccard similarity, we use file_count
    distributions as a proxy. This measures the similarity in file modification
    patterns across contributors.

    Approach:
    1. Get top contributors (excluding founder post-departure)
    2. For each contributor, compute distribution of file_counts
    3. Compute pairwise similarity using cosine similarity of distributions
    4. Average to get project-level KR
    
    Args:
        max_commits: Maximum number of commits to use (sample if more)
    """
    if not departure_date or not repo_records:
        return None, None

    # Define time window before departure
    window_start = departure_date - timedelta(days=time_window_months * 30)

    # Get commits in time window
    window_commits = [
        r for r in repo_records
        if window_start <= r['datetime'] <= departure_date
    ]

    if not window_commits:
        return None, None
    
    # LIMIT COMMITS for performance (sample if too many)
    if len(window_commits) > max_commits:
        logger.info(f"Sampling {max_commits} from {len(window_commits)} commits for performance")
        import random
        random.seed(42)
        window_commits = random.sample(window_commits, max_commits)

    # Get top contributors by commit count (exclude founder post-departure)
    contributor_commits = defaultdict(list)
    for commit in window_commits:
        author = commit['author_login']
        if author == founder:
            # Only include founder commits before departure
            if commit['datetime'] <= departure_date:
                contributor_commits[author].append(commit)
        else:
            contributor_commits[author].append(commit)

    # Keep top 5 contributors
    top_contributors = sorted(
        contributor_commits.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )[:5]

    if len(top_contributors) < 2:
        return None, None

    # Compute file_count distributions for each contributor
    contributor_distributions = {}
    for author, commits in top_contributors:
        file_counts = [c['file_count'] for c in commits if c['file_count'] > 0]
        if file_counts:
            # Create histogram (distribution) of file counts
            hist, _ = np.histogram(file_counts, bins=10, range=(0, max(file_counts)))
            contributor_distributions[author] = hist

    # Compute pairwise cosine similarity
    similarities = []
    for (auth1, dist1), (auth2, dist2) in combinations(contributor_distributions.items(), 2):
        # Cosine similarity
        dot_product = np.dot(dist1, dist2)
        norm1 = np.linalg.norm(dist1)
        norm2 = np.linalg.norm(dist2)

        if norm1 > 0 and norm2 > 0:
            sim = dot_product / (norm1 * norm2)
            similarities.append(sim)

    if not similarities:
        return None, None

    # Average pairwise similarity = Knowledge Redundancy
    kr = np.mean(similarities)
    kr_squared = kr ** 2

    return kr, kr_squared


def measure_survival(repo_records, departure_date, founder, observation_end_date=None):
    """Measure project survival after founder departure.

    Uses Avelino et al. (2019) TFDD definition:
    - Survives if new contributors join and project continues
    - More robust: check for commits 3+ months after departure

    Returns:
    - survived: binary (1 if survived, 0 if not)
    - survival_time: days from departure to first post-departure commit by NON-FOUNDER
    - censored: whether survival time is censored
    """
    if not departure_date or not repo_records or not founder:
        return None, None, None

    if observation_end_date is None:
        observation_end_date = max(r['datetime'] for r in repo_records)

    # Get commits 3+ months after departure by NON-FOUNDER contributors
    # This gives time for the project to actually "die" if it will
    three_months_after = departure_date + timedelta(days=90)
    
    post_departure = [
        r for r in repo_records
        if r['datetime'] > three_months_after and r['author_login'] != founder
    ]

    if not post_departure:
        # No post-departure commits by others after 3 months = did not survive
        # Censored at observation end
        survival_time = (observation_end_date - departure_date).days
        return 0, survival_time, 1

    # Sort by timestamp
    post_departure = sorted(post_departure, key=lambda x: x['datetime'])
    first_post_commit = post_departure[0]['datetime']

    # Project survived - compute time to first non-founder commit (from departure)
    all_post_departure = [
        r for r in repo_records
        if r['datetime'] > departure_date and r['author_login'] != founder
    ]
    all_post_departure = sorted(all_post_departure, key=lambda x: x['datetime'])
    
    if all_post_departure:
        survival_time = (all_post_departure[0]['datetime'] - departure_date).days
    else:
        survival_time = (observation_end_date - departure_date).days

    return 1, survival_time, 0


def compute_control_variables(repo_records, founder, departure_date):
    """Compute control variables for survival analysis."""
    if not repo_records:
        return {}

    # Project age at departure
    repo_created = min(r['datetime'] for r in repo_records)
    age_days = (departure_date - repo_created).days if departure_date else 0

    # Contributor count
    contributors = set(r['author_login'] for r in repo_records if r['datetime'] <= departure_date)
    contributor_count = len(contributors)

    # Total commits pre-departure
    pre_departure_commits = len([r for r in repo_records if r['datetime'] <= departure_date])

    # Bus factor approximation (simplified)
    # Using Avelino's insight: if top contributor has >50% commits, bus factor = 1
    commit_counts = defaultdict(int)
    for r in repo_records:
        if r['datetime'] <= departure_date:
            commit_counts[r['author_login']] += 1

    if commit_counts:
        max_contributions = max(commit_counts.values())
        bus_factor = 1 if max_contributions > pre_departure_commits * 0.5 else 2
    else:
        bus_factor = 1

    return {
        'project_age_days': age_days,
        'contributor_count': contributor_count,
        'total_commits_pre': pre_departure_commits,
        'bus_factor': bus_factor,
    }


def run_survival_analysis(results_df):
    """Run Cox proportional hazards model to test inverted-U hypothesis.

    H0: KR^2 coefficient = 0 (no inverted-U)
    H1: KR^2 coefficient < 0 (inverted-U: moderate KR optimal)
    """
    try:
        from lifelines import CoxPHFitter
        from lifelines.utils import concordance_index

        logger.info("Running Cox proportional hazards model...")

        # Prepare data
        df = results_df.copy()

        # Remove rows with missing data
        df = df.dropna(subset=['survival_time', 'survived', 'kr', 'kr_squared'])

        if len(df) < 10:
            logger.warning("Insufficient data for Cox model")
            return None

        # Fit Cox model
        # Formula: survival_time ~ KR + KR^2 + controls
        cph = CoxPHFitter(penalizer=0.01)  # Small penalty for stability

        # Prepare covariates
        covariates = ['kr', 'kr_squared', 'bus_factor', 'contributor_count', 'project_age_days']
        X = df[covariates].copy()
        X = X.apply(pd.to_numeric, errors='coerce')

        T = df['survival_time'].values
        E = df['survived'].values

        cph.fit(X, duration_col=None, event_col=None, T=T, E=E)

        # Extract results
        results = {
            'cox_model_summary': cph.summary.to_dict() if hasattr(cph, 'summary') else {},
            'kr_coef': cph.params_['kr'] if 'kr' in cph.params_ else None,
            'kr_squared_coef': cph.params_['kr_squared'] if 'kr_squared' in cph.params_ else None,
            'kr_squared_p_value': cph.summary.loc['kr_squared', 'p'] if 'kr_squared' in cph.summary.index else None,
            'hazard_ratios': {k: np.exp(v) for k, v in cph.params_.items()},
            'concordance': cph.concordance_index_,
        }

        # Test inverted-U: KR^2 coefficient should be negative
        kr2_coef = results.get('kr_squared_coef')
        kr2_p = results.get('kr_squared_p_value')

        if kr2_coef is not None and kr2_p is not None:
            results['inverted_u_supported'] = kr2_coef < 0 and kr2_p < 0.05
            results['inverted_u_direction'] = 'negative' if kr2_coef < 0 else 'positive'

        logger.info(f"Cox model complete. Concordance: {results.get('concordance', 'N/A')}")
        logger.info(f"KR^2 coefficient: {kr2_coef:.4f}, p-value: {kr2_p:.4f}")

        return results

    except ImportError:
        logger.error("lifelines not installed. Cannot run Cox model.")
        return None
    except Exception as e:
        logger.error(f"Cox model failed: {e}")
        return None


def run_kaplan_meier(results_df):
    """Run Kaplan-Meier survival curves with log-rank test."""
    try:
        from lifelines import KaplanMeierFitter
        from lifelines.statistics import logrank_test

        logger.info("Running Kaplan-Meier analysis...")

        df = results_df.copy()
        df = df.dropna(subset=['survival_time', 'survived', 'kr'])

        if len(df) < 10:
            return None

        # Create KR tertiles
        df['kr_tertile'] = pd.qcut(df['kr'], q=3, labels=['low', 'medium', 'high'])

        km_results = {}

        # Fit KM for each tertile
        for tertile in ['low', 'medium', 'high']:
            subset = df[df['kr_tertile'] == tertile]
            if len(subset) < 3:
                continue

            kmf = KaplanMeierFitter()
            kmf.fit(subset['survival_time'], event_observed=subset['survived'])

            km_results[tertile] = {
                'survival_function': kmf.survival_function_.to_dict(),
                'median_survival_time': kmf.median_survival_time_,
                'n_observed': len(subset),
            }

        # Log-rank test (low vs high)
        if 'low' in km_results and 'high' in km_results:
            low_group = df[df['kr_tertile'] == 'low']
            high_group = df[df['kr_tertile'] == 'high']

            if len(low_group) >= 3 and len(high_group) >= 3:
                lr_test = logrank_test(
                    low_group['survival_time'], high_group['survival_time'],
                    event_observed_A=low_group['survived'], event_observed_B=high_group['survived']
                )
                km_results['logrank_test'] = {
                    'statistic': lr_test.test_statistic,
                    'p_value': lr_test.p_value,
                }

        logger.info("Kaplan-Meier analysis complete")
        return km_results

    except ImportError:
        logger.error("lifelines not installed. Cannot run Kaplan-Meier.")
        return None
    except Exception as e:
        logger.error(f"Kaplan-Meier failed: {e}")
        return None


def bootstrap_confidence_intervals(results_df, n_bootstrap=200):
    """Compute bootstrap confidence intervals for effect sizes."""
    logger.info(f"Running bootstrap with {n_bootstrap} resamples...")

    # Need at least 3 samples for tertiles
    if len(results_df) < 3:
        logger.warning("Insufficient data for bootstrap (< 3 samples)")
        return None

    bootstrap_samples = []

    for i in range(n_bootstrap):
        # Resample with replacement
        sample = results_df.sample(n=len(results_df), replace=True)

        # Compute KR effect (difference in survival between tertiles)
        try:
            sample['kr_tertile'] = pd.qcut(sample['kr'], q=3, labels=['low', 'medium', 'high'], duplicates='drop')
        except:
            # If qcut fails, use simple median split
            median_kr = sample['kr'].median()
            sample['kr_tertile'] = sample['kr'].apply(lambda x: 'low' if x < median_kr else 'high')
            sample['kr_tertile'] = sample['kr_tertile'].replace({'low': 'low', 'high': 'high'})

        # Get survival rates for low and high KR
        if 'low' in sample['kr_tertile'].values and 'high' in sample['kr_tertile'].values:
            low_survival = sample[sample['kr_tertile'] == 'low']['survived'].mean()
            high_survival = sample[sample['kr_tertile'] == 'high']['survived'].mean()

            if not np.isnan(low_survival) and not np.isnan(high_survival):
                bootstrap_samples.append({
                    'low_survival': low_survival,
                    'high_survival': high_survival,
                    'diff': high_survival - low_survival,
                })

    if not bootstrap_samples:
        return None

    # Compute 95% CI
    diffs = [s['diff'] for s in bootstrap_samples]
    ci_lower = np.percentile(diffs, 2.5)
    ci_upper = np.percentile(diffs, 97.5)

    results = {
        'bootstrap_n': len(bootstrap_samples),
        'survival_diff_mean': np.mean(diffs),
        'survival_diff_95ci': [ci_lower, ci_upper],
    }

    logger.info(f"Bootstrap complete. 95% CI for survival diff: [{ci_lower:.3f}, {ci_upper:.3f}]")
    return results


@logger.catch(reraise=True)
def main():
    """Main experiment pipeline."""
    logger.info("=" * 60)
    logger.info("STARTING OSS SURVIVAL EXPERIMENT (FALLBACK APPROACH)")
    logger.info("=" * 60)
    logger.info("NOTE: Using pseudo-KR from file_count distributions")
    logger.info("Reason: Dataset lacks file paths for Jaccard similarity")
    
    # Setup
    setup_environment()
    
    # Load dataset
    dataset_paths = [
        '/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out/full_data_out_1.json',
        '/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out/full_data_out_2.json',
        '/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out/full_data_out_3.json',
        '/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out/full_data_out_4.json',
        '/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out/full_data_out_5.json',
    ]
    
    examples = load_dataset(dataset_paths)
    
    if not examples:
        logger.error("No data loaded. Exiting.")
        return
    
    # Parse examples
    records = parse_examples(examples)
    
    # Group by repo
    repos = group_by_repo(records)
    
    # Process each repo
    results = []
    
    # Skip very large repos for performance
    MAX_REPO_COMMITS = 20000
    
    for repo_id, repo_records in repos.items():
        logger.info(f"Processing repo: {repo_id} ({len(repo_records)} commits)")
        
        # Skip very large repos
        if len(repo_records) > MAX_REPO_COMMITS:
            logger.info(f"Skipping {repo_id}: too many commits ({len(repo_records)})")
            continue
        
        try:
            # Identify founder
            founder = identify_founder(repo_records)
            if not founder:
                logger.warning(f"No founder identified for {repo_id}")
                continue
            
            # Detect founder departure
            founder_login, departure_date = detect_founder_departure(repo_records, founder)
            
            if departure_date:
                logger.info(f"Founder {founder} departed on {departure_date}")
                
                # Compute pseudo-KR (knowledge redundancy)
                kr, kr_squared = compute_pseudo_kr(repo_records, founder, departure_date)
                if kr is None:
                    logger.warning(f"Could not compute KR for {repo_id}")
                    continue
                
                # Measure survival
                survived, survival_time, censored = measure_survival(repo_records, departure_date, founder)
                if survival_time is None:
                    continue
                
                # Compute control variables
                controls = compute_control_variables(repo_records, founder, departure_date)
                
                # Store results for departure case
                result = {
                    'repo_id': repo_id,
                    'founder': founder,
                    'departure_date': departure_date.isoformat(),
                    'kr': kr,
                    'kr_squared': kr_squared,
                    'survived': survived,
                    'survival_time': survival_time,
                    'censored': censored,
                    'has_departure': True,
                    **controls,
                }
                results.append(result)
                
                logger.info(f"Repo {repo_id}: KR={kr:.3f}, Survived={survived}, Time={survival_time}d")
            else:
                # No departure detected - still include as example with output="no_departure"
                # Compute KR anyway for completeness
                kr, kr_squared = compute_pseudo_kr(repo_records, founder, repo_records[-1]['datetime'])
                
                if kr is not None:
                    result = {
                        'repo_id': repo_id,
                        'founder': founder,
                        'departure_date': None,
                        'kr': kr,
                        'kr_squared': kr_squared,
                        'survived': None,  # No departure = no survival measurement
                        'survival_time': None,
                        'censored': None,
                        'has_departure': False,
                    }
                    results.append(result)
                    logger.info(f"Repo {repo_id}: No departure, KR={kr:.3f}")
            
        except Exception as e:
            logger.error(f"Error processing {repo_id}: {e}")
            continue
    
    logger.info(f"Processed {len(results)} repos with founder departure")
    
    if len(results) < 5:
        logger.error("Insufficient data for analysis (< 5 repos with departure)")
        return
    
    # Convert to DataFrame
    results_df = pd.DataFrame(results)
    
    # Save processed data
    results_df.to_csv('results/processed_data.csv', index=False)
    results_df.to_json('results/processed_data.json', orient='records', indent=2)
    logger.info("Saved processed data")
    
    # Run statistical analyses
    logger.info("\n" + "=" * 60)
    logger.info("STATISTICAL ANALYSIS")
    logger.info("=" * 60)
    
    # Cox proportional hazards model
    cox_results = run_survival_analysis(results_df)
    
    # Kaplan-Meier analysis
    km_results = run_kaplan_meier(results_df)
    
    # Bootstrap confidence intervals
    bootstrap_results = bootstrap_confidence_intervals(results_df, n_bootstrap=200)
    
    # Compile final results in exp_gen_sol_out format
    # Convert results to examples format with predict_* fields
    examples = []
    for r in results:
        # Skip results without departure for the survival analysis output
        if not r.get('has_departure'):
            continue
            
        # Baseline prediction: always predict survival=1 (since most repos survive)
        # Our method prediction: use KR threshold (moderate KR = survive)
        baseline_prediction = "1"  # Always predict survival
        
        # Simple prediction based on KR: if KR in medium range, predict survival
        our_method_prediction = "1" if r['kr'] > 0.3 and r['kr'] < 0.8 else "0"
        
        example = {
            'input': json.dumps({
                'repo_id': r['repo_id'],
                'founder': r['founder'],
                'departure_date': r['departure_date'],
                'kr': r['kr'],
                'kr_squared': r['kr_squared'],
            }),
            'output': str(r['survived']),
            'predict_baseline': baseline_prediction,
            'predict_our_method': our_method_prediction,
            'metadata_repo_id': r['repo_id'],
            'metadata_founder': r['founder'],
            'metadata_kr': r['kr'],
            'metadata_survived': r['survived'],
            'metadata_survival_time': r['survival_time'],
        }
        examples.append(example)
    
    # Filter results to only those with departure for summary stats
    departure_results = [r for r in results if r.get('has_departure')]
    
    final_output = {
        'datasets': [
            {
                'dataset': 'oss_survival_experiment',
                'examples': examples
            }
        ],
        'metadata': {
            'experiment_summary': {
                'n_repos': len(departure_results),
                'n_departures': len(departure_results),
                'n_survived': sum(r['survived'] for r in departure_results if r['survived'] is not None),
                'survival_rate': sum(r['survived'] for r in departure_results if r['survived'] is not None) / len(departure_results) if departure_results else 0,
                'mean_kr': float(np.mean([r['kr'] for r in departure_results])) if departure_results else 0,
                'kr_range': [float(min(r['kr'] for r in departure_results)), float(max(r['kr'] for r in departure_results))] if departure_results else [0, 0],
            },
            'cox_model': cox_results,
            'kaplan_meier': km_results,
            'bootstrap': bootstrap_results,
            'hypothesis_test': {
                'inverted_u_supported': cox_results.get('inverted_u_supported') if cox_results else None,
                'kr_squared_coef': cox_results.get('kr_squared_coef') if cox_results else None,
                'kr_squared_p_value': cox_results.get('kr_squared_p_value') if cox_results else None,
            },
            'methodology_note': (
                "Fallback approach used: pseudo-KR computed from file_count distributions "
                "due to lack of file path data for Jaccard similarity. "
                "See artifact plan fallback scenario 1."
            ),
        }
    }
    
    # Save final results in exp_gen_sol_out format
    with open('results/method_out.json', 'w') as f:
        json.dump(final_output, f, indent=2)
    
    # Also save the full output at root level for compatibility
    with open('method_out.json', 'w') as f:
        json.dump(final_output, f, indent=2)
    
    logger.info("\n" + "=" * 60)
    logger.info("EXPERIMENT COMPLETE")
    logger.info("=" * 60)
    logger.info(f"Results saved to results/method_out.json and method_out.json")
    logger.info(f"Processed {len(results)} repositories")
    
    # Print summary
    if cox_results and cox_results.get('kr_squared_coef') is not None:
        kr2_coef = cox_results['kr_squared_coef']
        kr2_p = cox_results.get('kr_squared_p_value', 1.0)
        logger.info(f"\nHYPOTHESIS TEST:")
        logger.info(f"  KR^2 coefficient: {kr2_coef:.4f}")
        logger.info(f"  p-value: {kr2_p:.4f}")
        if kr2_coef < 0 and kr2_p < 0.05:
            logger.info(f"  RESULT: Inverted-U hypothesis SUPPORTED")
        else:
            logger.info(f"  RESULT: Inverted-U hypothesis NOT supported")
    
    return final_output


if __name__ == "__main__":
    main()
