#!/usr/bin/env python3
"""
GitHub OSS Survival Dataset Collection Script

This script collects GitHub repository data to measure knowledge redundancy
and founder departure survival. It uses the GitHub REST API via PyGithub.

Requirements:
- PyGithub: pip install PyGithub
- pandas, numpy, tqdm: pip install pandas numpy tqdm
- GitHub Token: Set GITHUB_TOKEN environment variable

Usage:
    python collect_github_data.py --output data_out.json --max-repos 100

Without a GitHub token, the script is limited to 60 requests/hour.
With a token, it can make 5000 requests/hour.
"""

from github import Github
import os
import json
import time
from datetime import datetime, timedelta
from pathlib import Path
import argparse
from collections import defaultdict
from itertools import combinations

def setup_logging():
    """Setup basic logging."""
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s|%(levelname)s|%(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs/run.log')
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def search_repositories(g, queries, max_per_query=200):
    """Search for repositories matching queries."""
    repos = []
    for query in queries:
        try:
            logger.info(f"Searching: {query}")
            results = g.search_repositories(query=query, sort='stars', order='desc')
            count = 0
            for repo in results:
                if count >= max_per_query:
                    break
                repos.append({
                    'full_name': repo.full_name,
                    'stars': repo.stargazers_count,
                    'language': repo.language,
                    'created_at': repo.created_at.isoformat(),
                    'default_branch': repo.default_branch
                })
                count += 1
            logger.info(f"Found {count} repos for query: {query}")
        except Exception as e:
            logger.error(f"Error searching query '{query}': {e}")
    return repos

def validate_repository(repo):
    """Validate repository meets criteria."""
    try:
        # Check if archived
        if repo.archived:
            return False, "archived"
        
        # Check commit count
        commits = repo.get_commits()
        if commits.totalCount < 50:
            return False, f"too few commits: {commits.totalCount}"
        
        # Check contributor count
        contributors = repo.get_contributors()
        if contributors.totalCount < 3:
            return False, f"too few contributors: {contributors.totalCount}"
        
        # Check activity span (simplified check)
        first_commit = list(commits)[:1]
        if first_commit:
            first_date = first_commit[0].commit.author.date
            last_commit = list(repo.get_commits()[:1])[0]
            last_date = last_commit.commit.author.date
            months_active = (last_date - first_date).days / 30
            if months_active < 24:
                return False, f"insufficient activity span: {months_active:.1f} months"
        
        return True, "valid"
    except Exception as e:
        return False, f"validation error: {e}"

def collect_commit_data(repo, max_commits=300):
    """Collect commit data for a repository."""
    commits_data = []
    try:
        commits = repo.get_commits()
        commit_list = list(commits)[:max_commits]
        
        for commit in commit_list:
            if commit.author:
                commit_info = {
                    'sha': commit.sha,
                    'author': commit.author.login if commit.author else None,
                    'date': commit.commit.author.date.isoformat(),
                    'files': [f.filename for f in commit.files] if commit.files else [],
                    'additions': commit.stats.additions if commit.stats else 0,
                    'deletions': commit.stats.deletions if commit.stats else 0
                }
                commits_data.append(commit_info)
    except Exception as e:
        logger.error(f"Error collecting commits for {repo.full_name}: {e}")
    
    return commits_data

def identify_founder(repo_data):
    """Identify founder based on first 6 months of activity."""
    commits = repo_data.get('commits', [])
    if not commits:
        return None
    
    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])
    six_months_later = repo_created + timedelta(days=180)
    
    # Count commits per author in first 6 months
    author_commits = defaultdict(int)
    for commit in commits:
        commit_date = datetime.fromisoformat(commit['date'])
        if commit_date <= six_months_later and commit['author']:
            author_commits[commit['author']] += 1
    
    if author_commits:
        founder = max(author_commits, key=author_commits.get)
        return founder
    return None

def detect_departure(repo_data, founder):
    """Detect if founder has departed (12+ months inactivity)."""
    if not founder:
        return {'founder': None, 'departure_date': None, 'is_departed': False}
    
    founder_commits = [c for c in repo_data.get('commits', []) if c['author'] == founder]
    if not founder_commits:
        return {'founder': founder, 'departure_date': None, 'is_departed': False}
    
    last_commit_date = max(datetime.fromisoformat(c['date']) for c in founder_commits)
    now = datetime.now()
    
    if (now - last_commit_date).days >= 365:
        return {
            'founder': founder,
            'departure_date': last_commit_date.isoformat(),
            'is_departed': True
        }
    else:
        return {
            'founder': founder,
            'departure_date': None,
            'is_departed': False
        }

def compute_survival_metrics(repo_data, departure_info):
    """Compute pre/post departure activity and survival status."""
    if not departure_info or not departure_info['is_departed']:
        return {'has_departure': False}
    
    departure_date = datetime.fromisoformat(departure_info['departure_date'])
    commits = repo_data.get('commits', [])
    
    # Pre-departure: 12 months before departure
    pre_start = departure_date - timedelta(days=365)
    pre_commits = [c for c in commits 
                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]
    
    # Post-departure: 12 months after departure
    post_end = departure_date + timedelta(days=365)
    post_commits = [c for c in commits
                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]
    
    pre_rate = len(pre_commits) / 12.0  # commits per month
    post_rate = len(post_commits) / 12.0
    
    # Survival: post-departure activity >= 50% of pre-departure
    survival_status = 'survived' if post_rate >= (pre_rate * 0.5) else 'died'
    
    return {
        'has_departure': True,
        'pre_departure_commits_per_month': pre_rate,
        'post_departure_commits_per_month': post_rate,
        'survival_status': survival_status,
        'months_observed_post': min(12, len(post_commits) // 30) if post_commits else 0
    }

def compute_knowledge_redundancy(repo_data, top_n=5):
    """Compute pairwise Jaccard similarity among top contributors."""
    commits = repo_data.get('commits', [])
    
    # Get top contributors by commit count
    author_counts = defaultdict(int)
    for commit in commits:
        if commit['author']:
            author_counts[commit['author']] += 1
    
    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]
    
    # Get file sets for each contributor
    contributor_files = {}
    for author in top_contributors:
        files = set()
        for commit in commits:
            if commit['author'] == author:
                files.update(commit['files'])
        contributor_files[author] = files
    
    # Compute pairwise Jaccard similarity
    jaccard_scores = []
    for a, b in combinations(top_contributors, 2):
        intersection = len(contributor_files[a] & contributor_files[b])
        union = len(contributor_files[a] | contributor_files[b])
        if union > 0:
            jaccard_scores.append(intersection / union)
    
    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0
    
    return {
        'top_contributors': top_contributors,
        'pairwise_jaccard_scores': jaccard_scores,
        'redundancy_score': redundancy_score
    }

def main():
    parser = argparse.ArgumentParser(description='Collect GitHub OSS survival data')
    parser.add_argument('--output', default='data_out.json', help='Output file path')
    parser.add_argument('--max-repos', type=int, default=100, help='Maximum repos to collect')
    parser.add_argument('--token', help='GitHub token (or set GITHUB_TOKEN env var)')
    args = parser.parse_args()
    
    # Get GitHub token
    token = args.token or os.environ.get('GITHUB_TOKEN')
    if not token:
        logger.warning("No GitHub token provided. Rate limit: 60 requests/hour")
        logger.warning("Set GITHUB_TOKEN environment variable or use --token")
    
    # Initialize GitHub client
    g = Github(token) if token else Github()
    
    # Create output directory
    Path('logs').mkdir(exist_ok=True)
    
    # Search queries
    queries = [
        'stars:>=100 created:<2022-01-01 language:python',
        'stars:>=100 created:<2022-01-01 language:javascript',
        'stars:>=100 created:<2022-01-01 language:java',
        'stars:>=100 created:<2022-01-01 language:go',
    ]
    
    # Step 1: Search repositories
    logger.info("Step 1: Searching for repositories...")
    candidates = search_repositories(g, queries, max_per_query=50)
    logger.info(f"Found {len(candidates)} candidate repositories")
    
    # Step 2: Validate and collect data
    logger.info("Step 2: Validating and collecting data...")
    collected_data = []
    
    for i, repo_info in enumerate(candidates[:args.max_repos]):
        try:
            repo = g.get_repo(repo_info['full_name'])
            
            # Validate
            is_valid, reason = validate_repository(repo)
            if not is_valid:
                logger.info(f"Skipping {repo_info['full_name']}: {reason}")
                continue
            
            # Collect commits
            commits = collect_commit_data(repo, max_commits=300)
            
            repo_data = {
                'repo_id': repo_info['full_name'],
                'metadata': {
                    'stars': repo.stargazers_count,
                    'language': repo.language,
                    'created_date': repo.created_at.isoformat(),
                    'total_commits': repo.get_commits().totalCount
                },
                'commits': commits
            }
            
            # Compute metrics
            founder = identify_founder(repo_data)
            departure = detect_departure(repo_data, founder)
            survival = compute_survival_metrics(repo_data, departure)
            redundancy = compute_knowledge_redundancy(repo_data)
            
            # Build output record
            output = {
                'repo_id': repo_data['repo_id'],
                'metadata': repo_data['metadata'],
                'founder': departure,
                'survival': survival,
                'knowledge_redundancy': redundancy,
                'commits_sample': commits[-100:] if len(commits) > 100 else commits
            }
            collected_data.append(output)
            
            # Rate limiting
            time.sleep(0.8)
            
            # Checkpoint
            if i % 10 == 0:
                logger.info(f"Checkpoint: {i} repos processed")
                
        except Exception as e:
            logger.error(f"Error processing {repo_info['full_name']}: {e}")
            continue
    
    # Save output
    logger.info(f"Saving {len(collected_data)} repositories to {args.output}")
    with open(args.output, 'w') as f:
        json.dump(collected_data, f, indent=2)
    
    # Check file size
    file_size = Path(args.output).stat().st_size / (1024 * 1024)
    logger.info(f"Dataset size: {file_size:.2f} MB")
    
    # Print summary statistics
    departed = sum(1 for d in collected_data if d['survival'].get('has_departure', False))
    survived = sum(1 for d in collected_data if d['survival'].get('survival_status') == 'survived')
    logger.info(f"Summary: {len(collected_data)} repos, {departed} with departures, {survived} survived")

if __name__ == "__main__":
    main()
