#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy",
# ]
# ///

"""
Transform GitHub OSS survival dataset to exp_sel_data_out.json schema.

Each repository becomes an example with:
- input: JSON string of features (knowledge_redundancy, stars, language, etc.)
- output: survival status (survived/died/no_departure)
- metadata: repo information
"""

import json
import numpy as np
from pathlib import Path
from typing import Any

def load_dataset(path: str) -> list[dict[str, Any]]:
    """Load dataset from JSON file."""
    with open(path) as f:
        return json.load(f)

def encode_language(language: str) -> int:
    """Encode language as numeric value."""
    languages = {
        'python': 0, 'javascript': 1, 'java': 2, 'go': 3,
        'rust': 4, 'typescript': 5, 'c++': 6, 'ruby': 7
    }
    return languages.get(language, -1)

def create_example(repo: dict[str, Any]) -> dict[str, Any]:
    """Create an example from a repository record."""
    
    # Extract features for input
    features = {
        'knowledge_redundancy_score': repo['knowledge_redundancy']['redundancy_score'],
        'stars': repo['metadata']['stars'],
        'language_encoded': encode_language(repo['metadata']['language']),
        'total_commits': repo['metadata']['total_commits'],
        'top_contributors_count': len(repo['knowledge_redundancy']['top_contributors']),
    }
    
    # Add pre-departure metrics if available
    if repo['survival'].get('has_departure'):
        features['pre_departure_commits_per_month'] = repo['survival']['pre_departure_commits_per_month']
        features['post_departure_commits_per_month'] = repo['survival']['post_departure_commits_per_month']
        output = repo['survival']['survival_status']
    else:
        features['pre_departure_commits_per_month'] = 0
        features['post_departure_commits_per_month'] = 0
        output = 'no_departure'
    
    # Create example
    example = {
        'input': json.dumps(features),
        'output': output,
        'metadata_repo_id': repo['repo_id'],
        'metadata_founder': repo['founder']['founder'],
        'metadata_is_departed': repo['founder']['is_departed'],
        'metadata_has_departure': repo['survival']['has_departure'],
        'metadata_language': repo['metadata']['language'],
        'metadata_stars': repo['metadata']['stars'],
        'metadata_redundancy_score': repo['knowledge_redundancy']['redundancy_score'],
    }
    
    return example

def main():
    # Load the dataset
    dataset_path = Path('data_out.json')
    if not dataset_path.exists():
        print(f"Error: {dataset_path} not found")
        return
    
    repos = load_dataset(str(dataset_path))
    print(f"Loaded {len(repos)} repositories")
    
    # Create examples
    examples = [create_example(repo) for repo in repos]
    
    # Group by dataset (single dataset for this collection)
    output = {
        'datasets': [
            {
                'dataset': 'github_oss_survival',
                'examples': examples
            }
        ]
    }
    
    # Save output
    output_path = Path('full_data_out.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Saved {len(examples)} examples to {output_path}")
    
    # Print statistics
    outputs = [ex['output'] for ex in examples]
    unique_outputs = set(outputs)
    print(f"Output classes: {unique_outputs}")
    for cls in unique_outputs:
        count = sum(1 for o in outputs if o == cls)
        print(f"  {cls}: {count}")

if __name__ == '__main__':
    main()
