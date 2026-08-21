# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `iter1_924aa01cf43b` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 16:30:21 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: GitHub OSS survival data collection
summary: >-
  Collect comprehensive GitHub repository data for 1000+ open-source projects to empirically test the knowledge redundancy
  hypothesis. Extract complete commit histories with file modifications, identify founder departures using multiple heuristics,
  compute knowledge redundancy via Jaccard similarity with directory-level and file-level variants, measure project survival
  using multiple metrics (commit activity, release frequency, issue resolution), and control for confounding variables (project
  age, size, popularity, programming language, contributor count, bus factor).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  COMPREHENSIVE DATA REQUIREMENTS: Collect 1000+ GitHub repositories meeting stratified sampling criteria: (1) POPULARITY:
  100-1000 stars (40%), 1000-10000 stars (40%), 10000+ stars (20%) to ensure variance in survival pressures; (2) AGE: 2-5
  years (50%), 5+ years (50%) to capture different lifecycle stages; (3) LANGUAGES: Stratified sample across 12 languages
  - Python (20%), JavaScript/TypeScript (20%), Java (10%), Go (10%), Rust (10%), C/C++ (10%), Ruby (5%), PHP (5%), Swift (5%),
  Kotlin (5%) to control for language-specific development patterns; (4) ACTIVITY: Minimum 50 commits total, 5+ contributors,
  at least one commit in past 6 months at time of collection; (5) FORK STATUS: Exclude forks (analyze parent repo if fork
  is substantial divergence). MANDATORY DATA FIELDS: (A) REPOSITORY METADATA: name, owner, full_name, description, HTML URL,
  creation timestamp, last push timestamp, star count, fork count, watcher count, primary language, license info, default
  branch, size (KB), open issues count, has_wiki, has_pages, archived status; (B) CONTRIBUTOR DATA: login, id, avatar_url,
  gravatar_id, type, site_admin, total_commit_count, first_commit_date, last_commit_date, files_modified (complete list),
  lines_added (estimated), lines_deleted (estimated); (C) COMMIT DATA: sha, author_name, author_email, author_date, committer_name,
  committer_date, message, files_changed (list with status: added/modified/deleted/renamed), additions_count, deletions_count,
  is_merge_commit; (D) FOUNDER ANALYSIS: identified_founder_login, founder_identification_method (first_committer|most_commits_early|owner_account),
  founder_first_commit, founder_last_commit, founder_departure_date (if applicable), departure_confidence (high/medium/low);
  (E) SURVIVAL METRICS: founder_departed (bool), departure_date, survived_12mo (bool), survived_24mo (bool), commits_per_month_pre_6mo,
  commits_per_month_post_12mo, releases_pre_6mo, releases_post_12mo, issues_resolved_pre_6mo, issues_resolved_post_12mo, survival_score
  (continuous 0-1); (F) COMPUTED METRICS: knowledge_redundancy_jaccard_file (float 0-1), knowledge_redundancy_jaccard_dir
  (float 0-1), knowledge_redundancy_overlap_coefficient (float 0-1), bus_factor (int), contributor_count_active, contributor_count_total,
  commit_frequency_pre_departure (commits/month), commit_frequency_post_departure, gini_coefficient_contributions, code_ownership_herfindahl,
  median_commits_per_contributor, max_commits_single_contributor, file_count_total, file_count_modified_by_multiple; (G) CONTROL
  VARIABLES: project_age_days, stars_per_day, commits_per_day_history, contributor_growth_rate, language_ecosystem_age (Python=1991,
  JavaScript=1995, etc.), is_company_backed (detect from org/owner), has_readme, has_tests, has_ci, license_permissiveness
  (0=proprietary, 1=permissive, 2=copyleft), issue_closure_rate_pre, issue_closure_rate_post. OUTPUT FORMAT: Single JSON file
  with gzip compression option, schema versioned, maximum 300MB uncompressed. Each repository object must be self-contained
  with all computed metrics to enable independent analysis. DATA QUALITY THRESHOLDS: 80%+ repos must have identifiable founder
  departure, 90%+ must have computable redundancy scores, 95%+ must have complete commit histories (no missing months), 100%
  must pass JSON schema validation. STATISTICAL POWER: Target n=1000 provides 80% power to detect medium effect sizes (Cohen's
  h=0.3) in survival differences across redundancy quartiles, assuming 50% survival rate and alpha=0.05.
dataset_search_plan: "EXHAUSTIVE 8-PHASE DATA COLLECTION PLAN WITH MULTIPLE STRATEGIES:\n\nPHASE 1: REPOSITORY DISCOVERY &\
  \ STRATIFIED SAMPLING (2 hours)\nStrategy A - GitHub GraphQL Search API (PRIMARY):\n  Query template: 'stars:100..1000 language:Python\
  \ created:2018-01-01..2022-01-01 pushed:>2023-01-01 -fork:true'\n  Pagination: Use cursor-based pagination with pageInfo\
  \ { hasNextPage, endCursor }\n  Rate limit: 5000 req/hour with authentication, implement 0.8 sec delay between requests\n\
  \  GraphQL query structure:\n    query searchRepos($query: String!, $cursor: String, $first: Int = 50) {\n      search(query:\
  \ $query, type: REPOSITORY, first: $first, after: $cursor) {\n        repositoryCount\n        pageInfo { hasNextPage, endCursor\
  \ }\n        edges {\n          node {\n            ... on Repository {\n              nameWithOwner, description, stargazerCount,\
  \ forkCount, isFork\n              createdAt, pushedAt, updatedAt\n              primaryLanguage { name }\n            \
  \  licenseInfo { spdxId }\n              defaultBranchRef { name }\n              owner { login, __typename }\n        \
  \    }\n          }\n        }\n      }\n    }\n  Execute for each language × star bracket combination, collect 150% of\
  \ target to allow filtering\n\nStrategy B - GitHub REST Search API (FALLBACK if GraphQL fails):\n  Endpoint: GET /search/repositories?q={query}&sort=stars&order=desc&per_page=100&page={n}\n\
  \  Pagination: Link header with rel=\"next\", max 1000 results per query (GitHub limit)\n  Rate limit: 30 req/minute unauthenticated,\
  \ 5000 req/hour authenticated\n\nStrategy C - Existing Dataset Mining (ALTERNATIVE):\n  - GHTorrent (http://ghtorrent.org):\
  \ MySQL dumps, last updated 2020, may use if recent enough\n  - GH Archive (https://www.gharchive.org): Google BigQuery\
  \ public dataset, events since 2015\n  - Software Heritage (https://www.softwareheritage.org): Comprehensive archive, API\
  \ available\n  - World of Code (https://worldofcode.org): Snapshot-based, updated quarterly\n  Evaluate based on: data recency,\
  \ completeness of file modification data, ease of extraction\n\nPHASE 2: AUTHENTICATION & RATE LIMIT MANAGEMENT (30 mins\
  \ setup)\n  Token sources (in priority order):\n  1. GitHub Personal Access Token (PAT) with repo scope: 'ghp_xxxxxxxxxxxx'\n\
  \  2. GitHub App installation token (if available)\n  3. OAuth token from user authentication\n  Rate limit handling:\n\
  \  - Check X-RateLimit-Remaining header before each request\n  - If < 100 remaining, sleep until X-RateLimit-Reset timestamp\n\
  \  - Implement exponential backoff: 1s, 2s, 4s, 8s, 16s, then 60s max\n  - Secondary rate limits: 1 req/sec for REST, 10\
  \ req/sec for GraphQL (recommended)\n  - Use conditional requests: ETag/Last-Modified headers to avoid counting against\
  \ limit\n  Multiple token rotation:\n  - Prepare 3-5 tokens in advance\n  - Round-robin through tokens when primary is rate\
  \ limited\n  - Monitor rate limits per token independently\n\nPHASE 3: DETAILED DATA COLLECTION - HYBRID API STRATEGY (4-6\
  \ hours)\n\n3A. Commit History Collection (GraphQL - efficient for metadata):\n  Query structure:\n    query repoCommits($owner:\
  \ String!, $name: String!, $cursor: String) {\n      repository(owner: $owner, name: $name) {\n        defaultBranchRef\
  \ {\n          target {\n            ... on Commit {\n              history(first: 100, after: $cursor) {\n            \
  \    pageInfo { hasNextPage, endCursor }\n                edges {\n                  node {\n                    oid, messageHeadline,\
  \ committedDate, pushedDate\n                    author { user { login, id }, name, email }\n                    committer\
  \ { user { login, id }, name, email }\n                    changedFiles, additions, deletions\n                    parents(first:\
  \ 1) { edges { node { oid } } }\n                  }\n                }\n              }\n            }\n          }\n \
  \       }\n      }\n    }\n  Pagination: Collect ALL commits (may be 1000+ for large repos)\n  Optimization: Stop after\
  \ 500 commits if repo is very active (sample most recent)\n  Date filtering: Only collect commits from repo creation to\
  \ 2024-01-01 (cutoff for analysis)\n\n3B. File Modification Data Collection (REST - required for file names):\n  PRIMARY\
  \ METHOD: GET /repos/{owner}/{repo}/commits?sha={branch}&per_page=100&since={date}\n  Returns: array of commits with files\
  \ array containing filename, status, additions, deletions\n  \n  SECONDARY METHOD (if primary fails): GET /repos/{owner}/{repo}/commits/{sha}\n\
  \  Returns: single commit with complete file diff information\n  \n  TERTIARY METHOD (bulk): Use Git Trees API\n  GET /repos/{owner}/{repo}/git/trees/{sha}?recursive=1\n\
  \  Then cross-reference with commit list to infer modifications (less accurate)\n  \n  File path normalization:\n  - Convert\
  \ all paths to relative, lowercase for comparison\n  - Handle renames: track rename detection from commit data (status:\
  \ 'renamed')\n  - Handle deletions: keep in contributor's file set as 'previously modified'\n  - Directory extraction: also\
  \ compute directory-level modifications (parent dir of each file)\n\n3C. Contributor Metadata Collection:\n  GraphQL: repository(owner:\
  \ $owner, name: $name) { collaborators(first: 100) { edges { node { login, id, ... } } } }\n  REST: GET /repos/{owner}/{repo}/contributors?per_page=100\n\
  \  Note: GitHub API only returns top 500 contributors, paginate if needed\n  Affiliation: distinguish between 'owner', 'member',\
  \ 'contributor' if possible\n\nPHASE 4: FOUNDER IDENTIFICATION - MULTI-HEURISTIC APPROACH (1 hour)\n\nHeuristic 1 - First\
  \ Committer Method:\n  - Sort all commits by date ascending\n  - Founder = author of first commit (or first 5 commits if\
  \ first is bot)\n  - Confidence: HIGH if first commit is within 7 days of repo creation\n\nHeuristic 2 - Early Period Dominance\
  \ Method:\n  - Define early period: first 90 days after repo creation\n  - Count commits per author in early period\n  -\
  \ Founder = author with most commits in early period\n  - Confidence: HIGH if >50% of early commits, MEDIUM if 30-50%, LOW\
  \ if <30%\n\nHeuristic 3 - Owner Account Method:\n  - If repo owner is a user (not org), check if owner appears in contributors\n\
  \  - If yes and has commits in first 30 days, likely founder\n  - Confidence: MEDIUM (owner may have transferred repo)\n\
  \nHeuristic 4 - Repository Description / README Parsing:\n  - Parse repo description and README for phrases like 'Created\
  \ by', 'Author:', etc.\n  - Use regex: r'(?:created|authored|written|developed)\\s+(?:by\\s+)?@?(\\w+)'\n  - Confidence:\
  \ LOW (unreliable, use only as tiebreaker)\n\nHeuristic 5 - GitHub Organization Membership:\n  - If repo owned by org, check\
  \ org members for early contributors\n  - May not identify individual founder if org-created\n  - Confidence: LOW (often\
  \ team effort)\n\nFINAL FOUNDER SELECTION ALGORITHM:\n  def identify_founder(commits, repo_metadata):\n      methods = [\n\
  \          ('first_committer', heuristic1(commits)),\n          ('early_dominance', heuristic2(commits)),\n          ('owner_account',\
  \ heuristic3(repo_metadata, commits))\n      ]\n      # Weight by confidence\n      scores = {}\n      for method, (candidate,\
  \ confidence) in methods:\n          weight = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}[confidence]\n          scores[candidate]\
  \ = scores.get(candidate, 0) + weight\n      \n      # Return highest scoring candidate\n      founder = max(scores, key=scores.get)\n\
  \      \n      # Determine departure\n      founder_commits = [c for c in commits if c.author == founder]\n      last_commit\
  \ = max(c.committedDate for c in founder_commits)\n      \n      # Check 12+ months inactivity\n      cutoff_date = last_commit\
  \ + timedelta(days=365)\n      recent_commits = [c for c in commits if c.committedDate > cutoff_date]\n      \n      departed\
  \ = len(recent_commits) == 0\n      departure_date = last_commit if departed else None\n      \n      return founder, departure_date,\
  \ departed\n\nPHASE 5: KNOWLEDGE REDUNDANCY COMPUTATION - MULTIPLE METRICS (1 hour)\n\n5A. Jaccard Similarity (Primary Metric):\n\
  \  Definition: J(A,B) = |A ∩ B| / |A ∪ B|\n  Where A and B are sets of files modified by contributors A and B\n  \n  Implementation:\n\
  \  def compute_jaccard_redundancy(contributor_files):\n      '''\n      contributor_files: dict {contributor_login: set(file_paths)}\n\
  \      Returns: average pairwise Jaccard similarity (float 0-1)\n      '''\n      import itertools\n      from statistics\
  \ import mean\n      \n      contributors = list(contributor_files.keys())\n      if len(contributors) < 2:\n          return\
  \ 0.0\n      \n      similarities = []\n      for c1, c2 in itertools.combinations(contributors, 2):\n          files1 =\
  \ contributor_files[c1]\n          files2 = contributor_files[c2]\n          \n          if not files1 or not files2:\n\
  \              continue\n          \n          intersection = len(files1 & files2)\n          union = len(files1 | files2)\n\
  \          \n          if union > 0:\n              jaccard = intersection / union\n              similarities.append(jaccard)\n\
  \      \n      return mean(similarities) if similarities else 0.0\n\n5B. Directory-Level Jaccard (Secondary Metric):\n \
  \ - Extract directory paths from file paths (e.g., 'src/main.py' -> 'src/')\n  - Compute Jaccard on directory sets to capture\
  \ module-level redundancy\n  - May be more stable than file-level for large repos\n\n5C. Overlap Coefficient (Alternative\
  \ Metric):\n  Definition: O(A,B) = |A ∩ B| / min(|A|, |B|)\n  - More sensitive to small file sets\n  - Range: 0-1, where\
  \ 1 means one contributor's files are subset of other's\n\n5D. Contributor Filtering:\n  - Include only contributors with\
  \ 5+ commits (filter out one-time contributors)\n  - Exclude bot accounts (detect via login patterns: 'bot', '[bot]', 'dependabot',\
  \ etc.)\n  - Exclude merge commits from file modification counts\n  - Weight by commit frequency: weight = log(1 + commit_count)\
  \ to reduce outlier influence\n\nPHASE 6: SURVIVAL MEASUREMENT - MULTI-METRIC APPROACH (1 hour)\n\n6A. Survival Definition\
  \ (Primary):\n  Binary outcome: survived_12mo = 1 if project has ≥1 commit/month average in 12 months post-departure\n \
  \ Comparison: post_departure_rate ≥ 0.25 × pre_departure_rate\n  Pre-departure baseline: 6 months immediately before departure\n\
  \  \n  def measure_survival_binary(commits, departure_date):\n      if not departure_date:\n          return None\n    \
  \  \n      # Pre-departure period (6 months before)\n      pre_start = departure_date - timedelta(days=180)\n      pre_commits\
  \ = [c for c in commits \n                     if pre_start <= c.committedDate <= departure_date]\n      pre_rate = len(pre_commits)\
  \ / 6.0  # commits per month\n      \n      # Post-departure period (12 months after)\n      post_start = departure_date\n\
  \      post_end = departure_date + timedelta(days=365)\n      post_commits = [c for c in commits \n                    \
  \ if post_start <= c.committedDate <= post_end]\n      post_rate = len(post_commits) / 12.0\n      \n      # Binary survival\n\
  \      survived = post_rate >= (pre_rate * 0.25)\n      \n      return {\n          'survived_12mo': survived,\n       \
  \   'pre_rate': pre_rate,\n          'post_rate': post_rate,\n          'post_commits_12mo': len(post_commits)\n      }\n\
  \n6B. Continuous Survival Score (Secondary):\n  survival_score = min(1.0, post_rate / pre_rate) if pre_rate > 0 else 0.0\n\
  \  - Captures degree of survival, not just binary outcome\n  - Allows for regression analysis with continuous dependent\
  \ variable\n\n6C. Alternative Survival Metrics:\n  - Release-based: survived if ≥1 release in 12 months post-departure\n\
  \  - Issue-based: survived if ≥1 issue resolved in 12 months post-departure\n  - Hybrid: survived if any of commit/release/issue\
  \ activity\n\n6D. Censoring Handling:\n  - If departure_date is within 12 months of data collection, censor (mark as 'ongoing')\n\
  \  - If repo is archived, mark as 'archived' (definite non-survival)\n  - If repo has commits but very low rate, mark as\
  \ 'declining' (intermediate category)\n\nPHASE 7: CONTROL VARIABLE COMPUTATION (1 hour)\n\n7A. Bus Factor Calculation:\n\
  \  - Sort contributors by number of unique files modified (descending)\n  - Bus factor = smallest k such that top k contributors\
  \ modify >50% of all files\n  - Alternative: Truck factor algorithm (Avelino et al. 2016)\n\n7B. Project Age & Growth:\n\
  \  - age_days = collection_date - creation_date\n  - commits_per_day = total_commits / age_days\n  - stars_per_day = stargazers_count\
  \ / age_days\n  - contributor_growth_rate = (contributors_at_1yr - contributors_at_6mo) / 180\n\n7C. Code Ownership Metrics:\n\
  \  - Herfindahl index: H = Σ (contributor_commits / total_commits)²\n  - Gini coefficient of commit distribution among contributors\n\
  \  - Max contribution percentage: max_commits / total_commits\n\n7D. Language Ecosystem Controls:\n  - language_age = current_year\
  \ - language_creation_year\n  - language_popularity_rank (from TIOBE/RedMonk rankings)\n  - is_company_backed: detect from\
  \ owner (e.g., 'google', 'microsoft', 'facebook')\n\nPHASE 8: DATA VALIDATION, QUALITY CONTROL & EXPORT (1 hour)\n\n8A.\
  \ Schema Validation:\n  JSON schema definition (Draft 7):\n  {\n    \"$schema\": \"http://json-schema.org/draft-07/schema#\"\
  ,\n    \"title\": \"OSS Repository Data\",\n    \"type\": \"object\",\n    \"required\": [\"metadata\", \"repositories\"\
  ],\n    \"properties\": {\n      \"metadata\": { \"type\": \"object\", ... },\n      \"repositories\": {\n        \"type\"\
  : \"array\",\n        \"items\": {\n          \"type\": \"object\",\n          \"required\": [\"repo_id\", \"name\", \"\
  owner\", \"founder\", \"survival_outcome\", \"computed_metrics\"],\n          \"properties\": {\n            \"repo_id\"\
  : { \"type\": \"string\" },\n            \"knowledge_redundancy\": { \"type\": \"number\", \"minimum\": 0, \"maximum\":\
  \ 1 },\n            ...\n          }\n        }\n      }\n    }\n  }\n\n8B. Data Quality Checks:\n  def validate_repository(repo):\n\
  \      errors = []\n      warnings = []\n      \n      # Critical errors (exclude repo)\n      if not repo.get('founder',\
  \ {}).get('login'):\n          errors.append('No founder identified')\n      if repo.get('computed_metrics', {}).get('knowledge_redundancy')\
  \ is None:\n          errors.append('Knowledge redundancy not computable')\n      if len(repo.get('commits', [])) < 10:\n\
  \          errors.append('Too few commits (<10)')\n      \n      # Warnings (keep but flag)\n      if repo.get('survival_outcome',\
  \ {}).get('departure_date') is None:\n          warnings.append('Founder has not departed yet (censored)')\n      if len(repo.get('contributors',\
  \ [])) < 3:\n          warnings.append('Very few contributors (<3)')\n      \n      return errors, warnings\n\n8C. Outlier\
  \ Detection:\n  - Knowledge redundancy: flag if >3 standard deviations from mean\n  - Survival rate: flag if post-rate >\
  \ 10× pre-rate (anomaly)\n  - Contributor count: flag if >99th percentile (very large project)\n\n8D. Export Strategy:\n\
  \  - Primary: data_out.json (pretty-printed for readability)\n  - Compressed: data_out.json.gz (using gzip)\n  - Mini version:\
  \ mini_data_out.json (first 10 repos for testing)\n  - Metadata: data_out_metadata.json (summary statistics, collection\
  \ parameters)\n  - Schema: data_out_schema.json (JSON Schema for validation)\n\n  Export code:\n  import json, gzip\n  \n\
  \  # Main export\n  with open('data_out.json', 'w') as f:\n      json.dump(dataset, f, indent=2, default=str)\n  \n  # Compressed\n\
  \  with gzip.open('data_out.json.gz', 'wt') as f:\n      json.dump(dataset, f, default=str)\n  \n  # Check size\n  import\
  \ os\n  size_mb = os.path.getsize('data_out.json') / 1_000_000\n  if size_mb > 300:\n      print(f'WARNING: File size {size_mb:.1f}MB\
  \ exceeds 300MB limit')\n\nCOMPREHENSIVE FALLBACK STRATEGIES:\n\nFALLBACK 1 - API Rate Limit Exhaustion:\n  A. Multiple\
  \ Token Rotation: Prepare 5 GitHub tokens, rotate when limit reached\n  B. Reduce Scope: Collect 500 repos instead of 1000\
  \ (maintain stratification)\n  C. Use GitHub Archive via BigQuery: \n     - Query: SELECT repo_name, actor_login, committed_date,\
  \ files FROM `githubarchive.day.20230101` ...\n     - Free tier: 1TB/month query, sufficient for this analysis\n     - Requires\
  \ Google Cloud account setup\n  D. Use GHTorrent MySQL Dump:\n     - Download: http://ghtorrent.org/downloads.html\n   \
  \  - Last updated: ~2020, may be acceptable if hypothesis test is not time-sensitive\n     - Requires MySQL server setup\
  \ and ~100GB disk space\n\nFALLBACK 2 - File Modification Data Too Expensive:\n  A. Approximate from Commit Messages: Parse\
  \ file paths from commit messages (70% accuracy)\n  B. Sample Commits: Collect file data for only 25% of commits per repo\
  \ (systematic sample)\n  C. Use Directory-Level Only: Skip file-level, use directory modifications (less granular)\n  D.\
  \ Infer from Blame Data: Use git blame to determine file authorship (alternative approach)\n\nFALLBACK 3 - Founder Identification\
  \ Unclear:\n  A. Use Multiple Heuristics: Combine 3+ heuristics, use majority vote\n  B. Manual Review Sample: Flag 50 ambiguous\
  \ cases, manually review via web UI\n  C. Exclude Uncertain: Drop repos where confidence is LOW for all heuristics\n  D.\
  \ Sensitivity Analysis: Run analysis with/without ambiguous cases, check robustness\n\nFALLBACK 4 - Knowledge Redundancy\
  \ Computation Fails:\n  A. Use Commit Overlap: If file data missing, use commit timestamp overlap as proxy\n  B. Use Code\
  \ Review Data: If available, use PR reviewer assignments as proxy for expertise\n  C. Use Issue Assignment: Use issue assignee\
  \ data to infer contributor focus areas\n  D. Skip Metric: Mark as null, use only repos with computable redundancy\n\nFALLBACK\
  \ 5 - Survival Measurement Problematic:\n  A. Extend Window: Use 24-month post-departure if 12-month is noisy\n  B. Use\
  \ Multiple Metrics: Combine commit + release + issue metrics\n  C. Censor Appropriately: Mark repos with insufficient post-departure\
  \ data as censored\n  D. Use Time-Varying Survival: Kaplan-Meier curve instead of binary outcome\n\nEDGE CASES & SPECIAL\
  \ HANDLING:\n\n1. Monorepos: Google/Facebook style repos with multiple projects\n   - Detect via: >10000 files, >1000 contributors,\
  \ very high commit rate\n   - Handle via: exclude or analyze subprojects separately (complex)\n\n2. Bot-Heavy Repositories:\
  \ Automated commits (dependabot, CI bots)\n   - Detect via: login contains 'bot', '[bot]', or known bot accounts\n   - Handle\
  \ via: exclude bot commits from file modification analysis\n\n3. Corporate/Organization Repositories: Multiple founders,\
  \ team-based\n   - Detect via: owner is organization, not user\n   - Handle via: identify 'core team' (top 5 contributors)\
  \ instead of single founder\n\n4. Forked Repositories with Substantial Changes:\n   - Detect via: is_fork=true but >500\
  \ commits after fork, different primary language\n   - Handle via: analyze fork as independent project (exclude parent)\n\
  \n5. Archived Repositories:\n   - Detect via: archived=true field from GitHub API\n   - Handle via: mark as 'definite non-survival'\
  \ if archived post-departure\n\n6. Renamed/Migrated Repositories:\n   - Detect via: repository has 'parent' or 'source'\
  \ field pointing elsewhere\n   - Handle via: follow redirects, collect data from current URL\n\n7. Repositories with Very\
  \ Large Histories (>10000 commits):\n   - Handle via: sample 1000 most recent commits, document sampling method\n   - Alternative:\
  \ use Git API with shallow clone (not possible via GitHub API)\n\n8. Repositories with Force Pushes (rewritten history):\n\
  \   - Detect via: missing commits, non-linear history with gaps\n   - Handle via: flag as 'history may be incomplete', use\
  \ available data\n\n9. Multi-Language Repositories:\n   - Detect via: primary_language is null or multiple languages in\
  \ top 10 files\n   - Handle via: assign to 'primary' language based on file count, create 'mixed' category\n\n10. Repositories\
  \ with Binary Files (images, data):\n    - Handle via: exclude binary files from file modification sets (detect via extension)\n\
  \    - Extensions to exclude: .png, .jpg, .gif, .pdf, .zip, .tar, .dat, .bin\n\nPERFORMANCE OPTIMIZATION:\n\n1. Parallel\
  \ API Requests:\n   - Use asyncio with aiohttp for REST API calls (respect rate limits)\n   - Use threading for GraphQL\
  \ queries (Python GIL less relevant for I/O bound)\n   - Max 5 concurrent requests to avoid secondary rate limits\n\n2.\
  \ Caching Strategy:\n   - Cache commit data per repo: save after every 100 commits collected\n   - Cache intermediate results:\
  \ save progress every 10 repos\n   - Resume capability: if script crashes, resume from last saved state\n\n3. Memory Management:\n\
  \   - Stream large repos: don't load all commits into memory at once\n   - Use generators for file processing\n   - Delete\
  \ raw API responses after parsing\n\n4. Request Batching:\n   - GraphQL: batch multiple repo queries in one request (if\
  \ using aliases)\n   - REST: use ?per_page=100 to minimize requests\n   - Use conditional requests (ETag) to avoid re-fetching\
  \ unchanged data\n\nLEGAL & ETHICAL CONSIDERATIONS:\n\n1. Terms of Service Compliance:\n   - GitHub ToS: https://docs.github.com/en/site-policy/github-terms-of-service\n\
  \   - API ToS: https://docs.github.com/en/site-policy/github-acceptable-use-policies\n   - Rate limiting: respect all rate\
  \ limits and secondary rate limits\n   - Scraping: use official API only, no HTML scraping\n\n2. Data Privacy:\n   - Only\
  \ collect public repository data (no private repos)\n   - No personal data beyond public GitHub profile (login, name, avatar)\n\
  \   - No email addresses in final dataset (hash or remove)\n   - Comply with GDPR: right to deletion (if contributor requests)\n\
  \n3. Research Ethics:\n   - Data used for research purposes only\n   - No commercial use of collected data\n   - Attribute\
  \ GitHub as data source\n   - Consider publishing dataset with anonymization\n\n4. Attribution Requirements:\n   - Include\
  \ 'Data collected from GitHub API' in dataset metadata\n   - Link to GitHub API terms in documentation\n   - Consider CC-BY-SA\
  \ license for derived dataset\n\nSTATISTICAL CONSIDERATIONS:\n\n1. Sample Size Calculation:\n   - Power analysis: n=1000\
  \ provides 80% power to detect OR=1.5 in logistic regression\n   - Effect size: expect medium effect (Cohen's h ≈ 0.3) based\
  \ on prior literature\n   - Alpha=0.05, two-tailed test\n   - Adjust for 20% attrition: collect n=1250 to get n=1000 final\n\
  \n2. Stratified Sampling Validation:\n   - Verify strata are balanced: χ² test for language × survival contingency table\n\
  \   - Check for selection bias: compare collected sample to GitHub population (stars, age)\n\n3. Missing Data Handling:\n\
  \   - Type: MAR (Missing At Random) - assume missingness independent of survival\n   - Approach: listwise deletion if <10%\
  \ missing, multiple imputation if >10%\n   - Document: report % missing for each variable in final paper\n\n4. Confounding\
  \ Control:\n   - Measure all known confounders: project age, size, popularity, language\n   - Statistical control: include\
  \ as covariates in Cox model\n   - Sensitivity analysis: check if results hold without controls\n\nEXPECTED CHALLENGES &\
  \ SOLUTIONS:\n\nChallenge 1: GitHub API returns incomplete file data for large commits\n  Solution: Use REST API commit\
  \ detail endpoint (slower but complete)\n  Fallback: Sample files if commit has >50 files changed\n\nChallenge 2: Founder\
  \ departure date is ambiguous (sporadic commits)\n  Solution: Use 12-month window with no commits, not single date\n  Alternative:\
  \ use 'last meaningful commit' (excluding merges, bot commits)\n\nChallenge 3: Knowledge redundancy is correlated with bus\
  \ factor\n  Solution: This is expected! Control for bus factor in regression\n  Analysis: Check VIF (Variance Inflation\
  \ Factor) for multicollinearity\n\nChallenge 4: Some repos have very sparse commit data (git commits only)\n  Solution:\
  \ Exclude repos with <50 commits total\n  Alternative: use issue/PR data as proxy for activity\n\nChallenge 5: Time zone\
  \ handling in commit dates\n  Solution: Use ISO 8601 format from API, convert to UTC\n  Note: GitHub API returns dates in\
  \ ISO 8601 with timezone\n\nDELIVERABLES CHECKLIST:\n\n✓ data_out.json - Main dataset (<300MB)\n✓ data_out.json.gz - Compressed\
  \ version\n✓ data_out_schema.json - JSON Schema for validation\n✓ data_out_metadata.json - Collection parameters and summary\
  \ statistics\n✓ mini_data_out.json - 10-repo sample for testing\n✓ scripts/collect_data.py - Complete collection script\
  \ with all phases\n✓ scripts/validate_data.py - Validation and quality check script\n✓ scripts/compute_metrics.py - Redundancy\
  \ and survival computation\n✓ NOTES.md - Deviations from plan, known issues, assumptions\n✓ README.md - Dataset documentation,\
  \ schema description, usage examples\n\nVALIDATION CHECKLIST (Executor Must Complete):\n\n□ All 1000+ repos collected with\
  \ complete data\n□ JSON schema validation passes (100% of repos)\n□ File size <300MB (or document if larger with justification)\n\
  □ Knowledge redundancy computed for >90% of repos\n□ Founder departure identified for >80% of repos\n□ Survival outcome\
  \ determined for >80% of repos with departure\n□ Summary statistics computed and saved in metadata\n□ 10 repos spot-checked\
  \ manually for accuracy\n□ All GitHub API rate limits respected (no 403/429 errors in final run)\n□ Fallback strategies\
  \ documented if used\n□ Edge cases handled and documented\n□ Legal/ethical compliance verified\n\nThis exhaustive plan provides\
  \ multiple pathways to success, comprehensive error handling, and detailed technical specifications for every step of the\
  \ data collection process."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-21 16:30:21 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: "Applies this repo's Python conventions to experiment and evaluation scripts: uv-only environment setup (never pip), loguru logging with stdout plus a rotating file sink, @logger.catch(reraise=True) with explicit exception types, pathlib file access, type hints, and a standard main() script skeleton. ALWAYS read before writing or editing any Python script that runs an experiment, evaluation, or data-processing job. Triggers: writing or refactoring a Python script, uv venv, uv pip install, pyproject dependencies, loguru, logging setup, try/except and error handling, pathlib, script structure, Python 3.12. NOT for: parallelism, GPU throughput or hardware sizing (use aii-parallel-computing and aii-use-hardware), scaling long autonomous jobs (use aii-long-running-tasks), splitting oversized output files (use aii-file-size-limit), calling LLMs (use aii-openrouter-llms), or notebooks meant for Colab (use aii-colab)."
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: "Scales an experiment or evaluation up in stages — mini, 10, 50, 100, 200, then the largest run that fits — recording runtime at each step and extrapolating time-per-example against the remaining time budget before growing further, with background execution and hard RLIMIT_AS and RLIMIT_CPU caps. ALWAYS read before launching any script expected to run for many minutes or hours over a dataset. Triggers: long-running job, overnight or unattended run, time budget, how many examples fit, extrapolate runtime, start small then scale up, run in background and poll, avoid a timeout, full-dataset evaluation, resource limits. NOT for choosing the concurrency mechanism itself (aii-parallel-computing), measuring the machine's CPU, RAM or GPU (aii-use-hardware), or provisioning cloud pods (aii-runpod)."
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: "Validates JSON files against this repo's experiment-pipeline schemas (exp_sel_data_out, exp_gen_sol_out, exp_eval_sol_out, exp_proof_out) and generates size-optimized full, mini and preview variants of any JSON array file. ALWAYS use before treating a pipeline stage output as finished, whenever a schema or required-property error must be fixed, and whenever a large JSON file needs a small truncated version safe to read. Triggers: JSON schema validation, schema compliance, required property errors, pipeline stage outputs, the exp_*_out format names, mini and preview JSON generation, shrinking a large JSON before inspection. NOT for: discovering or downloading new datasets, which aii-hf-datasets and aii-owid-datasets cover; splitting oversized output files, which aii-file-size-limit covers; plotting JSON data, which aii-data-fig-gen covers; spreadsheet and .csv tabular data, which anthropic-xlsx covers."
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: "Splits an oversized generated output file into numbered parts that each fit a size limit: checks sizes with ls -lh, writes full_data_out_1.json, full_data_out_2.json and so on into a matching directory, deletes the original, repoints the reading code at a sorted glob, and regenerates mini and preview variants per part. ALWAYS run right after a script writes JSON output, and whenever a file is too big to keep, exceeds a stated file size limit, or gets rejected for its size. Triggers: file too large, output exceeds the size limit, oversized or huge JSON, ls -lh size check after generating results, splitting or chunking an output file into parts, output directory instead of one file. NOT for: schema validation or making mini and preview variants of a file already within the limit (use aii-json), or general Python script conventions (use aii-python)."
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: "Detects the CPU, RAM, GPU and VRAM actually available — cgroup v1 and v2 container quotas and CPU affinity rather than misleading host values — then sets RAM and VRAM budgets via resource.setrlimit and torch.cuda.set_per_process_memory_fraction so a script raises a catchable error instead of being OOM-killed, and picks the right torch wheel for the detected device. ALWAYS read before loading a large dataset, installing torch, or sizing batches and worker counts. Triggers: how much RAM or CPU or GPU is available, container memory limit, cgroup, OOM killed, MemoryError, os.cpu_count reports host cores, nproc, VRAM, CUDA available, CPU-only torch build, dataset too big for memory, chunking. NOT for spreading work across that hardware once measured (aii-parallel-computing), staged scale-up runs against a time budget (aii-long-running-tasks), or renting cloud machines (aii-runpod)."
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-08-21 16:30:35 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "Parallelises compute-heavy Python: asyncio with aiohttp and a bounded Semaphore for I/O-bound work, ProcessPoolExecutor under the spawn start method for CPU-bound work, NumPy vectorisation and batched PyTorch on GPU with an out-of-memory halving fallback. ALWAYS read before writing any script that loops over data, issues many API calls, downloads many files, or runs heavy computation — sequential loops are the default failure mode. Triggers: parallelise, make a slow script faster, concurrency, async, aiohttp, asyncio.gather, semaphore, multiprocessing, ProcessPoolExecutor, fork deadlock with loguru, worker count, batch size, CUDA out of memory, idle GPU, retries and rate limits. NOT for detecting what hardware exists or setting RAM and VRAM budgets (aii-use-hardware), staged scale-up against a time budget (aii-long-running-tasks), or provisioning cloud pods (aii-runpod)."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SKILL-INPUT — aii-hf-datasets · 2026-08-21 16:30:47 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: "Searches, previews, and downloads machine-learning datasets from the HuggingFace Hub catalogue — configs, splits, features and a loadable flag — saving full, mini and preview JSON files. Use whenever a task needs training data, an evaluation corpus, or a named public benchmark hosted on HuggingFace, and whenever candidate datasets must be discovered, compared and sampled before one is chosen. Triggers: HuggingFace, HF Hub, datasets library, dataset search or discovery, training data, benchmark corpus, parquet shards, configs and splits, dataset card, org/name dataset repo ids. NOT for: country-level global indicator statistics on energy, health, economics or demographics, which aii-owid-datasets covers; validating or reshaping JSON already on disk, which aii-json covers; plotting the numbers, which aii-data-fig-gen covers."
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [10] SKILL-INPUT — aii-owid-datasets · 2026-08-21 16:30:47 UTC

The agent loaded the **aii-owid-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-owid-datasets
description: "Searches and downloads country-and-year statistical tables from the Our World in Data (OWID) catalogue — energy, climate, health, COVID-19, economics, environment, demographics — returning real rows plus variable metadata as full, mini and preview JSON. Use whenever a task needs real-world global or per-country indicator data, national time series, or a specific OWID grapher or garden table path. Triggers: Our World in Data, OWID, owid.catalog, grapher or garden table path, global statistics, per-country time series, CO2 emissions, life expectancy, population, energy mix, GDP and development indicators. NOT for: machine-learning training or benchmark datasets on the HuggingFace Hub, which aii-hf-datasets covers; JSON schema validation, which aii-json covers; rendering the chart, which aii-data-fig-gen covers."
---

## Contents

- Workflow (2-phase table discovery process)
- Scripts (Search, Download with full parameters)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 2-Phase Table Discovery

### Phase 1: Search for Tables
Find tables with metadata (title, description, variables)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_search_datasets.py "renewable energy" --limit 5
```

### Phase 2: Download Table (if suitable)
Download the table after reviewing the search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_download_datasets.py "grapher/energy/2023-12-12/energy_mix"
```

---

## Scripts

### Search OWID tables (aii_owid_search_datasets.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_search_datasets.py "climate change" --limit 3
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_owid_search_datasets.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 3' ::: 'renewable energy' 'climate change' 'covid mortality'
```

**Example output:**
```
Found 3 OWID tables for 'climate change':

[1] Climate Change Impacts
    Path: grapher/climate/2023-10-15/climate_impacts
    Description: Global temperature anomalies and sea level rise...
    Variables (42 total):
      - Global temperature anomaly (°C): Annual global mean temperature anomaly
      - Sea level rise (mm): Global mean sea level change
      - Atmospheric CO2 concentration (ppm): Monthly CO2 concentration at Mauna Loa
      - Arctic sea ice extent (million km²): Monthly Arctic sea ice extent
      ...
```

**Parameters:**

`query` (required, positional)
- Search query string
- Examples: `"covid"`, `"energy mix"`, `"climate change"`

`--limit` (optional)
- Number of search results to return (default: 3)
- Higher values = more results to choose from

**Tips:**
- Search queries the OWID catalog index via ``owid.catalog.search`` (network required;
  the catalog is cached after the first call, which the worker warms at init)
- Returns metadata only - no data is downloaded
- Use the `path` field from results to download specific tables
- Ranking and matching are the catalog's own (fuzzy by default) across table titles,
  descriptions and paths
- Search returns tables from all channels (garden=highest quality, meadow=raw, backport=legacy, open_numbers=Gapminder)

---

### Download OWID table (aii_owid_download_datasets.py)

Download a table by path (from search results) and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_download_datasets.py "grapher/energy/2023-12-12/energy_mix"
```

**Parallel execution (multiple tables):**

IMPORTANT: When downloading multiple tables, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_owid_download_datasets.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'grapher/energy/2023-12-12/energy_mix' 'grapher/demography/2023-10-10/population' 'grapher/health/2023-08-01/life_expectancy'
```

**Example output:**
```
Downloaded OWID table: grapher/energy/2023-12-12/energy_mix

Dimensions: 15,420 rows x 12 columns
Columns: country, year, coal, oil, gas, nuclear, hydro, solar, wind, biofuels...

Files saved:
  Mini (READ THIS for development/testing): /path/to/mini_grapher_energy_2023-12-12_energy_mix.json
  Preview (DO NOT READ - for logging only): /path/to/preview_grapher_energy_2023-12-12_energy_mix.json
  Full (DO NOT READ - for scripts only):    /path/to/full_grapher_energy_2023-12-12_energy_mix.json

Sample data (first 3 rows):
  Row 1:
    country: Afghanistan
    year: 2000
    coal: 0.5
    ...
```

**Parameters:**

`path` (required, positional)
- Table path from search results
- Examples: `"grapher/energy/2023-12-12/energy_mix"`, `"garden/demography/2023-10-10/population"`

**Output files (auto-saved to `temp/tables/`):**
1. **Mini**: `mini_{path}.json` - 3 full rows - **READ THIS** for development/testing
2. **Preview**: `preview_{path}.json` - 3 truncated rows - **DO NOT READ directly** - for code you write to read
3. **Full**: `full_{path}.json` - All rows - **DO NOT READ directly** - for code you write to read

**Tips:**
- **Critical**: Only read the mini file directly with Read tool. Preview and full are input paths for code you write
- Use the `path` from search results to download specific tables
- Downloads directly from OWID catalog (network required)
- Files always saved to `temp/tables/` (path included in response)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [11] SKILL-INPUT — aii-web-tools · 2026-08-21 16:30:47 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
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

### [12] SYSTEM-USER prompt · 2026-08-21 16:34:47 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: GitHub OSS survival data collection
summary: >-
  Collect comprehensive GitHub repository data for 1000+ open-source projects to empirically test the knowledge redundancy
  hypothesis. Extract complete commit histories with file modifications, identify founder departures using multiple heuristics,
  compute knowledge redundancy via Jaccard similarity with directory-level and file-level variants, measure project survival
  using multiple metrics (commit activity, release frequency, issue resolution), and control for confounding variables (project
  age, size, popularity, programming language, contributor count, bus factor).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  COMPREHENSIVE DATA REQUIREMENTS: Collect 1000+ GitHub repositories meeting stratified sampling criteria: (1) POPULARITY:
  100-1000 stars (40%), 1000-10000 stars (40%), 10000+ stars (20%) to ensure variance in survival pressures; (2) AGE: 2-5
  years (50%), 5+ years (50%) to capture different lifecycle stages; (3) LANGUAGES: Stratified sample across 12 languages
  - Python (20%), JavaScript/TypeScript (20%), Java (10%), Go (10%), Rust (10%), C/C++ (10%), Ruby (5%), PHP (5%), Swift (5%),
  Kotlin (5%) to control for language-specific development patterns; (4) ACTIVITY: Minimum 50 commits total, 5+ contributors,
  at least one commit in past 6 months at time of collection; (5) FORK STATUS: Exclude forks (analyze parent repo if fork
  is substantial divergence). MANDATORY DATA FIELDS: (A) REPOSITORY METADATA: name, owner, full_name, description, HTML URL,
  creation timestamp, last push timestamp, star count, fork count, watcher count, primary language, license info, default
  branch, size (KB), open issues count, has_wiki, has_pages, archived status; (B) CONTRIBUTOR DATA: login, id, avatar_url,
  gravatar_id, type, site_admin, total_commit_count, first_commit_date, last_commit_date, files_modified (complete list),
  lines_added (estimated), lines_deleted (estimated); (C) COMMIT DATA: sha, author_name, author_email, author_date, committer_name,
  committer_date, message, files_changed (list with status: added/modified/deleted/renamed), additions_count, deletions_count,
  is_merge_commit; (D) FOUNDER ANALYSIS: identified_founder_login, founder_identification_method (first_committer|most_commits_early|owner_account),
  founder_first_commit, founder_last_commit, founder_departure_date (if applicable), departure_confidence (high/medium/low);
  (E) SURVIVAL METRICS: founder_departed (bool), departure_date, survived_12mo (bool), survived_24mo (bool), commits_per_month_pre_6mo,
  commits_per_month_post_12mo, releases_pre_6mo, releases_post_12mo, issues_resolved_pre_6mo, issues_resolved_post_12mo, survival_score
  (continuous 0-1); (F) COMPUTED METRICS: knowledge_redundancy_jaccard_file (float 0-1), knowledge_redundancy_jaccard_dir
  (float 0-1), knowledge_redundancy_overlap_coefficient (float 0-1), bus_factor (int), contributor_count_active, contributor_count_total,
  commit_frequency_pre_departure (commits/month), commit_frequency_post_departure, gini_coefficient_contributions, code_ownership_herfindahl,
  median_commits_per_contributor, max_commits_single_contributor, file_count_total, file_count_modified_by_multiple; (G) CONTROL
  VARIABLES: project_age_days, stars_per_day, commits_per_day_history, contributor_growth_rate, language_ecosystem_age (Python=1991,
  JavaScript=1995, etc.), is_company_backed (detect from org/owner), has_readme, has_tests, has_ci, license_permissiveness
  (0=proprietary, 1=permissive, 2=copyleft), issue_closure_rate_pre, issue_closure_rate_post. OUTPUT FORMAT: Single JSON file
  with gzip compression option, schema versioned, maximum 300MB uncompressed. Each repository object must be self-contained
  with all computed metrics to enable independent analysis. DATA QUALITY THRESHOLDS: 80%+ repos must have identifiable founder
  departure, 90%+ must have computable redundancy scores, 95%+ must have complete commit histories (no missing months), 100%
  must pass JSON schema validation. STATISTICAL POWER: Target n=1000 provides 80% power to detect medium effect sizes (Cohen's
  h=0.3) in survival differences across redundancy quartiles, assuming 50% survival rate and alpha=0.05.
dataset_search_plan: "EXHAUSTIVE 8-PHASE DATA COLLECTION PLAN WITH MULTIPLE STRATEGIES:\n\nPHASE 1: REPOSITORY DISCOVERY &\
  \ STRATIFIED SAMPLING (2 hours)\nStrategy A - GitHub GraphQL Search API (PRIMARY):\n  Query template: 'stars:100..1000 language:Python\
  \ created:2018-01-01..2022-01-01 pushed:>2023-01-01 -fork:true'\n  Pagination: Use cursor-based pagination with pageInfo\
  \ { hasNextPage, endCursor }\n  Rate limit: 5000 req/hour with authentication, implement 0.8 sec delay between requests\n\
  \  GraphQL query structure:\n    query searchRepos($query: String!, $cursor: String, $first: Int = 50) {\n      search(query:\
  \ $query, type: REPOSITORY, first: $first, after: $cursor) {\n        repositoryCount\n        pageInfo { hasNextPage, endCursor\
  \ }\n        edges {\n          node {\n            ... on Repository {\n              nameWithOwner, description, stargazerCount,\
  \ forkCount, isFork\n              createdAt, pushedAt, updatedAt\n              primaryLanguage { name }\n            \
  \  licenseInfo { spdxId }\n              defaultBranchRef { name }\n              owner { login, __typename }\n        \
  \    }\n          }\n        }\n      }\n    }\n  Execute for each language × star bracket combination, collect 150% of\
  \ target to allow filtering\n\nStrategy B - GitHub REST Search API (FALLBACK if GraphQL fails):\n  Endpoint: GET /search/repositories?q={query}&sort=stars&order=desc&per_page=100&page={n}\n\
  \  Pagination: Link header with rel=\"next\", max 1000 results per query (GitHub limit)\n  Rate limit: 30 req/minute unauthenticated,\
  \ 5000 req/hour authenticated\n\nStrategy C - Existing Dataset Mining (ALTERNATIVE):\n  - GHTorrent (http://ghtorrent.org):\
  \ MySQL dumps, last updated 2020, may use if recent enough\n  - GH Archive (https://www.gharchive.org): Google BigQuery\
  \ public dataset, events since 2015\n  - Software Heritage (https://www.softwareheritage.org): Comprehensive archive, API\
  \ available\n  - World of Code (https://worldofcode.org): Snapshot-based, updated quarterly\n  Evaluate based on: data recency,\
  \ completeness of file modification data, ease of extraction\n\nPHASE 2: AUTHENTICATION & RATE LIMIT MANAGEMENT (30 mins\
  \ setup)\n  Token sources (in priority order):\n  1. GitHub Personal Access Token (PAT) with repo scope: 'ghp_xxxxxxxxxxxx'\n\
  \  2. GitHub App installation token (if available)\n  3. OAuth token from user authentication\n  Rate limit handling:\n\
  \  - Check X-RateLimit-Remaining header before each request\n  - If < 100 remaining, sleep until X-RateLimit-Reset timestamp\n\
  \  - Implement exponential backoff: 1s, 2s, 4s, 8s, 16s, then 60s max\n  - Secondary rate limits: 1 req/sec for REST, 10\
  \ req/sec for GraphQL (recommended)\n  - Use conditional requests: ETag/Last-Modified headers to avoid counting against\
  \ limit\n  Multiple token rotation:\n  - Prepare 3-5 tokens in advance\n  - Round-robin through tokens when primary is rate\
  \ limited\n  - Monitor rate limits per token independently\n\nPHASE 3: DETAILED DATA COLLECTION - HYBRID API STRATEGY (4-6\
  \ hours)\n\n3A. Commit History Collection (GraphQL - efficient for metadata):\n  Query structure:\n    query repoCommits($owner:\
  \ String!, $name: String!, $cursor: String) {\n      repository(owner: $owner, name: $name) {\n        defaultBranchRef\
  \ {\n          target {\n            ... on Commit {\n              history(first: 100, after: $cursor) {\n            \
  \    pageInfo { hasNextPage, endCursor }\n                edges {\n                  node {\n                    oid, messageHeadline,\
  \ committedDate, pushedDate\n                    author { user { login, id }, name, email }\n                    committer\
  \ { user { login, id }, name, email }\n                    changedFiles, additions, deletions\n                    parents(first:\
  \ 1) { edges { node { oid } } }\n                  }\n                }\n              }\n            }\n          }\n \
  \       }\n      }\n    }\n  Pagination: Collect ALL commits (may be 1000+ for large repos)\n  Optimization: Stop after\
  \ 500 commits if repo is very active (sample most recent)\n  Date filtering: Only collect commits from repo creation to\
  \ 2024-01-01 (cutoff for analysis)\n\n3B. File Modification Data Collection (REST - required for file names):\n  PRIMARY\
  \ METHOD: GET /repos/{owner}/{repo}/commits?sha={branch}&per_page=100&since={date}\n  Returns: array of commits with files\
  \ array containing filename, status, additions, deletions\n  \n  SECONDARY METHOD (if primary fails): GET /repos/{owner}/{repo}/commits/{sha}\n\
  \  Returns: single commit with complete file diff information\n  \n  TERTIARY METHOD (bulk): Use Git Trees API\n  GET /repos/{owner}/{repo}/git/trees/{sha}?recursive=1\n\
  \  Then cross-reference with commit list to infer modifications (less accurate)\n  \n  File path normalization:\n  - Convert\
  \ all paths to relative, lowercase for comparison\n  - Handle renames: track rename detection from commit data (status:\
  \ 'renamed')\n  - Handle deletions: keep in contributor's file set as 'previously modified'\n  - Directory extraction: also\
  \ compute directory-level modifications (parent dir of each file)\n\n3C. Contributor Metadata Collection:\n  GraphQL: repository(owner:\
  \ $owner, name: $name) { collaborators(first: 100) { edges { node { login, id, ... } } } }\n  REST: GET /repos/{owner}/{repo}/contributors?per_page=100\n\
  \  Note: GitHub API only returns top 500 contributors, paginate if needed\n  Affiliation: distinguish between 'owner', 'member',\
  \ 'contributor' if possible\n\nPHASE 4: FOUNDER IDENTIFICATION - MULTI-HEURISTIC APPROACH (1 hour)\n\nHeuristic 1 - First\
  \ Committer Method:\n  - Sort all commits by date ascending\n  - Founder = author of first commit (or first 5 commits if\
  \ first is bot)\n  - Confidence: HIGH if first commit is within 7 days of repo creation\n\nHeuristic 2 - Early Period Dominance\
  \ Method:\n  - Define early period: first 90 days after repo creation\n  - Count commits per author in early period\n  -\
  \ Founder = author with most commits in early period\n  - Confidence: HIGH if >50% of early commits, MEDIUM if 30-50%, LOW\
  \ if <30%\n\nHeuristic 3 - Owner Account Method:\n  - If repo owner is a user (not org), check if owner appears in contributors\n\
  \  - If yes and has commits in first 30 days, likely founder\n  - Confidence: MEDIUM (owner may have transferred repo)\n\
  \nHeuristic 4 - Repository Description / README Parsing:\n  - Parse repo description and README for phrases like 'Created\
  \ by', 'Author:', etc.\n  - Use regex: r'(?:created|authored|written|developed)\\s+(?:by\\s+)?@?(\\w+)'\n  - Confidence:\
  \ LOW (unreliable, use only as tiebreaker)\n\nHeuristic 5 - GitHub Organization Membership:\n  - If repo owned by org, check\
  \ org members for early contributors\n  - May not identify individual founder if org-created\n  - Confidence: LOW (often\
  \ team effort)\n\nFINAL FOUNDER SELECTION ALGORITHM:\n  def identify_founder(commits, repo_metadata):\n      methods = [\n\
  \          ('first_committer', heuristic1(commits)),\n          ('early_dominance', heuristic2(commits)),\n          ('owner_account',\
  \ heuristic3(repo_metadata, commits))\n      ]\n      # Weight by confidence\n      scores = {}\n      for method, (candidate,\
  \ confidence) in methods:\n          weight = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}[confidence]\n          scores[candidate]\
  \ = scores.get(candidate, 0) + weight\n      \n      # Return highest scoring candidate\n      founder = max(scores, key=scores.get)\n\
  \      \n      # Determine departure\n      founder_commits = [c for c in commits if c.author == founder]\n      last_commit\
  \ = max(c.committedDate for c in founder_commits)\n      \n      # Check 12+ months inactivity\n      cutoff_date = last_commit\
  \ + timedelta(days=365)\n      recent_commits = [c for c in commits if c.committedDate > cutoff_date]\n      \n      departed\
  \ = len(recent_commits) == 0\n      departure_date = last_commit if departed else None\n      \n      return founder, departure_date,\
  \ departed\n\nPHASE 5: KNOWLEDGE REDUNDANCY COMPUTATION - MULTIPLE METRICS (1 hour)\n\n5A. Jaccard Similarity (Primary Metric):\n\
  \  Definition: J(A,B) = |A ∩ B| / |A ∪ B|\n  Where A and B are sets of files modified by contributors A and B\n  \n  Implementation:\n\
  \  def compute_jaccard_redundancy(contributor_files):\n      '''\n      contributor_files: dict {contributor_login: set(file_paths)}\n\
  \      Returns: average pairwise Jaccard similarity (float 0-1)\n      '''\n      import itertools\n      from statistics\
  \ import mean\n      \n      contributors = list(contributor_files.keys())\n      if len(contributors) < 2:\n          return\
  \ 0.0\n      \n      similarities = []\n      for c1, c2 in itertools.combinations(contributors, 2):\n          files1 =\
  \ contributor_files[c1]\n          files2 = contributor_files[c2]\n          \n          if not files1 or not files2:\n\
  \              continue\n          \n          intersection = len(files1 & files2)\n          union = len(files1 | files2)\n\
  \          \n          if union > 0:\n              jaccard = intersection / union\n              similarities.append(jaccard)\n\
  \      \n      return mean(similarities) if similarities else 0.0\n\n5B. Directory-Level Jaccard (Secondary Metric):\n \
  \ - Extract directory paths from file paths (e.g., 'src/main.py' -> 'src/')\n  - Compute Jaccard on directory sets to capture\
  \ module-level redundancy\n  - May be more stable than file-level for large repos\n\n5C. Overlap Coefficient (Alternative\
  \ Metric):\n  Definition: O(A,B) = |A ∩ B| / min(|A|, |B|)\n  - More sensitive to small file sets\n  - Range: 0-1, where\
  \ 1 means one contributor's files are subset of other's\n\n5D. Contributor Filtering:\n  - Include only contributors with\
  \ 5+ commits (filter out one-time contributors)\n  - Exclude bot accounts (detect via login patterns: 'bot', '[bot]', 'dependabot',\
  \ etc.)\n  - Exclude merge commits from file modification counts\n  - Weight by commit frequency: weight = log(1 + commit_count)\
  \ to reduce outlier influence\n\nPHASE 6: SURVIVAL MEASUREMENT - MULTI-METRIC APPROACH (1 hour)\n\n6A. Survival Definition\
  \ (Primary):\n  Binary outcome: survived_12mo = 1 if project has ≥1 commit/month average in 12 months post-departure\n \
  \ Comparison: post_departure_rate ≥ 0.25 × pre_departure_rate\n  Pre-departure baseline: 6 months immediately before departure\n\
  \  \n  def measure_survival_binary(commits, departure_date):\n      if not departure_date:\n          return None\n    \
  \  \n      # Pre-departure period (6 months before)\n      pre_start = departure_date - timedelta(days=180)\n      pre_commits\
  \ = [c for c in commits \n                     if pre_start <= c.committedDate <= departure_date]\n      pre_rate = len(pre_commits)\
  \ / 6.0  # commits per month\n      \n      # Post-departure period (12 months after)\n      post_start = departure_date\n\
  \      post_end = departure_date + timedelta(days=365)\n      post_commits = [c for c in commits \n                    \
  \ if post_start <= c.committedDate <= post_end]\n      post_rate = len(post_commits) / 12.0\n      \n      # Binary survival\n\
  \      survived = post_rate >= (pre_rate * 0.25)\n      \n      return {\n          'survived_12mo': survived,\n       \
  \   'pre_rate': pre_rate,\n          'post_rate': post_rate,\n          'post_commits_12mo': len(post_commits)\n      }\n\
  \n6B. Continuous Survival Score (Secondary):\n  survival_score = min(1.0, post_rate / pre_rate) if pre_rate > 0 else 0.0\n\
  \  - Captures degree of survival, not just binary outcome\n  - Allows for regression analysis with continuous dependent\
  \ variable\n\n6C. Alternative Survival Metrics:\n  - Release-based: survived if ≥1 release in 12 months post-departure\n\
  \  - Issue-based: survived if ≥1 issue resolved in 12 months post-departure\n  - Hybrid: survived if any of commit/release/issue\
  \ activity\n\n6D. Censoring Handling:\n  - If departure_date is within 12 months of data collection, censor (mark as 'ongoing')\n\
  \  - If repo is archived, mark as 'archived' (definite non-survival)\n  - If repo has commits but very low rate, mark as\
  \ 'declining' (intermediate category)\n\nPHASE 7: CONTROL VARIABLE COMPUTATION (1 hour)\n\n7A. Bus Factor Calculation:\n\
  \  - Sort contributors by number of unique files modified (descending)\n  - Bus factor = smallest k such that top k contributors\
  \ modify >50% of all files\n  - Alternative: Truck factor algorithm (Avelino et al. 2016)\n\n7B. Project Age & Growth:\n\
  \  - age_days = collection_date - creation_date\n  - commits_per_day = total_commits / age_days\n  - stars_per_day = stargazers_count\
  \ / age_days\n  - contributor_growth_rate = (contributors_at_1yr - contributors_at_6mo) / 180\n\n7C. Code Ownership Metrics:\n\
  \  - Herfindahl index: H = Σ (contributor_commits / total_commits)²\n  - Gini coefficient of commit distribution among contributors\n\
  \  - Max contribution percentage: max_commits / total_commits\n\n7D. Language Ecosystem Controls:\n  - language_age = current_year\
  \ - language_creation_year\n  - language_popularity_rank (from TIOBE/RedMonk rankings)\n  - is_company_backed: detect from\
  \ owner (e.g., 'google', 'microsoft', 'facebook')\n\nPHASE 8: DATA VALIDATION, QUALITY CONTROL & EXPORT (1 hour)\n\n8A.\
  \ Schema Validation:\n  JSON schema definition (Draft 7):\n  {\n    \"$schema\": \"http://json-schema.org/draft-07/schema#\"\
  ,\n    \"title\": \"OSS Repository Data\",\n    \"type\": \"object\",\n    \"required\": [\"metadata\", \"repositories\"\
  ],\n    \"properties\": {\n      \"metadata\": { \"type\": \"object\", ... },\n      \"repositories\": {\n        \"type\"\
  : \"array\",\n        \"items\": {\n          \"type\": \"object\",\n          \"required\": [\"repo_id\", \"name\", \"\
  owner\", \"founder\", \"survival_outcome\", \"computed_metrics\"],\n          \"properties\": {\n            \"repo_id\"\
  : { \"type\": \"string\" },\n            \"knowledge_redundancy\": { \"type\": \"number\", \"minimum\": 0, \"maximum\":\
  \ 1 },\n            ...\n          }\n        }\n      }\n    }\n  }\n\n8B. Data Quality Checks:\n  def validate_repository(repo):\n\
  \      errors = []\n      warnings = []\n      \n      # Critical errors (exclude repo)\n      if not repo.get('founder',\
  \ {}).get('login'):\n          errors.append('No founder identified')\n      if repo.get('computed_metrics', {}).get('knowledge_redundancy')\
  \ is None:\n          errors.append('Knowledge redundancy not computable')\n      if len(repo.get('commits', [])) < 10:\n\
  \          errors.append('Too few commits (<10)')\n      \n      # Warnings (keep but flag)\n      if repo.get('survival_outcome',\
  \ {}).get('departure_date') is None:\n          warnings.append('Founder has not departed yet (censored)')\n      if len(repo.get('contributors',\
  \ [])) < 3:\n          warnings.append('Very few contributors (<3)')\n      \n      return errors, warnings\n\n8C. Outlier\
  \ Detection:\n  - Knowledge redundancy: flag if >3 standard deviations from mean\n  - Survival rate: flag if post-rate >\
  \ 10× pre-rate (anomaly)\n  - Contributor count: flag if >99th percentile (very large project)\n\n8D. Export Strategy:\n\
  \  - Primary: data_out.json (pretty-printed for readability)\n  - Compressed: data_out.json.gz (using gzip)\n  - Mini version:\
  \ mini_data_out.json (first 10 repos for testing)\n  - Metadata: data_out_metadata.json (summary statistics, collection\
  \ parameters)\n  - Schema: data_out_schema.json (JSON Schema for validation)\n\n  Export code:\n  import json, gzip\n  \n\
  \  # Main export\n  with open('data_out.json', 'w') as f:\n      json.dump(dataset, f, indent=2, default=str)\n  \n  # Compressed\n\
  \  with gzip.open('data_out.json.gz', 'wt') as f:\n      json.dump(dataset, f, default=str)\n  \n  # Check size\n  import\
  \ os\n  size_mb = os.path.getsize('data_out.json') / 1_000_000\n  if size_mb > 300:\n      print(f'WARNING: File size {size_mb:.1f}MB\
  \ exceeds 300MB limit')\n\nCOMPREHENSIVE FALLBACK STRATEGIES:\n\nFALLBACK 1 - API Rate Limit Exhaustion:\n  A. Multiple\
  \ Token Rotation: Prepare 5 GitHub tokens, rotate when limit reached\n  B. Reduce Scope: Collect 500 repos instead of 1000\
  \ (maintain stratification)\n  C. Use GitHub Archive via BigQuery: \n     - Query: SELECT repo_name, actor_login, committed_date,\
  \ files FROM `githubarchive.day.20230101` ...\n     - Free tier: 1TB/month query, sufficient for this analysis\n     - Requires\
  \ Google Cloud account setup\n  D. Use GHTorrent MySQL Dump:\n     - Download: http://ghtorrent.org/downloads.html\n   \
  \  - Last updated: ~2020, may be acceptable if hypothesis test is not time-sensitive\n     - Requires MySQL server setup\
  \ and ~100GB disk space\n\nFALLBACK 2 - File Modification Data Too Expensive:\n  A. Approximate from Commit Messages: Parse\
  \ file paths from commit messages (70% accuracy)\n  B. Sample Commits: Collect file data for only 25% of commits per repo\
  \ (systematic sample)\n  C. Use Directory-Level Only: Skip file-level, use directory modifications (less granular)\n  D.\
  \ Infer from Blame Data: Use git blame to determine file authorship (alternative approach)\n\nFALLBACK 3 - Founder Identification\
  \ Unclear:\n  A. Use Multiple Heuristics: Combine 3+ heuristics, use majority vote\n  B. Manual Review Sample: Flag 50 ambiguous\
  \ cases, manually review via web UI\n  C. Exclude Uncertain: Drop repos where confidence is LOW for all heuristics\n  D.\
  \ Sensitivity Analysis: Run analysis with/without ambiguous cases, check robustness\n\nFALLBACK 4 - Knowledge Redundancy\
  \ Computation Fails:\n  A. Use Commit Overlap: If file data missing, use commit timestamp overlap as proxy\n  B. Use Code\
  \ Review Data: If available, use PR reviewer assignments as proxy for expertise\n  C. Use Issue Assignment: Use issue assignee\
  \ data to infer contributor focus areas\n  D. Skip Metric: Mark as null, use only repos with computable redundancy\n\nFALLBACK\
  \ 5 - Survival Measurement Problematic:\n  A. Extend Window: Use 24-month post-departure if 12-month is noisy\n  B. Use\
  \ Multiple Metrics: Combine commit + release + issue metrics\n  C. Censor Appropriately: Mark repos with insufficient post-departure\
  \ data as censored\n  D. Use Time-Varying Survival: Kaplan-Meier curve instead of binary outcome\n\nEDGE CASES & SPECIAL\
  \ HANDLING:\n\n1. Monorepos: Google/Facebook style repos with multiple projects\n   - Detect via: >10000 files, >1000 contributors,\
  \ very high commit rate\n   - Handle via: exclude or analyze subprojects separately (complex)\n\n2. Bot-Heavy Repositories:\
  \ Automated commits (dependabot, CI bots)\n   - Detect via: login contains 'bot', '[bot]', or known bot accounts\n   - Handle\
  \ via: exclude bot commits from file modification analysis\n\n3. Corporate/Organization Repositories: Multiple founders,\
  \ team-based\n   - Detect via: owner is organization, not user\n   - Handle via: identify 'core team' (top 5 contributors)\
  \ instead of single founder\n\n4. Forked Repositories with Substantial Changes:\n   - Detect via: is_fork=true but >500\
  \ commits after fork, different primary language\n   - Handle via: analyze fork as independent project (exclude parent)\n\
  \n5. Archived Repositories:\n   - Detect via: archived=true field from GitHub API\n   - Handle via: mark as 'definite non-survival'\
  \ if archived post-departure\n\n6. Renamed/Migrated Repositories:\n   - Detect via: repository has 'parent' or 'source'\
  \ field pointing elsewhere\n   - Handle via: follow redirects, collect data from current URL\n\n7. Repositories with Very\
  \ Large Histories (>10000 commits):\n   - Handle via: sample 1000 most recent commits, document sampling method\n   - Alternative:\
  \ use Git API with shallow clone (not possible via GitHub API)\n\n8. Repositories with Force Pushes (rewritten history):\n\
  \   - Detect via: missing commits, non-linear history with gaps\n   - Handle via: flag as 'history may be incomplete', use\
  \ available data\n\n9. Multi-Language Repositories:\n   - Detect via: primary_language is null or multiple languages in\
  \ top 10 files\n   - Handle via: assign to 'primary' language based on file count, create 'mixed' category\n\n10. Repositories\
  \ with Binary Files (images, data):\n    - Handle via: exclude binary files from file modification sets (detect via extension)\n\
  \    - Extensions to exclude: .png, .jpg, .gif, .pdf, .zip, .tar, .dat, .bin\n\nPERFORMANCE OPTIMIZATION:\n\n1. Parallel\
  \ API Requests:\n   - Use asyncio with aiohttp for REST API calls (respect rate limits)\n   - Use threading for GraphQL\
  \ queries (Python GIL less relevant for I/O bound)\n   - Max 5 concurrent requests to avoid secondary rate limits\n\n2.\
  \ Caching Strategy:\n   - Cache commit data per repo: save after every 100 commits collected\n   - Cache intermediate results:\
  \ save progress every 10 repos\n   - Resume capability: if script crashes, resume from last saved state\n\n3. Memory Management:\n\
  \   - Stream large repos: don't load all commits into memory at once\n   - Use generators for file processing\n   - Delete\
  \ raw API responses after parsing\n\n4. Request Batching:\n   - GraphQL: batch multiple repo queries in one request (if\
  \ using aliases)\n   - REST: use ?per_page=100 to minimize requests\n   - Use conditional requests (ETag) to avoid re-fetching\
  \ unchanged data\n\nLEGAL & ETHICAL CONSIDERATIONS:\n\n1. Terms of Service Compliance:\n   - GitHub ToS: https://docs.github.com/en/site-policy/github-terms-of-service\n\
  \   - API ToS: https://docs.github.com/en/site-policy/github-acceptable-use-policies\n   - Rate limiting: respect all rate\
  \ limits and secondary rate limits\n   - Scraping: use official API only, no HTML scraping\n\n2. Data Privacy:\n   - Only\
  \ collect public repository data (no private repos)\n   - No personal data beyond public GitHub profile (login, name, avatar)\n\
  \   - No email addresses in final dataset (hash or remove)\n   - Comply with GDPR: right to deletion (if contributor requests)\n\
  \n3. Research Ethics:\n   - Data used for research purposes only\n   - No commercial use of collected data\n   - Attribute\
  \ GitHub as data source\n   - Consider publishing dataset with anonymization\n\n4. Attribution Requirements:\n   - Include\
  \ 'Data collected from GitHub API' in dataset metadata\n   - Link to GitHub API terms in documentation\n   - Consider CC-BY-SA\
  \ license for derived dataset\n\nSTATISTICAL CONSIDERATIONS:\n\n1. Sample Size Calculation:\n   - Power analysis: n=1000\
  \ provides 80% power to detect OR=1.5 in logistic regression\n   - Effect size: expect medium effect (Cohen's h ≈ 0.3) based\
  \ on prior literature\n   - Alpha=0.05, two-tailed test\n   - Adjust for 20% attrition: collect n=1250 to get n=1000 final\n\
  \n2. Stratified Sampling Validation:\n   - Verify strata are balanced: χ² test for language × survival contingency table\n\
  \   - Check for selection bias: compare collected sample to GitHub population (stars, age)\n\n3. Missing Data Handling:\n\
  \   - Type: MAR (Missing At Random) - assume missingness independent of survival\n   - Approach: listwise deletion if <10%\
  \ missing, multiple imputation if >10%\n   - Document: report % missing for each variable in final paper\n\n4. Confounding\
  \ Control:\n   - Measure all known confounders: project age, size, popularity, language\n   - Statistical control: include\
  \ as covariates in Cox model\n   - Sensitivity analysis: check if results hold without controls\n\nEXPECTED CHALLENGES &\
  \ SOLUTIONS:\n\nChallenge 1: GitHub API returns incomplete file data for large commits\n  Solution: Use REST API commit\
  \ detail endpoint (slower but complete)\n  Fallback: Sample files if commit has >50 files changed\n\nChallenge 2: Founder\
  \ departure date is ambiguous (sporadic commits)\n  Solution: Use 12-month window with no commits, not single date\n  Alternative:\
  \ use 'last meaningful commit' (excluding merges, bot commits)\n\nChallenge 3: Knowledge redundancy is correlated with bus\
  \ factor\n  Solution: This is expected! Control for bus factor in regression\n  Analysis: Check VIF (Variance Inflation\
  \ Factor) for multicollinearity\n\nChallenge 4: Some repos have very sparse commit data (git commits only)\n  Solution:\
  \ Exclude repos with <50 commits total\n  Alternative: use issue/PR data as proxy for activity\n\nChallenge 5: Time zone\
  \ handling in commit dates\n  Solution: Use ISO 8601 format from API, convert to UTC\n  Note: GitHub API returns dates in\
  \ ISO 8601 with timezone\n\nDELIVERABLES CHECKLIST:\n\n✓ data_out.json - Main dataset (<300MB)\n✓ data_out.json.gz - Compressed\
  \ version\n✓ data_out_schema.json - JSON Schema for validation\n✓ data_out_metadata.json - Collection parameters and summary\
  \ statistics\n✓ mini_data_out.json - 10-repo sample for testing\n✓ scripts/collect_data.py - Complete collection script\
  \ with all phases\n✓ scripts/validate_data.py - Validation and quality check script\n✓ scripts/compute_metrics.py - Redundancy\
  \ and survival computation\n✓ NOTES.md - Deviations from plan, known issues, assumptions\n✓ README.md - Dataset documentation,\
  \ schema description, usage examples\n\nVALIDATION CHECKLIST (Executor Must Complete):\n\n□ All 1000+ repos collected with\
  \ complete data\n□ JSON schema validation passes (100% of repos)\n□ File size <300MB (or document if larger with justification)\n\
  □ Knowledge redundancy computed for >90% of repos\n□ Founder departure identified for >80% of repos\n□ Survival outcome\
  \ determined for >80% of repos with departure\n□ Summary statistics computed and saved in metadata\n□ 10 repos spot-checked\
  \ manually for accuracy\n□ All GitHub API rate limits respected (no 403/429 errors in final run)\n□ Fallback strategies\
  \ documented if used\n□ Edge cases handled and documented\n□ Legal/ethical compliance verified\n\nThis exhaustive plan provides\
  \ multiple pathways to success, comprehensive error handling, and detailed technical specifications for every step of the\
  \ data collection process."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 2 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 1 DATASET based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [13] SYSTEM-USER prompt · 2026-08-21 16:36:53 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: GitHub OSS survival data collection
summary: >-
  Collect comprehensive GitHub repository data for 1000+ open-source projects to empirically test the knowledge redundancy
  hypothesis. Extract complete commit histories with file modifications, identify founder departures using multiple heuristics,
  compute knowledge redundancy via Jaccard similarity with directory-level and file-level variants, measure project survival
  using multiple metrics (commit activity, release frequency, issue resolution), and control for confounding variables (project
  age, size, popularity, programming language, contributor count, bus factor).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  COMPREHENSIVE DATA REQUIREMENTS: Collect 1000+ GitHub repositories meeting stratified sampling criteria: (1) POPULARITY:
  100-1000 stars (40%), 1000-10000 stars (40%), 10000+ stars (20%) to ensure variance in survival pressures; (2) AGE: 2-5
  years (50%), 5+ years (50%) to capture different lifecycle stages; (3) LANGUAGES: Stratified sample across 12 languages
  - Python (20%), JavaScript/TypeScript (20%), Java (10%), Go (10%), Rust (10%), C/C++ (10%), Ruby (5%), PHP (5%), Swift (5%),
  Kotlin (5%) to control for language-specific development patterns; (4) ACTIVITY: Minimum 50 commits total, 5+ contributors,
  at least one commit in past 6 months at time of collection; (5) FORK STATUS: Exclude forks (analyze parent repo if fork
  is substantial divergence). MANDATORY DATA FIELDS: (A) REPOSITORY METADATA: name, owner, full_name, description, HTML URL,
  creation timestamp, last push timestamp, star count, fork count, watcher count, primary language, license info, default
  branch, size (KB), open issues count, has_wiki, has_pages, archived status; (B) CONTRIBUTOR DATA: login, id, avatar_url,
  gravatar_id, type, site_admin, total_commit_count, first_commit_date, last_commit_date, files_modified (complete list),
  lines_added (estimated), lines_deleted (estimated); (C) COMMIT DATA: sha, author_name, author_email, author_date, committer_name,
  committer_date, message, files_changed (list with status: added/modified/deleted/renamed), additions_count, deletions_count,
  is_merge_commit; (D) FOUNDER ANALYSIS: identified_founder_login, founder_identification_method (first_committer|most_commits_early|owner_account),
  founder_first_commit, founder_last_commit, founder_departure_date (if applicable), departure_confidence (high/medium/low);
  (E) SURVIVAL METRICS: founder_departed (bool), departure_date, survived_12mo (bool), survived_24mo (bool), commits_per_month_pre_6mo,
  commits_per_month_post_12mo, releases_pre_6mo, releases_post_12mo, issues_resolved_pre_6mo, issues_resolved_post_12mo, survival_score
  (continuous 0-1); (F) COMPUTED METRICS: knowledge_redundancy_jaccard_file (float 0-1), knowledge_redundancy_jaccard_dir
  (float 0-1), knowledge_redundancy_overlap_coefficient (float 0-1), bus_factor (int), contributor_count_active, contributor_count_total,
  commit_frequency_pre_departure (commits/month), commit_frequency_post_departure, gini_coefficient_contributions, code_ownership_herfindahl,
  median_commits_per_contributor, max_commits_single_contributor, file_count_total, file_count_modified_by_multiple; (G) CONTROL
  VARIABLES: project_age_days, stars_per_day, commits_per_day_history, contributor_growth_rate, language_ecosystem_age (Python=1991,
  JavaScript=1995, etc.), is_company_backed (detect from org/owner), has_readme, has_tests, has_ci, license_permissiveness
  (0=proprietary, 1=permissive, 2=copyleft), issue_closure_rate_pre, issue_closure_rate_post. OUTPUT FORMAT: Single JSON file
  with gzip compression option, schema versioned, maximum 300MB uncompressed. Each repository object must be self-contained
  with all computed metrics to enable independent analysis. DATA QUALITY THRESHOLDS: 80%+ repos must have identifiable founder
  departure, 90%+ must have computable redundancy scores, 95%+ must have complete commit histories (no missing months), 100%
  must pass JSON schema validation. STATISTICAL POWER: Target n=1000 provides 80% power to detect medium effect sizes (Cohen's
  h=0.3) in survival differences across redundancy quartiles, assuming 50% survival rate and alpha=0.05.
dataset_search_plan: "EXHAUSTIVE 8-PHASE DATA COLLECTION PLAN WITH MULTIPLE STRATEGIES:\n\nPHASE 1: REPOSITORY DISCOVERY &\
  \ STRATIFIED SAMPLING (2 hours)\nStrategy A - GitHub GraphQL Search API (PRIMARY):\n  Query template: 'stars:100..1000 language:Python\
  \ created:2018-01-01..2022-01-01 pushed:>2023-01-01 -fork:true'\n  Pagination: Use cursor-based pagination with pageInfo\
  \ { hasNextPage, endCursor }\n  Rate limit: 5000 req/hour with authentication, implement 0.8 sec delay between requests\n\
  \  GraphQL query structure:\n    query searchRepos($query: String!, $cursor: String, $first: Int = 50) {\n      search(query:\
  \ $query, type: REPOSITORY, first: $first, after: $cursor) {\n        repositoryCount\n        pageInfo { hasNextPage, endCursor\
  \ }\n        edges {\n          node {\n            ... on Repository {\n              nameWithOwner, description, stargazerCount,\
  \ forkCount, isFork\n              createdAt, pushedAt, updatedAt\n              primaryLanguage { name }\n            \
  \  licenseInfo { spdxId }\n              defaultBranchRef { name }\n              owner { login, __typename }\n        \
  \    }\n          }\n        }\n      }\n    }\n  Execute for each language × star bracket combination, collect 150% of\
  \ target to allow filtering\n\nStrategy B - GitHub REST Search API (FALLBACK if GraphQL fails):\n  Endpoint: GET /search/repositories?q={query}&sort=stars&order=desc&per_page=100&page={n}\n\
  \  Pagination: Link header with rel=\"next\", max 1000 results per query (GitHub limit)\n  Rate limit: 30 req/minute unauthenticated,\
  \ 5000 req/hour authenticated\n\nStrategy C - Existing Dataset Mining (ALTERNATIVE):\n  - GHTorrent (http://ghtorrent.org):\
  \ MySQL dumps, last updated 2020, may use if recent enough\n  - GH Archive (https://www.gharchive.org): Google BigQuery\
  \ public dataset, events since 2015\n  - Software Heritage (https://www.softwareheritage.org): Comprehensive archive, API\
  \ available\n  - World of Code (https://worldofcode.org): Snapshot-based, updated quarterly\n  Evaluate based on: data recency,\
  \ completeness of file modification data, ease of extraction\n\nPHASE 2: AUTHENTICATION & RATE LIMIT MANAGEMENT (30 mins\
  \ setup)\n  Token sources (in priority order):\n  1. GitHub Personal Access Token (PAT) with repo scope: 'ghp_xxxxxxxxxxxx'\n\
  \  2. GitHub App installation token (if available)\n  3. OAuth token from user authentication\n  Rate limit handling:\n\
  \  - Check X-RateLimit-Remaining header before each request\n  - If < 100 remaining, sleep until X-RateLimit-Reset timestamp\n\
  \  - Implement exponential backoff: 1s, 2s, 4s, 8s, 16s, then 60s max\n  - Secondary rate limits: 1 req/sec for REST, 10\
  \ req/sec for GraphQL (recommended)\n  - Use conditional requests: ETag/Last-Modified headers to avoid counting against\
  \ limit\n  Multiple token rotation:\n  - Prepare 3-5 tokens in advance\n  - Round-robin through tokens when primary is rate\
  \ limited\n  - Monitor rate limits per token independently\n\nPHASE 3: DETAILED DATA COLLECTION - HYBRID API STRATEGY (4-6\
  \ hours)\n\n3A. Commit History Collection (GraphQL - efficient for metadata):\n  Query structure:\n    query repoCommits($owner:\
  \ String!, $name: String!, $cursor: String) {\n      repository(owner: $owner, name: $name) {\n        defaultBranchRef\
  \ {\n          target {\n            ... on Commit {\n              history(first: 100, after: $cursor) {\n            \
  \    pageInfo { hasNextPage, endCursor }\n                edges {\n                  node {\n                    oid, messageHeadline,\
  \ committedDate, pushedDate\n                    author { user { login, id }, name, email }\n                    committer\
  \ { user { login, id }, name, email }\n                    changedFiles, additions, deletions\n                    parents(first:\
  \ 1) { edges { node { oid } } }\n                  }\n                }\n              }\n            }\n          }\n \
  \       }\n      }\n    }\n  Pagination: Collect ALL commits (may be 1000+ for large repos)\n  Optimization: Stop after\
  \ 500 commits if repo is very active (sample most recent)\n  Date filtering: Only collect commits from repo creation to\
  \ 2024-01-01 (cutoff for analysis)\n\n3B. File Modification Data Collection (REST - required for file names):\n  PRIMARY\
  \ METHOD: GET /repos/{owner}/{repo}/commits?sha={branch}&per_page=100&since={date}\n  Returns: array of commits with files\
  \ array containing filename, status, additions, deletions\n  \n  SECONDARY METHOD (if primary fails): GET /repos/{owner}/{repo}/commits/{sha}\n\
  \  Returns: single commit with complete file diff information\n  \n  TERTIARY METHOD (bulk): Use Git Trees API\n  GET /repos/{owner}/{repo}/git/trees/{sha}?recursive=1\n\
  \  Then cross-reference with commit list to infer modifications (less accurate)\n  \n  File path normalization:\n  - Convert\
  \ all paths to relative, lowercase for comparison\n  - Handle renames: track rename detection from commit data (status:\
  \ 'renamed')\n  - Handle deletions: keep in contributor's file set as 'previously modified'\n  - Directory extraction: also\
  \ compute directory-level modifications (parent dir of each file)\n\n3C. Contributor Metadata Collection:\n  GraphQL: repository(owner:\
  \ $owner, name: $name) { collaborators(first: 100) { edges { node { login, id, ... } } } }\n  REST: GET /repos/{owner}/{repo}/contributors?per_page=100\n\
  \  Note: GitHub API only returns top 500 contributors, paginate if needed\n  Affiliation: distinguish between 'owner', 'member',\
  \ 'contributor' if possible\n\nPHASE 4: FOUNDER IDENTIFICATION - MULTI-HEURISTIC APPROACH (1 hour)\n\nHeuristic 1 - First\
  \ Committer Method:\n  - Sort all commits by date ascending\n  - Founder = author of first commit (or first 5 commits if\
  \ first is bot)\n  - Confidence: HIGH if first commit is within 7 days of repo creation\n\nHeuristic 2 - Early Period Dominance\
  \ Method:\n  - Define early period: first 90 days after repo creation\n  - Count commits per author in early period\n  -\
  \ Founder = author with most commits in early period\n  - Confidence: HIGH if >50% of early commits, MEDIUM if 30-50%, LOW\
  \ if <30%\n\nHeuristic 3 - Owner Account Method:\n  - If repo owner is a user (not org), check if owner appears in contributors\n\
  \  - If yes and has commits in first 30 days, likely founder\n  - Confidence: MEDIUM (owner may have transferred repo)\n\
  \nHeuristic 4 - Repository Description / README Parsing:\n  - Parse repo description and README for phrases like 'Created\
  \ by', 'Author:', etc.\n  - Use regex: r'(?:created|authored|written|developed)\\s+(?:by\\s+)?@?(\\w+)'\n  - Confidence:\
  \ LOW (unreliable, use only as tiebreaker)\n\nHeuristic 5 - GitHub Organization Membership:\n  - If repo owned by org, check\
  \ org members for early contributors\n  - May not identify individual founder if org-created\n  - Confidence: LOW (often\
  \ team effort)\n\nFINAL FOUNDER SELECTION ALGORITHM:\n  def identify_founder(commits, repo_metadata):\n      methods = [\n\
  \          ('first_committer', heuristic1(commits)),\n          ('early_dominance', heuristic2(commits)),\n          ('owner_account',\
  \ heuristic3(repo_metadata, commits))\n      ]\n      # Weight by confidence\n      scores = {}\n      for method, (candidate,\
  \ confidence) in methods:\n          weight = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}[confidence]\n          scores[candidate]\
  \ = scores.get(candidate, 0) + weight\n      \n      # Return highest scoring candidate\n      founder = max(scores, key=scores.get)\n\
  \      \n      # Determine departure\n      founder_commits = [c for c in commits if c.author == founder]\n      last_commit\
  \ = max(c.committedDate for c in founder_commits)\n      \n      # Check 12+ months inactivity\n      cutoff_date = last_commit\
  \ + timedelta(days=365)\n      recent_commits = [c for c in commits if c.committedDate > cutoff_date]\n      \n      departed\
  \ = len(recent_commits) == 0\n      departure_date = last_commit if departed else None\n      \n      return founder, departure_date,\
  \ departed\n\nPHASE 5: KNOWLEDGE REDUNDANCY COMPUTATION - MULTIPLE METRICS (1 hour)\n\n5A. Jaccard Similarity (Primary Metric):\n\
  \  Definition: J(A,B) = |A ∩ B| / |A ∪ B|\n  Where A and B are sets of files modified by contributors A and B\n  \n  Implementation:\n\
  \  def compute_jaccard_redundancy(contributor_files):\n      '''\n      contributor_files: dict {contributor_login: set(file_paths)}\n\
  \      Returns: average pairwise Jaccard similarity (float 0-1)\n      '''\n      import itertools\n      from statistics\
  \ import mean\n      \n      contributors = list(contributor_files.keys())\n      if len(contributors) < 2:\n          return\
  \ 0.0\n      \n      similarities = []\n      for c1, c2 in itertools.combinations(contributors, 2):\n          files1 =\
  \ contributor_files[c1]\n          files2 = contributor_files[c2]\n          \n          if not files1 or not files2:\n\
  \              continue\n          \n          intersection = len(files1 & files2)\n          union = len(files1 | files2)\n\
  \          \n          if union > 0:\n              jaccard = intersection / union\n              similarities.append(jaccard)\n\
  \      \n      return mean(similarities) if similarities else 0.0\n\n5B. Directory-Level Jaccard (Secondary Metric):\n \
  \ - Extract directory paths from file paths (e.g., 'src/main.py' -> 'src/')\n  - Compute Jaccard on directory sets to capture\
  \ module-level redundancy\n  - May be more stable than file-level for large repos\n\n5C. Overlap Coefficient (Alternative\
  \ Metric):\n  Definition: O(A,B) = |A ∩ B| / min(|A|, |B|)\n  - More sensitive to small file sets\n  - Range: 0-1, where\
  \ 1 means one contributor's files are subset of other's\n\n5D. Contributor Filtering:\n  - Include only contributors with\
  \ 5+ commits (filter out one-time contributors)\n  - Exclude bot accounts (detect via login patterns: 'bot', '[bot]', 'dependabot',\
  \ etc.)\n  - Exclude merge commits from file modification counts\n  - Weight by commit frequency: weight = log(1 + commit_count)\
  \ to reduce outlier influence\n\nPHASE 6: SURVIVAL MEASUREMENT - MULTI-METRIC APPROACH (1 hour)\n\n6A. Survival Definition\
  \ (Primary):\n  Binary outcome: survived_12mo = 1 if project has ≥1 commit/month average in 12 months post-departure\n \
  \ Comparison: post_departure_rate ≥ 0.25 × pre_departure_rate\n  Pre-departure baseline: 6 months immediately before departure\n\
  \  \n  def measure_survival_binary(commits, departure_date):\n      if not departure_date:\n          return None\n    \
  \  \n      # Pre-departure period (6 months before)\n      pre_start = departure_date - timedelta(days=180)\n      pre_commits\
  \ = [c for c in commits \n                     if pre_start <= c.committedDate <= departure_date]\n      pre_rate = len(pre_commits)\
  \ / 6.0  # commits per month\n      \n      # Post-departure period (12 months after)\n      post_start = departure_date\n\
  \      post_end = departure_date + timedelta(days=365)\n      post_commits = [c for c in commits \n                    \
  \ if post_start <= c.committedDate <= post_end]\n      post_rate = len(post_commits) / 12.0\n      \n      # Binary survival\n\
  \      survived = post_rate >= (pre_rate * 0.25)\n      \n      return {\n          'survived_12mo': survived,\n       \
  \   'pre_rate': pre_rate,\n          'post_rate': post_rate,\n          'post_commits_12mo': len(post_commits)\n      }\n\
  \n6B. Continuous Survival Score (Secondary):\n  survival_score = min(1.0, post_rate / pre_rate) if pre_rate > 0 else 0.0\n\
  \  - Captures degree of survival, not just binary outcome\n  - Allows for regression analysis with continuous dependent\
  \ variable\n\n6C. Alternative Survival Metrics:\n  - Release-based: survived if ≥1 release in 12 months post-departure\n\
  \  - Issue-based: survived if ≥1 issue resolved in 12 months post-departure\n  - Hybrid: survived if any of commit/release/issue\
  \ activity\n\n6D. Censoring Handling:\n  - If departure_date is within 12 months of data collection, censor (mark as 'ongoing')\n\
  \  - If repo is archived, mark as 'archived' (definite non-survival)\n  - If repo has commits but very low rate, mark as\
  \ 'declining' (intermediate category)\n\nPHASE 7: CONTROL VARIABLE COMPUTATION (1 hour)\n\n7A. Bus Factor Calculation:\n\
  \  - Sort contributors by number of unique files modified (descending)\n  - Bus factor = smallest k such that top k contributors\
  \ modify >50% of all files\n  - Alternative: Truck factor algorithm (Avelino et al. 2016)\n\n7B. Project Age & Growth:\n\
  \  - age_days = collection_date - creation_date\n  - commits_per_day = total_commits / age_days\n  - stars_per_day = stargazers_count\
  \ / age_days\n  - contributor_growth_rate = (contributors_at_1yr - contributors_at_6mo) / 180\n\n7C. Code Ownership Metrics:\n\
  \  - Herfindahl index: H = Σ (contributor_commits / total_commits)²\n  - Gini coefficient of commit distribution among contributors\n\
  \  - Max contribution percentage: max_commits / total_commits\n\n7D. Language Ecosystem Controls:\n  - language_age = current_year\
  \ - language_creation_year\n  - language_popularity_rank (from TIOBE/RedMonk rankings)\n  - is_company_backed: detect from\
  \ owner (e.g., 'google', 'microsoft', 'facebook')\n\nPHASE 8: DATA VALIDATION, QUALITY CONTROL & EXPORT (1 hour)\n\n8A.\
  \ Schema Validation:\n  JSON schema definition (Draft 7):\n  {\n    \"$schema\": \"http://json-schema.org/draft-07/schema#\"\
  ,\n    \"title\": \"OSS Repository Data\",\n    \"type\": \"object\",\n    \"required\": [\"metadata\", \"repositories\"\
  ],\n    \"properties\": {\n      \"metadata\": { \"type\": \"object\", ... },\n      \"repositories\": {\n        \"type\"\
  : \"array\",\n        \"items\": {\n          \"type\": \"object\",\n          \"required\": [\"repo_id\", \"name\", \"\
  owner\", \"founder\", \"survival_outcome\", \"computed_metrics\"],\n          \"properties\": {\n            \"repo_id\"\
  : { \"type\": \"string\" },\n            \"knowledge_redundancy\": { \"type\": \"number\", \"minimum\": 0, \"maximum\":\
  \ 1 },\n            ...\n          }\n        }\n      }\n    }\n  }\n\n8B. Data Quality Checks:\n  def validate_repository(repo):\n\
  \      errors = []\n      warnings = []\n      \n      # Critical errors (exclude repo)\n      if not repo.get('founder',\
  \ {}).get('login'):\n          errors.append('No founder identified')\n      if repo.get('computed_metrics', {}).get('knowledge_redundancy')\
  \ is None:\n          errors.append('Knowledge redundancy not computable')\n      if len(repo.get('commits', [])) < 10:\n\
  \          errors.append('Too few commits (<10)')\n      \n      # Warnings (keep but flag)\n      if repo.get('survival_outcome',\
  \ {}).get('departure_date') is None:\n          warnings.append('Founder has not departed yet (censored)')\n      if len(repo.get('contributors',\
  \ [])) < 3:\n          warnings.append('Very few contributors (<3)')\n      \n      return errors, warnings\n\n8C. Outlier\
  \ Detection:\n  - Knowledge redundancy: flag if >3 standard deviations from mean\n  - Survival rate: flag if post-rate >\
  \ 10× pre-rate (anomaly)\n  - Contributor count: flag if >99th percentile (very large project)\n\n8D. Export Strategy:\n\
  \  - Primary: data_out.json (pretty-printed for readability)\n  - Compressed: data_out.json.gz (using gzip)\n  - Mini version:\
  \ mini_data_out.json (first 10 repos for testing)\n  - Metadata: data_out_metadata.json (summary statistics, collection\
  \ parameters)\n  - Schema: data_out_schema.json (JSON Schema for validation)\n\n  Export code:\n  import json, gzip\n  \n\
  \  # Main export\n  with open('data_out.json', 'w') as f:\n      json.dump(dataset, f, indent=2, default=str)\n  \n  # Compressed\n\
  \  with gzip.open('data_out.json.gz', 'wt') as f:\n      json.dump(dataset, f, default=str)\n  \n  # Check size\n  import\
  \ os\n  size_mb = os.path.getsize('data_out.json') / 1_000_000\n  if size_mb > 300:\n      print(f'WARNING: File size {size_mb:.1f}MB\
  \ exceeds 300MB limit')\n\nCOMPREHENSIVE FALLBACK STRATEGIES:\n\nFALLBACK 1 - API Rate Limit Exhaustion:\n  A. Multiple\
  \ Token Rotation: Prepare 5 GitHub tokens, rotate when limit reached\n  B. Reduce Scope: Collect 500 repos instead of 1000\
  \ (maintain stratification)\n  C. Use GitHub Archive via BigQuery: \n     - Query: SELECT repo_name, actor_login, committed_date,\
  \ files FROM `githubarchive.day.20230101` ...\n     - Free tier: 1TB/month query, sufficient for this analysis\n     - Requires\
  \ Google Cloud account setup\n  D. Use GHTorrent MySQL Dump:\n     - Download: http://ghtorrent.org/downloads.html\n   \
  \  - Last updated: ~2020, may be acceptable if hypothesis test is not time-sensitive\n     - Requires MySQL server setup\
  \ and ~100GB disk space\n\nFALLBACK 2 - File Modification Data Too Expensive:\n  A. Approximate from Commit Messages: Parse\
  \ file paths from commit messages (70% accuracy)\n  B. Sample Commits: Collect file data for only 25% of commits per repo\
  \ (systematic sample)\n  C. Use Directory-Level Only: Skip file-level, use directory modifications (less granular)\n  D.\
  \ Infer from Blame Data: Use git blame to determine file authorship (alternative approach)\n\nFALLBACK 3 - Founder Identification\
  \ Unclear:\n  A. Use Multiple Heuristics: Combine 3+ heuristics, use majority vote\n  B. Manual Review Sample: Flag 50 ambiguous\
  \ cases, manually review via web UI\n  C. Exclude Uncertain: Drop repos where confidence is LOW for all heuristics\n  D.\
  \ Sensitivity Analysis: Run analysis with/without ambiguous cases, check robustness\n\nFALLBACK 4 - Knowledge Redundancy\
  \ Computation Fails:\n  A. Use Commit Overlap: If file data missing, use commit timestamp overlap as proxy\n  B. Use Code\
  \ Review Data: If available, use PR reviewer assignments as proxy for expertise\n  C. Use Issue Assignment: Use issue assignee\
  \ data to infer contributor focus areas\n  D. Skip Metric: Mark as null, use only repos with computable redundancy\n\nFALLBACK\
  \ 5 - Survival Measurement Problematic:\n  A. Extend Window: Use 24-month post-departure if 12-month is noisy\n  B. Use\
  \ Multiple Metrics: Combine commit + release + issue metrics\n  C. Censor Appropriately: Mark repos with insufficient post-departure\
  \ data as censored\n  D. Use Time-Varying Survival: Kaplan-Meier curve instead of binary outcome\n\nEDGE CASES & SPECIAL\
  \ HANDLING:\n\n1. Monorepos: Google/Facebook style repos with multiple projects\n   - Detect via: >10000 files, >1000 contributors,\
  \ very high commit rate\n   - Handle via: exclude or analyze subprojects separately (complex)\n\n2. Bot-Heavy Repositories:\
  \ Automated commits (dependabot, CI bots)\n   - Detect via: login contains 'bot', '[bot]', or known bot accounts\n   - Handle\
  \ via: exclude bot commits from file modification analysis\n\n3. Corporate/Organization Repositories: Multiple founders,\
  \ team-based\n   - Detect via: owner is organization, not user\n   - Handle via: identify 'core team' (top 5 contributors)\
  \ instead of single founder\n\n4. Forked Repositories with Substantial Changes:\n   - Detect via: is_fork=true but >500\
  \ commits after fork, different primary language\n   - Handle via: analyze fork as independent project (exclude parent)\n\
  \n5. Archived Repositories:\n   - Detect via: archived=true field from GitHub API\n   - Handle via: mark as 'definite non-survival'\
  \ if archived post-departure\n\n6. Renamed/Migrated Repositories:\n   - Detect via: repository has 'parent' or 'source'\
  \ field pointing elsewhere\n   - Handle via: follow redirects, collect data from current URL\n\n7. Repositories with Very\
  \ Large Histories (>10000 commits):\n   - Handle via: sample 1000 most recent commits, document sampling method\n   - Alternative:\
  \ use Git API with shallow clone (not possible via GitHub API)\n\n8. Repositories with Force Pushes (rewritten history):\n\
  \   - Detect via: missing commits, non-linear history with gaps\n   - Handle via: flag as 'history may be incomplete', use\
  \ available data\n\n9. Multi-Language Repositories:\n   - Detect via: primary_language is null or multiple languages in\
  \ top 10 files\n   - Handle via: assign to 'primary' language based on file count, create 'mixed' category\n\n10. Repositories\
  \ with Binary Files (images, data):\n    - Handle via: exclude binary files from file modification sets (detect via extension)\n\
  \    - Extensions to exclude: .png, .jpg, .gif, .pdf, .zip, .tar, .dat, .bin\n\nPERFORMANCE OPTIMIZATION:\n\n1. Parallel\
  \ API Requests:\n   - Use asyncio with aiohttp for REST API calls (respect rate limits)\n   - Use threading for GraphQL\
  \ queries (Python GIL less relevant for I/O bound)\n   - Max 5 concurrent requests to avoid secondary rate limits\n\n2.\
  \ Caching Strategy:\n   - Cache commit data per repo: save after every 100 commits collected\n   - Cache intermediate results:\
  \ save progress every 10 repos\n   - Resume capability: if script crashes, resume from last saved state\n\n3. Memory Management:\n\
  \   - Stream large repos: don't load all commits into memory at once\n   - Use generators for file processing\n   - Delete\
  \ raw API responses after parsing\n\n4. Request Batching:\n   - GraphQL: batch multiple repo queries in one request (if\
  \ using aliases)\n   - REST: use ?per_page=100 to minimize requests\n   - Use conditional requests (ETag) to avoid re-fetching\
  \ unchanged data\n\nLEGAL & ETHICAL CONSIDERATIONS:\n\n1. Terms of Service Compliance:\n   - GitHub ToS: https://docs.github.com/en/site-policy/github-terms-of-service\n\
  \   - API ToS: https://docs.github.com/en/site-policy/github-acceptable-use-policies\n   - Rate limiting: respect all rate\
  \ limits and secondary rate limits\n   - Scraping: use official API only, no HTML scraping\n\n2. Data Privacy:\n   - Only\
  \ collect public repository data (no private repos)\n   - No personal data beyond public GitHub profile (login, name, avatar)\n\
  \   - No email addresses in final dataset (hash or remove)\n   - Comply with GDPR: right to deletion (if contributor requests)\n\
  \n3. Research Ethics:\n   - Data used for research purposes only\n   - No commercial use of collected data\n   - Attribute\
  \ GitHub as data source\n   - Consider publishing dataset with anonymization\n\n4. Attribution Requirements:\n   - Include\
  \ 'Data collected from GitHub API' in dataset metadata\n   - Link to GitHub API terms in documentation\n   - Consider CC-BY-SA\
  \ license for derived dataset\n\nSTATISTICAL CONSIDERATIONS:\n\n1. Sample Size Calculation:\n   - Power analysis: n=1000\
  \ provides 80% power to detect OR=1.5 in logistic regression\n   - Effect size: expect medium effect (Cohen's h ≈ 0.3) based\
  \ on prior literature\n   - Alpha=0.05, two-tailed test\n   - Adjust for 20% attrition: collect n=1250 to get n=1000 final\n\
  \n2. Stratified Sampling Validation:\n   - Verify strata are balanced: χ² test for language × survival contingency table\n\
  \   - Check for selection bias: compare collected sample to GitHub population (stars, age)\n\n3. Missing Data Handling:\n\
  \   - Type: MAR (Missing At Random) - assume missingness independent of survival\n   - Approach: listwise deletion if <10%\
  \ missing, multiple imputation if >10%\n   - Document: report % missing for each variable in final paper\n\n4. Confounding\
  \ Control:\n   - Measure all known confounders: project age, size, popularity, language\n   - Statistical control: include\
  \ as covariates in Cox model\n   - Sensitivity analysis: check if results hold without controls\n\nEXPECTED CHALLENGES &\
  \ SOLUTIONS:\n\nChallenge 1: GitHub API returns incomplete file data for large commits\n  Solution: Use REST API commit\
  \ detail endpoint (slower but complete)\n  Fallback: Sample files if commit has >50 files changed\n\nChallenge 2: Founder\
  \ departure date is ambiguous (sporadic commits)\n  Solution: Use 12-month window with no commits, not single date\n  Alternative:\
  \ use 'last meaningful commit' (excluding merges, bot commits)\n\nChallenge 3: Knowledge redundancy is correlated with bus\
  \ factor\n  Solution: This is expected! Control for bus factor in regression\n  Analysis: Check VIF (Variance Inflation\
  \ Factor) for multicollinearity\n\nChallenge 4: Some repos have very sparse commit data (git commits only)\n  Solution:\
  \ Exclude repos with <50 commits total\n  Alternative: use issue/PR data as proxy for activity\n\nChallenge 5: Time zone\
  \ handling in commit dates\n  Solution: Use ISO 8601 format from API, convert to UTC\n  Note: GitHub API returns dates in\
  \ ISO 8601 with timezone\n\nDELIVERABLES CHECKLIST:\n\n✓ data_out.json - Main dataset (<300MB)\n✓ data_out.json.gz - Compressed\
  \ version\n✓ data_out_schema.json - JSON Schema for validation\n✓ data_out_metadata.json - Collection parameters and summary\
  \ statistics\n✓ mini_data_out.json - 10-repo sample for testing\n✓ scripts/collect_data.py - Complete collection script\
  \ with all phases\n✓ scripts/validate_data.py - Validation and quality check script\n✓ scripts/compute_metrics.py - Redundancy\
  \ and survival computation\n✓ NOTES.md - Deviations from plan, known issues, assumptions\n✓ README.md - Dataset documentation,\
  \ schema description, usage examples\n\nVALIDATION CHECKLIST (Executor Must Complete):\n\n□ All 1000+ repos collected with\
  \ complete data\n□ JSON schema validation passes (100% of repos)\n□ File size <300MB (or document if larger with justification)\n\
  □ Knowledge redundancy computed for >90% of repos\n□ Founder departure identified for >80% of repos\n□ Survival outcome\
  \ determined for >80% of repos with departure\n□ Summary statistics computed and saved in metadata\n□ 10 repos spot-checked\
  \ manually for accuracy\n□ All GitHub API rate limits respected (no 403/429 errors in final run)\n□ Fallback strategies\
  \ documented if used\n□ Edge cases handled and documented\n□ Legal/ethical compliance verified\n\nThis exhaustive plan provides\
  \ multiple pathways to success, comprehensive error handling, and detailed technical specifications for every step of the\
  \ data collection process."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [14] SYSTEM-USER prompt · 2026-08-21 16:37:55 UTC

```
<verification_failed>
Your dataset output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: data.py

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Use 'ls' to check what files exist, then create the missing ones.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files (data.py, full_data_out.json, preview_data_out.json, mini_data_out.json)

After making changes, verify:
- 'ls -la' shows all required files
- JSON files are valid (use aii-json skill validation)
- full_data_out.json has at least 50 examples
</task>
```

### [15] SYSTEM-USER prompt · 2026-08-21 16:39:28 UTC

```
<verification_failed>
Your dataset output failed verification (attempt 2/10).
</verification_failed>

<schema_errors>
JSON SCHEMA VALIDATION ERRORS:
  - full_data_out.json: Missing required 'datasets' key
  - mini_data_out.json: Missing required 'datasets' key
  - preview_data_out.json: Missing required 'datasets' key

Fix: Your JSON files must follow this datasets-grouped structure:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "metadata_feature_names": [...]
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields (e.g. metadata_fold, metadata_task_type).
     Read exp_sel_data_out.json schema in aii-json skill.
     Then update data.py and regenerate the output files.
</schema_errors>

<task>
FIX THESE ISSUES:
2. Fix JSON schema errors by updating data.py
3. Re-run data.py to regenerate all output files
4. Validate with aii-json skill: validate full_data_out.json against exp_sel_data_out schema

After making changes, verify:
- 'ls -la' shows all required files
- JSON files are valid (use aii-json skill validation)
- full_data_out.json has at least 50 examples
</task>
```
