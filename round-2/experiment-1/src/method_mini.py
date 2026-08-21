#!/usr/bin/env python3
"""
Mini-test version: Run on 2 repos to verify pipeline.
"""
import sys
sys.path.insert(0, '.')

from method import OSSSurvivalExperiment

# Mini-test with 3 repos
repo_list = ["11ty/eleventy", "BurntSushi/ripgrep", "Genymobile/scrcpy"]

experiment = OSSSurvivalExperiment(
    data_dir="/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1",
    output_dir=".",
    repo_list=repo_list
)

experiment.run_experiment()
print("Mini-test completed!")
