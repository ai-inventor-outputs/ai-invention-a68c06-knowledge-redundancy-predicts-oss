# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `iter1_924aa01cf43b` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 15:08:48 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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
````

### [2] HUMAN-USER prompt · 2026-08-21 15:08:48 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-21 15:09:00 UTC

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

### [4] SKILL-INPUT — aii-hf-datasets · 2026-08-21 15:09:00 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-08-21 15:09:00 UTC

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

### [6] SKILL-INPUT — aii-json · 2026-08-21 15:09:00 UTC

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

### [7] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 15:09:18 UTC

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

### [8] SKILL-INPUT — aii-file-size-limit · 2026-08-21 15:09:18 UTC

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

### [9] SKILL-INPUT — aii-use-hardware · 2026-08-21 15:09:20 UTC

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

### [10] SKILL-INPUT — aii-parallel-computing · 2026-08-21 15:09:20 UTC

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

### [11] SYSTEM-USER prompt · 2026-08-21 15:13:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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

### [12] SYSTEM-USER prompt · 2026-08-21 15:14:54 UTC

```
be more exhaustive
```

### [13] SYSTEM-USER prompt · 2026-08-21 15:17:00 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [14] SYSTEM-USER prompt · 2026-08-21 15:28:47 UTC

````
<human_message>
be more exhaustive
</human_message>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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
````

### [15] HUMAN-USER prompt · 2026-08-21 15:28:47 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [16] SYSTEM-USER prompt · 2026-08-21 15:40:52 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<human_message>
be more exhaustive
</human_message>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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

What determines whether an open-source project survives its founder stepping away?
````

### [17] SYSTEM-USER prompt · 2026-08-21 15:51:01 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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

### [18] SYSTEM-USER prompt · 2026-08-21 15:52:56 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: GitHub OSS survival dataset collection plan
summary: >-
  Collect GitHub data for 1000-1500 OSS projects to measure knowledge redundancy and founder departure survival using GitHub
  API with PyGithub.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) 2000+ GitHub repositories with 100+ stars and 2+ years of activity, (2) Complete commit
  histories with author information, timestamps, and file modifications, (3) Identified founders (primary initial contributors)
  and their departure dates (12+ months inactivity), (4) Pre/post-departure activity metrics, (5) Repository metadata (stars,
  forks, language, creation date), (6) All data stored in JSON format under 300MB. The dataset should enable computation of
  knowledge redundancy (Jaccard similarity of file modification patterns among top contributors) and survival outcomes (continued
  activity after founder departure).
dataset_search_plan: "## EXECUTIVE SUMMARY\n\nCollect GitHub repository data to measure knowledge redundancy, founder departure,\
  \ and post-departure survival. Target: 1000-1500 repositories (revised down from 2000 for feasibility), with complete commit\
  \ histories and computed metrics. Use GitHub REST API via PyGithub for simplicity; GraphQL only if optimization needed.\n\
  \n## PHASE 1: SEARCH FOR EXISTING DATASETS (1 hour)\n\nSearch HuggingFace Hub and academic repositories for pre-collected\
  \ GitHub data:\n\n1. **HuggingFace Hub Search**:\n   - Search queries: 'github', 'open source', 'software repository', 'github\
  \ commits', 'oss projects'\n   - Specific datasets to check:\n     - 'software-heritage/swh-dataset' (massive, may be too\
  \ large)\n     - Search for: 'ghtorrent', 'github-archive', 'world-of-code'\n   - Use aii-hf-datasets skill to search and\
  \ preview\n\n2. **Academic Dataset Repositories**:\n   - Harvard Dataverse: Search 'open source survival', 'bus factor',\
  \ 'github dataset'\n   - Zenodo: Search 'github repository data', 'oss mining'\n   - Papers with Code: Check datasets for\
  \ 'Avelino et al. 2019', 'Cosentino et al. 2016'\n   - GHTorrent project (ghtorrent.org): Download MySQL dump or CSV exports\n\
  \   - World of Code (woc.com): Research dataset with GitHub commit history\n\n3. **Evaluate Found Datasets**:\n   - Check\
  \ if commit-level data with file modifications is included\n   - Check date range (need projects active 2020-2024)\n   -\
  \ Check if founder/departure data already computed\n   - If suitable dataset found: download, transform to required schema,\
  \ skip Phase 2\n\n## PHASE 2: API-BASED DATA COLLECTION (4-5 hours if no existing dataset)\n\n### PREREQUISITES\n- **GitHub\
  \ Token**: Set GITHUB_TOKEN environment variable\n  - Create at: https://github.com/settings/tokens/new\n  - Select scope:\
  \ 'public_repo' (minimum) or 'repo' (full)\n  - Without token: 60 requests/hour (insufficient); With token: 5000 requests/hour\n\
  - **Python packages**: `pip install PyGithub pandas numpy tqdm`\n- **Rate limit strategy**: 5000 req/hour = 1.4 req/sec;\
  \ implement sleep(0.8) between requests\n\n### STEP 1: Project Discovery (45 minutes)\n**Goal**: Identify 1500 candidate\
  \ repositories\n\nUse GitHub Search API via PyGithub:\n```python\nfrom github import Github\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Search queries - execute in parallel\nqueries = [\n    'stars:>=100 created:<2022-01-01 language:python',\n    'stars:>=100\
  \ created:<2022-01-01 language:javascript', \n    'stars:>=100 created:<2022-01-01 language:java',\n    'stars:>=100 created:<2022-01-01\
  \ language:go',\n    'stars:>=100 created:<2022-01-01 language:rust',\n    'stars:>=100 created:<2022-01-01 language:typescript',\n\
  \    'stars:>=100 created:<2022-01-01 language:c++',\n    'stars:>=100 created:<2022-01-01 language:ruby'\n]\n\nrepos =\
  \ []\nfor query in queries:\n    results = g.search_repositories(query=query, sort='stars', order='desc')\n    for repo\
  \ in results[:200]:  # Top 200 per language\n        repos.append({\n            'full_name': repo.full_name,\n        \
  \    'stars': repo.stargazers_count,\n            'language': repo.language,\n            'created_at': repo.created_at.isoformat(),\n\
  \            'default_branch': repo.default_branch\n        })\n```\n\nDeduplicate and save candidate list as `candidates.json`.\n\
  \n### STEP 2: Repository Validation (30 minutes)\n**Goal**: Filter to 1000-1200 high-quality repositories\n\nFor each candidate,\
  \ verify via API:\n- Has >= 50 commits (use `repo.get_commits().totalCount`)\n- Has >= 3 contributors (use `repo.get_contributors().totalCount`)\n\
  - Not archived (check `repo.archived`)\n- Activity spans >= 24 months (check first and last commit dates)\n\nSave validated\
  \ list as `validated_repos.json`.\n\n### STEP 3: Commit History Collection (2.5 hours - MOST CRITICAL)\n**Goal**: Collect\
  \ commit data for all validated repos\n\n**Optimization Strategy**:\n- Collect commits page by page (100 per page max via\
  \ API)\n- Store only essential fields to minimize size\n- Use checkpoints: save progress every 100 repos\n\n**Implementation**:\n\
  ```python\nimport json\nfrom github import Github\nfrom datetime import datetime, timedelta\nimport time\n\ng = Github(os.environ['GITHUB_TOKEN'])\n\
  \n# Load validated repos\nwith open('validated_repos.json') as f:\n    repos = json.load(f)\n\ncollected_data = []\n\nfor\
  \ i, repo_info in enumerate(repos):\n    try:\n        repo = g.get_repo(repo_info['full_name'])\n        \n        # Get\
  \ commits (paginated)\n        commits = repo.get_commits()\n        commit_data = []\n        \n        # LIMIT: Collect\
  \ max 300 commits per repo to stay under size limit\n        # Prioritize: last 300 commits (most relevant for recent activity)\n\
  \        commit_list = list(commits)[:300]  # This is still slow; see optimization below\n        \n        for commit in\
  \ commit_list:\n            if commit.author:\n                commit_data.append({\n                    'sha': commit.sha,\n\
  \                    'author': commit.author.login if commit.author else None,\n                    'date': commit.commit.author.date.isoformat(),\n\
  \                    'files': [f.filename for f in commit.files] if commit.files else [],\n                    'additions':\
  \ commit.stats.additions if commit.stats else 0,\n                    'deletions': commit.stats.deletions if commit.stats\
  \ else 0\n                })\n        \n        collected_data.append({\n            'repo_id': repo_info['full_name'],\n\
  \            'metadata': {\n                'stars': repo.stargazers_count,\n                'language': repo.language,\n\
  \                'created_date': repo.created_at.isoformat(),\n                'total_commits': commits.totalCount\n   \
  \         },\n            'commits': commit_data\n        })\n        \n        # Rate limiting: 0.8 sec between repos\n\
  \        time.sleep(0.8)\n        \n        # Checkpoint every 50 repos\n        if i % 50 == 0:\n            with open(f'checkpoint_{i}.json',\
  \ 'w') as f:\n                json.dump(collected_data, f)\n            print(f'Checkpoint: {i} repos collected')\n    \
  \        \n    except Exception as e:\n        print(f'Error collecting {repo_info[\"full_name\"]}: {e}')\n        continue\n\
  ```\n\n**CRITICAL OPTIMIZATION - Sample Commits**:\n- Do NOT collect all commits for repos with 1000+ commits\n- Strategy:\
  \ Collect 300 commits distributed across project history:\n  - First 50 commits (founder period)\n  - Last 200 commits (recent\
  \ activity)\n  - Sample 50 commits from middle (random sample)\n- This reduces API calls while preserving data needed for\
  \ analysis\n\n### STEP 4: Founder Identification (30 minutes)\n**Goal**: Identify founder for each repository\n\nDefine\
  \ founder as:\n1. Contributor with most commits in first 6 months of project, OR\n2. First committer in project history,\
  \ OR  \n3. Repository owner (if available via `repo.owner`)\n\n```python\ndef identify_founder(repo_data):\n    commits\
  \ = repo_data['commits']\n    repo_created = datetime.fromisoformat(repo_data['metadata']['created_date'])\n    six_months_later\
  \ = repo_created + timedelta(days=180)\n    \n    # Count commits per author in first 6 months\n    author_commits = {}\n\
  \    for commit in commits:\n        commit_date = datetime.fromisoformat(commit['date'])\n        if commit_date <= six_months_later\
  \ and commit['author']:\n            author_commits[commit['author']] = author_commits.get(commit['author'], 0) + 1\n  \
  \  \n    if author_commits:\n        founder = max(author_commits, key=author_commits.get)\n        return founder\n   \
  \ return None\n```\n\n### STEP 5: Departure Detection (30 minutes)\n**Goal**: Identify founder departure events\n\n```python\n\
  def detect_departure(repo_data, founder):\n    if not founder:\n        return None\n    \n    founder_commits = [c for\
  \ c in repo_data['commits'] if c['author'] == founder]\n    if not founder_commits:\n        return None\n    \n    last_commit_date\
  \ = max(datetime.fromisoformat(c['date']) for c in founder_commits)\n    now = datetime.now()\n    \n    # Departure = 12+\
  \ months since last commit\n    if (now - last_commit_date).days >= 365:\n        return {\n            'founder': founder,\n\
  \            'departure_date': last_commit_date.isoformat(),\n            'is_departed': True\n        }\n    else:\n  \
  \      return {\n            'founder': founder,\n            'departure_date': None,\n            'is_departed': False\n\
  \        }\n```\n\n### STEP 6: Activity Metrics & Survival (45 minutes)\n**Goal**: Compute pre/post departure activity and\
  \ survival status\n\n```python\ndef compute_survival_metrics(repo_data, departure_info):\n    if not departure_info or not\
  \ departure_info['is_departed']:\n        return {'has_departure': False}\n    \n    departure_date = datetime.fromisoformat(departure_info['departure_date'])\n\
  \    \n    # Pre-departure: 12 months before departure\n    pre_start = departure_date - timedelta(days=365)\n    pre_commits\
  \ = [c for c in repo_data['commits'] \n                   if pre_start <= datetime.fromisoformat(c['date']) <= departure_date]\n\
  \    \n    # Post-departure: 12 months after departure  \n    post_end = departure_date + timedelta(days=365)\n    post_commits\
  \ = [c for c in repo_data['commits']\n                    if departure_date <= datetime.fromisoformat(c['date']) <= post_end]\n\
  \    \n    pre_rate = len(pre_commits) / 12.0  # commits per month\n    post_rate = len(post_commits) / 12.0\n    \n   \
  \ # Survival: post-departure activity >= 50% of pre-departure\n    survival_status = 'survived' if post_rate >= (pre_rate\
  \ * 0.5) else 'died'\n    \n    return {\n        'has_departure': True,\n        'pre_departure_commits_per_month': pre_rate,\n\
  \        'post_departure_commits_per_month': post_rate,\n        'survival_status': survival_status,\n        'months_observed_post':\
  \ min(12, len(post_commits) // 30)  # Approximate\n    }\n```\n\n### STEP 7: Knowledge Redundancy (45 minutes)\n**Goal**:\
  \ Compute pairwise Jaccard similarity among top contributors\n\n```python\nfrom itertools import combinations\n\ndef compute_knowledge_redundancy(repo_data,\
  \ top_n=5):\n    # Get top contributors by commit count\n    author_counts = {}\n    for commit in repo_data['commits']:\n\
  \        if commit['author']:\n            author_counts[commit['author']] = author_counts.get(commit['author'], 0) + 1\n\
  \    \n    top_contributors = sorted(author_counts, key=author_counts.get, reverse=True)[:top_n]\n    \n    # Get file sets\
  \ for each contributor\n    contributor_files = {}\n    for author in top_contributors:\n        files = set()\n       \
  \ for commit in repo_data['commits']:\n            if commit['author'] == author:\n                files.update(commit['files'])\n\
  \        contributor_files[author] = files\n    \n    # Compute pairwise Jaccard similarity\n    jaccard_scores = []\n \
  \   for a, b in combinations(top_contributors, 2):\n        intersection = len(contributor_files[a] & contributor_files[b])\n\
  \        union = len(contributor_files[a] | contributor_files[b])\n        if union > 0:\n            jaccard_scores.append(intersection\
  \ / union)\n    \n    redundancy_score = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0\n    \n    return\
  \ {\n        'top_contributors': top_contributors,\n        'pairwise_jaccard_scores': jaccard_scores,\n        'redundancy_score':\
  \ redundancy_score\n    }\n```\n\n### STEP 8: Final Assembly & Size Check (30 minutes)\n**Goal**: Assemble final dataset\
  \ under 300MB\n\n```python\n# Assemble final dataset\nfinal_dataset = []\nfor repo_data in collected_data:\n    # Compute\
  \ all metrics\n    founder = identify_founder(repo_data)\n    departure = detect_departure(repo_data, founder)\n    survival\
  \ = compute_survival_metrics(repo_data, departure)\n    redundancy = compute_knowledge_redundancy(repo_data)\n    \n   \
  \ # Build output record (MINIMIZE FIELDS for size)\n    output = {\n        'repo_id': repo_data['repo_id'],\n        'metadata':\
  \ repo_data['metadata'],\n        'founder': departure,\n        'survival': survival,\n        'knowledge_redundancy':\
  \ redundancy,\n        # Store only 100 most recent commits to save space\n        'commits_sample': repo_data['commits'][-100:]\n\
  \    }\n    final_dataset.append(output)\n\n# Save with size check\nwith open('data_out.json', 'w') as f:\n    json.dump(final_dataset,\
  \ f)\n\nimport os\nfile_size = os.path.getsize('data_out.json') / (1024 * 1024)  # MB\nprint(f'Dataset size: {file_size:.2f}\
  \ MB')\n\nif file_size > 300:\n    print('WARNING: Exceeds 300MB, reducing sample...')\n    # Reduce commits_sample to 50\
  \ per repo\n    for item in final_dataset:\n        item['commits_sample'] = item['commits_sample'][-50:]\n    with open('data_out.json',\
  \ 'w') as f:\n        json.dump(final_dataset, f)\n```\n\n## PHASE 3: FALLBACK PLANS\n\n### If Rate Limits Exceeded:\n1.\
  \ Implement exponential backoff with `time.sleep(60)` when rate limit hit\n2. Reduce target to 500 repos\n3. Use multiple\
  \ GitHub tokens (if available) rotating between requests\n\n### If 1000 Repos Not Achievable:\n1. Target 600 repos with\
  \ confirmed founder departures (~250 departures expected)\n2. Focus on most popular languages (Python, JavaScript, Java)\n\
  3. Use stratified sampling: ensure representation across star ranges (100-500, 500-2000, 2000+)\n\n### If GraphQL Needed\
  \ for Speed:\nUse this GraphQL query for batch commit collection:\n```graphql\nquery($owner: String!, $name: String!, $cursor:\
  \ String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n\
  \          history(first: 100, after: $cursor) {\n            edges {\n              node {\n                oid\n     \
  \           author { user { login } }\n                committedDate\n                changedFiles\n              }\n  \
  \          }\n            pageInfo { hasNextPage endCursor }\n          }\n        }\n      }\n    }\n  }\n}\n```\n\n##\
  \ VALIDATION CHECKLIST\n\nBefore finalizing, verify:\n- [ ] JSON is valid and parseable\n- [ ] File size < 300MB (check\
  \ with `ls -lh data_out.json`)\n- [ ] At least 400 repos with `has_departure: true`\n- [ ] At least 150 repos with `survival_status:\
  \ 'survived'`\n- [ ] No missing values in critical fields (repo_id, founder, survival)\n- [ ] Knowledge redundancy scores\
  \ are between 0 and 1\n- [ ] Spot-check 10 repos manually (verify founder, departure, survival)\n\n## EXPECTED OUTPUT FILES\n\
  \n1. **data_out.json**: Full dataset (< 300MB)\n2. **data_out_mini.json**: 10 randomly sampled repos (for development)\n\
  3. **data_out_preview.json**: 3 repos with first 3 commits only (for inspection)\n4. **collection_log.json**: Log of API\
  \ calls, errors, filtering stats\n5. **stats_summary.json**: Dataset statistics:\n   - Total repos collected\n   - Repos\
  \ with founder departure\n   - Survival rates (survived vs died)\n   - Distribution of knowledge redundancy scores\n   -\
  \ Average commits per repo\n\n## TIME BUDGET ALLOCATION (6 hours total)\n\n- Hour 1: Existing dataset search + Project discovery\n\
  - Hour 2-3: Repository validation + Commit collection (first 400 repos)\n- Hour 4: Continue commit collection (400-800 repos)\n\
  - Hour 5: Finish collection + Founder/Departure detection\n- Hour 6: Survival/Redundancy computation + Final assembly +\
  \ Validation\n\n## CRITICAL SUCCESS FACTORS\n\n1. **GitHub Token**: Must have valid token with 5000 req/hour limit\n2. **Rate\
  \ Limit Handling**: Implement `time.sleep(0.8)` between requests\n3. **Checkpointing**: Save progress every 50 repos to\
  \ avoid losing work\n4. **Size Management**: Limit commits per repo to 100-300, truncate fields\n5. **Error Handling**:\
  \ Catch exceptions per repo, continue to next\n6. **Validation**: Run validation checklist before declaring complete"
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````
