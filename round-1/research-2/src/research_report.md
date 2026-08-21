# Knowledge Redundancy Measurement and Survival Analysis Validation for OSS Projects

## Summary

## Executive Summary

This research provides exhaustive validation of the technical feasibility of measuring knowledge redundancy from git commit data and testing the inverted-U hypothesis about OSS project survival after founder departure. The investigation covers measurement validation, statistical methodology, data collection feasibility, and statistical power requirements with extensive literature review.

## Phase 1: Knowledge Redundancy Measurement Validation

### 1.1 Jaccard Similarity for File Modification Overlap

**Finding**: Jaccard similarity (|A∩B|/|A∪B|) is a standard measure for set overlap [1], but its application to measuring 'knowledge redundancy' in OSS projects requires careful consideration. The literature directly validating Jaccard for knowledge overlap in git contexts is limited.

**Weighted Jaccard**: Available for positive vectors [1]. J_w(A,B) = Σ min(a_i, b_i) / Σ max(a_i, b_i) where weights = commit counts.

**Overlap Coefficient vs Jaccard**: Overlap coefficient = |A∩B|/min(|A|,|B|) [14]. Preferred for different-sized sets [15]. Jaccard penalizes differences more [16].

**Recommendation**: Jaccard baseline + sensitivity analysis with weighted Jaccard, overlap coefficient, and DOA [2][3].

### 1.2 Degree of Authorship (DOA) Metric

**DOA Formula** (Avelino et al. 2016 [17]): DOA = 3.293 + 1.098×FA + 0.164×DL − 0.321×ln(1+AC)
- FA: First Authorship (binary, strongest predictor)
- DL: Deliveries (number of changes)
- AC: Acceptances (changes by others, logarithmic decay)

**Validation**: 84% agreement in survey of 67 GitHub projects [17].

### 1.3 Alternative Measures

**HHI Index**: HHI = Σ s_i² [18]. Ranges 1/N to 1. >0.15 = moderate concentration.
**Shannon Entropy**: H = -Σ p_i log(p_i) [4]. Higher = more diverse.

## Phase 2: Survival Analysis Methodology

### 2.1 Cox Model for Inverted-U Test

**Model**: h(t,X) = h_0(t) * exp(β₁*X + β₂*X² + β₃*Z)
- Inverted-U: β₁ > 0 AND β₂ < 0
- Hazard ratio = exp(β₁ + 2*β₂*X), depends on X [7]
- Turning point = -β₁/(2*β₂) [7]

**Time-Varying Covariates**: Use CoxTimeVaryingFitter in lifelines [19].

### 2.2 Survival Definition

**Validated** (Avelino et al. [3]):
- Event: No commits from core contributors for 12+ months
- Threshold validated: 1-year best harmonic mean (66%) across 5 thresholds
- Censoring: Right-censoring at data collection end

**Competing Risks**: Consider Fine-Gray model [20].

## Phase 3: Control Variables

### 3.1 Bus Factor Algorithm

**Recommendation**: Avelino et al. DOA algorithm [3][17]
- Validated: 84% agreement (67 projects)
- Best precision/recall (SBCARS 2016) [21]
- Implementation: https://github.com/aserg-ufmg/Truck-Factor

### 3.2 Project Characteristics

**Validated Measures** (Ali et al. [5], Avelino et al. [3]):
1. Age: Days first commit to founder departure
2. Size: Commits, files (log-transformed)
3. Popularity: Stars, forks, contributors (HR=0.997 [5])
4. Releases: Binary (HR=0.15 [5])

## Phase 4: Statistical Power

**Rule**: 10 events per variable [9]
**Variables**: ~10-15
**Expected Events**: 2000 × 15% × 60% = 180
**Conclusion**: Sufficient power.

## Phase 5: Data Collection

### 5.1 GitHub API

**Rate Limits** [10]: 5000/hour authenticated, 5000 points/hour GraphQL [11]
**GraphQL Optimization** [22][23][24]: 60-80% reduction in calls vs. REST
**Time Estimate**: 2 hours for 2000 repos (3-5 GraphQL calls/repo)

### 5.2 Founder Departure

**Algorithm** [3]:
1. Founder = most commits first 6 months
2. 12+ months inactivity after last commit
3. Edge case: <6 commits in 12 months = departed

**Validation**: Manual check 30-50 samples.

## Phase 6: Synthesis

### 6.1 Pipeline

**Scripts**:
1. 01_collect_data.py: GraphQL API
2. 02_compute_measurements.py: Jaccard, DOA, HHI, bus factor
3. 03_survival_analysis.py: Cox model, quadratic term
4. 04_sensitivity_analysis.py: Robustness checks

### 6.2 Diagnostics

1. Proportional hazards: Schoenfeld test (p > 0.05)
2. Linearity: Martingale residuals
3. Collinearity: VIF < 5
4. Quadratic term: Likelihood ratio test

## Confidence Assessment

**High**: Cox model, Avelino algorithm, 2000 projects power, GraphQL feasibility
**Medium**: Jaccard validity, 12-month threshold
**Low**: Optimal weighting, knowledge decay, competing risks

## Key Recommendations

1. Jaccard + DOA/HHI sensitivity
2. Avelino DOA bus factor algorithm
3. Cox PH with quadratic term + diagnostics
4. GitHub GraphQL API with caching
5. 2000 projects sufficient
6. Validate 30-50 founder departures

## References

[1] Jaccard Index - Wikipedia
[2] DOA Explanation - ContributorIQ
[3] Avelino et al. (2019) arXiv:1906.08058
[4] Shannon Entropy - Wikipedia
[5] Ali et al. (2020) MSR '20
[6] Cox Model - Wikipedia
[7] Cox Quadratic Interpretation - Cross Validated
[8] Cosentino et al. (2015) IEEE SANER
[9] Power Analysis - Stata
[10] GitHub Rate Limits
[11] GraphQL vs REST - GitHub
[12] GHTorrent Status
[13] Software Heritage MSR 2019
[14] Overlap Coefficient - Wikipedia
[15] Jaccard vs Overlap - NVIDIA

## Research Findings

## Executive Summary

This research provides exhaustive validation of the technical feasibility of measuring knowledge redundancy from git commit data and testing the inverted-U hypothesis about OSS project survival after founder departure. The investigation covers measurement validation, statistical methodology, data collection feasibility, and statistical power requirements with extensive literature review.

## Phase 1: Knowledge Redundancy Measurement Validation

### 1.1 Jaccard Similarity for File Modification Overlap

**Finding**: Jaccard similarity (|A∩B|/|A∪B|) is a standard measure for set overlap [1], but its application to measuring 'knowledge redundancy' in OSS projects requires careful consideration. The literature directly validating Jaccard for knowledge overlap in git contexts is limited.

**Weighted Jaccard**: Available for positive vectors [1]. J_w(A,B) = Σ min(a_i, b_i) / Σ max(a_i, b_i) where weights = commit counts.

**Overlap Coefficient vs Jaccard**: Overlap coefficient = |A∩B|/min(|A|,|B|) [14]. Preferred for different-sized sets [15]. Jaccard penalizes differences more [16].

**Recommendation**: Jaccard baseline + sensitivity analysis with weighted Jaccard, overlap coefficient, and DOA [2][3].

### 1.2 Degree of Authorship (DOA) Metric

**DOA Formula** (Avelino et al. 2016 [17]): DOA = 3.293 + 1.098×FA + 0.164×DL − 0.321×ln(1+AC)
- FA: First Authorship (binary, strongest predictor)
- DL: Deliveries (number of changes)
- AC: Acceptances (changes by others, logarithmic decay)

**Validation**: 84% agreement in survey of 67 GitHub projects [17].

### 1.3 Alternative Measures

**HHI Index**: HHI = Σ s_i² [18]. Ranges 1/N to 1. >0.15 = moderate concentration.
**Shannon Entropy**: H = -Σ p_i log(p_i) [4]. Higher = more diverse.

## Phase 2: Survival Analysis Methodology

### 2.1 Cox Model for Inverted-U Test

**Model**: h(t,X) = h_0(t) * exp(β₁*X + β₂*X² + β₃*Z)
- Inverted-U: β₁ > 0 AND β₂ < 0
- Hazard ratio = exp(β₁ + 2*β₂*X), depends on X [7]
- Turning point = -β₁/(2*β₂) [7]

**Time-Varying Covariates**: Use CoxTimeVaryingFitter in lifelines [19].

### 2.2 Survival Definition

**Validated** (Avelino et al. [3]):
- Event: No commits from core contributors for 12+ months
- Threshold validated: 1-year best harmonic mean (66%) across 5 thresholds
- Censoring: Right-censoring at data collection end

**Competing Risks**: Consider Fine-Gray model [20].

## Phase 3: Control Variables

### 3.1 Bus Factor Algorithm

**Recommendation**: Avelino et al. DOA algorithm [3][17]
- Validated: 84% agreement (67 projects)
- Best precision/recall (SBCARS 2016) [21]
- Implementation: https://github.com/aserg-ufmg/Truck-Factor

### 3.2 Project Characteristics

**Validated Measures** (Ali et al. [5], Avelino et al. [3]):
1. Age: Days first commit to founder departure
2. Size: Commits, files (log-transformed)
3. Popularity: Stars, forks, contributors (HR=0.997 [5])
4. Releases: Binary (HR=0.15 [5])

## Phase 4: Statistical Power

**Rule**: 10 events per variable [9]
**Variables**: ~10-15
**Expected Events**: 2000 × 15% × 60% = 180
**Conclusion**: Sufficient power.

## Phase 5: Data Collection

### 5.1 GitHub API

**Rate Limits** [10]: 5000/hour authenticated, 5000 points/hour GraphQL [11]
**GraphQL Optimization** [22][23][24]: 60-80% reduction in calls vs. REST
**Time Estimate**: 2 hours for 2000 repos (3-5 GraphQL calls/repo)

### 5.2 Founder Departure

**Algorithm** [3]:
1. Founder = most commits first 6 months
2. 12+ months inactivity after last commit
3. Edge case: <6 commits in 12 months = departed

**Validation**: Manual check 30-50 samples.

## Phase 6: Synthesis

### 6.1 Pipeline

**Scripts**:
1. 01_collect_data.py: GraphQL API
2. 02_compute_measurements.py: Jaccard, DOA, HHI, bus factor
3. 03_survival_analysis.py: Cox model, quadratic term
4. 04_sensitivity_analysis.py: Robustness checks

### 6.2 Diagnostics

1. Proportional hazards: Schoenfeld test (p > 0.05)
2. Linearity: Martingale residuals
3. Collinearity: VIF < 5
4. Quadratic term: Likelihood ratio test

## Confidence Assessment

**High**: Cox model, Avelino algorithm, 2000 projects power, GraphQL feasibility
**Medium**: Jaccard validity, 12-month threshold
**Low**: Optimal weighting, knowledge decay, competing risks

## Key Recommendations

1. Jaccard + DOA/HHI sensitivity
2. Avelino DOA bus factor algorithm
3. Cox PH with quadratic term + diagnostics
4. GitHub GraphQL API with caching
5. 2000 projects sufficient
6. Validate 30-50 founder departures

## References

[1] Jaccard Index - Wikipedia
[2] DOA Explanation - ContributorIQ
[3] Avelino et al. (2019) arXiv:1906.08058
[4] Shannon Entropy - Wikipedia
[5] Ali et al. (2020) MSR '20
[6] Cox Model - Wikipedia
[7] Cox Quadratic Interpretation - Cross Validated
[8] Cosentino et al. (2015) IEEE SANER
[9] Power Analysis - Stata
[10] GitHub Rate Limits
[11] GraphQL vs REST - GitHub
[12] GHTorrent Status
[13] Software Heritage MSR 2019
[14] Overlap Coefficient - Wikipedia
[15] Jaccard vs Overlap - NVIDIA
[16] Similarity Coefficients - Medium
[17] Avelino et al. (2016) arXiv:1604.06766
[18] HHI Index - Wikipedia
[19] Time-varying lifelines
[20] Competing Risks - PMC
[21] Truck Factor Comparison - SBCARS 2016
[22] GraphQL Examples - Tracy Lum
[23] GraphQL Pagination - GitHub
[24] GraphQL Efficiency - Steve Mar

## Sources

[1] [Jaccard Index - Wikipedia](https://en.wikipedia.org/wiki/Jaccard_index) — Defines Jaccard similarity, weighted Jaccard for positive vectors

[2] [DOA Explanation](https://contributoriq.com/blog/degree-of-authorship-code-ownership-explained) — DOA metric with FA, DL, AC components

[3] [Avelino et al. (2019)](https://arxiv.org/abs/1906.08058) — 1932 GitHub projects, 16% TFDD, 41% survival, 1-year threshold validated

[4] [Shannon Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) — Measures diversity for knowledge distribution

[5] [Ali et al. (2020)](http://www1.chapman.edu/~linstead/aliMSR2020.pdf) — Cox model 2059 projects, HR=0.997 per contributor

[6] [Cox Proportional Hazards](https://en.wikipedia.org/wiki/Proportional_hazards_model) — Cox model assumptions and hazard ratios

[7] [Cox Quadratic Term](https://stats.stackexchange.com/questions/386563) — Hazard ratio depends on current value, turning point formula

[8] [Cosentino et al. (2015)](https://ieeexplore.ieee.org/document/7081864/) — Bus factor algorithms for git repos

[9] [Power Analysis Cox](https://www.stata.com/manuals15/psspowercox.pdf) — 10 events per variable rule

[10] [GitHub Rate Limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) — 5000 requests/hour authenticated

[11] [GraphQL vs REST](https://docs.github.com/en/rest/about-the-rest-api/comparing-githubs-rest-api-and-graphql-api) — GraphQL more efficient for batch queries

[12] [GHTorrent Status](https://github.com/ghtorrent/ghtorrent.org) — Stopped 2019, outdated

[13] [Software Heritage](https://dl.acm.org/doi/10.1145/3379597.3387510) — Largest source code archive, 3-6 month lag

[14] [Overlap Coefficient](https://en.wikipedia.org/wiki/Overlap_coefficient) — |A∩B|/min(|A|,|B|), different-sized sets

[15] [Jaccard vs Overlap](https://developer.nvidia.com/blog/similarity-in-graphs-jaccard-versus-the-overlap-coefficient/) — Overlap for subset relationships

[16] [Similarity Coefficients](https://medium.com/@igniobydigitate/similarity-coefficients) — Jaccard vs Overlap comparison

[17] [Avelino et al. (2016)](https://arxiv.org/abs/1604.06766) — DOA formula, 84% survey agreement

[18] [HHI Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) — Concentration measure for knowledge distribution

[19] [Time-varying lifelines](https://lifelines.readthedocs.io/en/latest/Time+varying+survival+regression.html) — CoxTimeVaryingFitter documentation

[20] [Competing Risks](https://pmc.ncbi.nlm.nih.gov/articles/PMC5764182/) — Fine-Gray model for competing events

[21] [Truck Factor Comparison](https://doi.org/10.1109/sbcars.2016.20) — Avelino best precision/recall

[22] [GraphQL Examples](https://www.tracylum.com/blog/2017-09-09-querying-githubs-graphql-api/) — GitHub GraphQL query examples

[23] [GraphQL Pagination](https://docs.github.com/en/graphql/guides/using-pagination-in-the-graphql-api) — Cursor-based pagination documentation

[24] [GraphQL Efficiency](https://www.stevemar.net/github-graphql-vs-rest/) — 60-80% reduction in API calls

## Follow-up Questions

- What is the optimal threshold for defining project abandonment after founder departure, and how sensitive are results to this choice (6 vs. 12 vs. 18 months)?
- How does Jaccard similarity compare to DOA-based and HHI-based measures in terms of predictive validity for project survival?
- What is the actual founder departure rate in popular GitHub repositories, and how does it vary by project characteristics?

---
*Generated by AI Inventor Pipeline*
