# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_rhx_UB8HZyTw` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 02:28:27 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study
abstract: >-
  Open-source software projects frequently depend on a small number of core developers, and founder departure is a major threat
  to project continuity. While the 'bus factor' (the minimal number of developers whose departure would stall a project) is
  well-studied, it fails to capture an important dimension: the degree of overlap in what contributors know. This paper introduces
  knowledge redundancy—the average pairwise overlap in contributor expertise areas—as a distinct construct for predicting
  post-founder project survival. We hypothesize an inverted-U relationship: projects with moderate redundancy survive at higher
  rates than both those with very low redundancy and those with very high redundancy. We present a methodological framework
  for measuring knowledge redundancy from git commit data using Jaccard similarity and testing the hypothesis using survival
  analysis. Applying this framework to a dataset of 500,000 commits from 13 open-source repositories, we identify founder
  departure events in 6 repositories. Due to data limitations (lack of file path information for Jaccard computation) and
  complete survival of all 6 projects, we could not statistically test the inverted-U hypothesis. Instead, we report descriptive
  patterns and provide open-source tools for future large-scale validation. Our conceptual analysis suggests that knowledge
  redundancy captures a dimension of project resilience not reflected in bus factor alone, offering a foundation for future
  empirical work.
paper_text: |
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

  2. **Methodological**: We provide a complete measurement framework for computing knowledge redundancy from git commit data using Jaccard similarity, including fallback approaches when file path data are unavailable \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-1/research-1}}.

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

  We collected commit history data from 13 open-source repositories on GitHub, comprising 500,000 commit records (Table 1). The data were sourced from the HuggingFace dataset `AdhyanshVerma/open-github-major-repos`, which contains 2.85 million commits from 98 repositories \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-1/dataset-1}}.

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

  1. **First commit author**: The contributor who made the first commit to the repository, identified via commit timestamp ordering \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-1/research-2}}.

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

  We use a 2-year time window based on Avelino et al.'s recommendation to balance recency and stability .

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

  **Kaplan-Meier Estimator**: A non-parametric method to estimate the survival function $S(t) = P(T > t)$, where $T$ is time from founder departure to project abandonment. We would use the log-rank test to compare survival curves across knowledge redundancy quartiles .

  **Cox Proportional Hazards Model**: A semi-parametric regression model relating the hazard function $\lambda(t|X)$ to covariates $X$:

  $$\lambda(t|X) = \lambda_0(t) \exp(\beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p)$$

  We would include knowledge redundancy as a key predictor with both linear and quadratic terms to test the inverted-U hypothesis:

  $$\log \lambda(t|KR) = \log \lambda_0(t) + \beta_1 KR + \beta_2 KR^2 + \beta_3 \mathbf{Z}$$

  where $\mathbf{Z}$ represents control variables. The inverted-U prediction is confirmed if $\beta_1 > 0$ and $\beta_2 < 0$ (positive linear term, negative quadratic term) .

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
summary: >-
  This paper introduces knowledge redundancy as a construct for predicting open-source project survival after founder departure.
  Due to data limitations (lack of file paths for Jaccard similarity, N=6 repositories with departure, 100% survival rate),
  we could not empirically test the inverted-U hypothesis. Instead, we provide a methodological framework, validate it on
  synthetic data, and offer open-source tools for future validation with adequate data.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Knowledge Redundancy Concept
caption: >-
  Conceptual diagram showing how knowledge redundancy differs from bus factor. Two projects can have the same bus factor (2
  critical contributors) but different knowledge redundancy: low redundancy (contributors work on different subsystems) vs.
  high redundancy (contributors work on overlapping code).
image_gen_detailed_description: >-
  Horizontal comparison diagram, left to right. Title at top: 'Bus Factor vs Knowledge Redundancy'. Left side: 'Project A:
  Bus Factor = 2, Low Redundancy'. Show two developer icons (Dev1, Dev2) each connected to different code modules (Module
  A, Module B). Right side: 'Project B: Bus Factor = 2, High Redundancy'. Show two developer icons (Dev1, Dev2) both connected
  to the same code module (Module A). Use blue for developers, gray for modules. Arrows show 'modifies' relationships. Sans-serif
  font, clean white background, no 3D.
aspect_ratio: '21:9'
summary: Conceptual diagram contrasting bus factor and knowledge redundancy
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Pseudo-Knowledge Redundancy Distribution
caption: >-
  Pseudo-knowledge redundancy scores (from file count distributions) for 6 repositories with founder departure events. Scores
  range from 0.119 (low redundancy) to 0.969 (high redundancy). All 6 projects survived, preventing statistical comparison
  across redundancy levels.
image_gen_detailed_description: >-
  Bar chart. X-axis: Repository names (abbreviated): 'free-prog-books', 'builder', 'mitosis', 'partytown', 'ripgrep', 'system-design-101'.
  Y-axis: Pseudo-KR score (0.0 to 1.0). Values: 0.119, 0.969, 0.576, 0.226, 0.348, 0.779. All bars colored blue. Title: 'Pseudo-Knowledge
  Redundancy by Repository'. Note at bottom: 'All 6 projects survived (100% survival rate)'. Sans-serif font, white background.
aspect_ratio: '16:9'
summary: Shows pseudo-KR scores for 6 repositories with founder departure
figure_path: figures/fig2_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 02:28:27 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-21 02:28:41 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated vector PDFs and JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. This document class is ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt either way) and gains nothing, while restricting the float
  to a page top
- ALWAYS constrain with `width` and `keepaspectratio`. Add `height` only as a
  LAST RESORT against a very tall figure overrunning the page, and keep it
  generous — `0.85\textheight`. A tight height cap binds on ordinary figures
  and LaTeX then shrinks the TEXT with them: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt.
  The figure generator measures legibility at the figure's OWN size, so it
  cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 02:28:41 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
