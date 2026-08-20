#!/usr/bin/env python3
"""Load and standardize GitHub repository dataset for OSS survival study."""

from pathlib import Path
import json
from collections import defaultdict

# Load a LARGER sample of the dataset for better coverage
print("Loading GitHub dataset (expanded sample)...")

# Load from the full dataset but limit to first 500k records (~15-20 repos)
with open("temp/datasets/github_final_full.json", "r") as f:
    data = json.load(f)

# Take a larger sample - first 500k records
data = data[:500000]
print(f"Loaded {len(data)} commit records (expanded sample)")

# Group data by repository
repos = defaultdict(list)
for record in data:
    repo_id = record["repo_id"]
    repos[repo_id].append(record)

print(f"Found {len(repos)} repositories")

# Create examples from commit data
examples = []

for repo_id, commits in repos.items():
    # Sort commits by timestamp
    commits_sorted = sorted(commits, key=lambda x: x["commit_timestamp"] if x["commit_timestamp"] else "")

    # Get repo metadata
    repo_name = commits[0]["repo_name"] if commits else ""
    repo_owner = commits[0]["repo_owner"] if commits else ""

    # Calculate contributor patterns (pre-compute)
    contributor_commits = defaultdict(int)
    for commit in commits_sorted:
        author = commit["author_login"]
        if author:
            contributor_commits[author] += 1

    # Create examples - each commit is an example
    for i, commit in enumerate(commits_sorted):
        author = commit["author_login"]
        is_founder = commit["is_founder"]

        # Create input features
        input_features = {
            "repo_id": repo_id,
            "repo_name": repo_name,
            "author_login": author,
            "is_founder": is_founder,
            "file_count": commit["file_count"],
            "commit_sequence_num": i,
            "author_total_commits": contributor_commits.get(author, 0),
            "repo_total_commits": len(commits),
            "commit_timestamp": commit["commit_timestamp"]
        }

        # Output: founder vs contributor
        output = "founder" if is_founder else "contributor"

        example = {
            "input": json.dumps(input_features),
            "output": output,
            "metadata_repo_id": repo_id,
            "metadata_author": author,
            "metadata_is_founder": is_founder,
            "metadata_commit_sha": commit["commit_sha"],
            "metadata_timestamp": commit["commit_timestamp"],
            "metadata_task_type": "classification",
            "metadata_n_classes": 2
        }

        examples.append(example)

print(f"Created {len(examples)} examples")

# Group by dataset
output = {
    "datasets": [
        {
            "dataset": "github_oss_commits",
            "examples": examples
        }
    ]
}

# Save to full_data_out.json
output_path = Path("full_data_out.json")
with open(output_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"Saved {len(examples)} examples to {output_path}")

# Print sample
print("\nSample example:")
if examples:
    sample = examples[0]
    print(f"  Input: {sample['input'][:200]}...")
    print(f"  Output: {sample['output']}")
    print(f"  Metadata: repo_id={sample['metadata_repo_id']}, author={sample['metadata_author']}")
