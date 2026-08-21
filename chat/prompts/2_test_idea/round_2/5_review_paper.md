# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_rhx_UB8HZyTw` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 01:33:19 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
# Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study

## Abstract

Open-source software projects frequently depend on a small number of core developers, and founder departure is a major threat to project continuity. While the "bus factor" (the minimal number of developers whose departure would stall a project) is well-studied, it fails to capture an important dimension: the degree of overlap in what contributors know. This paper introduces *knowledge redundancy*—the average pairwise overlap in contributor expertise areas—as a distinct construct for predicting post-founder project survival. We hypothesize an inverted-U relationship: projects with moderate redundancy survive at higher rates than both those with very low redundancy and those with very high redundancy. We present a methodological framework for measuring knowledge redundancy from git commit data using Jaccard similarity and testing the hypothesis using survival analysis. Applying this framework to a dataset of 500,000 commits from 13 open-source repositories, we identify founder departure events in 6 repositories. Due to data limitations (lack of file path information for Jaccard computation) and complete survival of all 6 projects, we could not statistically test the inverted-U hypothesis. Instead, we report descriptive patterns and provide open-source tools for future large-scale validation. Our conceptual analysis suggests that knowledge redundancy captures a dimension of project resilience not reflected in bus factor alone, offering a foundation for future empirical work.

**Keywords:** open-source software, project survival, knowledge redundancy, bus factor, founder departure, survival analysis

## 1. Introduction

Open-source software (OSS) projects form the backbone of modern software infrastructure, yet their sustainability remains precarious. A central threat to project continuity is the departure of founders—the original creators who often hold critical, undocumented knowledge about design decisions, codebase structure, and project vision [1]. When founders leave, projects face an elevated risk of abandonment: Avelino et al. [1] found that 16% of 1,932 GitHub projects experienced founder departure, with only 41% surviving this transition.

The dominant framework for understanding this risk is the "bus factor" (also called truck factor)—the minimal number of developers whose simultaneous departure would render a project unable to continue [2]. A project with bus factor = 1 has a single point of failure; higher values indicate more distributed knowledge. While bus factor measurement has matured through multiple validated algorithms [1, 2, 3], it captures only the *number* of critical contributors, not the *structure* of their knowledge.

Consider two projects, both with bus factor = 2. In the first, the two critical contributors work on completely different subsystems (low knowledge redundancy). In the second, they work on largely overlapping code areas (high knowledge redundancy). Bus factor alone cannot distinguish these cases, yet their resilience to founder departure may differ substantially. Low redundancy leaves the project vulnerable because no one else understands the founder's domain; high redundancy wastes human resources on duplication rather than specialization.

This paper introduces *knowledge redundancy* as a measurable construct distinct from bus factor. Knowledge redundancy is defined as the average pairwise Jaccard similarity in the sets of files modified by project contributors. We hypothesize an **inverted-U relationship** between knowledge redundancy and survival: projects with moderate redundancy survive best, while both very low and very high redundancy lead to lower survival rates. This prediction draws from three cross-disciplinary analogies: (1) error-correcting codes in information theory, which use controlled redundancy to enable recovery from data loss; (2) organizational psychology research showing that moderate expertise overlap enables backup behavior during member absence [12]; and (3) the diversity-stability hypothesis in ecology, where ecosystems with moderate redundancy in species roles are most resilient to disturbance.

Our study makes the following contributions:

1. **Conceptual**: We define knowledge redundancy as a distinct construct from bus factor and demonstrate its theoretical relevance to OSS survival.

2. **Methodological**: We provide a complete measurement framework for computing knowledge redundancy from git commit data using Jaccard similarity, including fallback approaches when file path data are unavailable [ARTIFACT:art_iicMCU3WgldY].

3. **Empirical**: We apply our framework to 500,000 commits from 13 open-source repositories, identifying 6 founder departure events and computing pseudo-knowledge redundancy scores. While data limitations prevented statistical hypothesis testing, we report descriptive patterns and validate our approach on synthetic data [ARTIFACT:art_pOI-AO_xwHdm].

4. **Practical**: We provide open-source tools and methodological guidance for future large-scale validation studies with adequate sample sizes and proper file path data.

The remainder of this paper is organized as follows. Section 2 reviews related work on bus factor, knowledge distribution, and OSS survival. Section 3 describes our data collection and measurement methodology, including limitations. Section 4 presents our statistical analysis approach. Section 5 reports descriptive results and methodological validation. Section 6 discusses implications, limitations, and future work. Section 7 concludes.

[FIGURE:fig1]

## 2. Related Work

### 2.1 Bus Factor and Knowledge Distribution

The bus factor concept originated in practitioner literature and was formalized through multiple algorithms. Avelino et al. [1] introduced the Degree of Authorship (DOA) algorithm, which computes contributor expertise using file creation, commit count, and other-contributor activity. A developer is considered an author of a file if DOA exceeds a threshold and constitutes 75% of the maximum DOA for that file. The bus factor is then the minimum number of top authors to remove until more than 50% of files are abandoned. This algorithm achieved the best precision and recall in a comparative study of 35 open-source projects [4].

Cosentino et al. [2] proposed the CST algorithm, which defines primary developers (≥ 1/N of contributions) and secondary developers (0.5/N to 1/N), with bus factor as the union of both sets. Recent work by Jabrayilzade et al. [6] extends DOA to incorporate code reviews and meeting data, while Piccolo et al. [7] propose graph-theoretic approaches modeling projects as bipartite developer-task graphs.

Despite this rich literature on *measuring* bus factor, prior work has not examined the *overlap* in contributor knowledge as a distinct dimension. Bus factor counts critical contributors; knowledge redundancy measures how much they overlap.

### 2.2 Open-Source Project Survival

Avelino et al. [1] conducted the largest empirical study of OSS survival to date, analyzing 1,932 GitHub projects. They defined "Truck Factor Developer Detachment" (TFDD) as the event where all truck factor developers have been inactive for ≥1 year, and measured survival as the project's ability to attract new truck factor developers. Their sensitivity analysis validated the 12-month threshold, which achieved the highest harmonic mean (0.66) across precision and recall.

Qiu et al. [3] applied survival analysis (Kaplan-Meier estimator, Cox proportional hazards) to study sustained participation in OSS, defining disengagement as 12 months of inactivity. Ferreira et al. [8] examined core developer turnover in Brazilian OSS projects, finding that 59.7% of projects experience ≥30% annual turnover. Coelho et al. [9] used machine learning to classify project maintenance status, finding that 16% of active projects become unmaintained within one year.

Recent work by Miller et al. [10] examines how write access provisioning and organizational ownership affect project novelty and survival, while Choudhary et al. [11] studies how demographic and motivational diversity among contributors impacts survival. Our work differs by focusing on *knowledge* diversity/redundancy rather than demographic diversity or governance mechanisms.

### 2.3 Knowledge Redundancy in Teams

The concept of knowledge redundancy in teams appears in organizational psychology and management literature. Research on "transactive memory systems" shows that teams with moderate overlap in expertise can provide backup behavior when members are absent, but excessive overlap reduces specialization benefits [12]. Wegner [14] introduced the transactive memory framework, which Ren and Argote [12] later synthesized across 25 years of research.

In software engineering, Fritz et al. [13] introduced the Degree of Knowledge (DOK) metric to measure code ownership, finding that knowledge distribution affects maintenance effort. However, no prior work has empirically tested an inverted-U relationship between knowledge redundancy (measured via Jaccard similarity) and project survival after founder departure.

### 2.4 Novelty of This Work

To assess novelty, we searched for prior work combining "knowledge redundancy," "Jaccard similarity," and "project survival" in venues including ICSE, FSE, ESEC, EMSE, and TSE. While related concepts appear in transactive memory literature [12, 14] and bus factor research [1, 2, 6], the specific combination of:
- Jaccard similarity for measuring knowledge overlap in OSS,
- Survival analysis for founder departure events,
- Testing an inverted-U hypothesis,

appears to be novel. Our literature search did not identify prior work proposing and empirically evaluating this specific relationship.

## 3. Methodology

### 3.1 Data Collection

We collected commit history data from 13 open-source repositories on GitHub, comprising 500,000 commit records (Table 1). The data were sourced from the HuggingFace dataset `AdhyanshVerma/open-github-major-repos`, which contains 2.85 million commits from 98 repositories [ARTIFACT:art_FiPBECDY22qD].

**Table 1: Dataset Summary**

| Repository | Total Commits | Founder | Contributors |
|------------|--------------|---------|--------------|
| 11ty/eleventy | 2,283 | Zach Leatherman | 116 |
| BuilderIO/builder | 4,482 | Steve Sewell | 121 |
| BuilderIO/mitosis | 1,279 | Steve Sewell | 107 |
| BuilderIO/partytown | 693 | Adam Bradley | 128 |
| BurntSushi/ripgrep | 1,824 | Andrew Gallant | 459 |
| ByteByteGoHq/system-design-101 | 22 | Sahn Lam | 14 |
| EbookFoundation/free-programming-books | 15,736 | Victor Felder | 3,366 |
| FFmpeg/FFmpeg | 143,288 | Vesselin Bontchev | 2,492 |
| Genymobile/scrcpy | 6,251 | Romain Vimont | 172 |
| JetBrains/intellij-community | 90,943 | no_reply@jetbrains.com | 613 |
| Kubernetes/kubernetes | 85,321 | Joe Beda | 1,847 |
| tensorflow/tensorflow | 52,143 | Martín Abadi | 1,243 |
| vuejs/vue | 3,421 | Evan You | 287 |

### 3.2 Important Data Limitation

A critical limitation of our dataset is that it contains only `file_count` per commit (the number of files modified), not the actual `files_modified` (the file paths). Computing Jaccard similarity requires the set of files modified by each contributor, which cannot be constructed from file counts alone. This limitation prevented us from computing true knowledge redundancy via Jaccard similarity.

As a fallback, we implemented a *pseudo-knowledge redundancy* measure using cosine similarity of file count distributions across contributors. While this approach captures some notion of contributor similarity, it is a poor proxy for true Jaccard-based knowledge redundancy. We report results using this fallback measure while being transparent about its limitations. Future work with full git log data (including file paths) is needed for proper validation [ARTIFACT:art_pOI-AO_xwHdm].

### 3.3 Founder Identification

We identified founders using two complementary methods:

1. **First commit author**: The contributor who made the first commit to the repository, identified via commit timestamp ordering [ARTIFACT:art_uYucfGHDjfdU].

2. **Repository creator**: The owner field from GitHub API metadata (where available).

For all 13 repositories, the first commit author method yielded clear founder identification. In cases where the repository owner differed (e.g., organizational repositories like JetBrains/intellij-community), we used the earliest prolific contributor as the founder.

### 3.4 Founder Departure Definition

Consistent with Avelino et al. [1], we defined founder departure as the point where the founder has no commits for ≥12 months before the project's most recent commit. This threshold was validated through sensitivity analysis across 3, 6, 12, 18, and 24-month thresholds, with 12 months achieving the highest harmonic mean of precision and recall [1, ARTIFACT:art_uYucfGHDjfdU].

### 3.5 Knowledge Redundancy Measurement

#### Ideal Method (Jaccard Similarity)

Given access to file paths, knowledge redundancy would be measured as follows. For each contributor $i$, define their file set $F_i$ as the set of files modified by that contributor within a 2-year time window before founder departure. The pairwise Jaccard similarity between contributors $i$ and $j$ is:

$$J_{ij} = \frac{|F_i \cap F_j|}{|F_i \cup F_j|}$$

The knowledge redundancy $KR$ for a project with $n$ contributors is the average pairwise Jaccard similarity:

$$KR = \frac{2}{n(n-1)} \sum_{i<j} J_{ij}$$

We use a 2-year time window based on Avelino et al.'s recommendation to balance recency and stability [ARTIFACT:art_iicMCU3WgldY].

#### Fallback Method (Pseudo-KR from File Counts)

Due to the unavailability of file paths, we implemented a fallback measure. For each contributor, we computed the distribution of file counts across their commits. We then computed the cosine similarity between contributor file count distributions, averaged across all contributor pairs. This *pseudo-knowledge redundancy* (PKR) serves as a rough proxy but cannot capture true file overlap [ARTIFACT:art_pOI-AO_xwHdm].

### 3.6 Project Survival Measurement

We measured project survival using Avelino et al.'s [1] "Truck Factor Developer Detachment" (TFDD) definition: a project survives if it continues to attract new contributors (or has any commit) within 12 months of founder departure. This binary survival measure aligns with prior OSS survival literature [1, 3, 8].

### 3.7 Control Variables

Consistent with prior OSS survival studies [1, 3, 8], we included the following control variables:

- **Bus factor**: Computed using the DOA algorithm [1]
- **Project age**: Days from repository creation to founder departure
- **Project size**: Total number of commits before founder departure
- **Contributor count**: Number of distinct contributors before founder departure

## 4. Statistical Analysis

### 4.1 Planned Analysis

We planned to employ two complementary survival analysis methods:

**Kaplan-Meier Estimator**: A non-parametric method to estimate the survival function $S(t) = P(T > t)$, where $T$ is time from founder departure to project abandonment. We would use the log-rank test to compare survival curves across knowledge redundancy quartiles [ARTIFACT:art_uYucfGHDjfdU].

**Cox Proportional Hazards Model**: A semi-parametric regression model relating the hazard function $\lambda(t|X)$ to covariates $X$:

$$\lambda(t|X) = \lambda_0(t) \exp(\beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p)$$

We would include knowledge redundancy as a key predictor with both linear and quadratic terms to test the inverted-U hypothesis:

$$\log \lambda(t|KR) = \log \lambda_0(t) + \beta_1 KR + \beta_2 KR^2 + \beta_3 \mathbf{Z}$$

where $\mathbf{Z}$ represents control variables. The inverted-U prediction is confirmed if $\beta_1 > 0$ and $\beta_2 < 0$ (positive linear term, negative quadratic term) [ARTIFACT:art_uYucfGHDjfdU].

### 4.2 Actual Analysis Given Data Constraints

Due to data limitations (see Section 3.2) and the fact that all 6 projects with founder departure survived (100% survival rate), we could not fit Cox proportional hazards models or conduct survival analysis. Instead, we:

1. Computed descriptive statistics for pseudo-knowledge redundancy across the 6 projects
2. Validated our measurement and analysis approach on synthetic data with known inverted-U relationships
3. Discuss the methodological framework for future validation with adequate data

## 5. Results

### 5.1 Founder Departure Detection

Of the 13 repositories analyzed, 6 (46%) had detectable founder departure events (defined as 12+ months without founder commits). Table 2 shows the departure events and project characteristics.

**Table 2: Founder Departure Events**

| Repository | Founder | Departure Date | Project Age (days) | Contributors | Bus Factor | Pseudo-KR |
|------------|----------|----------------|-------------------|--------------|------------|-----------|
| EbookFoundation/free-programming-books | Victor Felder | 2015-04-03 | 539 | 569 | 2 | 0.119 |
| BuilderIO/builder | Steve Sewell | 2023-07-31 | 1637 | 67 | 2 | 0.969 |
| BuilderIO/mitosis | Steve Sewell | 2025-04-03 | 1608 | 103 | 2 | 0.576 |
| BuilderIO/partytown | Adam Bradley | 2023-04-18 | 605 | 80 | 1 | 0.226 |
| BurntSushi/ripgrep | Andrew Gallant | 2021-07-19 | 1956 | 294 | 1 | 0.348 |
| ByteByteGoHq/system-design-101 | Sahn Lam | 2023-11-06 | 21 | 13 | 2 | 0.779 |

*Note: Pseudo-KR = pseudo-knowledge redundancy from file count distributions (fallback method).*

### 5.2 Survival Outcomes

All 6 projects (100%) with founder departure events survived according to our TFDD definition (continued activity after departure). This complete survival rate prevented statistical comparison across redundancy levels. The survival rate in our sample (100%) is higher than the 41% reported by Avelino et al. [1], likely due to:
1. Small sample size (N=6 vs. N=1,932)
2. Selection bias toward large, popular repositories in our dataset
3. Different time windows (some departures occurred recently, with limited post-departure observation)

### 5.3 Pseudo-Knowledge Redundancy Distribution

Pseudo-knowledge redundancy scores ranged from 0.119 to 0.969 (mean = 0.503, SD = 0.299). This range spans from very low redundancy (0.119, indicating contributors modify very different numbers of files) to very high redundancy (0.969, indicating contributors have similar file count patterns).

However, we caution that these pseudo-KR scores are computed from file counts, not file paths, and therefore do not represent true knowledge redundancy. The wide range likely reflects differences in contributor activity levels rather than true overlap in expertise areas.

### 5.4 Synthetic Data Validation

To validate that our statistical approach *could* detect an inverted-U relationship given proper data, we generated synthetic datasets with:
- Known inverted-U relationship between knowledge redundancy and survival
- Proper file path data for Jaccard similarity computation
- Varied sample sizes (N=50, N=100, N=200)

Results showed that with N=50+ repositories and adequate outcome variation, the Cox proportional hazards model with quadratic term can detect inverted-U relationships when present (power ≈ 0.65 for N=50, ≈ 0.85 for N=100). The synthetic validation confirms that our *methodology* is sound, even though our *data* were insufficient for empirical testing [ARTIFACT:art_pOI-AO_xwHdm].

[FIGURE:fig2]

### 5.5 Methodological Contribution

While we could not empirically test the inverted-U hypothesis, we make the following methodological contributions:

1. **Open-source implementation**: We provide Python code for computing knowledge redundancy from git repositories, including both Jaccard similarity (when file paths are available) and fallback approaches [ARTIFACT:art_pOI-AO_xwHdm].

2. **Measurement framework**: We document the data requirements for proper knowledge redundancy measurement and provide a checklist for future studies.

3. **Statistical analysis pipeline**: We implement survival analysis (Kaplan-Meier, Cox models) with bootstrap confidence intervals and multicollinearity checks, validated on synthetic data.

## 6. Discussion

### 6.1 Interpretation of Findings

Our study encountered three critical data limitations that prevented empirical validation of the inverted-U hypothesis:

1. **Lack of file path data**: The dataset contained only file counts, not file paths, preventing Jaccard similarity computation.
2. **Small sample size**: Only 6 repositories with founder departure events were identified.
3. **No survival variation**: All 6 projects survived, providing no outcome variance to model.

Despite these limitations, our conceptual analysis and methodological validation provide value. The knowledge redundancy construct is theoretically grounded in transactive memory systems [12, 14], information theory, and ecological stability theory. The inverted-U prediction follows logically from these foundations: too little redundancy leaves the project vulnerable to knowledge loss; too much redundancy wastes resources on duplication.

### 6.2 Relationship to Prior Work

Our conceptual framework extends Avelino et al. [1] by proposing that bus factor alone is insufficient: two projects with identical bus factor can have different survival rates due to differing knowledge redundancy. This prediction remains to be empirically tested.

Our work also complements Jabrayilzade et al. [6], who found that multimodal knowledge (VCS + code reviews + meetings) improves bus factor accuracy. We propose that the *structure* of knowledge (redundancy) matters beyond its *amount* (bus factor), a hypothesis that could be tested with multimodal data.

### 6.3 Practical Implications

For OSS project maintainers, our findings suggest:

1. **Measure knowledge distribution**: Use Jaccard similarity of contributor file sets (when file path data are available) to assess knowledge redundancy.

2. **Aim for moderate redundancy**: While we could not empirically identify the optimal level, theory suggests targeting moderate overlap (neither fully specialized nor fully overlapping).

3. **Avoid both extremes**: Don't let all contributors cluster on the same subsystems (high redundancy), but ensure at least some overlap so contributors can cover for each other (low redundancy).

### 6.4 Limitations

Several limitations constrain the conclusions of this study:

1. **Data limitations**: The dataset lacked file paths needed for Jaccard similarity, forcing use of a fallback pseudo-KR measure with unknown validity.

2. **Sample size**: Our analysis includes 6 repositories with founder departure, which is insufficient for survival modeling. Prior work suggests N≥50 with 10-20 events per predictor variable for Cox models [1].

3. **Complete survival**: All 6 projects survived, preventing any statistical comparison across redundancy levels.

4. **Selection bias**: The 13 repositories are large, popular projects from a "major-repos" dataset. Findings may not generalize to smaller or less popular projects.

5. **Founder departure identification**: We used first commit author as founder, which may not capture cases where the legal founder differs from the primary contributor.

6. **Survival measurement**: Our binary survival definition (any activity vs. none) is coarse. Future work should measure survival quality (maintenance level, feature velocity).

### 6.5 Future Research

This study identifies several priorities for future research:

1. **Large-scale data collection**: Clone repositories directly from GitHub and use `git log --name-only` to extract file paths for Jaccard similarity. Target N≥200 repositories with founder departure events.

2. **Multimodal knowledge**: Incorporate code reviews, issue discussions, and documentation contributions into the redundancy measure, following Jabrayilzade et al. [6].

3. **Temporal dynamics**: Study how knowledge redundancy evolves over time and how this affects survival at different project lifecycle stages.

4. **Intervention studies**: Conduct controlled experiments where OSS projects are randomly assigned different redundancy targets to test causal effects on survival.

5. **Validation of pseudo-KR**: Compare pseudo-KR (from file counts) against true Jaccard KR (from file paths) to assess the fallback measure's validity.

## 7. Conclusion

This paper introduced knowledge redundancy—the degree of overlap in contributor expertise—as a construct for predicting open-source project survival after founder departure. While data limitations prevented empirical validation of our inverted-U hypothesis, we make three contributions:

1. **Conceptual**: We defined knowledge redundancy as distinct from bus factor and provided theoretical grounding for the inverted-U prediction.

2. **Methodological**: We provided a complete measurement and analysis framework, including open-source tools and validation on synthetic data.

3. **Empirical**: We applied our framework to 13 repositories, identifying 6 founder departure events and documenting data requirements for future large-scale validation.

The knowledge redundancy construct captures a dimension of project resilience not reflected in bus factor alone. Future work with proper file path data and adequate sample sizes can test whether moderate knowledge redundancy optimizes post-founder survival. As open-source software continues to underpin critical infrastructure, understanding and optimizing knowledge distribution within projects becomes increasingly important.

## Acknowledgments

We thank the developers of the open-source projects in our dataset for making their commit histories publicly available. This research was conducted as part of the AI Inventor automated research system.

## References

[1] Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. (2019). On the abandonment and survival of open source projects: An empirical investigation. *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*, 1-12.

[2] Cosentino, V., Izquierdo, J. L. C., & Cabot, J. (2015). Assessing the bus factor of Git repositories. *2015 IEEE 22nd International Conference on Software Analysis, Evolution, and Reengineering (SANER)*, 499-503.

[3] Qiu, H. S., Nolte, A., Brown, A. R., Serebrenik, A., & Vasilescu, B. (2019). Going farther together: The impact of social capital on sustained participation in open source. *2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE)*, 688-699.

[4] Ferreira, M., Avelino, G., Valente, M. T., & Ferreira, K. A. M. (2019). A comparative study of algorithms for estimating truck factor. *CBSOFT 2019*.

[5] Rigby, P. C., & Hassan, A. E. (2007). What can OSS mailing lists tell us? *2007 IEEE International Working Conference on Mining Software Repositories (MSR)*.

[6] Jabrayilzade, E., Evtikhiev, M., Tüzün, E., & Kovalenko, V. (2022). Bus factor in practice. *2022 IEEE/ACM 44th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)*, 299-310.

[7] Piccolo, S. A., et al. (2025). Fast and accurate heuristics for bus-factor estimation. *arXiv:2508.09828*.

[8] Ferreira, F., Silva, L. L., & Valente, M. T. (2020). Turnover in open-source projects: The case of core developers. *Proceedings of the XXXIV Brazilian Symposium on Software Engineering (SBES)*.

[9] Coelho, J., Valente, M. T., & Silva, L. L. (2020). Is this GitHub project maintained? *Empirical Software Engineering*, 25(6), 4954-4990.

[10] Miller, B., et al. (2025). Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival. *Research Policy*, 54(2), 105284.

[11] Choudhary, A., et al. (2023). The state of survival in OSS: The impact of diversity. *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE) - Student Research Competition*.

[12] Ren, Y., & Argote, L. (2011). Transactive memory systems 1985-2010: An integrative framework of key dimensions. *Academy of Management Annals*, 5(1), 189-229.

[13] Fritz, T., Ou, J., Murphy, G. C., & Murphy-Hill, E. (2010). A degree-of-knowledge model to capture source code familiarity. *Proceedings of the 32nd ACM/IEEE International Conference on Software Engineering (ICSE)*, 385-394.

[14] Wegner, D. M. (1985). Transactive memory: A contemporary analysis of the group mind. *Advances in social cognition*, 2, 185-208.

[15] Davidson-Pilon, C. (2019). lifelines: Survival analysis in Python. *Journal of Open Source Software*, 4(40), 1317.

[16] CodeScene. (2023). Knowledge distribution and bus factor analysis. *CodeScene Documentation*. https://codescene.ta.philips.com/docs/guides/social/knowledge-distribution.html

## Appendix A: Corrected Citations

This appendix documents corrections made to citations from the previous draft:

1. **Citation [5]**: Previously cited as Rigby & Hassan 2007 on "blame-based ownership." The actual 2007 paper by Rigby & Hassan is on mining mailing lists [5]. The text now cites the correct paper and removes the claim about blame-based ownership (which could not be verified in the 2007 paper).

2. **Citation [13]**: Previously cited as Fritz et al. 2007 on "personal information management." The correct paper on the Degree-of-Knowledge (DOK) metric is Fritz et al. 2010 [13]. This has been corrected.

3. **Citation [11]**: Verified as a Student Research Competition paper at ESEC/FSE 2023. The text now notes this is a short paper/abstract rather than a full research paper.

## Appendix B: Synthetic Data Generation

To validate our methodology, we generated synthetic datasets with the following properties:
- N=50, 100, 200 repositories
- Known inverted-U relationship: survival peaks at KR ≈ 0.5
- Proper file path data for Jaccard similarity computation
- Varied survival rates (30%-90%)

The synthetic validation confirmed that with adequate sample size and outcome variation, the Cox proportional hazards model with quadratic term can detect inverted-U relationships. Full synthetic data code is available in the artifact repository [ARTIFACT:art_pOI-AO_xwHdm].

## Appendix C: Repository Cloning for File Path Extraction

As part of this study, we cloned 9 repositories from GitHub to extract file path data directly from git logs:
- 11ty/eleventy
- BurntSushi/ripgrep
- Genymobile/scrcpy
- django/django
- expressjs/express
- jashkenas/coffeescript
- mojombo/grit
- npm/npm
- twitter/bootstrap

However, integrating this data with the HuggingFace dataset proved challenging due to differences in commit formatting. Future work should use directly cloned repositories as the primary data source, avoiding pre-processed datasets that lack file path information.

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_FiPBECDY22qD
type: dataset
title: GitHub OSS commit dataset for survival analysis
summary: >-
  Collected and processed GitHub repository data from HuggingFace dataset (AdhyanshVerma/open-github-major-repos) containing
  2.85M commit records from 98 repositories. Transformed data into standardized schema with 500,000 examples from 13 repositories.
  Each example represents one commit event with features including repo_id, author_login, is_founder, file_count, commit_sequence_num,
  author_total_commits, repo_total_commits, and commit_timestamp. Output label is 'founder' or 'contributor'. Identified founders
  for all repositories (earliest committer). Data validated against exp_sel_data_out.json schema. Due to memory constraints
  and lack of GitHub API token, only 13 repos were processed (target was 2000+). Dataset suitable for knowledge redundancy
  analysis and founder departure event detection.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_iicMCU3WgldY
type: research
title: Knowledge Redundancy and Bus Factor from Git Data
summary: >-
  This research provides a comprehensive synthesis of state-of-the-art methods for measuring knowledge distribution in open-source
  projects from git repository data. The study reviews 15+ key papers (2010-2025) and identifies: (1) Avelino's Degree of
  Authorship (DOA) algorithm as the most validated bus factor method [1, 2], (2) Jaccard similarity as the primary approach
  for knowledge redundancy measurement [3], (3) Validation evidence from 1,932 GitHub projects showing 16% abandonment rate
  and 41% survival rate [2], (4) Recent advances in graph-theoretic approaches [4] and multimodal measurements [5], (5) Implementation
  tools and practical guidance. The report includes exact formulas, algorithm pseudocode, validation metrics, and a recommended
  measurement framework for hypothesis testing.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_uYucfGHDjfdU
type: research
title: OSS Founder Departure and Survival Methods
summary: >-
  Exhaustive research synthesizing methodologies from 15+ peer-reviewed papers on operationalizing founder departure (12-month
  inactivity threshold per Avelino et al.'s sensitivity analysis), measuring project survival (Truck Factor Developer Detachment
  definition), implementing survival analysis (Kaplan-Meier + Cox proportional hazards), and identifying control variables
  for OSS survival studies. Includes recent 2025 literature and implementation details for GitHub API data collection. Avelino
  et al. (2019) conducted sensitivity analysis of five thresholds (3 months, 6 months, 1 year, 1.5 years, 2 years) and found
  1-year threshold achieved highest harmonic mean (0.66). The research covers founder identification methods via GitHub API,
  departure threshold validation, survival metrics, statistical methods including survival analysis with lifelines Python
  library, comprehensive control variables from multiple studies, multicollinearity considerations with VIF, and threats to
  validity. Recent 2025 papers on developer departure and core developer turnover provide updated insights.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_expected_files:
- research_out.json

--- Item 4 ---
id: art_pOI-AO_xwHdm
type: experiment
title: OSS founder departure survival analysis
summary: >-
  Implemented experiment to test inverted-U hypothesis between knowledge redundancy (KR) and OSS project survival after founder
  departure. Used fallback approach (pseudo-KR from file_count distributions) due to dataset lacking file paths for Jaccard
  similarity. Processed 500,000 commit records from 13 repositories, detected founder departures using Avelino et al. (2019)
  12-month threshold with gap detection. Measured survival using TFDD definition (3+ months without founder commits). Computed
  pseudo-KR using cosine similarity of file_count histograms across top contributors. Results: 6 repos with founder departure
  detected, all survived (100% survival rate), KR range 0.119-0.969. Statistical analysis limited by lack of outcome variation.
  Output formatted in exp_gen_sol_out schema with datasets/examples structure and predict_* fields. Key limitations: only
  6 examples (need 50+), insufficient sample size, no survival variation, fallback KR measure, large repos excluded for performance.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_YOQ_fg8YSxRo
type: research
title: Verify and correct paper citations for knowledge redundancy
summary: >-
  Conducted thorough verification of 15 citations in the paper draft 'Knowledge Redundancy Predicts Open-Source Project Survival
  After Founder Departure.' Identified two significant citation errors: (1) Citation [13] Fritz et al. incorrectly listed
  as 2007 ICSE PIM paper, corrected to 2010 ICSE paper on Degree-of-Knowledge (DOK) model; (2) Citation [5] Rigby & Hassan
  2007 references mailing list paper but text discusses blame-based ownership - requires clarification. Verified all other
  citations against actual paper content via ACM Digital Library, arXiv, DBLP, and publisher websites. Searched for additional
  related work on knowledge redundancy, transactive memory systems, and OSS survival, identifying 5+ relevant papers. Assessed
  novelty of inverted-U hypothesis and found no direct prior work testing this specific relationship, though related concepts
  exist in transactive memory literature. Generated corrected BibTeX file with all 15 citations plus 3 additional recommended
  references. Research report includes detailed verification evidence, correction recommendations, and follow-up questions
  for further investigation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) The dataset used (HuggingFace AdhyanshVerma/open-github-major-repos) only contains file_count per commit, NOT actual file paths. Jaccard similarity requires the set of files modified by each contributor (file paths), which are not available in this dataset. The DATASET_SUMMARY.md explicitly states: 'files_modified (actual file paths) not available, only file_count' (Section 'Limitations'). The paper's reported knowledge redundancy scores (Table 1, Appendix A) and all results relying on them are therefore impossible to compute from the described data. This is a fatal methodological flaw.
  Action: Use a dataset with actual file paths per commit. Options: (1) GitHub API with `git log --name-only --format='%H %an'`, (2) GHTorrent dataset (ghtorrent.org), (3) World of Code (woc.') (4) Directly clone repositories and run git log. Recompute all knowledge redundancy scores. If file paths are truly unavailable, the Jaccard approach must be abandoned and a different metric (e.g., cosine similarity on file_count vectors, though this is a poor proxy) must be used and justified.
- [MAJOR] (evidence) Sample size is N=13 repositories, but the paper frames it as '500,000 commits from 13 open-source repositories' (Abstract, Section 3.1). This is misleading: the unit of analysis for survival models is repositories (not commits), so N=13. Cox proportional hazards with 6+ predictors (KR, KR², bus factor, log(contributors), project age, project size) and N=13 is severely underpowered. The significant p-values (0.012, 0.031) are likely spurious—with N=13 and this many parameters, the model is overfitting. Harrell's rule of thumb suggests 10-20 events per predictor variable for Cox PH.
  Action: Increase the sample to minimum N=50 repositories (preferably N=100+) with founder departure events. If N=13 is all that's available, use a simpler model (e.g., just KR + KR² + bus factor) and apply regularization or bootstrapping to assess stability of coefficients. Alternatively, use non-parametric tests (e.g., log-rank test comparing high/low redundancy groups) which require fewer assumptions.
- [MAJOR] (rigor) Citation [5] (Rigby & Hassan 2007) is cited as 'Rigby et al. - RIG Algorithm (Blame-based)'. However, the 2007 paper by Rigby & Hassan titled 'What can OSS mailing lists tell us?' is about mining mailing lists, not a blame-based bus factor algorithm. The correct citation for blame-based ownership might be a different Rigby paper (e.g., 'Understanding peer review on open source projects' or similar). Citation [13] (Fritz et al. 2007) is cited for 'Degree of Knowledge (DOK) metric' but the 2007 Fritz et al. paper appears to be about personal information management tools. The DOK/code ownership paper may be a different paper (possibly Fritz et al. ICSE 2010 or similar). These citation errors undermine confidence in the literature review.
  Action: Verify ALL citations by accessing the actual papers. Correct reference [5] to the appropriate Rigby paper on blame-based analysis. Correct reference [13] to the correct Fritz paper on code ownership/DOK. Use tools like Google Scholar, DBLP, or Semantic Scholar to verify citations. In future, use a reference manager to avoid this class of error.
- [MINOR] (novelty) The paper claims 'Our study is the first to empirically test an inverted-U relationship between knowledge redundancy and OSS survival' (Section 2.3). This may be true, but the literature review on 'knowledge redundancy in teams' is thin (only 2 citations: [12] Ren & Argote 2011 on transactive memory, [13] Fritz et al. 2007 on DOK). There may be relevant work in (a) developer recommendation literature (knowledge overlap for task assignment), (b) distributed software development (geographic knowledge redundancy), (c) code review literature (reviewer expertise overlap). A more thorough search is needed to confirm novelty.
  Action: Conduct a more thorough literature search on: (1) 'knowledge overlap' + 'open source', (2) 'expertise overlap' + 'software teams', (3) 'code ownership' + 'redundancy', (4) 'bus factor' + 'knowledge distribution'. Search venues: ICSE, FSE, ESEC, EMSE, TSE. If prior work is found that tests a similar hypothesis, the paper must position itself more carefully (e.g., 'first to test inverted-U relationship' vs. 'first to propose knowledge redundancy metric').
- [MINOR] (methodology) The survival definition in Section 3.5 requires 'Commit activity in the 12 months post-departure was statistically indistinguishable from pre-departure trends (Mann-Whitney U test, p > 0.05).' This is problematic: (1) Mann-Whitney tests location difference, not 'statistically indistinguishable'—the wording is misleading, (2) Using p > 0.05 to 'confirm' no difference is a misapplication of NHST (absence of evidence is not evidence of absence), (3) This makes the survival definition very conservative (projects with ANY change in commit pattern would be classified 'not survived'). The paper should use a more standard survival definition (e.g., Avelino et al.'s TFDD definition).
  Action: Simplify the survival definition to match Avelino et al. (2019): Project 'survives' if it attracts new core developers (or has any commit) within 12 months of founder departure. Remove the Mann-Whitney U condition which adds noise and is statistically misinterpreted. If trend change is important, use a separate analysis (e.g., intervention analysis on time series) rather than baking it into the survival definition.
- [MINOR] (clarity) Table 2 reports 'Hazard Ratio' for KR² as 0.021. This is the hazard RATIO for a 1-unit change in KR². Since KR² ranges from 0 to ~0.16 (if KR ranges 0-0.4), a 1-unit change is outside the data range. The interpretation 'each unit increase in KR² reduces the hazard by a factor of 0.021' is technically correct but misleading. Readers may misinterpret this as a large effect. Better to report the hazard ratio for a 1-SD change in KR², or show predicted survival curves (Figure 3) with actual KR values.
  Action: In Table 2, add a row reporting hazard ratio for a 1-SD change in KR² (or a 0.1 change, given KR range ~0.1-0.4). In the text, clarify that the HR for KR² = 0.021 means 'for two projects differing by 1 unit in KR²...' but note this is outside the observed range. Use Figure 3 (predicted survival probability) as the primary effect size communication tool.
- [MINOR] (scope) The generalizability of findings is limited: (1) Only 13 repos, mostly large/popular projects (given they are from a 'major-repos' dataset), (2) All repos are from GitHub—findings may not generalize to GitLab, Bitbucket, or non-git OSS, (3) The survival analysis only considers founder departure, not general core developer departure. The discussion should be more upfront about these scope limitations.
  Action: Add a subsection in Discussion (Section 6) explicitly listing scope limitations: (1) Generalizability to small/popular projects, (2) GitHub-only, (3) Founder-only vs. general core developer departure, (4) Language bias (if all projects are in same language). Consider a 'future work' item on replicating with a more diverse sample (e.g., small OSS projects, non-GitHub forges).
- [MINOR] (rigor) The paper cites 'Miller et al. (2025)' and 'Choudhary et al. (2023)' in Related Work (Section 2.2) but the references appear incomplete. The Choudhary et al. 2023 citation [11] links to an ESEC/FSE 2023 Student Research Competition abstract (not a full paper)—this should be verified and properly categorized. The Miller et al. 2025 citation [10] appears to be a real paper (in Research Policy) but should be verified for relevance to OSS survival.
  Action: Verify references [10] and [11]. If [11] is a student research competition abstract (2-page format), it should not be cited as primary related work—use it only as a pointer to the author's later full paper (if any). Ensure all citations are to peer-reviewed, archival-quality sources (not preprints, blog posts, or abstracts). Use DBLP or the venue's official proceedings to verify publication type.
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 01:33:19 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-tools · 2026-08-21 01:33:29 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: free-first web search (general or scholarly, Serper fallback), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
