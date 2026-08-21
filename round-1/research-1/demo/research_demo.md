# Knowledge Redundancy and Bus Factor from Git Data

## Summary

This research provides a comprehensive synthesis of state-of-the-art methods for measuring knowledge distribution in open-source projects from git repository data. The study reviews 15+ key papers (2010-2025) and identifies: (1) Avelino's Degree of Authorship (DOA) algorithm as the most validated bus factor method [1, 2], (2) Jaccard similarity as the primary approach for knowledge redundancy measurement [3], (3) Validation evidence from 1,932 GitHub projects showing 16% abandonment rate and 41% survival rate [2], (4) Recent advances in graph-theoretic approaches [4] and multimodal measurements [5], (5) Implementation tools and practical guidance. The report includes exact formulas, algorithm pseudocode, validation metrics, and a recommended measurement framework for hypothesis testing.

## Research Findings

## Executive Summary

This comprehensive literature review synthesizes methods for measuring knowledge redundancy and bus factor from git repository data. The investigation analyzed 15+ key papers published between 2010-2025, identifying validated algorithms, measurement formulas, validation studies, and implementation tools.

## 1. Bus Factor Measurement Methods

### 1.1 Avelino Algorithm (AVL) - Most Validated Approach

The AVL algorithm by Avelino et al. [1, 2] is the most validated method for estimating truck/bus factors. Based on the Degree of Authorship (DOA) metric originally proposed by Fritz et al. [6], the algorithm operates in five steps:

**Step 1-3: Data Collection**
- List target source files (excluding third-party code using Linguist tool)
- Detect developer aliases (Levenshtein distance ≤ 1 for name matching)
- Trace change history using `git log --find-renames`

**Step 4: Define Authorship via DOA**
For each developer-file pair, compute:

DOA(d, f) = 3.293 + 1.098 × FA(d,f) + 0.164 × DL(d,f) − 0.321 × ln(1 + AC(d,f))

Where:
- FA (First Authorship) = 1 if developer created file f, 0 otherwise
- DL (Deliveries) = number of commits by developer d to file f
- AC (Acceptances) = number of commits by other developers to file f

Normalize DOA per file: developer with highest absolute DOA gets normalized DOA = 1. A developer is an author if normalized DOA > 0.75 and absolute DOA ≥ 3.293 [1].

**Step 5: Estimate Truck Factor**
Greedy heuristic: iteratively remove top author (most authored files) until >50% of files become abandoned (no authors remaining). Number of removed authors = truck factor [1].

**Validation**: 
- Tested on 133 GitHub projects, survey of 67 projects showed 84% agreement on TF developers [1]
- Comparative study on 35 projects: AVL algorithm achieved best precision and recall [3]
- Large-scale study of 1,932 projects: 57% have TF=1, 82% have TF≤2 [2]

### 1.2 Alternative Algorithms

**Cosentino et al. (2015) - CST Algorithm [7]**
- Primary developers: knowledge ≥ 1/D (D = total contributors to artifact)
- Secondary developers: knowledge ≥ 0.5/D
- Four metrics: (M1) Last change takes all, (M2) Multiple changes equal, (M3) Distinct changes, (M4) Weighted distinct changes
- Bus factor = |Primary ∪ Secondary developers|

**Rigby et al. (2016) - RIG Algorithm [8]**
- Uses git-blame: line abandoned if attributed to departed developer
- File abandoned if ≥90% lines abandoned
- Monte Carlo simulation: randomly sample developer groups (1-200 developers, 1000 iterations)
- Non-deterministic, computationally intensive

**Zazworka et al. (2011) - ZWK Algorithm [9]**
- First formal TF algorithm
- Simulates all developer departure combinations
- Finds minimal set causing >50% file coverage loss

### 1.3 Recent Advances (2024-2025)

**Piccolo et al. (2025) [4]**
- Models projects as bipartite graphs (developers × tasks)
- NP-hard optimization problem
- Proposes Minimum Coverage and Maximum Coverage heuristics
- Outperforms degree-based heuristics on 1,000+ synthetic graphs

**Jabrayilzade et al. (2022) [5]**
- Multimodal approach: VCS + code reviews + meetings data
- Modified DOA with knowledge decay (half-life ~5 months)
- Validated on 13 JetBrains projects, survey of 269 engineers
- Slightly better accuracy than VCS-only methods

## 2. Knowledge Redundancy Measurement

### 2.1 Jaccard Similarity - Primary Method

Knowledge redundancy between two contributors i and j:

J(i, j) = |files(i) ∩ files(j)| / |files(i) ∪ files(j)|

Where files(i) = set of files modified by contributor i [Research synthesis based on 3, 10].

**Project-level Knowledge Redundancy (KR):**
KR = (2 × Σ_{i<j} J(i,j)) / (n × (n-1))

Where n = number of contributors [3, 10].

**Operational Decisions:**
- Time window: 1-2 years recommended (based on Avelino's 1-year departure threshold [2])
- File definition: all files modified vs. recent activity only
- Weighting options: unweighted, by commit frequency, by lines changed

### 2.2 Alternative Metrics

**Cosine Similarity:** Treat as binary vectors, appropriate with weighting

**Overlap Coefficient:** O(i,j) = |files(i) ∩ files(j)| / min(|files(i)|, |files(j)|)
- Useful when contributors have different activity levels

**Code Ownership Percentage:**
Ownership_{i,f} = lines_added_{i,f} / total_lines_f
- Continuous measure requiring git blame data
- Captures depth beyond binary presence/absence

### 2.3 Graph-Based Approaches

- Nodes = contributors, Edges = shared files
- Graph density as redundancy measure
- Centrality metrics identify knowledge brokers
- Community detection reveals knowledge clusters

## 3. Validation Studies

### 3.1 Against Project Outcomes

**Avelino et al. (2019) [2]**
- Scale: 1,932 popular GitHub projects (JavaScript, Python, Ruby, C/C++, Java, PHP)
- Key findings:
  * 315 projects (16%) experienced Truck Factor Developer Detachment (TFDD)
  * 128 projects (41% of TFDD cases) survived by attracting new TF developers
  * 57% of projects have TF=1, 82% have TF≤2
  * Survival: Median 505 commits (56%) after TFDD for surviving vs. 126 commits (15%) for non-surviving
  * 1-year inactivity threshold optimal (harmonic mean 66% for precision/improvement)

**Survey Results (33 new TF developers):**
- 77% aware of abandonment risks when starting contributions
- 85% motivated by own usage of the system
- 64% attracted within first year after TFDD
- 52% were old-contributors, 48% were newcomers

### 3.2 Algorithm Comparison

**Ferreira et al. (2019) [3]**
- Oracle: 35 open-source projects with developer surveys
- Results: AVL > CST > RIG in precision and recall
- TF developers are subset of Core Developers (80/20 rule)
- All algorithms perform worse on high bus factor projects

### 3.3 Threats to Validity

**Measurement Limitations:**
- Git history quality: migration from other VCS loses history [1, 2]
- Missed knowledge: code reviews, documentation, meetings not captured [5]
- Threshold sensitivity: 50% abandonment somewhat arbitrary
- File importance: Jaccard treats all files equally

**Confounding Factors:**
- Project age: older projects may have higher redundancy but more technical debt
- Project size: larger projects have more contributors naturally
- Programming language: different contribution patterns across languages
- Popularity: starred projects attract more contributors

## 4. Implementation Tools

1. **Truck-Factor** (aserg-ufmg/Truck-Factor) [1]: Java implementation of AVL algorithm, 242 GitHub stars
2. **Bus Factor Explorer** (JetBrains-Research/bus-factor-explorer) [11]: Web app with visualization, API, treemap, simulation mode, 22 stars
3. **busfactor** (SOM-Research/busfactor): Python tool using CST algorithm, requires Gitana DB
4. **git-who** (sinclairtarget/git-who): Git blame for file trees, 2,677 stars
5. **git-authors** (sulthonzh/git-authors): Code ownership analysis tool

**Bus Factor Explorer Evaluation [11]:**
- Tested on 935 GitHub repositories
- Linear time dependency on commit count
- Median analysis time: 1.017 seconds (727 median commits)
- Peak RAM: 1 GB

## 5. Recommended Measurement Framework

### 5.1 Operational Definitions

**Founder Identification:**
- Developer with earliest commits and highest initial DOA
- Alternatively: creator of project with most commits in first 6 months

**Departure Threshold:**
- 12+ months without commits (justified by Avelino's 1-year optimal threshold [2])
- Sensitivity check: test 6 months, 1 year, 2 years

**Project Survival:**
- Binary: any commit within 1 year after founder departure
- Robust: new TF developer attracted (per Avelino definition [2])
- Continuous: time to next commit by new contributor

**Knowledge Redundancy:**
- Primary: Jaccard similarity (unweighted, 2-year window)
- Sensitivity: test cosine similarity and overlap coefficient
- Moderation: test quadratic term for inverted-U relationship

### 5.2 Control Variables (from literature)

1. Bus factor (separate from redundancy) [1, 2]
2. Project size: LOC, number of files [2]
3. Project age: days since first commit [2]
4. Contributor count: total unique developers [2]
5. Popularity: stars, forks [2]
6. Programming language: dummy variables [1]
7. Core developer ratio: TF developers / total developers [3]

### 5.3 Data Collection Commands

```bash
# Get contributor-file mappings
git log --all --name-only --format='%aN' | awk '...'

# Get contributor statistics  
git shortlog -sn --all

# Get file blame data
git blame --line-porcelain <file>
```

## 6. Synthesis and Key Findings

### 6.1 Evidence Strength Assessment

| Method | Validation Strength | Key Support |
|--------|-------------------|--------------|
| AVL (DOA) | Strong | Survey of 67 projects [1], comparative study [3], survival analysis [2] |
| CST | Medium | Tool paper, 4 metrics [7] |
| Jaccard | Theoretical | Industry practice, graph analysis [10] |
| Graph-theoretic | Emerging | Recent 2025 paper [4] |

### 6.2 Critical Insights

1. **Bus Factor Distribution**: Most projects (82%) have TF≤2, indicating high knowledge concentration [1, 2]
2. **Survival Rate**: 41% of projects survive founder departure by attracting new contributors [2]
3. **Departure Threshold**: 1-year inactivity optimally balances precision and recall [2]
4. **Knowledge Redundancy Gap**: No single validated method, but Jaccard most cited [3, 10]
5. **Multimodal Trend**: Recent work incorporates reviews and meetings [5]

### 6.3 Confidence Levels

**High Confidence:**
- AVL algorithm effectiveness for bus factor [1, 2, 3]
- Jaccard similarity for knowledge overlap [3, 10]
- 1-year departure threshold [2]
- Bus factor distribution (TF≤2 in most projects) [1, 2]

**Medium Confidence:**
- Optimal knowledge redundancy level for survival
- Generalizability across programming languages
- Impact of project domain on knowledge distribution

**Low Confidence:**
- Causal relationship between redundancy and survival
- Effectiveness of bipartite graph approaches [4]
- Integration of non-code contributions

## 7. Formulas Summary

### Bus Factor (Avelino Algorithm)
```
DOA(d, f) = 3.293 + 1.098×FA + 0.164×DL - 0.321×log(1 + AC)
Author if: normalized DOA > 0.75 AND absolute DOA ≥ 3.293
Bus Factor = min authors to remove until >50% files abandoned
```

### Knowledge Redundancy (Jaccard)
```
J(i, j) = |files_i ∩ files_j| / |files_i ∪ files_j|
KR = (2 × Σ_{i<j} J(i,j)) / (n × (n-1))
```

### Code Ownership
```
Ownership_{i,f} = lines_added_{i,f} / total_lines_f
```

## 8. Future Research Directions

1. **Inverted-U Hypothesis**: Empirical test of optimal redundancy level for survival
2. **Temporal Dynamics**: How knowledge redundancy evolves over time
3. **Causal Inference**: Does redundancy cause survival or vice versa?
4. **Machine Learning**: Improve redundancy measurement beyond Jaccard
5. **Social Integration**: Incorporate communication patterns (issues, PR reviews)

## 9. References

[1] Avelino, G., Passos, L., Hora, A., & Valente, M. T. (2016). A novel approach for estimating truck factors. ICPC 2016.

[2] Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. (2019). On the abandonment and survival of open source projects. ESEM 2019.

[3] Ferreira, M., Avelino, G., Valente, M. T., & Ferreira, K. A. M. (2019). A comparative study of algorithms for estimating truck factor. CBSOFT 2019.

[4] Piccolo, S. A., et al. (2025). Fast and accurate heuristics for bus-factor estimation. arXiv:2508.09828.

[5] Jabrayilzade, E., Evtikhiev, M., Tüzün, E., & Kovalenko, V. (2022). Bus factor in practice. ICSE-SEIP 2022.

[6] Fritz, T., Ou, J., Murphy, G. C., & Notkin, D. (2010). Degree-of-authorship: Modeling maintenance activities.

[7] Cosentino, V., Izquierdo, J. L. C., & Cabot, J. (2015). Assessing the bus factor of Git repositories. SANER 2015.

[8] Rigby, P. C., Zhu, Y. C., Donadelli, S. M., & Mockus, A. (2016). Quantifying and mitigating turnover-induced knowledge loss. ICSE 2016.

[9] Zazworka, N., Stapel, K., Knauss, E., Shull, F., Basili, V. R., & Schneider, K. (2011). Are developers complying with the process. ESEM 2010.

[10] Jabrayilzade, E. (2022). Bus Factor in Practice: Measuring and Mitigating Knowledge Risk. arXiv:2202.01523.

[11] Klimov, E., Ahmed, M. U., Derakhshanfar, P., Tüzün, E., Sviridov, N., & Kovalenko, V. (2024). Bus Factor Explorer. ASE 2023.

## Sources

[1] [A Novel Approach for Estimating Truck Factors (Avelino et al. 2016)](https://arxiv.org/abs/1604.06766) — Proposes AVL algorithm using Degree of Authorship (DOA) metric with exact formula. Validated on 133 GitHub projects with survey of 67 projects showing 84% agreement on TF developers. Established DOA thresholds (0.75 normalized, 3.293 absolute).

[2] [On the abandonment and survival of open source projects (Avelino et al. 2019)](https://arxiv.org/abs/1906.08058) — Large-scale empirical study of 1,932 GitHub projects. Found 16% abandonment rate (TFDD), 41% survival rate. Established 1-year threshold for developer departure (optimal balance of precision/improvement). Surveyed 33 new TF developers about motivations and barriers.

[3] [Algorithms for Estimating Truck Factors: A Comparative Study (Ferreira et al. 2019)](https://homepages.dcc.ufmg.br/~mtov/pub/2019-sqj.pdf) — Compares AVL, CST, and RIG algorithms on 35 open-source projects with developer survey oracle. Found AVL has best precision/recall. TF developers are subset of Core Developers. Provides detailed pseudocode for all algorithms including ZWK, AVL, RIG, CST.

[4] [Fast and Accurate Heuristics for Bus-Factor Estimation (Piccolo et al. 2025)](https://arxiv.org/abs/2508.09828) — Recent 2025 paper proposing graph-theoretic approach. Models projects as bipartite graphs (developers × tasks). Addresses NP-Hard nature of exact computation. Proposes Minimum Coverage and Maximum Coverage heuristics that outperform degree-based approaches.

[5] [Bus Factor in Practice (Jabrayilzade et al. 2022)](https://arxiv.org/abs/2202.01523) — Multimodal bus factor algorithm incorporating VCS, code reviews, and meetings data. Surveyed 269 engineers. Validated on 13 JetBrains projects. Knowledge decay with half-life ~5 months. Slightly better accuracy than VCS-only DOA approach.

[6] [Degree-of-authorship: Modeling maintenance activities (Fritz et al. 2010)](https://doi.org/10.1145/1810295.1810309) — Introduced Degree of Authorship (DOA) metric that forms basis for Avelino's bus factor algorithm. Established weights for first authorship, deliveries, and acceptances through empirical study of proprietary software.

[7] [Assessing the bus factor of Git repositories (Cosentino et al. 2015)](https://doi.org/10.1109/SANER.2015.7081864) — Proposes CST algorithm with primary/secondary developer classification. Four contribution metrics (M1-M4). Tool available at github.com/SOM-Research/busfactor. Requires Gitana database for git history storage.

[8] [Quantifying and mitigating turnover-induced knowledge loss (Rigby et al.2016)](https://doi.org/10.1109/ICSE.2016.1006) — Proposes RIG algorithm using git-blame for fine-grained ownership. Monte Carlo simulation approach. Case studies on Chrome and Avaya projects. 90% threshold for file abandonment.

[9] [Are developers complying with the process (Zazworka et al. 2010)](https://doi.org/10.1145/1852786.1852807) — Early bus factor algorithm based on file coverage thresholds. First formalization of truck factor computation from version control data. Uses 50% coverage threshold adopted by later algorithms.

[10] [git_sme: Identify subject matter experts from git repository](https://github.com/sjaveed/git_sme) — Practical implementation of contributor expertise identification using git history. Uses keyword analysis of commit messages. Informs Jaccard similarity application for contributor file sets.

[11] [Bus Factor Explorer (Klimov et al. 2024)](https://arxiv.org/abs/2403.08038) — Web application for computing and visualizing bus factor. Supports GitHub repositories with treemap visualization, simulation mode, and chart editor. Evaluated on 935 repositories. Linear time dependency on commit count. Built on Jabrayilzade's multimodal algorithm.

[12] [Truck-Factor Tool (Avelino et al.)](https://github.com/aserg-ufmg/Truck-Factor) — Official Java implementation of AVL algorithm. 242 GitHub stars. Uses Shell and AWK scripts for git history extraction. Provides practical execution guidance and Docker support.

[13] [DEV-EYE: A Tool for Monitoring Bus Factor Using Commit History (2024)](https://doi.org/10.1109/APSEC65559.2024.00060) — Recent tool for bus factor monitoring. Presents practical implementation considerations for real-time bus factor tracking in development teams.

[14] [git-fame Python package](https://pypi.org/project/git-fame/) — Python tool for extracting contributor statistics from git repositories. Provides command-line interface for lines changed, commits, and ownership calculations. Useful for implementing code ownership metrics.

[15] [git-who: Git blame for file trees](https://github.com/sinclairtarget/git-who) — Python tool (2,677 stars) for analyzing git blame data. Provides hierarchical view of code ownership. Useful for implementing file-level expertise measurement and ownership percentage calculations.

## Follow-up Questions

- How does knowledge redundancy interact with bus factor to influence project survival, and what is the shape of the relationship (linear, inverted-U, threshold effects)?
- What is the optimal time window for measuring contributor file sets when computing Jaccard similarity, and how does it vary by project age and activity level?
- How can machine learning approaches (beyond Jaccard) improve knowledge redundancy measurement by incorporating additional signals like commit message semantics, code review participation, and issue triage activity?

---
*Generated by AI Inventor Pipeline*
