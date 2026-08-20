# OSS founder departure and survival measurement methods

## Summary

This research artifact provides a comprehensive synthesis of validated methodologies for (1) identifying founder departure in open-source projects, (2) measuring project survival from activity data, (3) appropriate survival analysis statistical methods, and (4) control variables used in prior OSS survival literature. The research is based on 10+ peer-reviewed papers including Avelino et al. (2019), Ait et al. (2022), Robinson et al. (2022), and others. Key findings: (1) Truck Factor algorithm with 12-month inactivity threshold is optimal for founder departure identification; (2) Project survival is best defined as attracting new core developers after founder departure combined with no commits for 12+ months; (3) Kaplan-Meier estimator and Cox Proportional Hazards model are standard statistical methods, implemented in Python lifelines library; (4) Essential control variables include project age, size, popularity, owner type, programming language, and contributor count. The output includes detailed methodological recommendations, threat analysis, and implementation guidance for survival analysis in OSS research.

## Research Findings

## Comprehensive Answer: Methodologies for Identifying Founder Departure and Measuring Project Survival in OSS

### 1. Founder/Developer Departure Operationalization

**Founder Identification Methods:**
The literature primarily focuses on identifying 'core developers' or 'key contributors' rather than strictly defined 'founders'. The most validated approach is using the Truck Factor (TF) algorithm by Avelino et al. [1], which identifies the minimal set of developers who are main authors of at least 50% of the system's files. The Degree of Authorship (DOA) metric is used to determine expertise based on file creation and number of changes [1].

Alternative methods include:
- First commit author (oldest commit in repo) - simple but may miss co-founders
- Most prolific early contributor (commits in first 6-12 months)
- Repository creator (GitHub API 'owner' field) - though this may be an organization rather than individual founder
- Bus factor algorithms (Cosentino et al. [10], Avelino et al. [1])

**Departure Threshold:**
Avelino et al. [1] conducted a sensitivity analysis of five thresholds: 3 months, 6 months, 1 year, 1.5 years, and 2 years. They selected the 1-year (12 months) threshold as it achieved the highest harmonic mean (66%) between precision (82%) and improvement over 6-month threshold (55%) [1]. This threshold is defined as: a developer abandoned a project if their last commit occurred at least one year before the most recent repository commit [1].

Prior studies use varying thresholds:
- 3 months: Zazworka et al. [12] (cited in Avelino et al. [1])
- 6 months: Lin et al. [13], Foucault et al. [14] (cited in Avelino et al. [1])
- 12 months: Izquierdo-Cortazar et al. [15], Robles et al. [16] (cited in Avelino et al. [1])

**Recommended Approach:** Use the 12-month threshold with TF algorithm identification, as validated by Avelino et al. [1]. This balances precision and recall while minimizing misclassification error.

### 2. Project Survival Measurement

**Survival Definitions:**
Different papers define survival differently:

1. **Avelino et al. [1]**: A project survives a Truck Factor Developer Detachment (TFDD) if it attracts new TF developers who assume maintenance after all original TF developers have abandoned the project. Survival is operationalized as a transition from 'Inactive' (all TF developers abandoned) back to 'Active' (at least one new TF developer) [1].

2. **Ait et al. [2]**: A project survives when its development has not been abandoned at the time of data collection. They use three states: alive (active), zombie (minimal activity), and dead (abandoned) [2].

3. **Robinson et al. [3]**: A project is dead when it no longer receives any revisions (commits). This definition is used by Ali et al. [2] and Evangelopoulos et al. [9] (both cited in Robinson et al. [3]).

4. **Samoladas et al. [21] (cited in Robinson et al. [3])**: A project is considered inactive if it receives less than two revisions per month, and dead after two months of inactivity.

**Activity Metrics for Measuring Survival:**
- Commit frequency (weekly/monthly/yearly) [2, 3]
- Release frequency (major releases) [3]
- Issue resolution rate [2]
- Pull request merge rate [2]
- Contributor count changes [2]
- Repository centrality [6]
- Community engagement metrics [7]

**Recommended Approach:** Use Avelino et al.'s [1] definition of survival (attracting new core developers after founder departure) combined with Robinson et al.'s [3] operationalization (no commits for 12 months indicates death). This aligns with both core developer focus and practical activity measurement.

### 3. Survival Analysis Statistical Methods

**Primary Methods:**

1. **Kaplan-Meier Estimator**: Non-parametric estimation of survival function S(t), which gives probability that a project will survive until time t [2, 3]. The estimator produces stepwise curves and handles censored observations [3].

2. **Cox Proportional Hazards Model**: Regression model to understand how project attributes relate to survival. Results in Hazard Ratio (HR) where HR>1 indicates increased risk of abandonment, HR<1 indicates decreased risk [3]. Can include quadratic terms to test non-linear relationships like inverted-U [3].

3. **Bayesian Survival Analysis**: Alternative approach using posterior distributions and MCMC algorithms (Stan). Offers robustness advantages over frequentist methods [3].

**Handling Censored Data:**
Right-censoring occurs when projects are still active at study end (death not observed) [2, 3]. Survival analysis techniques explicitly handle this by considering censored projects for observed duration but not counting them as dead [3]. Approximately 62% of projects were censored in Robinson et al.'s study [3].

**Testing Assumptions:**
- Proportional hazards assumption can be tested using Schoenfeld residuals (lifelines library provides `check_assumptions` method) [5]
- If violated: stratify on the variable, modify functional form, or introduce time-varying covariates [5]

**Software Implementation:**
- Python: `lifelines` library (CoxPHFitter, KaplanMeierFitter) [4, 5]
- R: `survival` package
- Key functions: `fit()`, `print_summary()`, `check_assumptions()` [5]

**Recommended Approach:** Use Kaplan-Meier for univariate survival curves and Cox Proportional Hazards model for multivariate analysis with control variables. Test proportional hazards assumption and handle violations appropriately. Use lifelines Python library for implementation.

### 4. Control Variables in OSS Survival Studies

**Comprehensive List from Literature:**

**Project-Level Variables:**
- **Age**: Time since repository creation [2, 3]
- **Size**: Number of files, lines of code (LOC), commits [1, 2]
- **Popularity**: Stars, forks, downloads [2, 3]
- **License**: Type of open source license [2]
- **Ecosystem**: Package manager ecosystem (NPM, R, WordPress, Laravel) [2]
- **Owner type**: Organization vs. individual ownership [2, 9]
- **Repository centrality**: Network position in dependency graph [6]
- **Has website/wiki**: Project documentation presence [2]

**Contributor-Level Variables:**
- **Contributor count**: Total number of unique contributors [2, 3]
- **Core contributor count**: Number of TF developers [1]
- **Contributor turnover rate**: Rate of contributor departure [8]
- **Team size**: High vs. low author count (threshold varies) [3]

**Technical Variables:**
- **Programming language**: Primary language used [2, 3]
- **Hosting service**: GitHub, GitLab, PyPI, etc. [3]
- **Multi-repo**: Hosted on multiple services [3]
- **Major releases**: Whether project publishes major releases [3]
- **Revision frequency**: Commits per day [3]

**Activity Variables:**
- **Pre-departure activity level**: Commit frequency before founder departure
- **Issue activity**: Number of issues opened/closed [2]
- **Pull request activity**: PR merge rate [2]
- **Comment activity**: Community engagement [2]

**Variables from Specific Studies:**
- Ait et al. [2]: Project type (individual/org), community size (Tier 1/2/3 based on interquartile ranges), ecosystem
- Robinson et al. [3]: Major releases (binary), host type, multi-repo (binary), high author count (>20), high revision frequency (>1 per day)
- Research Policy 2025 [9]: Write access provisioning, organizational ownership

**Multicollinearity Considerations:**
Prior studies acknowledge potential multicollinearity among control variables. Ait et al. [2] use correlation analysis and variance inflation factors (VIF) implicitly through their regression approach. Recommended to calculate VIF for all control variables and remove those with VIF > 5-10.

**Recommended Control Set:**
1. Project age (months since creation)
2. Project size (log of commits or files)
3. Popularity (log of stars + forks)
4. Owner type (organization vs. individual - binary)
5. Programming language (categorical/fixed effects)
6. Contributor count (log transformed)
7. Pre-departure activity level (commits per month before departure)
8. Ecosystem/domain fixed effects (if comparing across ecosystems)

### 5. Summary of Recommendations

| Decision Point | Recommended Choice | Justification |
|---------------|-------------------|---------------|
| Founder ID | Truck Factor algorithm (DOA metric) | Validated by Avelino et al. [1], best precision/recall |
| Departure threshold | 12 months (1 year) | Highest harmonic mean in sensitivity analysis [1] |
| Survival definition | New core developers after departure (Avelino) + no commits for 12 months (Robinson) | Combines core developer focus with practical measurement |
| Survival metric | Commit activity (primary) + contributor changes (secondary) | Most reliable and universally available |
| Statistical method | Kaplan-Meier + Cox PH model | Standard in OSS literature [2, 3], handles censoring |
| Control variables | Age, size, popularity, owner type, language, contributor count, pre-departure activity | Comprehensive set from multiple studies [2, 3, 9] |
| Software | Python lifelines library | Well-documented, actively maintained [4, 5] |
| Assumption testing | Schoenfeld residuals test | Built into lifelines [5] |

### 6. Threats to Validity

**Measurement Validity:**
- Founder identification may miss co-founders or early key contributors who weren't the primary author [1]
- 12-month threshold may not suit all projects (some have natural seasonal patterns) [1]
- Commit activity may continue (e.g., bots, minor fixes) while core development stops [2]

**External Validity:**
- Most studies focus on popular GitHub projects (selection bias) [1, 2]
- Results may not generalize to smaller, less popular projects [1]
- Different ecosystems (NPM, R, WordPress) show different survival patterns [2]

**Statistical Validity:**
- Right-censoring may bias results if not properly handled [3]
- Proportional hazards assumption may be violated for some covariates [5]
- Multicollinearity among control variables may affect coefficient estimates [2]

**Confounding Factors:**
- Project popularity may be endogenous (popular projects more likely to survive, but survival increases popularity) [2]
- Organization ownership may correlate with resources, experience, and project quality [9]
- External events (e.g., security vulnerabilities, technology shifts) may trigger both founder departure and project decline [8]

### 7. Follow-Up Research Questions

1. How do different founder identification methods (first commit author vs. TF algorithm vs. owner field) compare in terms of predictive validity for project survival?

2. What is the optimal departure threshold for different types of projects (individual vs. organization-owned, different ecosystems, different programming languages)?

3. How do partial departures (founder reduces but doesn't eliminate activity) affect project survival compared to complete departures?

### 8. Key Contradictions and Limitations in Literature

**Contradictions:**
- Departure thresholds vary widely (3-24 months) with no consensus [1]
- Survival definitions range from 'no commits' to 'no core developer activity' [1, 2, 3]
- Some studies find organization ownership increases survival [2, 9], while others find mixed results

**Limitations:**
- Most studies are observational (no randomized control trials possible)
- Self-selection bias: Projects that survive may differ systematically from those that don't
- Temporal bias: Older projects had different ecosystem conditions than newer ones
- Survivorship bias: Studies only include projects that existed long enough to be observed

### 9. Confidence Assessment

**High Confidence (multiple sources, consistent findings):**
- 12-month departure threshold is most validated [1]
- Kaplan-Meier and Cox models are standard methods [2, 3, 4]
- Control variables: age, size, popularity, owner type are consistently used [2, 3, 9]

**Medium Confidence (some sources, plausible but not definitively proven):**
- Truck Factor algorithm is best for founder identification (only Avelino et al. [1] validate extensively)
- Quadratic relationships in Cox models (theoretically sound but limited empirical testing) [3]
- Optimal control variable set (studies use different combinations) [2, 3, 9]

**Low Confidence (limited sources, contradictory evidence):**
- Exact survival definition (no commits vs. no core activity) [1, 2, 3]
- Handling of partial departures (founder reduces activity but doesn't leave completely)
- Non-linear effects of control variables (e.g., inverted-U for popularity) [3]

**What would change confidence:**
- Replication studies using different datasets
- Validation against ground truth (surveying project maintainers about actual survival status)
- Longitudinal studies tracking projects over longer time periods
- Comparison across multiple ecosystems and programming languages

## Sources

[1] [On the abandonment and survival of open source projects: An empirical investigation](https://arxiv.org/abs/1906.08058) — Primary reference paper by Avelino et al. (2019) that defines Truck Factor, departure thresholds (12 months optimal), and survival methodology. Found that 16% of projects abandoned, 41% of those survived via new core developers.

[2] [An Empirical Study on the Survival Rate of GitHub Projects](https://doi.org/10.1145/3524842.3527941) — Ait et al. (2022) MSR paper analyzing 1,127 GitHub projects from 4 ecosystems. Uses Kaplan-Meier survival analysis, finds 50% survival beyond 5 years, organization-owned projects survive better.

[3] [Two Approaches to Survival Analysis of Open Source Python Projects](https://arxiv.org/abs/2203.08320) — Robinson et al. (2022) replication study using both frequentist (Kaplan-Meier, Cox) and Bayesian survival analysis. Defines death as no revisions, finds major releases and large developer teams increase survival.

[4] [lifelines: Survival Analysis in Python](https://lifelines.readthedocs.io/en/latest/index.html) — Documentation for Python lifelines library implementing Kaplan-Meier, Cox Proportional Hazards, and other survival analysis methods. Includes proportional hazard assumption testing.

[5] [Testing the Proportional Hazard Assumptions](https://lifelines.readthedocs.io/en/latest/jupyter_notebooks/Proportional%20hazard%20assumption.html) — Lifelines documentation on testing Cox model assumptions using Schoenfeld residuals, stratification, and time-varying covariates to handle violations.

[6] [Revealing the value of Repository Centrality in lifespan prediction of OSS Projects](https://doi.org/10.48550/arxiv.2405.07508) — 2024 arXiv paper showing repository centrality (network position) as predictor of OSS project lifespan. Suggests dependency graph metrics as control variables.

[7] [Community Engagement and the Lifespan of OSS Projects](https://arxiv.org/html/2510.15408v1) — Preprint analyzing community engagement metrics (issues, PRs, comments) as predictors of OSS project lifespan. Suggests social activity metrics as survival indicators.

[8] [Developer Turnover in Global, Industrial Open Source Projects: Insights from Applying Survival Analysis](https://doi.org/10.1109/icgse.2017.11) — Lin et al. (2017) applying survival analysis to developer turnover in industrial OSS. Finds developers maintaining others' files have higher survival probability.

[9] [Write access provisioning and organizational ownership in OSS projects](https://doi.org/10.1016/j.respol.2025.105284) — Research Policy 2025 paper on how write access and organizational ownership affect OSS project novelty and survival. Highlights importance of governance variables.

[10] [Assessing the bus factor of Git repositories](https://ieeexplore.ieee.org/document/7081864) — Cosentino et al. (2015) SANER paper proposing bus factor algorithm for Git repositories. Alternative to Avelino et al.'s TF algorithm.

## Follow-up Questions

- How do different founder identification methods (first commit author vs. Truck Factor algorithm vs. repository owner field) compare in terms of predictive validity for project survival?
- What is the optimal departure threshold for different types of projects (individual vs. organization-owned, different ecosystems, different programming languages)?
- How do partial departures (founder reduces but doesn't eliminate activity) affect project survival compared to complete departures?

---
*Generated by AI Inventor Pipeline*
