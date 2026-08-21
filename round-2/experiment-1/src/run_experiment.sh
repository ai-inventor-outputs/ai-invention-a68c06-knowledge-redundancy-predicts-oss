#!/bin/bash
# Run experiment with timeout
cd /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
export PYTHONPATH=.
timeout 1800 .venv/bin/python method.py > experiment_output.log 2>&1
echo "Experiment completed with exit code: $?"
