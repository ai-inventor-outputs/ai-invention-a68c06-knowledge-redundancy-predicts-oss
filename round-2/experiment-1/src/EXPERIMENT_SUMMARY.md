# OSS Survival Experiment Summary

## Experiment Status: COMPLETED (with limitations)

### What Was Done

1. Implemented fallback approach using pseudo-KR from file_count distributions
2. Processed 500,000 commit records from 13 repositories
3. Detected founder departures using Avelino et al. (2019) threshold
4. Measured survival using TFDD definition
5. Computed pseudo-KR using cosine similarity

### Results

- Repos processed: 6 with founder departure detected
- Survival rate: 100% (all repos survived)
- KR range: 0.119 to 0.969
- Statistical analysis: Not possible due to no variation

### Key Limitations

1. Insufficient sample size (need 30+ repos)
2. No survival variation (dataset bias)
3. Fallback KR measure (no file paths for Jaccard)
4. Large repos excluded for performance

### Methodology Note

Fallback approach used per artifact plan Scenario 1.
Pseudo-KR computed from file_count distributions.
