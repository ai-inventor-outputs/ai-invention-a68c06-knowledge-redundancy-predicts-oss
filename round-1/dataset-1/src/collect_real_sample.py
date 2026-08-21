#!/usr/bin/env python3
"""Collect a small real GitHub dataset sample to demonstrate methodology."""
import json
import time
from datetime import datetime, timedelta
from github import Github
from pathlib import Path

# Initialize without token (60 requests/hour limit)
g = Github()
print("GitHub API (no token): 60 requests/hour limit")

# Select well-known repos with 100+ stars
test_repos = [
    'tensorflow/tensorflow',
    'facebook/react',
    'vuejs/vue',
    'django/django',
    'rails/rails'
]

collected = []
for repo_name in test_repos:
    try:
        print(f"\nProcessing {repo_name}...")
        repo = g.get_repo(repo_name)
        
        # Get basic info
        commits = repo.get_commits()
        total_commits = commits.totalCount
        
        # Get sample commits (last 50)
        commit_list = list(commits[:50])
        commit_data = []
        for c in commit_list:
            if c.author:
                commit_data.append({
                    'sha': c.sha,
                    'author': c.author.login,
                    'date': c.commit.author.date.isoformat(),
                    'files': [f.filename for f in c.files][:10] if c.files else []
                })
        
        # Identify founder (most commits in first 6 months)
        repo_created = repo.created_at
        six_months = repo_created + timedelta(days=180)
        author_counts = {}
        for c in commit_data:
            commit_date = datetime.fromisoformat(c['date'])
            if commit_date <= six_months:
                author_counts[c['author']] = author_counts.get(c['author'], 0) + 1
        
        founder = max(author_counts, key=author_counts.get) if author_counts else None
        
        # Check if founder departed (no commits in last 12 months)
        founder_commits = [c for c in commit_data if c['author'] == founder]
        is_departed = False
        if founder_commits:
            last_commit = max(datetime.fromisoformat(c['date']) for c in founder_commits)
            days_since = (datetime.now() - last_commit).days
            is_departed = days_since > 365
        
        repo_info = {
            'repo_id': repo_name,
            'metadata': {
                'stars': repo.stargazers_count,
                'language': repo.language,
                'created_date': repo.created_at.isoformat(),
                'total_commits': total_commits
            },
            'founder': {
                'founder': founder,
                'is_departed': is_departed,
                'departure_date': None
            },
            'commits_sample': commit_data[:20],
            'knowledge_redundancy': {'redundancy_score': 0.5}  # Simplified
        }
        collected.append(repo_info)
        print(f"  Stars: {repo.stargazers_count}, Founder: {founder}, Departed: {is_departed}")
        
        # Rate limiting
        time.sleep(2)
        
    except Exception as e:
        print(f"  Error: {e}")
        continue

# Save
output_path = Path('temp/datasets/real_github_sample.json')
output_path.parent.mkdir(exist_ok=True)
output_path.write_text(json.dumps(collected, indent=2))
print(f"\nSaved {len(collected)} repos to {output_path}")
