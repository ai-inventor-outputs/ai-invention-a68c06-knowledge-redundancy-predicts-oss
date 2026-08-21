#!/usr/bin/env python3
"""Cox Proportional Hazards Model for OSS Project Survival Analysis.

Tests whether knowledge redundancy has an inverted-U relationship with OSS project
survival after founder departure using Cox proportional hazards models.
Implements the complete experimental design from the artifact plan.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
import pandas as pd
from lifelines import CoxPHFitter
from lifelines.statistics import proportional_hazard_test, logrank_test
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import gc
import os
import resource

# Configure logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Set memory limits (30GB out of ~31GB available)
RAM_BUDGET = 30 * 1024**3  # 30GB
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))


class CoxSurvivalAnalyzer:
    """Cox proportional hazards model analyzer for OSS survival data."""

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.df = None
        self.cph_linear = None
        self.cph_quadratic = None
        self.results = {}
        self.df_survival = None
        self.model_df = None

    def load_data(self):
        """Load and parse the dataset from full_data_out.json."""
        logger.info(f"Loading data from {self.data_path}")
        with open(self.data_path, 'r') as f:
            data = json.load(f)

        examples = data['datasets'][0]['examples']
        logger.info(f"Loaded {len(examples)} examples from JSON")

        # Parse input JSON strings and create records
        records = []
        for i, ex in enumerate(examples):
            try:
                input_dict = json.loads(ex['input'])
                record = {
                    'knowledge_redundancy_score': input_dict['knowledge_redundancy_score'],
                    'stars': input_dict['stars'],
                    'language_encoded': input_dict['language_encoded'],
                    'total_commits': input_dict['total_commits'],
                    'top_contributors_count': input_dict['top_contributors_count'],
                    'pre_departure_commits_per_month': input_dict['pre_departure_commits_per_month'],
                    'post_departure_commits_per_month': input_dict.get('post_departure_commits_per_month', 0),
                    'output': ex['output'],
                    'metadata_has_departure': ex.get('metadata_has_departure', False),
                    'metadata_repo_id': ex.get('metadata_repo_id', f'repo-{i}'),
                    'metadata_language': ex.get('metadata_language', 'unknown')
                }
                records.append(record)
            except Exception as e:
                logger.error(f"Failed to parse example {i}: {e}")
                continue

        self.df = pd.DataFrame(records)
        logger.info(f"Parsed {len(self.df)} valid records")

        # Log data summary
        logger.info(f"Output distribution: {self.df['output'].value_counts().to_dict()}")
        logger.info(f"Has departure distribution: {self.df['metadata_has_departure'].value_counts().to_dict()}")

        return self

    def prepare_survival_data(self):
        """Create survival analysis variables (T, E, KR, KR^2) as per artifact plan."""
        logger.info("Preparing survival analysis variables according to artifact plan")

        # Filter to only repos with founder departure (EXCLUDE 'no_departure' cases)
        df_departed = self.df[self.df['metadata_has_departure'] == True].copy()
        logger.info(f"Repos with founder departure: {len(df_departed)}")

        if len(df_departed) == 0:
            raise ValueError("No repos with founder departure found")

        # Create survival variables as specified in plan:
        # For 'died' cases: estimate time-to-death from commit patterns
        # For 'survived' cases: T=12 (full observation period), E=0 (censored)

        df_departed['T'] = 12.0  # Default: full observation period
        df_departed['E'] = 0  # Default: censored (survived)

        # Process died cases
        died_mask = df_departed['output'] == 'died'
        survived_mask = df_departed['output'] == 'survived'

        # For died cases, estimate time-to-death using post_departure_commits_per_month
        # APPROACH A (preferred from plan): Estimate from commit patterns
        for idx in df_departed.index:
            if df_departed.loc[idx, 'output'] == 'died':
                pre = df_departed.loc[idx, 'pre_departure_commits_per_month']
                post = df_departed.loc[idx, 'post_departure_commits_per_month']

                # If post_departure_commits_per_month drops to <10% of pre_departure rate
                if pre > 0 and post < 0.1 * pre:
                    # Estimate death_time as month when drop occurred
                    # Use a conservative estimate: month 3-6
                    df_departed.loc[idx, 'T'] = 4.0  # Conservative estimate
                else:
                    # No clear drop pattern, use T=6 (median approximation for died cases)
                    df_departed.loc[idx, 'T'] = 6.0

                df_departed.loc[idx, 'E'] = 1  # Event occurred (died)

        # Verify the assignments
        logger.info(f"Died cases (E=1): {(df_departed['E'] == 1).sum()}")
        logger.info(f"Survived cases (E=0): {(df_departed['E'] == 0).sum()}")
        logger.info(f"T summary: min={df_departed['T'].min()}, max={df_departed['T'].max()}, mean={df_departed['T'].mean():.2f}")

        # Create quadratic term for knowledge redundancy as per plan
        # KR = knowledge_redundancy_score (already in [0,1] range)
        # KR_squared = KR^2
        # Center KR at mean to reduce multicollinearity: KR_centered = KR - mean(KR)

        kr_mean = df_departed['knowledge_redundancy_score'].mean()
        df_departed['KR'] = df_departed['knowledge_redundancy_score']
        df_departed['KR_centered'] = df_departed['KR'] - kr_mean
        df_departed['KR_squared'] = df_departed['KR_centered'] ** 2

        logger.info(f"KR mean for centering: {kr_mean:.4f}")

        # Prepare control variables as per plan:
        # stars_log = log(stars + 1)  # log-transform skewed variable
        # total_commits_log = log(total_commits + 1)
        # top_contributors_count (bus factor proxy)
        # language_dummies = one-hot encode language_encoded (exclude one as reference)
        # pre_departure_commits_per_month (activity level control)

        df_departed['stars_log'] = np.log(df_departed['stars'] + 1)
        df_departed['total_commits_log'] = np.log(df_departed['total_commits'] + 1)

        # Create language dummies (one-hot encode)
        df_departed['language_str'] = df_departed['language_encoded'].astype(str)
        language_dummies = pd.get_dummies(df_departed['language_str'], prefix='lang')
        df_departed = pd.concat([df_departed, language_dummies], axis=1)

        # Store prepared data
        self.df_survival = df_departed

        logger.info(f"Survival data prepared: {len(self.df_survival)} samples")
        logger.info(f"  - Knowledge redundancy range: [{df_departed['KR'].min():.3f}, {df_departed['KR'].max():.3f}]")
        logger.info(f"  - Events (died): {(df_departed['E'] == 1).sum()}")
        logger.info(f"  - Censored (survived): {(df_departed['E'] == 0).sum()}")

        return self

    def fit_models(self):
        """Fit linear and quadratic Cox models as per artifact plan."""
        logger.info("Fitting Cox proportional hazards models")

        # Prepare DataFrame for lifelines
        # Columns: T (duration), E (event indicator), KR, KR_squared, [control variables]
        base_cols = ['T', 'E', 'KR_centered', 'KR_squared', 'stars_log',
                    'total_commits_log', 'top_contributors_count',
                    'pre_departure_commits_per_month']

        # Add language dummy columns
        lang_cols = [col for col in self.df_survival.columns if col.startswith('lang_')]
        all_cols = base_cols + lang_cols

        self.df_model = self.df_survival[all_cols].copy()
        self.df_model = self.df_model.dropna()
        logger.info(f"Model data after removing NA: {len(self.df_model)} samples")

        if len(self.df_model) == 0:
            raise ValueError("No valid data for model fitting after removing NA")

        # Check minimum events required
        n_events = (self.df_model['E'] == 1).sum()
        logger.info(f"Number of events (deaths): {n_events}")
        if n_events < 10:
            logger.warning(f"Low number of events ({n_events}) for reliable Cox model")

        # Model 1: Linear-only model (baseline) - as per plan
        # Formula: hazard = baseline * exp(β1*KR + β_controls*controls)
        logger.info("Fitting Model 1: Linear-only Cox model (baseline)")
        self.cph_linear = CoxPHFitter(penalizer=0.01)  # Add small penalty for stability

        try:
            # Build formula without KR_squared for linear model
            linear_formula = 'KR_centered + stars_log + total_commits_log + '
            linear_formula += 'top_contributors_count + pre_departure_commits_per_month + '
            linear_formula += ' + '.join([f'C({col})' for col in lang_cols])

            self.cph_linear.fit(
                self.df_model,
                duration_col='T',
                event_col='E',
                formula=linear_formula
            )
            logger.info("Model 1 (Linear) fitted successfully")
            logger.info(f"Linear model concordance: {self.cph_linear.concordance_index_:.4f}")
            logger.info(f"Linear model partial AIC: {self.cph_linear.AIC_partial_:.2f}")
        except Exception as e:
            logger.error(f"Failed to fit linear model: {e}")
            raise

        # Model 2: Quadratic model (tests inverted-U) - as per plan
        # Formula: hazard = baseline * exp(β1*KR + β2*KR^2 + β_controls*controls)
        logger.info("Fitting Model 2: Quadratic Cox model (tests inverted-U)")
        self.cph_quadratic = CoxPHFitter(penalizer=0.01)

        try:
            # Build formula with KR_squared for quadratic model
            quad_formula = 'KR_centered + KR_squared + stars_log + total_commits_log + '
            quad_formula += 'top_contributors_count + pre_departure_commits_per_month + '
            quad_formula += ' + '.join([f'C({col})' for col in lang_cols])

            self.cph_quadratic.fit(
                self.df_model,
                duration_col='T',
                event_col='E',
                formula=quad_formula
            )
            logger.info("Model 2 (Quadratic) fitted successfully")
            logger.info(f"Quadratic model concordance: {self.cph_quadratic.concordance_index_:.4f}")
            logger.info(f"Quadratic model partial AIC: {self.cph_quadratic.AIC_partial_:.2f}")
        except Exception as e:
            logger.error(f"Failed to fit quadratic model: {e}")
            raise

        # Model comparison using likelihood ratio test as per plan
        logger.info("Performing model comparison using likelihood ratio test")
        lr_test_stat = 2 * (self.cph_quadratic.log_likelihood_ - self.cph_linear.log_likelihood_)
        lr_p_value = 1 - stats.chi2.cdf(lr_test_stat, df=1)  # 1 df for quadratic term

        self.model_comparison = {
            'LR_test_statistic': lr_test_stat,
            'LR_test_p_value': lr_p_value,
            'AIC_linear': self.cph_linear.AIC_partial_,
            'AIC_quadratic': self.cph_quadratic.AIC_partial_
        }

        logger.info(f"Likelihood ratio test: statistic={lr_test_stat:.4f}, p={lr_p_value:.4f}")
        logger.info(f"Partial AIC: Linear={self.cph_linear.AIC_partial_:.2f}, Quadratic={self.cph_quadratic.AIC_partial_:.2f}")

        return self

    def test_hypothesis(self):
        """Test the inverted-U hypothesis as per artifact plan."""
        logger.info("Testing inverted-U hypothesis")

        # Get coefficients from quadratic model
        # KEY STATISTICAL CORRECTION from plan:
        # For quadratic terms, the relationship between KR and log-hazard is:
        # log(hazard) = β1*KR + β2*KR^2 + ...
        # d(log(hazard))/d(KR) = β1 + 2*β2*KR
        # Inverted-U in SURVIVAL means U-shaped in HAZARD (since survival ∝ 1/hazard)
        # For inverted-U survival (hypothesis): β2 > 0 (positive quadratic coefficient for hazard)
        # Turning point (maximum hazard): KR* = -β1/(2*β2)

        coef = self.cph_quadratic.params_
        beta1 = coef['KR_centered']
        beta2 = coef['KR_squared']

        logger.info(f"Coefficient β1 (linear KR): {beta1:.4f}")
        logger.info(f"Coefficient β2 (quadratic KR^2): {beta2:.4f}")

        # Statistical test for quadratic term
        # H0: β2 = 0 (no quadratic relationship)
        # H1: β2 > 0 (positive quadratic term, indicating U-shaped hazard = inverted-U survival)
        p_value = self.cph_quadratic.summary.loc['KR_squared', 'p']

        logger.info(f"β2 p-value: {p_value:.4f}")

        # Turning point calculation (maximum hazard for quadratic)
        # KR* = -β1/(2*β2)
        if beta2 != 0:
            turning_point = -beta1 / (2 * beta2)
        else:
            turning_point = np.nan

        logger.info(f"Turning point (KR for max hazard): {turning_point:.4f}")

        # Check if turning point is within [0, 1] range
        turning_point_in_range = 0 <= turning_point <= 1 if not np.isnan(turning_point) else False

        # Hypothesis test criteria as per plan:
        # H0: β2 = 0 (no quadratic relationship)
        # H1: β2 > 0 (positive quadratic term, indicating U-shaped hazard = inverted-U survival)
        # Statistical significance: p-value < 0.05 for β2
        inverted_U_confirmed = (beta2 > 0) and (p_value < 0.05) and turning_point_in_range

        # Correct hazard ratio calculation as per plan:
        # WRONG: HR = exp(β2) for quadratic term alone
        # RIGHT: HR(KR = x vs KR = 0) = exp(β1*x + β2*x^2)
        # For continuous range: Plot HR across KR values [0, 1]
        # Compute HR at key percentiles

        kr_values = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
        hazard_ratios = {}

        for kr in kr_values:
            # HR(KR = x) = exp(β1*x_centered + β2*x_centered^2)
            kr_centered = kr - self.df_survival['KR'].mean()
            log_hr = beta1 * kr_centered + beta2 * (kr_centered ** 2)
            hr = np.exp(log_hr)
            hazard_ratios[f'at_KR_{kr}'] = float(hr)

        logger.info(f"Hazard ratios at key KR values: {hazard_ratios}")

        # Compute survival curves as per plan
        # Use cph.predict_survival_function() for representative KR values
        # Plot survival curves for KR = 0.2, 0.4, 0.6, 0.8
        # Verify that moderate KR (0.3-0.5) shows highest survival

        kr_plot_values = [0.2, 0.4, 0.6, 0.8]
        survival_probabilities_at_t12 = []
        median_survival_times = []

        for kr in kr_plot_values:
            # Create a sample with this KR value
            sample = self.df_model.iloc[0:1].copy()
            sample['KR_centered'] = kr - self.df_survival['KR'].mean()
            sample['KR_squared'] = sample['KR_centered'] ** 2

            try:
                surv_func = self.cph_quadratic.predict_survival_function(sample)

                # Get survival probability at t=12
                if 12 in surv_func.index:
                    survival_prob = surv_func.loc[12].values[0]
                else:
                    # Interpolate if 12 not in index
                    survival_prob = np.interp(12, surv_func.index, surv_func.values.flatten())

                survival_probabilities_at_t12.append(float(survival_prob))

                # Estimate median survival time
                median_survival = surv_func[surv_func < 0.5].index.min() if (surv_func < 0.5).any() else np.nan
                median_survival_times.append(float(median_survival) if not np.isnan(median_survival) else None)

            except Exception as e:
                logger.error(f"Failed to compute survival for KR={kr}: {e}")
                survival_probabilities_at_t12.append(None)
                median_survival_times.append(None)

        # Test survival rate differences as per plan:
        # Define groups by KR percentiles:
        # Low KR: bottom 10th percentile (KR < ~0.3)
        # Moderate KR: 25th-75th percentile (KR ~ 0.3-0.5)
        # High KR: top 10th percentile (KR > ~0.6)

        kr_threshold_low = self.df_survival['KR'].quantile(0.1)
        kr_threshold_high = self.df_survival['KR'].quantile(0.9)

        logger.info(f"KR thresholds: low < {kr_threshold_low:.3f}, high > {kr_threshold_high:.3f}")

        # Group KR into tertiles (low/moderate/high)
        kr_groups = {
            'low': self.df_survival[self.df_survival['KR'] < 0.3],
            'moderate': self.df_survival[
                (self.df_survival['KR'] >= 0.3) &
                (self.df_survival['KR'] <= 0.5)
            ],
            'high': self.df_survival[self.df_survival['KR'] > 0.6]
        }

        # Compare survival probabilities at t=12 months
        # S(mod) - S(low) should be > 0.20 (20% higher survival)
        # S(mod) - S(high) should be > 0.10 (10% higher survival)

        survival_at_12 = {}
        for group_name, group_df in kr_groups.items():
            if len(group_df) > 0:
                # Predict survival at t=12 for this group
                try:
                    surv_funcs = self.cph_quadratic.predict_survival_function(group_df)
                    # Average survival probability at t=12
                    if 12 in surv_funcs.index:
                        avg_survival = surv_funcs.loc[12].mean()
                    else:
                        # Interpolate
                        avg_survival = np.mean([
                            np.interp(12, surv_funcs.index, surv_funcs.iloc[:, i].values)
                            for i in range(surv_funcs.shape[1])
                        ])
                    survival_at_12[group_name] = float(avg_survival)
                except Exception as e:
                    logger.error(f"Failed to compute survival for {group_name} group: {e}")
                    survival_at_12[group_name] = None

        logger.info(f"Survival probabilities at t=12: {survival_at_12}")

        # Compute survival rate differences
        survival_differences = {}
        if 'moderate' in survival_at_12 and 'low' in survival_at_12 and survival_at_12['moderate'] is not None:
            survival_differences['moderate_vs_low'] = survival_at_12['moderate'] - survival_at_12['low']
        if 'moderate' in survival_at_12 and 'high' in survival_at_12 and survival_at_12['moderate'] is not None:
            survival_differences['moderate_vs_high'] = survival_at_12['moderate'] - survival_at_12['high']

        logger.info(f"Survival rate differences: {survival_differences}")

        # Verify control variable effects as per plan
        # Verify bus factor (top_contributors_count) has expected negative relationship with hazard
        # Verify stars/popularity has expected negative relationship with hazard

        control_effects = {}
        for var in ['top_contributors_count', 'stars_log']:
            if var in self.cph_quadratic.params_:
                control_effects[var] = {
                    'coefficient': float(self.cph_quadratic.params_[var]),
                    'p_value': float(self.cph_quadratic.summary.loc[var, 'p']),
                    'expected_sign': 'negative' if var in ['top_contributors_count', 'stars_log'] else 'any'
                }

        logger.info(f"Control variable effects: {control_effects}")

        # Store results
        self.results['model_results'] = {
            'linear_model': {
                'coefficients': self.cph_linear.params_.to_dict(),
                'p_values': self.cph_linear.summary['p'].to_dict(),
                'concordance': float(self.cph_linear.concordance_index_),
                'log_likelihood': float(self.cph_linear.log_likelihood_),
                'AIC_partial': float(self.cph_linear.AIC_partial_)
            },
            'quadratic_model': {
                'coefficients': self.cph_quadratic.params_.to_dict(),
                'p_values': self.cph_quadratic.summary['p'].to_dict(),
                'concordance': float(self.cph_quadratic.concordance_index_),
                'log_likelihood': float(self.cph_quadratic.log_likelihood_),
                'AIC_partial': float(self.cph_quadratic.AIC_partial_),
                'turning_point_KR': float(turning_point) if not np.isnan(turning_point) else None,
                'quadratic_term_significant': bool(p_value < 0.05)
            },
            'model_comparison': self.model_comparison
        }

        self.results['hypothesis_test'] = {
            'inverted_U_confirmed': inverted_U_confirmed,
            'beta1_coefficient': float(beta1),
            'beta2_coefficient': float(beta2),
            'beta2_p_value': float(p_value),
            'turning_point': float(turning_point) if not np.isnan(turning_point) else None,
            'turning_point_in_range': turning_point_in_range,
            'survival_rate_differences': survival_differences,
            'hazard_ratios': hazard_ratios,
            'control_variable_effects': control_effects
        }

        self.results['survival_curves'] = {
            'KR_values': kr_plot_values,
            'survival_probabilities_at_t12': survival_probabilities_at_t12,
            'median_survival_times': median_survival_times
        }

        self.results['data_summary'] = {
            'n_total': int(len(self.df)),
            'n_departed': int(len(self.df_survival)),
            'n_died': int((self.df_survival['E'] == 1).sum()),
            'n_survived': int((self.df_survival['E'] == 0).sum()),
            'KR_mean': float(self.df_survival['KR'].mean()),
            'KR_std': float(self.df_survival['KR'].std())
        }

        logger.info(f"Inverted-U hypothesis confirmed: {inverted_U_confirmed}")
        logger.info(f"Beta2 coefficient: {beta2:.4f} (p={p_value:.4f})")
        logger.info(f"Turning point: {turning_point:.4f}")

        return self

    def generate_outputs(self):
        """Generate method_out.json and diagnostic plots as per artifact plan."""
        logger.info("Generating outputs")

        # Create output directory
        output_dir = Path('.')
        output_dir.mkdir(exist_ok=True)

        # Convert numpy types to Python native types for JSON serialization
        def convert_to_native(obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.bool_):
                return bool(obj)
            elif isinstance(obj, dict):
                return {k: convert_to_native(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_to_native(v) for v in obj]
            else:
                return obj

        # Create examples array with individual repository results
        examples = []
        for idx, row in self.df_survival.iterrows():
            # Create sample for prediction with all required columns
            sample_data = {
                'KR_centered': [float(row['KR']) - float(self.df_survival['KR'].mean())],
                'KR_squared': [(float(row['KR']) - float(self.df_survival['KR'].mean()))**2],
                'stars_log': [float(row['stars_log'])],
                'total_commits_log': [float(row['total_commits_log'])],
                'top_contributors_count': [int(row['top_contributors_count'])],
                'pre_departure_commits_per_month': [float(row['pre_departure_commits_per_month'])]
            }
            # Add language dummy columns
            for col in self.df_model.columns:
                if col.startswith('lang_'):
                    sample_data[col] = [float(row[col]) if col in row.index else 0.0]
            
            sample = pd.DataFrame(sample_data)
            
            # Get survival probability at t=12
            try:
                surv_linear = self.cph_linear.predict_survival_function(sample)
                surv_quad = self.cph_quadratic.predict_survival_function(sample)
                prob_linear = float(surv_linear[12].values[0]) if 12 in surv_linear.index else None
                prob_quad = float(surv_quad[12].values[0]) if 12 in surv_quad.index else None
            except Exception as e:
                logger.error(f"Failed to predict for repo {idx}: {e}")
                prob_linear = None
                prob_quad = None
            
            example = {
                'input': json.dumps({
                    'knowledge_redundancy_score': float(row['KR']),
                    'stars': int(row['stars']),
                    'total_commits': int(row['total_commits']),
                    'top_contributors_count': int(row['top_contributors_count']),
                    'pre_departure_commits_per_month': float(row['pre_departure_commits_per_month'])
                }),
                'output': row['output'],  # 'survived' or 'died'
                'metadata_repo_id': row.get('metadata_repo_id', f'repo-{idx}'),
                'metadata_has_departure': bool(row['metadata_has_departure']),
                'metadata_KR': float(row['KR']),
                'metadata_T': float(row['T']),
                'metadata_E': int(row['E']),
                'predict_linear_survival': json.dumps({'survival_probability_at_12': prob_linear}),
                'predict_quadratic_survival': json.dumps({'survival_probability_at_12': prob_quad})
            }
            examples.append(example)

        # Add summary example with overall results
        summary_example = {
            'input': json.dumps({
                'analysis_type': 'Cox proportional hazards survival analysis summary',
                'dataset_size': int(self.results['data_summary']['n_total'])
            }),
            'output': json.dumps(convert_to_native({
                'inverted_U_confirmed': self.results['hypothesis_test']['inverted_U_confirmed'],
                'beta2_coefficient': self.results['hypothesis_test']['beta2_coefficient'],
                'beta2_p_value': self.results['hypothesis_test']['beta2_p_value'],
                'turning_point': self.results['hypothesis_test']['turning_point']
            })),
            'metadata_n_total': int(self.results['data_summary']['n_total']),
            'metadata_n_departed': int(self.results['data_summary']['n_departed']),
            'metadata_n_died': int(self.results['data_summary']['n_died']),
            'metadata_n_survived': int(self.results['data_summary']['n_survived']),
            'predict_model_results': json.dumps(convert_to_native(self.results['model_results'])),
            'predict_hypothesis_test': json.dumps(convert_to_native(self.results['hypothesis_test']))
        }
        examples.append(summary_example)

        output = {
            'datasets': [
                {
                    'dataset': 'github_oss_survival',
                    'examples': examples
                }
            ]
        }

        # Save method_out.json
        output_path = output_dir / 'method_out.json'
        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        logger.info(f"Saved method_out.json to {output_path} with {len(examples)} examples")

        # Generate diagnostic plots
        self.generate_plots(output_dir)

        return output

    def generate_plots(self, output_dir: Path):
        """Generate diagnostic plots for Cox models as per artifact plan."""
        logger.info("Generating diagnostic plots")

        # Create plots directory if not exists
        plots_dir = output_dir / 'plots'
        plots_dir.mkdir(exist_ok=True)

        # Set plot style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (10, 6)

        # Plot 1: Survival curves for different KR values (as per plan)
        logger.info("Plotting survival curves")
        fig, ax = plt.subplots()

        kr_mean = self.df_survival['KR'].mean()
        colors = ['red', 'green', 'blue', 'orange']

        for i, kr in enumerate([0.2, 0.4, 0.6, 0.8]):
            # Create sample DataFrame
            sample_df = self.df_model.iloc[[0]].copy()
            sample_df['KR_centered'] = kr - kr_mean
            sample_df['KR_squared'] = (kr - kr_mean) ** 2

            try:
                surv_func = self.cph_quadratic.predict_survival_function(sample_df)
                ax.plot(surv_func.index, surv_func.values.flatten(),
                       label=f'KR={kr}', color=colors[i], linewidth=2)
            except Exception as e:
                logger.error(f"Failed to plot survival curve for KR={kr}: {e}")

        ax.set_xlabel('Time (months)', fontsize=12)
        ax.set_ylabel('Survival Probability', fontsize=12)
        ax.set_title('Survival Curves by Knowledge Redundancy Level', fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(plots_dir / 'survival_curves.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Plot 2: Hazard ratio plot (as per plan)
        logger.info("Plotting hazard ratio curve")
        fig, ax = plt.subplots()

        kr_range = np.linspace(0, 1, 100)
        hr_values = []

        beta1 = self.cph_quadratic.params_.get('KR_centered', 0)
        beta2 = self.cph_quadratic.params_.get('KR_squared', 0)
        kr_mean = self.df_survival['KR'].mean()

        for kr in kr_range:
            kr_c = kr - kr_mean
            log_hr = beta1 * kr_c + beta2 * kr_c**2
            hr_values.append(np.exp(log_hr))

        ax.plot(kr_range, hr_values, linewidth=2, color='blue')
        ax.axhline(y=1, color='red', linestyle='--', alpha=0.5, label='HR=1')
        if not np.isnan(self.results['hypothesis_test']['turning_point']):
            ax.axvline(x=self.results['hypothesis_test']['turning_point'],
                      color='green', linestyle='--', alpha=0.5,
                      label=f"Turning point={self.results['hypothesis_test']['turning_point']:.2f}")
        ax.set_xlabel('Knowledge Redundancy Score', fontsize=12)
        ax.set_ylabel('Hazard Ratio (vs reference)', fontsize=12)
        ax.set_title('Hazard Ratio vs Knowledge Redundancy', fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(plots_dir / 'hazard_ratio_plot.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Plot 3: Schoenfeld residuals test for proportional hazards (as per plan)
        logger.info("Plotting Schoenfeld residuals test")
        try:
            fig, ax = plt.subplots()
            # Get Schoenfeld residuals
            schoenfeld_residuals = self.cph_quadratic.compute_residuals(self.df_model, 'schoenfeld')
            # Plot residuals vs time for main variable
            if 'KR_centered' in schoenfeld_residuals.columns:
                ax.scatter(range(len(schoenfeld_residuals)), schoenfeld_residuals['KR_centered'],
                          alpha=0.5, s=10)
                ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
                ax.set_xlabel('Observation Index', fontsize=12)
                ax.set_ylabel('Schoenfeld Residuals (KR)', fontsize=12)
                ax.set_title('Schoenfeld Residuals Test for Proportional Hazards', fontsize=14)
                ax.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig(plots_dir / 'cox_zph_test.png', dpi=300, bbox_inches='tight')
            plt.close()
        except Exception as e:
            logger.error(f"Failed to plot Schoenfeld residuals: {e}")

        # Plot 4: Martingale residuals for model fit (as per plan)
        logger.info("Plotting martingale residuals")
        try:
            fig, ax = plt.subplots()
            # Get martingale residuals
            martingale_residuals = self.cph_quadratic.compute_residuals(self.df_model, 'martingale')
            ax.hist(martingale_residuals.values.flatten(), bins=50, edgecolor='black', alpha=0.7)
            ax.set_xlabel('Martingale Residuals', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            ax.set_title('Martingale Residuals Distribution (Model Fit Diagnostics)', fontsize=14)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(plots_dir / 'martingale_residuals.png', dpi=300, bbox_inches='tight')
            plt.close()
            logger.info("Martingale residuals plot saved")
        except Exception as e:
            logger.error(f"Failed to plot martingale residuals: {e}")

        logger.info(f"Diagnostic plots saved to {plots_dir}")

        return self

    def print_summary(self):
        """Print a comprehensive summary of the analysis."""
        logger.info("=" * 70)
        logger.info("COX PROPORTIONAL HAZARDS SURVIVAL ANALYSIS SUMMARY")
        logger.info("=" * 70)

        logger.info("\n1. DATA SUMMARY:")
        logger.info(f"   Total repos: {self.results['data_summary']['n_total']}")
        logger.info(f"   Repos with founder departure: {self.results['data_summary']['n_departed']}")
        logger.info(f"   Died (events): {self.results['data_summary']['n_died']}")
        logger.info(f"   Survived (censored): {self.results['data_summary']['n_survived']}")
        logger.info(f"   KR mean: {self.results['data_summary']['KR_mean']:.4f}")
        logger.info(f"   KR std: {self.results['data_summary']['KR_std']:.4f}")

        logger.info("\n2. QUADRATIC MODEL RESULTS:")
        logger.info(f"   Beta1 (linear KR): {self.results['hypothesis_test']['beta1_coefficient']:.4f}")
        logger.info(f"   Beta2 (quadratic KR^2): {self.results['hypothesis_test']['beta2_coefficient']:.4f}")
        logger.info(f"   Beta2 p-value: {self.results['hypothesis_test']['beta2_p_value']:.4f}")
        logger.info(f"   Turning point (KR for max hazard): {self.results['hypothesis_test']['turning_point']:.4f}")

        logger.info("\n3. HYPOTHESIS TEST (Inverted-U):")
        logger.info(f"   Inverted-U confirmed: {self.results['hypothesis_test']['inverted_U_confirmed']}")
        logger.info(f"   Criteria: β2 > 0, p < 0.05, turning point in [0,1]")

        if 'moderate_vs_low' in self.results['hypothesis_test']['survival_rate_differences']:
            logger.info(f"   Survival diff (mod vs low): "
                       f"{self.results['hypothesis_test']['survival_rate_differences']['moderate_vs_low']:.4f}")
        if 'moderate_vs_high' in self.results['hypothesis_test']['survival_rate_differences']:
            logger.info(f"   Survival diff (mod vs high): "
                       f"{self.results['hypothesis_test']['survival_rate_differences']['moderate_vs_high']:.4f}")

        logger.info("\n4. MODEL COMPARISON:")
        logger.info(f"   Linear model concordance: {self.cph_linear.concordance_index_:.4f}")
        logger.info(f"   Quadratic model concordance: {self.cph_quadratic.concordance_index_:.4f}")
        logger.info(f"   Partial AIC: Linear={self.cph_linear.AIC_partial_:.2f}, Quadratic={self.cph_quadratic.AIC_partial_:.2f}")
        logger.info(f"   LR test p-value: {self.model_comparison['LR_test_p_value']:.4f}")

        logger.info("\n5. HAZARD RATIOS AT KEY KR VALUES:")
        for kr, hr in self.results['hypothesis_test']['hazard_ratios'].items():
            logger.info(f"   {kr}: HR = {hr:.4f}")

        logger.info("=" * 70)


@logger.catch(reraise=True)
def main():
    """Main execution function."""
    # Create logs directory
    Path('logs').mkdir(exist_ok=True)

    # Initialize analyzer with data from dependency
    # Path to the full dataset from iter_1/gen_art/gen_art_dataset_1
    data_path = '/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json'

    # Check if data exists
    if not Path(data_path).exists():
        logger.error(f"Data file not found: {data_path}")
        sys.exit(1)

    logger.info("Starting Cox Survival Analysis...")
    logger.info(f"Data path: {data_path}")

    # Initialize and run analysis pipeline
    analyzer = CoxSurvivalAnalyzer(data_path)
    analyzer.load_data()
    analyzer.prepare_survival_data()
    analyzer.fit_models()
    analyzer.test_hypothesis()
    results = analyzer.generate_outputs()
    analyzer.print_summary()

    logger.info("Analysis completed successfully!")

    # Clean up
    del analyzer
    gc.collect()

    return results


if __name__ == '__main__':
    main()
