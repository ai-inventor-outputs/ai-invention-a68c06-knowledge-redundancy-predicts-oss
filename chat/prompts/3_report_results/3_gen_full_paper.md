# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `iter1_924aa01cf43b` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 18:50:26 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
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
  Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study
abstract: >-
  Open-source software (OSS) projects frequently depend on a small number of core developers, making founder departure a major
  threat to project continuity. While the 'bus factor' is well-studied, it fails to capture the overlap in contributor expertise.
  This paper introduces knowledge redundancy—the overlap in contributor expertise measured via Jaccard similarity of file
  modification patterns—as a candidate predictor of post-founder survival. We test the hypothesis that knowledge redundancy
  has an inverted-U relationship with project survival using Cox proportional hazards models on 1,000 synthetic GitHub repositories
  designed to match real-world distributions. The quadratic term is not statistically significant (p = 0.71), and survival
  rate differences are small (1-3%), failing to confirm the inverted-U hypothesis. We discuss methodological implications,
  provide open-source tools for computing knowledge redundancy, and outline future steps for real-data validation. This study
  demonstrates the importance of transparent null-result reporting and methodological validation before large-scale data collection.
paper_text: |
  # Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study

  ## Abstract

  Open-source software (OSS) projects frequently depend on a small number of core developers, making founder departure a major threat to project continuity. While the "bus factor" (the minimal number of developers whose departure would stall a project) is well-studied, it fails to capture an important dimension: the degree of overlap in what contributors know. This paper introduces knowledge redundancy—the overlap in contributor expertise measured via Jaccard similarity of file modification patterns—as a candidate predictor of post-founder survival. We describe the metric's construction, validate it against synthetic data designed to match real-world distributions from 1,000 GitHub repositories, and test the hypothesis that knowledge redundancy has an inverted-U relationship with project survival. Using Cox proportional hazards models with quadratic terms, we do **not** find evidence for the inverted-U relationship: the quadratic term is not statistically significant (β₂ = -2.34, p = 0.71), and model comparison favors the linear model (AIC difference = 1.86). Survival rates show only a 1.5% difference between moderate and low redundancy projects, far below the hypothesized 20% effect. These null results suggest that either the relationship does not exist in the synthetic data, the effect size is smaller than anticipated, or the measurement approach requires refinement. We discuss methodological implications, provide open-source tools for computing knowledge redundancy, and outline future steps for real-data validation.

  **Keywords**: open-source software, project survival, knowledge redundancy, bus factor, survival analysis, null results

  ## 1. Introduction

  ### 1.1 The Problem: Founder Dependence in Open-Source Software

  Open-source software (OSS) projects form the infrastructure of modern computing, yet many depend critically on a small number of core developers. When these key contributors depart—whether due to burnout, career changes, or loss of interest—projects often face abandonment. Avelino et al. [1] found that 16% of popular GitHub projects experience founder departure (termed "Truck Factor Developer Detachment"), and while 41% of these survive by attracting new maintainers, the remainder become abandoned or dormant.

  The traditional metric for assessing this vulnerability is the "bus factor"—the minimal number of contributors whose simultaneous departure would render a project unable to continue [3]. A bus factor of 1 means a single person holds all critical knowledge; higher values indicate more distributed knowledge. However, bus factor measurement has a critical limitation: it counts the number of critical contributors but does not measure the overlap in their expertise.

  ### 1.2 The Gap: Counting Contributors vs. Measuring Overlap

  Consider two projects, each with a bus factor of 2. In Project A, the two contributors work on completely different modules—one handles the frontend, the other the backend. In Project B, both contributors work primarily on the same core files. Both projects have the same bus factor, but their resilience to founder departure may differ dramatically. Project A has low knowledge redundancy—if the founder leaves, the remaining contributor cannot maintain the founder's modules. Project B has high knowledge redundancy—the remaining contributor can step in, but the project may suffer from coordination overhead and lack of specialization.

  This distinction—between the number of critical contributors and the overlap in their knowledge—is not captured by existing metrics. Knowledge redundancy, defined as the degree of overlap in expertise areas among contributors, may be a distinct and measurable predictor of project survival after founder departure.

  ### 1.3 Why It Is Hard: Measuring Invisible Knowledge

  Measuring knowledge redundancy from observable data is challenging. Contributor expertise is not directly observable; it must be inferred from contribution patterns. Prior work has used file authorship [2], code review participation, and communication records to map knowledge networks [9], but these approaches have not been synthesized into a continuous metric of knowledge overlap suitable for survival analysis.

  Additionally, the relationship between knowledge redundancy and survival may be non-monotonic. Organizational psychology literature suggests an inverted-U relationship: too little redundancy creates single points of failure, while too much redundancy reduces specialization benefits and increases coordination costs [7, 8]. Testing this hypothesis requires large-scale data, appropriate statistical models (Cox proportional hazards with quadratic terms), and careful control for confounding variables.

  ### 1.4 This Study: Methodological Validation

  This paper takes a methodological validation approach. Rather than claiming a confirmed empirical relationship, we:

  1. **Define and validate the metric**: We introduce knowledge redundancy as the average pairwise Jaccard similarity of file modifications among top contributors, a continuous [0,1] metric computable from git history.

  2. **Test the hypothesis on synthetic data**: We apply the metric to 1,000 synthetic GitHub repositories designed to match real-world distributions and test the inverted-U hypothesis using Cox proportional hazards models.

  3. **Report null results transparently**: We find no evidence for the inverted-U relationship in the synthetic data and discuss possible reasons.

  4. **Provide open-source tools**: We release code for computing knowledge redundancy and collecting real GitHub data, enabling future validation studies.

  This approach acknowledges a critical reality: before investing in large-scale data collection from the GitHub API (which requires authentication, rate limiting, and substantial computational resources), the measurement approach and statistical methods must be validated. Our synthetic data study provides this validation.

  ### 1.5 Summary of Findings

  The main findings are:

  1. **Null result on inverted-U**: The quadratic term for knowledge redundancy in Cox models is not significant (p = 0.71), and the coefficient has the opposite sign (negative) than predicted by the inverted-U hypothesis.

  2. **Small effect sizes**: Survival rate differences between redundancy levels are 1-3%, far below the hypothesized 20%.

  3. **Methodological contribution**: The knowledge redundancy metric is computable at scale, correlates appropriately with bus factor (r = -0.34, p < 0.001), and can be integrated into existing OSS sustainability dashboards.

  \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-1/research-1}}

  [FIGURE:fig1]

  ## 2. Related Work

  ### 2.1 Open-Source Project Survival

  Avelino et al. [1] conducted the seminal large-scale study of OSS survival, analyzing 1,932 GitHub projects and finding that 16% experience founder departure (Truck Factor Developer Detachment), with 41% of these surviving through new maintainer adoption. Survival was defined as the project transitioning from "inactive" (all truck factor developers gone) to "active" (new truck factor developer appears) within one year. The study validated a 12-month inactivity threshold as optimal for distinguishing departure from temporary absence.

  Subsequent work has identified multiple predictors of survival. Constantinou and Mens [11] used Cox proportional hazards models and found that social capital (bonding, bridging, and linking ties) significantly predicts sustained participation (HR = 1.45, 95% CI: 1.21-1.74). Trinkenreich et al. [5] found that contributor diversity affects survival, with company-backed and Western contributors having higher survival probability than volunteer and Non-Western contributors.

  However, these studies focus on social and demographic factors, not the structure of technical knowledge distribution. Our work addresses this gap by introducing knowledge redundancy as a technical predictor.

  ### 2.2 Bus Factor Measurement

  The bus factor (or truck factor) was formalized by Cosentino et al. [3], who proposed three algorithms for computing it from git repositories: AVL (Avelino et al.), CST (Cosentino et al.), and RIG (Rigby et al.). A comparative study found that the AVL algorithm, which uses the Degree of Authorship (DOA) metric, achieves the best precision (77-100%) and recall (73-100%) when validated against developer surveys.

  The DOA metric [2] computes contributor expertise as:
  DOA = 3.293 + 1.098×FA + 0.164×DL - 0.321×ln(1+AC)
  where FA = First Authorship (binary), DL = Deliveries (number of changes), and AC = Acceptances (changes by others). A threshold of DOA > 0.75 identifies authorship.

  While bus factor measurement is well-validated, it has limitations. Haratian et al. [19] note that not all files are equally important—bus factor algorithms that weight files by significance improve accuracy by 15%. Additionally, bus factor counts contributors but does not measure knowledge overlap, which is the focus of our work.

  ### 2.3 Knowledge Redundancy in Teams

  The concept of knowledge redundancy originates in organizational psychology. Transactive Memory Systems (TMS) research [6] shows that teams with well-distributed knowledge (moderate redundancy) perform better than those with either too little or too much overlap. A meta-analysis by Van Knippenberg and Schippers [7] found an inverted-U relationship between team diversity (a related construct) and performance.

  In software engineering, knowledge networks have been mapped using code authorship [9], review participation, and communication data. Linstead et al. [9] identified "knowledge islands"—developers with concentrated expertise—and demonstrated that knowledge distribution affects team performance. However, these studies map networks descriptively; they do not predict survival outcomes or test the inverted-U hypothesis.

  Wang et al. [8] recently confirmed an inverted-U relationship between knowledge diversity and societal impact in scientific research, providing theoretical support for our hypothesis. However, no prior work has tested this relationship in the OSS context.

  ### 2.4 Novelty of This Work

  This research makes three specific contributions:

  **Contribution 1: Knowledge Redundancy as Continuous Predictor**
  Unlike the bus factor [2, 3], which counts critical developers as a discrete metric, we measure knowledge redundancy as a continuous variable (0-1 scale). This captures nuanced differences between projects with identical bus factors but different expertise overlap structures.

  **Contribution 2: Methodological Validation**
  While organizational psychology literature supports inverted-U relationships [7, 8], this relationship has not been tested in OSS contexts. We provide the first methodological validation of the measurement approach using synthetic data, enabling future real-data studies.

  **Contribution 3: Open-Source Implementation**
  We adapt Jaccard similarity [6] to OSS contexts and provide open-source tools for computing knowledge redundancy at scale, lowering the barrier for adoption by OSS maintainers and researchers.

  **Explicit Contrast with Prior Work**:
  - Unlike Avelino et al. [1], who measure bus factor as a count, we measure continuous knowledge overlap.
  - Unlike Cosentino et al. [3], who focus on estimation algorithms, we use bus factor as a starting point but extend it to measure expertise overlap structure.
  - Unlike Linstead et al. [9], who map knowledge networks descriptively, we use network metrics to predict survival outcomes.
  - Unlike community smells research [12], which captures negative social patterns, we quantify positive knowledge distribution structure.

  \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-2/research-1}}

  ## 3. Methods

  ### 3.1 Data Collection and Synthetic Data Generation

  We generated a synthetic dataset of 1,000 GitHub repositories with the following characteristics designed to match real-world distributions:

  - **Founders and contributors**: Simulated contributor networks with realistic commit patterns
  - **Knowledge redundancy scores**: Computed using the Jaccard similarity method described below
  - **Survival outcomes**: Simulated based on parameters from Avelino et al. [1] (16% abandonment rate, 41% survival rate among abandoned)
  - **Repository metadata**: Stars, forks, creation dates, primary languages sampled from real GitHub distributions

  The data generation process is described in detail in the accompanying dataset artifact [ARTIFACT:art_5yxZHBH-Wwc_]. The synthetic data enables methodological validation without requiring GitHub API authentication and rate limiting.

  **Important caveat**: The results presented here are based on synthetic data. While the data generation process was designed to match real-world distributions, validation on real GitHub data is required to confirm these findings. Section 5.4 discusses this limitation in detail.

  ### 3.2 Founder Identification and Departure

  We defined the **founder** as the contributor with the highest number of commits in the project's first 6 months. This operationalization aligns with Avelino et al. [1] and captures the original creator/main contributor.

  **Founder departure** was defined as 12+ months of inactivity (no commits) after a period of active contribution (≥6 commits in the 12 months prior). This threshold was validated by Avelino et al. [1], who found that 12 months provides the best harmonic mean (66%) across five candidate thresholds for distinguishing departure from temporary absence.

  ### 3.3 Knowledge Redundancy Measurement

  Knowledge redundancy was measured as the average pairwise Jaccard similarity of file modification patterns among the top 5 contributors (by total commits). For each contributor *i*, we computed the set of files they modified: *S_i* = {files modified by contributor *i*}.

  The Jaccard similarity between contributors *i* and *j* is:
  J(i,j) = |S_i ∩ S_j| / |S_i ∪ S_j|

  The knowledge redundancy score for a repository is the mean Jaccard similarity across all pairs of the top 5 contributors:
  KR = (2/(n(n-1))) × Σ_{i<j} J(i,j)
  where n = min(5, number of contributors).

  This metric ranges from 0 (no overlap—each contributor modifies completely disjoint file sets) to 1 (complete overlap—all contributors modify the same files). The choice of Jaccard similarity is validated by organizational psychology literature [6] and prior work on knowledge networks [9].

  **Alternative measures** considered include weighted Jaccard (weighting by commit count), overlap coefficient (|S_i ∩ S_j| / min(|S_i|, |S_j|)), and Shannon entropy of file distributions. Sensitivity analysis using these alternatives is reported in Section 4.4.

  ### 3.4 Survival Definition

  Project survival was defined as continued development activity after founder departure at levels statistically consistent with pre-departure trends. Specifically:

  1. **Pre-departure activity**: Mean commits per month in the 12 months before founder departure
  2. **Post-departure activity**: Mean commits per month in the 12 months after founder departure
  3. **Survival criterion**: Post-departure activity ≥ 50% of pre-departure activity

  This 50% threshold ensures that surviving projects maintain substantial activity, not just minimal maintenance. Sensitivity analysis with 25% and 75% thresholds is reported in Section 4.4.

  Projects that did not meet the survival criterion were classified as "died." Projects where the founder had not departed by the data collection end date were right-censored in survival analysis.

  ### 3.5 Statistical Analysis

  We used Cox proportional hazards models to test the relationship between knowledge redundancy and survival. The base model is:

  h(t, KR) = h₀(t) × exp(β₁KR + β₂KR²)

  where KR is knowledge redundancy, and the quadratic term KR² tests the inverted-U hypothesis.

  **Inverted-U confirmation criteria** (from hypothesis):
  1. β₂ < 0 and statistically significant (p < 0.05)
  2. Projects with moderate redundancy (25th-75th percentile) show 20%+ higher survival than very low redundancy (<10th percentile)
  3. Projects with very high redundancy (>90th percentile) show 10%+ LOWER survival than moderate redundancy

  **Control variables** included:
  - Bus factor (computed via Avelino et al. [2] DOA algorithm)
  - Project age (days from first commit to founder departure)
  - Project size (total commits, log-transformed)
  - Popularity (stars, log-transformed)
  - Programming language (one-hot encoded)
  - Number of top contributors (count)

  **Model diagnostics**:
  - Proportional hazards assumption: Schoenfeld residuals test (p > 0.05)
  - Linearity: Martingale residuals examination
  - Collinearity: Variance Inflation Factor (VIF < 5)
  - Quadratic term significance: Likelihood ratio test

  All analyses were conducted in Python using the `lifelines` library [20].

  ## 4. Results

  ### 4.1 Dataset Overview

  The synthetic dataset comprises 1,000 GitHub repositories with the following characteristics:

  - **Founder departures**: 768 repositories (76.8%) had founder departure
  - **Survival outcomes**: Among departed projects, 601 survived (78.3%) and 167 died (21.7%)
  - **Knowledge redundancy**: Mean = 0.412, Std = 0.185, Min = 0.05, Max = 0.78
  - **Bus factor**: Mean = 1.8, Std = 0.9 (consistent with Avelino et al. [1] finding 57% of projects have TF=1)
  - **Project age**: Mean = 3.2 years at founder departure
  - **Programming languages**: Python (13.6%), JavaScript (12.8%), Java (12.6%), Go (12.6%), Rust (12.6%), TypeScript (12.4%), C++ (12.6%), Ruby (10.8%)

  [ARTIFACT:art_5yxZHBH-Wwc_]

  ### 4.2 Knowledge Redundancy Distribution

  Figure 1 shows the distribution of knowledge redundancy scores across all repositories.

  [FIGURE:fig1]

  The distribution is approximately normal with a slight right skew (skewness = 0.34), suggesting that most projects have moderate redundancy (0.3-0.5) with fewer projects at the extremes. The 10th percentile is at KR = 0.15, the 25th at KR = 0.27, the 75th at KR = 0.56, and the 90th at KR = 0.65.

  ### 4.3 Survival Rates by Redundancy Level

  Table 1 shows survival rates stratified by knowledge redundancy quartiles.

  **Table 1: Survival Rates by Knowledge Redundancy Quartile**

  | Redundancy Range | N (Departed) | Survived | Survival Rate (%) |
  |------------------|--------------|----------|-------------------|
  | Very Low (0-0.15) | 77 | 52 | 67.5% |
  | Low (0.15-0.27) | 115 | 89 | 77.4% |
  | Moderate (0.27-0.56) | 384 | 301 | 78.4% |
  | High (0.56-0.65) | 115 | 89 | 77.4% |
  | Very High (0.65-1.0) | 77 | 70 | 90.9%* |

  *Note: The very high redundancy category shows anomalously high survival—this is explained by the small sample size and will be addressed in regression analysis.

  Projects with moderate redundancy (0.27-0.56) show a 10.9 percentage point higher survival rate than those with very low redundancy (0-0.15), corresponding to a 16.2% relative improvement. However, this raw comparison does not account for control variables.

  ### 4.4 Cox Proportional Hazards Model

  Table 2 presents the Cox model results testing the inverted-U hypothesis.

  **Table 2: Cox Proportional Hazards Model Results**

  | Predictor | β Coefficient | Hazard Ratio | p-value |
  |-----------|---------------|--------------|---------|
  | KR (linear) | 0.615 | 1.85 | 0.45 |
  | KR² (quadratic) | -2.34 | 0.10 | 0.71 |
  | Bus Factor | -0.059 | 0.94 | 0.21 |
  | log(Stars) | -0.002 | 1.00 | 0.98 |
  | log(Total Commits) | 0.072 | 1.07 | 0.44 |
  | Pre-departure Commits/Month | 0.004 | 1.00 | 0.74 |
  | Contributors Count | -0.058 | 0.94 | 0.21 |
  | Language (ref: Python) | - | - | - |
  | - JavaScript | 0.268 | 1.31 | 0.53 |
  | - Java | -0.189 | 0.83 | 0.68 |
  | - Go | -0.407 | 0.67 | 0.37 |
  | - Rust | 0.027 | 1.03 | 0.95 |
  | - TypeScript | -0.041 | 0.96 | 0.92 |
  | - C++ | 0.248 | 1.28 | 0.56 |
  | - Ruby | -0.178 | 0.84 | 0.69 |

  **Key findings**:

  1. **Inverted-U NOT confirmed**: The quadratic term for knowledge redundancy is negative (β = -2.34) but NOT statistically significant (p = 0.71), failing to confirm the inverted-U relationship. The sign is opposite to what would indicate an inverted-U in the hazard function (a positive β₂ with negative β₁ would create a U-shaped hazard, meaning survival is inverted-U).

  2. **Turning point**: The estimated turning point from the quadratic model is at KR* = -β₁/(2β₂) = -0.615/(2 × -2.34) = 0.131. However, since the quadratic term is not significant, this estimate is unreliable.

  3. **Hazard ratios**: Because the quadratic term is not significant, hazard ratios vary depending on the value of KR. At KR = 0.2, HR = exp(0.615×0.2 - 2.34×0.04) = exp(0.123 - 0.094) = exp(0.029) = 1.03. At KR = 0.4, HR = exp(0.615×0.4 - 2.34×0.16) = exp(0.246 - 0.374) = exp(-0.128) = 0.88. At KR = 0.6, HR = exp(0.615×0.6 - 2.34×0.36) = exp(0.369 - 0.842) = exp(-0.473) = 0.62. The hazard ratio pattern (1.03 → 0.88 → 0.62) shows decreasing hazard (increasing survival) with higher KR, which is a linear rather than inverted-U relationship.

  4. **Model comparison**: The linear model (AIC = 2194.49) outperforms the quadratic model (AIC = 2196.35) by 1.86 AIC points, suggesting the linear model is preferred. The likelihood ratio test comparing the two models yields χ² = 0.145, p = 0.70, confirming that adding the quadratic term does not improve model fit.

  5. **Control variables**: None of the control variables (bus factor, stars, commits, age, contributor count) significantly predict survival in this synthetic dataset, which may reflect limitations of the data generation process.

  [FIGURE:fig2]

  Figure 2 visualizes the relationship between knowledge redundancy and survival probability, showing the predicted survival curve from both linear and quadratic Cox models.

  ### 4.5 Hypothesis Evaluation

  The three success criteria from the hypothesis are evaluated:

  1. **Quadratic term significant**: β₂ = -2.34, p = 0.71 ✗ **NOT CONFIRMED**
  2. **Moderate vs. very low redundancy**: Moderate redundancy (25th-75th percentile) shows 1.5% higher survival than very low (<10th percentile) in the adjusted model ✗ **NOT CONFIRMED** (hypothesized >20%)
  3. **Very high vs. moderate redundancy**: Very high redundancy (>90th percentile) shows 2.8% higher survival than moderate in the adjusted model ✗ **NOT CONFIRMED** (hypothesized 10% lower)

  **All three criteria failed to confirm the hypothesis.** The inverted-U relationship between knowledge redundancy and OSS project survival is not supported by the synthetic data.

  ### 4.6 Sensitivity Analysis

  **Alternative redundancy measures**: Using weighted Jaccard (weighting by commit count) yields similar null results (β₁ = 0.58, β₂ = -2.19, p = 0.73). Overlap coefficient produces a similar pattern (β₁ = 0.72, β₂ = -2.87, p = 0.68). Shannon entropy (where higher = more diverse = lower redundancy) shows a weak positive linear relationship with survival, but no quadratic effect.

  **Survival threshold**: Changing the survival threshold from 50% to 25% increases the survival rate but preserves the null result (β₁ = 0.54, β₂ = -2.11, p = 0.74). At 75% threshold, the effect remains null (β₁ = 0.63, β₂ = -2.45, p = 0.69).

  **Founder identification**: Using "most commits ever" instead of "most commits in first 6 months" for founder identification changes 12% of classifications but does not alter the main findings (β₁ = 0.59, β₂ = -2.28, p = 0.72).

  **Departure threshold**: Using 6 months instead of 12 months for departure definition increases the number of departures but weakens the effect further (β₁ = 0.41, β₂ = -1.67, p = 0.78).

  ## 5. Discussion

  ### 5.1 Interpretation of Null Results

  The inverted-U relationship between knowledge redundancy and OSS project survival was NOT confirmed in this synthetic dataset. Several explanations are possible:

  **1. True null effect**: The relationship may not exist in real OSS data. While organizational psychology literature supports inverted-U relationships in teams [7, 8], OSS projects may differ fundamentally. OSS contributors are often distributed globally, work asynchronously, and have different commitment levels than organizational teams. The mechanisms that create inverted-U relationships in co-located teams (coordination costs, free-riding) may not operate the same way in OSS.

  **2. Effect size too small**: The true effect may be smaller than our hypothesized 20% difference. The observed differences in our synthetic data are 1-3%, suggesting that if the effect exists, it is small and requires larger sample sizes or more precise measurement to detect.

  **3. Measurement error**: The Jaccard similarity method may not accurately capture "knowledge redundancy." Contributors may modify files without deep understanding (e.g., minor fixes), or may have expertise not reflected in recent commits (e.g., architectural knowledge). The top-5-contributors operationalization may miss important knowledge holders.

  **4. Synthetic data limitations**: The data generation process may not have captured the true relationship. The synthetic data was designed to match distributions (means, variances) but may not capture the joint distribution between knowledge redundancy and survival. Real GitHub data is needed.

  ### 5.2 Comparison to Prior Work

  Our null findings contrast with organizational psychology literature that finds inverted-U relationships between knowledge diversity and performance [7, 8]. However, there are important differences:

  1. **Context difference**: Organizational teams are typically co-located, synchronous, and have formal coordination mechanisms. OSS projects are distributed, asynchronous, and have informal coordination.

  2. **Measurement difference**: Prior work measures knowledge diversity through surveys and self-reports [7, 8]. We measure it through file modification patterns, which may capture different constructs.

  3. **Outcome difference**: Prior work measures team performance (sales, quality) [7, 8]. We measure project survival (continued activity), which is a longer-term, binary outcome.

  Our findings align with the null results in some OSS studies. For example, several unpublished citations suggest weak relationships between contributor metrics and survival. The OSS context may simply have different predictors than organizational teams.

  ### 5.3 Methodological Contributions

  Despite the null results, this study makes methodological contributions:

  1. **Metric definition**: We provide a clear, computable definition of knowledge redundancy using Jaccard similarity on file modifications. The metric is continuous, scalable, and automatable.

  2. **Open-source tools**: We release code for computing knowledge redundancy and collecting GitHub data, lowering the barrier for future research.

  3. **Statistical approach**: We demonstrate the use of Cox proportional hazards models with quadratic terms for testing inverted-U hypotheses in survival data.

  4. **Synthetic data validation**: We show that synthetic data can be used to validate measurement approaches before investing in large-scale data collection.

  ### 5.4 Limitations

  **Synthetic data caveat**: The dataset used in this study is synthetic data [ARTIFACT:art_5yxZHBH-Wwc_]. While the data generation process was designed to match real-world distributions (based on Avelino et al. [1] and other empirical studies), validation on real GitHub data is needed. The dataset artifact includes a data collection script suitable for real-world deployment.

  **Measurement limitations**: Knowledge redundancy measured via file modifications is a proxy for actual expertise. Contributors may modify files without deep understanding (e.g., minor fixes), or may have expertise not reflected in recent commits (e.g., architectural knowledge). Future work could incorporate code review data, issue discussions, and developer surveys.

  **Survival definition**: Our 50% activity threshold is somewhat arbitrary. While sensitivity analysis shows the null result is robust to threshold changes, the optimal threshold may vary by project type.

  **Confounding variables**: While we control for several known predictors, unobserved variables (e.g., project governance, company backing, external events) may influence both redundancy and survival.

  **Generalizability**: The 8 programming languages studied may not represent all OSS projects. Web frameworks, data science libraries, and system tools may have different optimal redundancy levels.

  ### 5.5 Future Research

  1. **Validate on real data**: Apply the methodology to real GitHub data using the provided collection script. This is the most critical next step.

  2. **Refine measurement**: Explore alternative measures of knowledge redundancy, such as code review participation, issue discussions, and developer surveys.

  3. **Temporal dynamics**: Study how knowledge redundancy evolves over time and whether changes in redundancy predict survival.

  4. **Intervention studies**: Test whether intentionally increasing redundancy (through mentoring, documentation) improves survival.

  5. **Alternative hypotheses**: Test linear or other functional forms of the relationship. The null quadratic result does not rule out a linear relationship.

  6. **Qualitative mechanisms**: Survey contributors to understand the processes (backup behavior, coordination costs) that mediate the redundancy-survival relationship.

  ## 6. Conclusion

  This paper introduced knowledge redundancy—the overlap in contributor expertise measured via Jaccard similarity of file modifications—as a candidate predictor of open-source project survival after founder departure. Using Cox proportional hazards models to test the inverted-U hypothesis on 1,000 synthetic GitHub repositories, we did **not** find evidence for the hypothesized relationship. The quadratic term was not significant (p = 0.71), and survival rate differences were small (1-3%).

  These null results suggest several possibilities: (1) the inverted-U relationship may not exist in OSS contexts, (2) the effect size may be smaller than anticipated, or (3) the measurement approach requires refinement. Importantly, this study provides open-source tools for computing knowledge redundancy and collecting real GitHub data, enabling future validation studies.

  For OSS project maintainers and researchers, the key takeaway is methodological: knowledge redundancy can be measured at scale from git history, but its relationship to survival remains unconfirmed. Future work should prioritize validation on real GitHub data, refinement of the measurement approach, and exploration of alternative functional forms.

  We contribute: (1) a validated metric definition, (2) open-source implementation, (3) statistical approach for testing inverted-U hypotheses, and (4) honest reporting of null results—an important but underreported outcome in software engineering research.

  ## Acknowledgments

  We thank the anonymous reviewers for their feedback on earlier drafts. This work was conducted as part of the AI Inventor automated research system.

  ## References

  [1] Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. (2019). On the abandonment and survival of open source projects: An empirical investigation. *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*, 1-12.

  [2] Avelino, G., Passos, L., Hora, A., & Valente, M. T. (2016). A novel approach for estimating Truck Factors. *2016 IEEE 24th International Conference on Program Comprehension (ICPC)*, 1-10.

  [3] Cosentino, V., Cánovas Izquierdo, J. L., & Cabot, J. (2015). Assessing the bus factor of Git repositories. *2015 IEEE 22nd International Conference on Software Analysis, Evolution, and Reengineering (SANER)*, 499-503.

  [4] Validation study (SBCARS 2016). Truck Factor Comparison Study.

  [5] Trinkenreich, B. et al. (2023). The State of Survival in OSS: The Impact of Diversity. *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)*.

  [6] Cooke, N. J., Salas, E., Cannon-Bowers, J. A., & Stout, R. J. (2000). Measuring Team Knowledge. *Human Factors: The Journal of Human Factors and Ergonomics Society*, 42(1), 151-173.

  [7] Van Knippenberg, D., & Schippers, M. (2007). Work group diversity. *Annual Review of Psychology*, 58, 515-541.

  [8] Wang, G., Gan, Y., & Yang, H. (2022). The inverted U-shaped relationship between knowledge diversity of researchers and societal impact. *Scientific Reports*, 12, 18585.

  [9] Linstead, E., Burch, C., Dye, A., Koehl, A., Roper, P., Finley, P., Jenkins, J., Pollock, L., Stotts, D., & Cartwright, R. (2017). Software teams and their knowledge networks in large-scale software development. *Information and Software Technology*, 84, 1-15.

  [10] Kaushik, M. & Chahal, K. (2026). The death spiral of open source projects: A post-mortem analysis of pull request workflow dynamics. *Journal of Systems and Software*, 240, 112942.

  [11] Constantinou, E. & Mens, T. (2019). Going Farther Together: The Impact of Social Capital on Sustained Participation in Open Source. *2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE)*, 688-699.

  [12] Ahammed, T., Asad, M., & Sakib, K. (2021). Understanding the Relationship between Missing Link Community Smell and Fix-inducing Changes. *Proceedings of the 16th International Conference on Evaluation of Novel Approaches to Software Engineering (ENASE)*, 469-475.

  [13] SBCARS. (2016). Truck Factor Comparison Study. *SBCARS*.

  [14] Avelino et al. (2016). Degree of Authorship in Git Repositories. *arXiv:1604.06766*.

  [15] Haratian et al. (2023). File Significance in Bus Factor. *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering*.

  [16] Klein, D., Šmite, D., Moe, N., Sablis, A., & Wohlin, C. (2017). Software teams and their knowledge networks. *Information and Software Technology*, 86, 71-86.

  [17] Cox, D. R. (1972). Regression models and life-tables. *Journal of the Royal Statistical Society*, Series B, 34(2), 187-220.

  [18] Hosmer, D. W., Lemeshow, S., & May, S. (2008). *Applied Survival Analysis: Regression Modeling of Time-to-Event Data* (2nd ed.). Wiley.

  [19] Haratian, V., Evtikhiev, M., Derakhshanfar, P., Tüzün, E., & Kovalenko, V. (2023). BFSig: Leveraging File Significance in Bus Factor Estimation. *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering*.

  [20] Davidson-Pilon, C. (2019). lifelines: survival analysis in Python. *Journal of Open Source Software*, 4(40), 1317.

  ## Appendix A: Data Collection

  The data collection methodology and scripts are available in the dataset artifact [ARTIFACT:art_5yxZHBH-Wwc_]. The approach uses the GitHub GraphQL API to efficiently collect commit histories and contributor data, with rate limiting (5000 requests/hour for authenticated users).

  ## Appendix B: Measurement Validation

  Additional validation of the knowledge redundancy metric is provided in the research artifact \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/main/round-1/research-2}}, including comparisons to alternative measures (weighted Jaccard, overlap coefficient, HHI index, Shannon entropy) and correlations with bus factor.

  ## Appendix C: Cox Model Diagnostics

  Schoenfeld residuals test: p = 0.42 (proportional hazards assumption holds).
  Martingale residuals: No significant non-linearity detected.
  Variance Inflation Factor (VIF): All VIFs < 2.5 (no multicollinearity).
  Likelihood ratio test for quadratic term: χ² = 0.145, p = 0.70 (not significant).
summary: >-
  This methodological validation study introduces knowledge redundancy (measured via Jaccard similarity of file modifications)
  as a candidate predictor of open-source project survival after founder departure. Testing the inverted-U hypothesis on 1,000
  synthetic GitHub repositories using Cox proportional hazards models, the study finds no evidence for the hypothesized relationship:
  the quadratic term is not significant (p = 0.71), and survival rate differences are small (1-3%). The paper provides open-source
  tools for computing knowledge redundancy, honestly reports null results, and outlines future steps for real-data validation.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Knowledge Redundancy Measurement Method
caption: >-
  Illustration of knowledge redundancy measurement using Jaccard similarity. Left: Two contributors (A and B) with disjoint
  file sets (low redundancy, J=0.0). Middle: Contributors with partial overlap (moderate redundancy, J=0.4). Right: Contributors
  with identical file sets (high redundancy, J=1.0). Knowledge redundancy for a repository is the average pairwise Jaccard
  similarity among top contributors.
image_gen_detailed_description: >-
  Three-panel horizontal diagram. Panel 1 (Low Redundancy): Two circles labeled 'Contributor A' and 'Contributor B', each
  with 3 distinct boxes representing files (A1,A2,A3 and B1,B2,B3). No overlap. Label: 'J=0.0'. Panel 2 (Moderate Redundancy):
  Two circles with 1 overlapping file box (shared file S1). Contributor A has A1,A2,S1. Contributor B has B1,S1,B2. Label:
  'J=0.4'. Panel 3 (High Redundancy): Two circles with all 3 file boxes overlapping. Both have files S1,S2,S3. Label: 'J=1.0'.
  Bottom: Formula 'KR = average J(i,j) for all contributor pairs'. Title at top: 'Knowledge Redundancy via Jaccard Similarity'.
  Clean white background, sans-serif font, light blue circles, gray file boxes.
aspect_ratio: '21:9'
summary: >-
  Concept diagram explaining how knowledge redundancy is measured using Jaccard similarity
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Survival Probability by Knowledge Redundancy
caption: >-
  Predicted survival probability from Cox proportional hazards models with linear (blue) and quadratic (orange) terms. The
  quadratic model shows a slight upward trend but the quadratic term is not significant (p = 0.71). Both models predict higher
  survival at higher knowledge redundancy, but the relationship is not statistically significant. Shaded areas represent 95%
  confidence intervals.
image_gen_detailed_description: >-
  Line plot with scatter points. X-axis: Knowledge Redundancy Score (0.0 to 0.8, ticks at 0.0, 0.2, 0.4, 0.6, 0.8). Y-axis:
  Predicted Survival Probability at 12 months (0.0 to 1.0). Linear model (blue line with circles): KR=0.1, survival=0.65;
  KR=0.2, survival=0.67; KR=0.3, survival=0.69; KR=0.4, survival=0.71; KR=0.5, survival=0.73; KR=0.6, survival=0.75; KR=0.7,
  survival=0.77; KR=0.8, survival=0.79. Quadratic model (orange line with squares): KR=0.1, survival=0.64; KR=0.2, survival=0.67;
  KR=0.3, survival=0.70; KR=0.4, survival=0.72; KR=0.5, survival=0.73; KR=0.6, survival=0.74; KR=0.7, survival=0.74; KR=0.8,
  survival=0.73. Shaded 95% confidence intervals for both lines. Title: 'Survival Probability vs Knowledge Redundancy'. Sans-serif
  font, white background.
aspect_ratio: '4:3'
summary: >-
  Visualizes the relationship between knowledge redundancy and survival probability from Cox models
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 18:50:26 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-21 18:50:40 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: "Assembles and compiles a LaTeX paper into paper.pdf: documentclass and package preamble, figure floats that includegraphics pre-generated vector .pdf and .jpg files, float-placement and width rules, and the required pdflatex, bibtex, pdflatex, pdflatex run sequence. Use whenever pre-written text and pre-generated figures must become a compiled PDF, and whenever a build misbehaves — citations printing as question marks, figures drifting to the end or above the title, shrunken axis labels, undefined references. Triggers: latex, tex, pdflatex, bibtex, natbib, includegraphics, figure float, htbp, compile or build the paper, paper.tex, paper.pdf. NOT for: writing the paper's text or deciding its structure (use aii-paper-writing), creating the figure images (aii-data-fig-gen, aii-concept-fig-gen), or fetching bibliography entries (use aii-semscholar-bib); NOT for reshaping a PDF that already exists — merging, splitting, form filling, table extraction (use anthropic-pdf)."
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

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 18:50:40 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and writes the result into references.bib, with a mandatory web-search fallback for anything not found. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX first. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
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
