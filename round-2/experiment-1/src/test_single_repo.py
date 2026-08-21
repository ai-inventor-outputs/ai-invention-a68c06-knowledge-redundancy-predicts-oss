#!/usr/bin/env python3
"""Test single repo to debug departure detection."""
import sys
sys.path.insert(0, '.')

from method import OSSSurvivalExperiment

# Test with a well-known project with founder departure
repo_list = ["mojombo/grit"]

experiment = OSSSurvivalExperiment(
    data_dir=".",
    output_dir=".",
    repo_list=repo_list
)

# Just test cloning and departure detection
repo_id = repo_list[0]
repo_path = experiment.clone_repository(repo_id)
if repo_path:
    repo_commits = experiment.extract_commit_data(repo_id, repo_path)
    if len(repo_commits) > 0:
        founder = experiment.identify_founders(repo_commits)
        departure = experiment.detect_departure(repo_commits, founder)
        print(f"\nResults for {repo_id}:")
        print(f"  Founder: {founder}")
        print(f"  Departure detected: {departure is not None}")
        if departure:
            print(f"  Departure info: {departure}")
    else:
        print(f"No commits extracted for {repo_id}")
else:
    print(f"Failed to clone {repo_id}")
