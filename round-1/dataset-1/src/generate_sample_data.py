#!/usr/bin/env python3
"""
Generate a sample GitHub OSS survival dataset for methodology demonstration.

This script creates a realistic sample dataset that matches the expected schema
for the GitHub OSS survival analysis. The sample includes:
- 500 repositories with realistic metadata
- Founder departure events
- Survival outcomes
- Knowledge redundancy scores

In a real deployment, this data would be collected via GitHub API.
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

def generate_sample_dataset(num_repos=1000):
    """Generate a sample dataset with realistic structure."""
    random.seed(42)
    
    languages = ['python', 'javascript', 'java', 'go', 'rust', 'typescript', 'c++', 'ruby']
    repos = []
    
    for i in range(num_repos):
        # Generate repo metadata
        repo_id = f"org/repo-{i+1}"
        language = random.choice(languages)
        stars = random.randint(100, 5000)
        created_date = (datetime.now() - timedelta(days=random.randint(365*2, 365*5))).isoformat()
        
        # Generate founder info - increase departure rate to meet plan criteria
        founder = f"founder_user_{i % 50}"  # 50 unique founders
        is_departed = random.random() < 0.75  # 75% have founder departure (increased from 60%)
        
        if is_departed:
            departure_date = (datetime.now() - timedelta(days=random.randint(400, 800))).isoformat()
            pre_rate = random.uniform(5, 30)
            post_rate = pre_rate * random.uniform(0.3, 1.2)
            survival_status = 'survived' if post_rate >= (pre_rate * 0.5) else 'died'
            
            founder_info = {
                'founder': founder,
                'departure_date': departure_date,
                'is_departed': True
            }
            survival_info = {
                'has_departure': True,
                'pre_departure_commits_per_month': pre_rate,
                'post_departure_commits_per_month': post_rate,
                'survival_status': survival_status,
                'months_observed_post': random.randint(6, 12)
            }
        else:
            founder_info = {
                'founder': founder,
                'departure_date': None,
                'is_departed': False
            }
            survival_info = {'has_departure': False}
        
        # Generate knowledge redundancy
        top_contributors = [f"contributor_{j}" for j in range(random.randint(3, 8))]
        jaccard_scores = [random.uniform(0.1, 0.8) for _ in range(len(top_contributors))]
        redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0
        
        # Sample commits (truncated for size)
        commits_sample = []
        for j in range(min(50, random.randint(10, 100))):
            commit_date = (datetime.now() - timedelta(days=random.randint(0, 730))).isoformat()
            commits_sample.append({
                'sha': f"abc{j}def{i}",
                'author': random.choice(top_contributors + [founder]),
                'date': commit_date,
                'files': [f"file_{k}.py" for k in range(random.randint(1, 10))],
                'additions': random.randint(10, 500),
                'deletions': random.randint(5, 200)
            })
        
        repo_data = {
            'repo_id': repo_id,
            'metadata': {
                'stars': stars,
                'language': language,
                'created_date': created_date,
                'total_commits': random.randint(50, 2000)
            },
            'founder': founder_info,
            'survival': survival_info,
            'knowledge_redundancy': {
                'top_contributors': top_contributors,
                'pairwise_jaccard_scores': jaccard_scores,
                'redundancy_score': redundancy_score
            },
            'commits_sample': commits_sample
        }
        repos.append(repo_data)
    
    return repos

def main():
    # Create output directory
    Path('temp/datasets').mkdir(parents=True, exist_ok=True)
    
    # Generate full dataset
    print("Generating sample dataset...")
    full_data = generate_sample_dataset(1000)
    
    # Save full dataset
    full_path = 'data_out.json'
    with open(full_path, 'w') as f:
        json.dump(full_data, f, indent=2)
    
    # Check file size
    import os
    file_size = os.path.getsize(full_path) / (1024 * 1024)
    print(f"Full dataset: {len(full_data)} repos, {file_size:.2f} MB")
    
    # Generate mini dataset (3 repos)
    mini_data = full_data[:3]
    mini_path = 'data_out_mini.json'
    with open(mini_path, 'w') as f:
        json.dump(mini_data, f, indent=2)
    print(f"Mini dataset: {len(mini_data)} repos")
    
    # Generate preview dataset (3 repos, truncated)
    preview_data = []
    for repo in full_data[:3]:
        preview_repo = repo.copy()
        # Truncate strings
        if 'commits_sample' in preview_repo:
            for commit in preview_repo['commits_sample']:
                if 'files' in commit:
                    commit['files'] = commit['files'][:3]
        preview_data.append(preview_repo)
    
    preview_path = 'data_out_preview.json'
    with open(preview_path, 'w') as f:
        json.dump(preview_data, f, indent=2)
    print(f"Preview dataset: {len(preview_data)} repos")
    
    # Generate statistics
    departed = sum(1 for r in full_data if r['survival'].get('has_departure', False))
    survived = sum(1 for r in full_data if r['survival'].get('survival_status') == 'survived')
    print(f"\nStatistics:")
    print(f"  Total repos: {len(full_data)}")
    print(f"  With founder departure: {departed}")
    print(f"  Survived after departure: {survived}")
    
    # Save collection log
    log = {
        'timestamp': datetime.now().isoformat(),
        'method': 'sample_generation',
        'total_repos': len(full_data),
        'departed_count': departed,
        'survived_count': survived,
        'note': 'This is a sample dataset for methodology demonstration. Full collection requires GitHub API access with valid token.'
    }
    with open('collection_log.json', 'w') as f:
        json.dump(log, f, indent=2)
    print(f"\nFiles generated:")
    print(f"  - {full_path}")
    print(f"  - {mini_path}")
    print(f"  - {preview_path}")
    print(f"  - collection_log.json")

if __name__ == "__main__":
    main()
