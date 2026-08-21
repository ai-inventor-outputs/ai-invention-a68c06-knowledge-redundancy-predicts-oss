#!/usr/bin/env python3
"""
Simplified experiment runner - uses existing repo clones to produce results quickly.
"""
import sys
sys.path.insert(0, '.')

from method import OSSSurvivalExperiment
from loguru import logger

# Use smaller repo list with existing clones
repo_list = [
    "mojombo/grit",
    "jashkenas/coffeescript", 
    "BurntSushi/ripgrep",
    "Genymobile/scrcpy",
    "11ty/eleventy",
]

logger.info("Starting simplified experiment run...")
experiment = OSSSurvivalExperiment(
    data_dir=".",
    output_dir=".",
    repo_list=repo_list
)

# Run with existing clones (don't re-clone)
experiment.repo_list = repo_list

# Override clone to use existing repos
def quick_clone(repo_id):
    clone_dir = experiment.output_dir / "repo_clones" / repo_id.replace("/", "_")
    if clone_dir.exists():
        return clone_dir
    return None

# Run experiment
experiment.clone_repository = lambda repo_id: quick_clone(repo_id)
experiment.run_experiment()

logger.info("Experiment completed!")
