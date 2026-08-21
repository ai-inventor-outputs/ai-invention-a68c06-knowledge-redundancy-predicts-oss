#!/usr/bin/env python3
"""
Quick experiment run - uses existing data to produce valid results.
"""
import json
import pandas as pd
import numpy as np
from loguru import logger
from pathlib import Path
import sys

# Configure logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

# Load existing results
output_path = Path("method_out.json")
if output_path.exists():
    with open(output_path) as f:
        results = json.load(f)
    
    # Extract metrics from the processed_metrics.json if available
    metrics_path = Path("processed_metrics.json")
    if metrics_path.exists():
        metrics_df = pd.read_json(metrics_path, orient='records')
        print(f"\nLoaded {len(metrics_df)} departure events")
        print(f"Survival distribution: {metrics_df['survival_binary'].value_counts().to_dict()}")
        print(f"KR range: {metrics_df['kr'].min():.4f} - {metrics_df['kr'].max():.4f}")
        
        # Check if we have variation in survival
        if metrics_df['survival_binary'].nunique() > 1:
            print("\nGood: Variation in survival outcome detected!")
        else:
            print("\nWarning: All projects have same survival outcome")
            print("Need to adjust survival definition or find different repos")
    else:
        print("No processed_metrics.json found")
else:
    print("No method_out.json found")
