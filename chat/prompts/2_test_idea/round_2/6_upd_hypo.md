# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_rhx_UB8HZyTw` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 01:38:33 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Knowledge redundancy predicts OSS survival after founder leaves
hypothesis: >-
  The relationship between knowledge redundancy (overlap in contributor expertise) and open-source project survival after
  founder departure is inverted-U shaped: projects with moderate knowledge redundancy survive at higher rates than both those
  with zero redundancy (all critical knowledge held by founder) and those with excessive redundancy (all contributors know
  the same things, with no specialization). This prediction is grounded in information theory (error-correcting codes), organizational
  psychology (transactive memory systems), and ecology (diversity-stability hypothesis). However, empirical testing requires
  commit-level file path data (not just file counts) from a sufficiently large sample (N≥50 repositories with founder departure
  events) to compute Jaccard similarity and fit survival models with adequate statistical power.
motivation: >-
  Open-source projects frequently depend on a small number of core developers, and founder departure is a major threat to
  project continuity. While 'bus factor' (the minimal number of developers whose departure would stall a project) is well-studied,
  it fails to capture an important dimension: the DEGREE OF OVERLAP in what contributors know. Two projects could both have
  bus factor = 2, but in one the two contributors know completely different things (low redundancy) while in the other they
  know largely the same things (high redundancy). This hypothesis identifies knowledge redundancy as a distinct, measurable
  predictor of post-founder survival, with a non-monotonic relationship that reveals an optimal level of redundancy for project
  resilience.
assumptions:
- >-
  Knowledge redundancy can be measured from observable contribution patterns (code commits, file modifications, issue discussions)
  as the degree of overlap in contributor expertise areas
- >-
  Founder departure can be identified as the point where the original creator/main contributor stops making commits for an
  extended period (12+ months)
- >-
  Project survival can be measured as continued development activity (commits, releases, issue resolutions) after founder
  departure, beyond what would be expected from pre-departure trends
- >-
  The effect of knowledge redundancy is separable from bus factor, project size, popularity, and other known predictors, allowing
  for controlled analysis
investigation_approach: >-
  1. DATA COLLECTION: Mine GitHub API to identify ~2000 popular open-source projects (100+ stars, 2+ years active), extract
  commit histories, file modification records, and contributor metadata. 2. FOUNDER DEPARTURE IDENTIFICATION: Define founder
  as the contributor with highest initial authorship; mark departure as 12+ months without commits after a period of activity.
  3. KNOWLEDGE REDUNDANCY MEASUREMENT: Compute redundancy as the average pairwise overlap in file modification patterns among
  top contributors (using Jaccard similarity of file sets modified by each contributor). 4. SURVIVAL MEASUREMENT: Define survival
  as continued development activity (commits, releases) for 12+ months after founder departure at levels statistically indistinguishable
  from pre-departure trends. 5. ANALYSIS: Fit survival models (Cox proportional hazards) with knowledge redundancy as key
  predictor, including quadratic term to test inverted-U prediction, controlling for bus factor, project size, age, popularity,
  programming language, and contributor count.
success_criteria: >-
  The hypothesis is confirmed if: (1) The quadratic term for knowledge redundancy in survival models is statistically significant
  (p < 0.05) and negative, indicating an inverted-U relationship; (2) Projects with moderate redundancy (25th-75th percentile)
  show 20%+ higher survival rates than projects with very low redundancy (bottom 10th percentile); (3) Projects with very
  high redundancy (top 10th percentile) show 10%+ LOWER survival rates than those with moderate redundancy, confirming the
  non-monotonic prediction. The hypothesis is disconfirmed if knowledge redundancy shows only a linear relationship with survival
  or no significant relationship after controlling for bus factor.
related_works:
- >-
  Avelino et al. (2019) 'On the abandonment and survival of open source projects: An empirical investigation' - This paper
  studies bus/truck factor and finds that 41% of projects survive founder departure through new core developers. However,
  it measures only the NUMBER of critical contributors (bus factor), not the OVERLAP in their knowledge. My hypothesis introduces
  knowledge redundancy as a distinct construct that predicts survival beyond bus factor alone.
- >-
  Cosentino et al. (2016) 'Assessing the bus factor from repository data' - Proposes algorithms to compute bus factor from
  git repositories. My work differs by focusing on knowledge REDUNDANCY (overlap) rather than just the MINIMAL set of critical
  contributors, and by predicting survival outcomes rather than just measuring risk.
- >-
  Write access provisioning and organizational ownership in open source software projects (2025) - This recent paper explores
  how write access affects project novelty and survival. My hypothesis differs by focusing on the STRUCTURE of knowledge distribution
  (redundancy) rather than governance mechanisms (who has commit access), though these may interact.
- >-
  The State of Survival in OSS: The Impact of Diversity (ESEC/FSE 2023) - Studies demographic and motivational diversity among
  contributors. My hypothesis focuses on KNOWLEDGE diversity/redundancy (what contributors know) rather than demographic diversity
  (who they are), and predicts a non-monotonic rather than linear relationship.
inspiration: >-
  This hypothesis draws from three cross-disciplinary inspirations: (1) FROM INFORMATION THEORY: Error-correcting codes use
  controlled redundancy to enable recovery from data loss - too little redundancy fails to correct errors, too much wastes
  bandwidth. This inspired the inverted-U hypothesis for knowledge redundancy in projects. (2) FROM ORGANIZATIONAL PSYCHOLOGY:
  Research on team redundancy shows that some overlap in expertise enables backup behavior during member absence, but excessive
  overlap reduces specialization benefits. (3) FROM ECOLOGY: The diversity-stability hypothesis suggests ecosystems with moderate
  redundancy in species roles are most resilient to disturbance - neither completely specialized (vulnerable to keystone species
  loss) nor completely redundant (wastes resources).
terms:
- term: Knowledge redundancy
  definition: >-
    The degree of overlap in expertise areas among project contributors, measured as the average pairwise similarity in the
    sets of files, modules, or code areas that contributors modify. High redundancy means contributors work on the same things;
    low redundancy means each contributor has unique areas of expertise.
- term: Founder departure
  definition: >-
    The event where a project's original creator or primary contributor (identified by highest initial code authorship) stops
    making commits for an extended period (12+ months), marking their effective exit from active development.
- term: Bus factor
  definition: >-
    The minimal number of contributors whose simultaneous departure would render a project unable to continue development.
    A bus factor of 1 means a single person holds all critical knowledge; higher values indicate more distributed knowledge.
- term: Project survival
  definition: >-
    The continuation of active development (commits, releases, issue resolutions) after a disruption event (founder departure)
    at levels statistically consistent with pre-disruption activity patterns, sustained for a minimum period (12+ months).
- term: Inverted-U relationship
  definition: >-
    A non-monotonic relationship where the dependent variable (survival) first increases then decreases as the independent
    variable (knowledge redundancy) increases, forming an upside-down U shape. This indicates an optimal intermediate level
    rather than a linear benefit.
summary: >-
  This hypothesis predicts that open-source projects survive founder departure best when knowledge is moderately redundant
  among contributors - not completely concentrated in the founder (zero redundancy) nor completely overlapping across all
  contributors (excessive redundancy). This inverted-U relationship is distinct from bus factor and reveals an optimal structure
  for post-founder resilience.
_relation_rationale: >-
  Refining claims from confirmed finding to testable prediction given data limitations
_confidence_delta: decreased
_key_changes:
- >-
  Added explicit caveat that empirical test is pending due to data quality issues (file paths unavailable in current dataset)
- >-
  Added sample size requirement (N≥50) based on reviewer feedback on statistical power
- Reframed from 'we found' to 'we predict' given fatal flaw in Jaccard computation
- >-
  Added justification for inverted-U from three cross-disciplinary sources (information theory, organizational psychology,
  ecology)
- >-
  Made explicit that Jaccard similarity requires actual file paths, not just file counts
- >-
  Preserved core conceptual contribution: knowledge redundancy as distinct from bus factor
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_FiPBECDY22qD
  label: dataset
- id: art_iicMCU3WgldY
  label: methodology
- id: art_uYucfGHDjfdU
  label: methods
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
</all_artifacts>

<new_artifacts_this_iteration>
These 2 artifacts were created THIS iteration.

id: art_pOI-AO_xwHdm
type: experiment
in_dependencies:
- id: art_FiPBECDY22qD
  label: dataset
- id: art_iicMCU3WgldY
  label: methodology
- id: art_uYucfGHDjfdU
  label: methods
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) The central empirical claim of the paper — that knowledge redundancy (measured via Jaccard similarity) can be computed and tested as a predictor of project survival — could not be executed due to data limitations. The dataset (HuggingFace AdhyanshVerma/open-github-major-repos) contains only file_count per commit, not the file paths needed for Jaccard similarity. The authors acknowledge this in Section 3.2 and use a 'pseudo-KR' fallback measure (cosine similarity of file count distributions), but this measure is acknowledged to be a poor proxy for true knowledge redundancy. All results based on pseudo-KR (Table 2, Section 5.3) are therefore of questionable validity. More critically, even the pseudo-KR analysis could not test the central hypothesis because all 6 projects with founder departure survived (100% survival rate), providing no outcome variance for survival modeling.
  Action: The only satisfactory resolution is to obtain proper data with file paths for Jaccard similarity computation. Clone repositories directly from GitHub (as attempted in Appendix C) and use 'git log --name-only --format="%H %an"' to extract commit-file mappings. Target N≥50 repositories with founder departure events (matching the scale of Avelino et al.'s 1,932 projects). If this is infeasible within the current iteration budget, the paper must be reframed as a purely conceptual/methodological proposal with no empirical results section, or submitted to a venue that accepts 'research previews' or 'methodology papers' that don't require full empirical validation. The current hybrid (claiming empirical analysis but not actually testing the hypothesis) is the worst of both worlds.
- [MAJOR] (evidence) The sample size for survival analysis is N=6 repositories with founder departure, which is insufficient for any meaningful statistical inference. The paper acknowledges this limitation (Section 6.4, Item 2), but then proceeds to report descriptive statistics and pseudo-KR scores as if they constitute evidence. Harrell's rule of thumb for Cox proportional hazards models suggests 10-20 events per predictor variable; with 6 events (departures) and multiple predictors (KR, KR², bus factor, controls), the model is severely underpowered. More fundamentally, with 100% survival rate (all 6 projects survived), there is no outcome variance to model — the inverted-U hypothesis cannot be tested with these data.
  Action: Increase the sample to minimum N=30-50 repositories with founder departure events. This requires a larger dataset (the current 13 repositories is far too small). Use the GitHub API or clone repositories directly to obtain commit data. If adequate sample size cannot be obtained, remove all statistical analysis and survival modeling claims. Report only: (1) descriptive statistics of KR distribution, (2) case study descriptions of the 6 projects, (3) synthetic validation of methodology. Be explicit that the hypothesis remains untested due to sample size limitations.
- [MINOR] (novelty) The novelty of 'knowledge redundancy' as a construct is moderate but not groundbreaking. The paper claims this is the first work to propose KR measured via Jaccard similarity for OSS survival — this appears true based on literature search. However, related concepts are well-established: (1) Transactive memory systems literature (Ren & Argote 2011, cited as [12]) extensively studies knowledge overlap in teams; (2) Code ownership metrics (Fritz et al. 2010, cited as [13]) measure developer familiarity with code; (3) Bus factor research (Avelino et al. 2019, Jabrayilzade et al. 2022) implicitly captures aspects of knowledge distribution. The specific combination (Jaccard KR + survival analysis + inverted-U hypothesis) appears novel, but the underlying constructs are not new. The paper could do more to position itself within this broader literature.
  Action: Strengthen the novelty claim by more explicitly contrasting KR with related constructs: (1) How does KR differ from bus factor? (Answer: bus factor counts critical contributors; KR measures overlap among them — they capture different dimensions); (2) How does KR differ from code ownership (DOK)? (Answer: DOK measures individual familiarity; KR measures pairwise overlap); (3) What does the inverted-U hypothesis add beyond transactive memory theory? (Answer: specific testable prediction for OSS survival context). Add a table comparing KR to related constructs on: measurement method, unit of analysis, predicted relationship with survival. This clarifies the incremental contribution.
- [MINOR] (clarity) The abstract is misleading about what was accomplished. It states: 'Applying this framework to 500,000 commits from 13 open-source repositories, we identify founder departure events in 6 repositories. Due to data limitations (lack of file path information for Jaccard computation) and complete survival of all 6 projects, we could not statistically test the inverted-U hypothesis.' The phrase 'applying this framework' implies the framework was actually applied (i.e., Jaccard KR was computed), when in fact the key measurement (Jaccard similarity) could not be computed due to missing file paths. The 'pseudo-KR' fallback is not the framework described in Section 3.5 (Jaccard similarity). This creates a mismatch between what the paper promises and what it delivers.
  Action: Revise the abstract to accurately describe what was actually done: 'We describe a framework for measuring knowledge redundancy via Jaccard similarity of contributor file sets and apply a fallback measurement (pseudo-KR from file count distributions) to 500,000 commits from 13 repositories. We identify 6 founder departure events, but due to complete survival of all projects and lack of file path data for Jaccard computation, we could not statistically test the inverted-U hypothesis. Instead, we report descriptive patterns, validate our methodology on synthetic data, and provide open-source tools for future large-scale validation.' This accurately sets reader expectations.
- [MINOR] (scope) The generalizability of findings is severely limited. The 13 repositories are all large, popular projects from a 'major-repos' dataset (HuggingFace AdhyanshVerma/open-github-major-repos). These are not representative of the typical OSS project — they have hundreds of contributors, thousands of commits, and high visibility. The 100% survival rate likely reflects this selection bias (popular projects are more resilient). The findings may not generalize to: (1) small/personal OSS projects, (2) less popular projects, (3) projects in different languages or domains, (4) projects hosted on non-GitHub platforms. The discussion (Section 6.4, Item 4) mentions selection bias but does not fully grapple with its implications.
  Action: Add a 'Generalizability' subsection in Discussion that explicitly lists the scope constraints: (1) GitHub-only (findings may not generalize to GitLab, Bitbucket, etc.), (2) Large/popular projects (findings may not generalize to small/niche projects), (3) Founder departure only (not general core developer turnover), (4) Specific dataset bias (HuggingFace major-repos dataset skews toward popular projects). Consider adding a diversity metric (e.g., project size quartiles) to show whether KR patterns differ across project sizes. If possible, include 2-3 small projects for contrast.
- [MINOR] (rigor) The 'pseudo-KR' measure (cosine similarity of file count distributions) is used throughout the results but its validity is not established. The paper acknowledges it is 'a poor proxy for true Jaccard-based knowledge redundancy' (Section 3.2), but then reports pseudo-KR scores in Table 2 and discusses their range (0.119 to 0.969) as if they are meaningful. Without validation against true Jaccard KR, these scores could be meaningless — the wide range (0.119 to 0.969) might reflect differences in contributor activity levels rather than true knowledge overlap. The paper should either validate pseudo-KR against true KR on a subset, or stop reporting pseudo-KR scores as if they measure knowledge redundancy.
  Action: Validate pseudo-KR against true Jaccard KR on a subset of 5-10 repositories where file path data can be obtained (the paper already cloned 9 repos per Appendix C). Compute both measures, report correlation (Pearson/Spearman). If correlation is high (r > 0.7), pseudo-KR may be an acceptable proxy and this should be stated. If correlation is low (r < 0.5), the paper should stop reporting pseudo-KR scores and acknowledge that no valid KR measurement was possible. Alternatively, remove all pseudo-KR results and report only that 'KR could not be measured due to data limitations' — this is honest and avoids reporting potentially meaningless numbers.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 01:38:33 UTC

```
What determines whether an open-source project survives its founder stepping away?
```
