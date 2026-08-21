# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_rhx_UB8HZyTw` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 19:12:35 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Collect GitHub repo data for OSS survival study
summary: >-
  Collect commit histories, file modifications, and contributor metadata from 2000+ GitHub repositories to study knowledge
  redundancy and project survival after founder departure.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) Repository metadata (stars, forks, language, creation date, last push), (2) Complete
  commit histories with author information, timestamps, and file modifications, (3) Contributor lists with join dates and
  activity periods, (4) At least 2000 repositories with 100+ stars, 2+ years old, and recent activity, (5) Repositories with
  identifiable founders (original creators) and sufficient commit history to analyze founder departure events, (6) Data structured
  as JSON with one row per commit/file modification event including: repo_id, commit_hash, author_id, timestamp, files_modified,
  file_paths, commit_message, and repository metadata. The dataset should be comprehensive enough to compute knowledge redundancy
  metrics (Jaccard similarity of file modification patterns) and identify founder departure events (12+ months without commits
  after active period).
dataset_search_plan: "PHASE 1: Evaluate Existing Dataset Sources (1 hour)\n\n1.1 Check HuggingFace for pre-existing GitHub\
  \ datasets:\n   - Search HuggingFace Hub for datasets containing GitHub repository data, commit histories, or open-source\
  \ project metadata\n   - Keywords: 'github', 'repository', 'commit', 'open source', 'git', 'software engineering'\n   -\
  \ Promising candidates: GHTorrent dataset, GitHub Archive datasets, software repository mining datasets\n   - Preview top\
  \ 3 candidates to assess data structure and completeness\n   - If suitable dataset found with 2000+ repos and commit-level\
  \ data, download and proceed to Phase 4\n\n1.2 Check for GHTorrent or GHArchive bulk data:\n   - GHTorrent (http://ghtorrent.org/)\
  \ provides MySQL dumps of GitHub data\n   - GHArchive (https://www.gharchive.org/) provides hourly archives of GitHub events\n\
  \   - Assess if these can be queried/downloaded within time constraints\n   - Check if preprocessed versions exist on HuggingFace\
  \ or academic repositories\n\nPHASE 2: GitHub API Data Collection Strategy (2 hours preparation + 3 hours execution)\n\n\
  2.1 Authentication Setup:\n   - Use GitHub Personal Access Token (if available in environment) for 5000 requests/hour limit\n\
  \   - If no token: Implement request throttling for 60 requests/hour (unauthenticated)\n   - Calculate feasible collection\
  \ rate: ~5000 repos with full commit history per hour with authentication\n\n2.2 Repository Discovery:\n   - Search GitHub\
  \ API for repositories matching criteria:\n     * 100+ stars\n     * Created 2+ years ago (before 2024-08-20)\n     * Recently\
  \ active (push event within last 6 months)\n     * Primary language: Python, JavaScript, Java, Go, TypeScript, C++, Ruby\
  \ (popular OSS languages)\n   - Use search API: 'GET /search/repositories?q=stars:>100+created:<2024-08-20+pushed:>2024-02-20&sort=stars&order=desc&per_page=100'\n\
  \   - Paginate through results to collect 2000+ repo URLs\n\n2.3 Data Collection per Repository (parallelized):\n   For\
  \ each repository (implement with asyncio for parallelism):\n   a) Repository metadata: 'GET /repos/{owner}/{repo}'\n  \
  \    - Extract: name, owner, stars, forks, language, created_at, updated_at, default_branch, size\n   \n   b) Contributors\
  \ list: 'GET /repos/{owner}/{repo}/contributors?per_page=100'\n      - Extract: contributor login, contributions count,\
  \ avatar_url\n      - Identify founder: contributor with earliest commit or highest initial contribution\n   \n   c) Commit\
  \ history: 'GET /repos/{owner}/{repo}/commits?per_page=100&since={2_years_ago}'\n      - For each commit: extract sha, author,\
  \ committer, timestamp, message\n      - For commits by top 10 contributors: fetch detailed diff\n   \n   d) Commit details\
  \ with file modifications: 'GET /repos/{owner}/{repo}/commits/{sha}'\n      - Extract: files modified (filename, status,\
  \ additions, deletions)\n      - Only fetch for commits by top contributors to manage API budget\n   \n   e) Identify founder\
  \ departure:\n      - Sort commits by timestamp per contributor\n      - Founder = contributor with first commit or most\
  \ commits in first 6 months\n      - Departure = 12+ months gap in founder's commits after active period\n\n2.4 Incremental\
  \ Saving and Fault Tolerance:\n   - Save data in batches of 50 repositories\n   - Implement checkpointing: resume from last\
  \ saved batch\n   - Handle rate limiting: implement exponential backoff with 403/429 responses\n   - Log failed repositories\
  \ for retry\n\nPHASE 3: Data Structuring and Export (1 hour)\n\n3.1 Transform raw API responses to structured format:\n\
  \   Schema per row (commit/file modification event):\n   {\n     'repo_id': str,  # owner/repo\n     'repo_name': str,\n\
  \     'repo_owner': str,\n     'repo_stars': int,\n     'repo_forks': int,\n     'repo_language': str,\n     'repo_created':\
  \ str,  # ISO timestamp\n     'repo_last_push': str,\n     'commit_sha': str,\n     'commit_timestamp': str,\n     'author_login':\
  \ str,\n     'author_id': str,\n     'is_founder': bool,\n     'files_modified': list,  # list of filenames\n     'file_count':\
  \ int,\n     'commit_message': str,\n     'contributor_join_date': str,  # first commit by this author\n     'contributor_total_commits':\
  \ int\n   }\n\n3.2 Create aggregated views:\n   - Repository-level summary: repo metadata + founder info + contributor count\n\
  \   - Contributor-level summary: per-contributor file modification patterns\n   - Time-series view: monthly commit counts\
  \ per repo for survival analysis\n\n3.3 Export to JSON:\n   - Full dataset: 'github_repo_data_full.json' (all commit events)\n\
  \   - Mini dataset: 'github_repo_data_mini.json' (sample 100 repos)\n   - Preview: 'github_repo_data_preview.json' (5 repos,\
  \ truncated)\n   - Repository summary: 'github_repo_summary.json' (one row per repo)\n\nPHASE 4: Validation and Quality\
  \ Checks (30 minutes)\n\n4.1 Verify data completeness:\n   - Check that 2000+ repositories are collected\n   - Verify commit\
  \ histories span at least 2 years for survival analysis\n   - Ensure founder identification is possible for >80% of repos\n\
  \   - Check for data consistency (no missing critical fields)\n\n4.2 Compute preliminary metrics:\n   - Bus factor (minimal\
  \ set of contributors whose departure stops development)\n   - Knowledge redundancy (average pairwise Jaccard similarity\
  \ of file sets)\n   - Founder departure events (repos where founder inactive 12+ months)\n\n4.3 Handle edge cases:\n   -\
  \ Repositories with only 1 contributor (founder = only contributor)\n   - Repositories with no identifiable founder (created\
  \ by organization)\n   - Repositories with incomplete commit history (GitHub API limitations)\n   - Forked repositories\
  \ (exclude or mark appropriately)\n\nFALLBACK STRATEGIES:\n\nFallback 1: If GitHub API rate limit insufficient:\n   - Use\
  \ GitHub Archive (gharchive.org) data from BigQuery or downloaded files\n   - Query for repository events filtered by criteria\n\
  \   - Process JSON event files to extract commit and contributor data\n\nFallback 2: If full commit histories too large:\n\
  \   - Sample top 20 contributors per repository\n   - Collect only last 2 years of commit history\n   - Focus on file modification\
  \ patterns rather than full diffs\n\nFallback 3: If 2000 repos not feasible:\n   - Target 1000 repositories with more comprehensive\
  \ data\n   - Prioritize repositories with clear founder departure events\n   - Use stratified sampling across programming\
  \ languages\n\nTOOLS AND LIBRARIES:\n- PyGithub (github library for Python) OR direct requests to GitHub REST API\n- asyncio\
  \ for parallel API calls\n- pandas for data manipulation\n- json for data export\n- time/backoff for rate limiting\n- tqdm\
  \ for progress tracking\n\nEXECUTION TIMELINE (6 hours total):\n- Hour 1: Phase 1 (evaluate existing datasets)\n- Hour 2-3:\
  \ Phase 2 preparation (authentication, repo discovery)\n- Hour 3-5: Phase 2 execution (data collection with parallel API\
  \ calls)\n- Hour 5-6: Phase 3-4 (structuring, export, validation)\n\nCRITICAL SUCCESS FACTORS:\n1. Obtain GitHub token for\
  \ higher rate limits (5000 vs 60 requests/hour)\n2. Implement efficient parallelization (asyncio, not sequential requests)\n\
  3. Incremental saving to avoid losing progress\n4. Filter repositories early to focus on those with identifiable founders\n\
  5. Balance data completeness vs. API budget constraints"
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

### [2] HUMAN-USER prompt · 2026-08-20 19:12:35 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-20 19:12:49 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-20 19:12:49 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
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

### [5] SKILL-INPUT — aii-json · 2026-08-20 19:12:49 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
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

### [6] SKILL-INPUT — aii-hf-datasets · 2026-08-20 19:12:49 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
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

### [7] SKILL-INPUT — aii-parallel-computing · 2026-08-20 19:12:49 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
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

### [8] SKILL-INPUT — aii-web-tools · 2026-08-20 19:18:11 UTC

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

### [9] SYSTEM-USER prompt · 2026-08-20 19:26:23 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Collect GitHub repo data for OSS survival study
summary: >-
  Collect commit histories, file modifications, and contributor metadata from 2000+ GitHub repositories to study knowledge
  redundancy and project survival after founder departure.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) Repository metadata (stars, forks, language, creation date, last push), (2) Complete
  commit histories with author information, timestamps, and file modifications, (3) Contributor lists with join dates and
  activity periods, (4) At least 2000 repositories with 100+ stars, 2+ years old, and recent activity, (5) Repositories with
  identifiable founders (original creators) and sufficient commit history to analyze founder departure events, (6) Data structured
  as JSON with one row per commit/file modification event including: repo_id, commit_hash, author_id, timestamp, files_modified,
  file_paths, commit_message, and repository metadata. The dataset should be comprehensive enough to compute knowledge redundancy
  metrics (Jaccard similarity of file modification patterns) and identify founder departure events (12+ months without commits
  after active period).
dataset_search_plan: "PHASE 1: Evaluate Existing Dataset Sources (1 hour)\n\n1.1 Check HuggingFace for pre-existing GitHub\
  \ datasets:\n   - Search HuggingFace Hub for datasets containing GitHub repository data, commit histories, or open-source\
  \ project metadata\n   - Keywords: 'github', 'repository', 'commit', 'open source', 'git', 'software engineering'\n   -\
  \ Promising candidates: GHTorrent dataset, GitHub Archive datasets, software repository mining datasets\n   - Preview top\
  \ 3 candidates to assess data structure and completeness\n   - If suitable dataset found with 2000+ repos and commit-level\
  \ data, download and proceed to Phase 4\n\n1.2 Check for GHTorrent or GHArchive bulk data:\n   - GHTorrent (http://ghtorrent.org/)\
  \ provides MySQL dumps of GitHub data\n   - GHArchive (https://www.gharchive.org/) provides hourly archives of GitHub events\n\
  \   - Assess if these can be queried/downloaded within time constraints\n   - Check if preprocessed versions exist on HuggingFace\
  \ or academic repositories\n\nPHASE 2: GitHub API Data Collection Strategy (2 hours preparation + 3 hours execution)\n\n\
  2.1 Authentication Setup:\n   - Use GitHub Personal Access Token (if available in environment) for 5000 requests/hour limit\n\
  \   - If no token: Implement request throttling for 60 requests/hour (unauthenticated)\n   - Calculate feasible collection\
  \ rate: ~5000 repos with full commit history per hour with authentication\n\n2.2 Repository Discovery:\n   - Search GitHub\
  \ API for repositories matching criteria:\n     * 100+ stars\n     * Created 2+ years ago (before 2024-08-20)\n     * Recently\
  \ active (push event within last 6 months)\n     * Primary language: Python, JavaScript, Java, Go, TypeScript, C++, Ruby\
  \ (popular OSS languages)\n   - Use search API: 'GET /search/repositories?q=stars:>100+created:<2024-08-20+pushed:>2024-02-20&sort=stars&order=desc&per_page=100'\n\
  \   - Paginate through results to collect 2000+ repo URLs\n\n2.3 Data Collection per Repository (parallelized):\n   For\
  \ each repository (implement with asyncio for parallelism):\n   a) Repository metadata: 'GET /repos/{owner}/{repo}'\n  \
  \    - Extract: name, owner, stars, forks, language, created_at, updated_at, default_branch, size\n   \n   b) Contributors\
  \ list: 'GET /repos/{owner}/{repo}/contributors?per_page=100'\n      - Extract: contributor login, contributions count,\
  \ avatar_url\n      - Identify founder: contributor with earliest commit or highest initial contribution\n   \n   c) Commit\
  \ history: 'GET /repos/{owner}/{repo}/commits?per_page=100&since={2_years_ago}'\n      - For each commit: extract sha, author,\
  \ committer, timestamp, message\n      - For commits by top 10 contributors: fetch detailed diff\n   \n   d) Commit details\
  \ with file modifications: 'GET /repos/{owner}/{repo}/commits/{sha}'\n      - Extract: files modified (filename, status,\
  \ additions, deletions)\n      - Only fetch for commits by top contributors to manage API budget\n   \n   e) Identify founder\
  \ departure:\n      - Sort commits by timestamp per contributor\n      - Founder = contributor with first commit or most\
  \ commits in first 6 months\n      - Departure = 12+ months gap in founder's commits after active period\n\n2.4 Incremental\
  \ Saving and Fault Tolerance:\n   - Save data in batches of 50 repositories\n   - Implement checkpointing: resume from last\
  \ saved batch\n   - Handle rate limiting: implement exponential backoff with 403/429 responses\n   - Log failed repositories\
  \ for retry\n\nPHASE 3: Data Structuring and Export (1 hour)\n\n3.1 Transform raw API responses to structured format:\n\
  \   Schema per row (commit/file modification event):\n   {\n     'repo_id': str,  # owner/repo\n     'repo_name': str,\n\
  \     'repo_owner': str,\n     'repo_stars': int,\n     'repo_forks': int,\n     'repo_language': str,\n     'repo_created':\
  \ str,  # ISO timestamp\n     'repo_last_push': str,\n     'commit_sha': str,\n     'commit_timestamp': str,\n     'author_login':\
  \ str,\n     'author_id': str,\n     'is_founder': bool,\n     'files_modified': list,  # list of filenames\n     'file_count':\
  \ int,\n     'commit_message': str,\n     'contributor_join_date': str,  # first commit by this author\n     'contributor_total_commits':\
  \ int\n   }\n\n3.2 Create aggregated views:\n   - Repository-level summary: repo metadata + founder info + contributor count\n\
  \   - Contributor-level summary: per-contributor file modification patterns\n   - Time-series view: monthly commit counts\
  \ per repo for survival analysis\n\n3.3 Export to JSON:\n   - Full dataset: 'github_repo_data_full.json' (all commit events)\n\
  \   - Mini dataset: 'github_repo_data_mini.json' (sample 100 repos)\n   - Preview: 'github_repo_data_preview.json' (5 repos,\
  \ truncated)\n   - Repository summary: 'github_repo_summary.json' (one row per repo)\n\nPHASE 4: Validation and Quality\
  \ Checks (30 minutes)\n\n4.1 Verify data completeness:\n   - Check that 2000+ repositories are collected\n   - Verify commit\
  \ histories span at least 2 years for survival analysis\n   - Ensure founder identification is possible for >80% of repos\n\
  \   - Check for data consistency (no missing critical fields)\n\n4.2 Compute preliminary metrics:\n   - Bus factor (minimal\
  \ set of contributors whose departure stops development)\n   - Knowledge redundancy (average pairwise Jaccard similarity\
  \ of file sets)\n   - Founder departure events (repos where founder inactive 12+ months)\n\n4.3 Handle edge cases:\n   -\
  \ Repositories with only 1 contributor (founder = only contributor)\n   - Repositories with no identifiable founder (created\
  \ by organization)\n   - Repositories with incomplete commit history (GitHub API limitations)\n   - Forked repositories\
  \ (exclude or mark appropriately)\n\nFALLBACK STRATEGIES:\n\nFallback 1: If GitHub API rate limit insufficient:\n   - Use\
  \ GitHub Archive (gharchive.org) data from BigQuery or downloaded files\n   - Query for repository events filtered by criteria\n\
  \   - Process JSON event files to extract commit and contributor data\n\nFallback 2: If full commit histories too large:\n\
  \   - Sample top 20 contributors per repository\n   - Collect only last 2 years of commit history\n   - Focus on file modification\
  \ patterns rather than full diffs\n\nFallback 3: If 2000 repos not feasible:\n   - Target 1000 repositories with more comprehensive\
  \ data\n   - Prioritize repositories with clear founder departure events\n   - Use stratified sampling across programming\
  \ languages\n\nTOOLS AND LIBRARIES:\n- PyGithub (github library for Python) OR direct requests to GitHub REST API\n- asyncio\
  \ for parallel API calls\n- pandas for data manipulation\n- json for data export\n- time/backoff for rate limiting\n- tqdm\
  \ for progress tracking\n\nEXECUTION TIMELINE (6 hours total):\n- Hour 1: Phase 1 (evaluate existing datasets)\n- Hour 2-3:\
  \ Phase 2 preparation (authentication, repo discovery)\n- Hour 3-5: Phase 2 execution (data collection with parallel API\
  \ calls)\n- Hour 5-6: Phase 3-4 (structuring, export, validation)\n\nCRITICAL SUCCESS FACTORS:\n1. Obtain GitHub token for\
  \ higher rate limits (5000 vs 60 requests/hour)\n2. Implement efficient parallelization (asyncio, not sequential requests)\n\
  3. Incremental saving to avoid losing progress\n4. Filter repositories early to focus on those with identifiable founders\n\
  5. Balance data completeness vs. API budget constraints"
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
```

### [10] SYSTEM-USER prompt · 2026-08-20 19:42:06 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Collect GitHub repo data for OSS survival study
summary: >-
  Collect commit histories, file modifications, and contributor metadata from 2000+ GitHub repositories to study knowledge
  redundancy and project survival after founder departure.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) Repository metadata (stars, forks, language, creation date, last push), (2) Complete
  commit histories with author information, timestamps, and file modifications, (3) Contributor lists with join dates and
  activity periods, (4) At least 2000 repositories with 100+ stars, 2+ years old, and recent activity, (5) Repositories with
  identifiable founders (original creators) and sufficient commit history to analyze founder departure events, (6) Data structured
  as JSON with one row per commit/file modification event including: repo_id, commit_hash, author_id, timestamp, files_modified,
  file_paths, commit_message, and repository metadata. The dataset should be comprehensive enough to compute knowledge redundancy
  metrics (Jaccard similarity of file modification patterns) and identify founder departure events (12+ months without commits
  after active period).
dataset_search_plan: "PHASE 1: Evaluate Existing Dataset Sources (1 hour)\n\n1.1 Check HuggingFace for pre-existing GitHub\
  \ datasets:\n   - Search HuggingFace Hub for datasets containing GitHub repository data, commit histories, or open-source\
  \ project metadata\n   - Keywords: 'github', 'repository', 'commit', 'open source', 'git', 'software engineering'\n   -\
  \ Promising candidates: GHTorrent dataset, GitHub Archive datasets, software repository mining datasets\n   - Preview top\
  \ 3 candidates to assess data structure and completeness\n   - If suitable dataset found with 2000+ repos and commit-level\
  \ data, download and proceed to Phase 4\n\n1.2 Check for GHTorrent or GHArchive bulk data:\n   - GHTorrent (http://ghtorrent.org/)\
  \ provides MySQL dumps of GitHub data\n   - GHArchive (https://www.gharchive.org/) provides hourly archives of GitHub events\n\
  \   - Assess if these can be queried/downloaded within time constraints\n   - Check if preprocessed versions exist on HuggingFace\
  \ or academic repositories\n\nPHASE 2: GitHub API Data Collection Strategy (2 hours preparation + 3 hours execution)\n\n\
  2.1 Authentication Setup:\n   - Use GitHub Personal Access Token (if available in environment) for 5000 requests/hour limit\n\
  \   - If no token: Implement request throttling for 60 requests/hour (unauthenticated)\n   - Calculate feasible collection\
  \ rate: ~5000 repos with full commit history per hour with authentication\n\n2.2 Repository Discovery:\n   - Search GitHub\
  \ API for repositories matching criteria:\n     * 100+ stars\n     * Created 2+ years ago (before 2024-08-20)\n     * Recently\
  \ active (push event within last 6 months)\n     * Primary language: Python, JavaScript, Java, Go, TypeScript, C++, Ruby\
  \ (popular OSS languages)\n   - Use search API: 'GET /search/repositories?q=stars:>100+created:<2024-08-20+pushed:>2024-02-20&sort=stars&order=desc&per_page=100'\n\
  \   - Paginate through results to collect 2000+ repo URLs\n\n2.3 Data Collection per Repository (parallelized):\n   For\
  \ each repository (implement with asyncio for parallelism):\n   a) Repository metadata: 'GET /repos/{owner}/{repo}'\n  \
  \    - Extract: name, owner, stars, forks, language, created_at, updated_at, default_branch, size\n   \n   b) Contributors\
  \ list: 'GET /repos/{owner}/{repo}/contributors?per_page=100'\n      - Extract: contributor login, contributions count,\
  \ avatar_url\n      - Identify founder: contributor with earliest commit or highest initial contribution\n   \n   c) Commit\
  \ history: 'GET /repos/{owner}/{repo}/commits?per_page=100&since={2_years_ago}'\n      - For each commit: extract sha, author,\
  \ committer, timestamp, message\n      - For commits by top 10 contributors: fetch detailed diff\n   \n   d) Commit details\
  \ with file modifications: 'GET /repos/{owner}/{repo}/commits/{sha}'\n      - Extract: files modified (filename, status,\
  \ additions, deletions)\n      - Only fetch for commits by top contributors to manage API budget\n   \n   e) Identify founder\
  \ departure:\n      - Sort commits by timestamp per contributor\n      - Founder = contributor with first commit or most\
  \ commits in first 6 months\n      - Departure = 12+ months gap in founder's commits after active period\n\n2.4 Incremental\
  \ Saving and Fault Tolerance:\n   - Save data in batches of 50 repositories\n   - Implement checkpointing: resume from last\
  \ saved batch\n   - Handle rate limiting: implement exponential backoff with 403/429 responses\n   - Log failed repositories\
  \ for retry\n\nPHASE 3: Data Structuring and Export (1 hour)\n\n3.1 Transform raw API responses to structured format:\n\
  \   Schema per row (commit/file modification event):\n   {\n     'repo_id': str,  # owner/repo\n     'repo_name': str,\n\
  \     'repo_owner': str,\n     'repo_stars': int,\n     'repo_forks': int,\n     'repo_language': str,\n     'repo_created':\
  \ str,  # ISO timestamp\n     'repo_last_push': str,\n     'commit_sha': str,\n     'commit_timestamp': str,\n     'author_login':\
  \ str,\n     'author_id': str,\n     'is_founder': bool,\n     'files_modified': list,  # list of filenames\n     'file_count':\
  \ int,\n     'commit_message': str,\n     'contributor_join_date': str,  # first commit by this author\n     'contributor_total_commits':\
  \ int\n   }\n\n3.2 Create aggregated views:\n   - Repository-level summary: repo metadata + founder info + contributor count\n\
  \   - Contributor-level summary: per-contributor file modification patterns\n   - Time-series view: monthly commit counts\
  \ per repo for survival analysis\n\n3.3 Export to JSON:\n   - Full dataset: 'github_repo_data_full.json' (all commit events)\n\
  \   - Mini dataset: 'github_repo_data_mini.json' (sample 100 repos)\n   - Preview: 'github_repo_data_preview.json' (5 repos,\
  \ truncated)\n   - Repository summary: 'github_repo_summary.json' (one row per repo)\n\nPHASE 4: Validation and Quality\
  \ Checks (30 minutes)\n\n4.1 Verify data completeness:\n   - Check that 2000+ repositories are collected\n   - Verify commit\
  \ histories span at least 2 years for survival analysis\n   - Ensure founder identification is possible for >80% of repos\n\
  \   - Check for data consistency (no missing critical fields)\n\n4.2 Compute preliminary metrics:\n   - Bus factor (minimal\
  \ set of contributors whose departure stops development)\n   - Knowledge redundancy (average pairwise Jaccard similarity\
  \ of file sets)\n   - Founder departure events (repos where founder inactive 12+ months)\n\n4.3 Handle edge cases:\n   -\
  \ Repositories with only 1 contributor (founder = only contributor)\n   - Repositories with no identifiable founder (created\
  \ by organization)\n   - Repositories with incomplete commit history (GitHub API limitations)\n   - Forked repositories\
  \ (exclude or mark appropriately)\n\nFALLBACK STRATEGIES:\n\nFallback 1: If GitHub API rate limit insufficient:\n   - Use\
  \ GitHub Archive (gharchive.org) data from BigQuery or downloaded files\n   - Query for repository events filtered by criteria\n\
  \   - Process JSON event files to extract commit and contributor data\n\nFallback 2: If full commit histories too large:\n\
  \   - Sample top 20 contributors per repository\n   - Collect only last 2 years of commit history\n   - Focus on file modification\
  \ patterns rather than full diffs\n\nFallback 3: If 2000 repos not feasible:\n   - Target 1000 repositories with more comprehensive\
  \ data\n   - Prioritize repositories with clear founder departure events\n   - Use stratified sampling across programming\
  \ languages\n\nTOOLS AND LIBRARIES:\n- PyGithub (github library for Python) OR direct requests to GitHub REST API\n- asyncio\
  \ for parallel API calls\n- pandas for data manipulation\n- json for data export\n- time/backoff for rate limiting\n- tqdm\
  \ for progress tracking\n\nEXECUTION TIMELINE (6 hours total):\n- Hour 1: Phase 1 (evaluate existing datasets)\n- Hour 2-3:\
  \ Phase 2 preparation (authentication, repo discovery)\n- Hour 3-5: Phase 2 execution (data collection with parallel API\
  \ calls)\n- Hour 5-6: Phase 3-4 (structuring, export, validation)\n\nCRITICAL SUCCESS FACTORS:\n1. Obtain GitHub token for\
  \ higher rate limits (5000 vs 60 requests/hour)\n2. Implement efficient parallelization (asyncio, not sequential requests)\n\
  3. Incremental saving to avoid losing progress\n4. Filter repositories early to focus on those with identifiable founders\n\
  5. Balance data completeness vs. API budget constraints"
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
```

### [11] SYSTEM-USER prompt · 2026-08-20 19:48:44 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Collect GitHub repo data for OSS survival study
summary: >-
  Collect commit histories, file modifications, and contributor metadata from 2000+ GitHub repositories to study knowledge
  redundancy and project survival after founder departure.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) Repository metadata (stars, forks, language, creation date, last push), (2) Complete
  commit histories with author information, timestamps, and file modifications, (3) Contributor lists with join dates and
  activity periods, (4) At least 2000 repositories with 100+ stars, 2+ years old, and recent activity, (5) Repositories with
  identifiable founders (original creators) and sufficient commit history to analyze founder departure events, (6) Data structured
  as JSON with one row per commit/file modification event including: repo_id, commit_hash, author_id, timestamp, files_modified,
  file_paths, commit_message, and repository metadata. The dataset should be comprehensive enough to compute knowledge redundancy
  metrics (Jaccard similarity of file modification patterns) and identify founder departure events (12+ months without commits
  after active period).
dataset_search_plan: "PHASE 1: Evaluate Existing Dataset Sources (1 hour)\n\n1.1 Check HuggingFace for pre-existing GitHub\
  \ datasets:\n   - Search HuggingFace Hub for datasets containing GitHub repository data, commit histories, or open-source\
  \ project metadata\n   - Keywords: 'github', 'repository', 'commit', 'open source', 'git', 'software engineering'\n   -\
  \ Promising candidates: GHTorrent dataset, GitHub Archive datasets, software repository mining datasets\n   - Preview top\
  \ 3 candidates to assess data structure and completeness\n   - If suitable dataset found with 2000+ repos and commit-level\
  \ data, download and proceed to Phase 4\n\n1.2 Check for GHTorrent or GHArchive bulk data:\n   - GHTorrent (http://ghtorrent.org/)\
  \ provides MySQL dumps of GitHub data\n   - GHArchive (https://www.gharchive.org/) provides hourly archives of GitHub events\n\
  \   - Assess if these can be queried/downloaded within time constraints\n   - Check if preprocessed versions exist on HuggingFace\
  \ or academic repositories\n\nPHASE 2: GitHub API Data Collection Strategy (2 hours preparation + 3 hours execution)\n\n\
  2.1 Authentication Setup:\n   - Use GitHub Personal Access Token (if available in environment) for 5000 requests/hour limit\n\
  \   - If no token: Implement request throttling for 60 requests/hour (unauthenticated)\n   - Calculate feasible collection\
  \ rate: ~5000 repos with full commit history per hour with authentication\n\n2.2 Repository Discovery:\n   - Search GitHub\
  \ API for repositories matching criteria:\n     * 100+ stars\n     * Created 2+ years ago (before 2024-08-20)\n     * Recently\
  \ active (push event within last 6 months)\n     * Primary language: Python, JavaScript, Java, Go, TypeScript, C++, Ruby\
  \ (popular OSS languages)\n   - Use search API: 'GET /search/repositories?q=stars:>100+created:<2024-08-20+pushed:>2024-02-20&sort=stars&order=desc&per_page=100'\n\
  \   - Paginate through results to collect 2000+ repo URLs\n\n2.3 Data Collection per Repository (parallelized):\n   For\
  \ each repository (implement with asyncio for parallelism):\n   a) Repository metadata: 'GET /repos/{owner}/{repo}'\n  \
  \    - Extract: name, owner, stars, forks, language, created_at, updated_at, default_branch, size\n   \n   b) Contributors\
  \ list: 'GET /repos/{owner}/{repo}/contributors?per_page=100'\n      - Extract: contributor login, contributions count,\
  \ avatar_url\n      - Identify founder: contributor with earliest commit or highest initial contribution\n   \n   c) Commit\
  \ history: 'GET /repos/{owner}/{repo}/commits?per_page=100&since={2_years_ago}'\n      - For each commit: extract sha, author,\
  \ committer, timestamp, message\n      - For commits by top 10 contributors: fetch detailed diff\n   \n   d) Commit details\
  \ with file modifications: 'GET /repos/{owner}/{repo}/commits/{sha}'\n      - Extract: files modified (filename, status,\
  \ additions, deletions)\n      - Only fetch for commits by top contributors to manage API budget\n   \n   e) Identify founder\
  \ departure:\n      - Sort commits by timestamp per contributor\n      - Founder = contributor with first commit or most\
  \ commits in first 6 months\n      - Departure = 12+ months gap in founder's commits after active period\n\n2.4 Incremental\
  \ Saving and Fault Tolerance:\n   - Save data in batches of 50 repositories\n   - Implement checkpointing: resume from last\
  \ saved batch\n   - Handle rate limiting: implement exponential backoff with 403/429 responses\n   - Log failed repositories\
  \ for retry\n\nPHASE 3: Data Structuring and Export (1 hour)\n\n3.1 Transform raw API responses to structured format:\n\
  \   Schema per row (commit/file modification event):\n   {\n     'repo_id': str,  # owner/repo\n     'repo_name': str,\n\
  \     'repo_owner': str,\n     'repo_stars': int,\n     'repo_forks': int,\n     'repo_language': str,\n     'repo_created':\
  \ str,  # ISO timestamp\n     'repo_last_push': str,\n     'commit_sha': str,\n     'commit_timestamp': str,\n     'author_login':\
  \ str,\n     'author_id': str,\n     'is_founder': bool,\n     'files_modified': list,  # list of filenames\n     'file_count':\
  \ int,\n     'commit_message': str,\n     'contributor_join_date': str,  # first commit by this author\n     'contributor_total_commits':\
  \ int\n   }\n\n3.2 Create aggregated views:\n   - Repository-level summary: repo metadata + founder info + contributor count\n\
  \   - Contributor-level summary: per-contributor file modification patterns\n   - Time-series view: monthly commit counts\
  \ per repo for survival analysis\n\n3.3 Export to JSON:\n   - Full dataset: 'github_repo_data_full.json' (all commit events)\n\
  \   - Mini dataset: 'github_repo_data_mini.json' (sample 100 repos)\n   - Preview: 'github_repo_data_preview.json' (5 repos,\
  \ truncated)\n   - Repository summary: 'github_repo_summary.json' (one row per repo)\n\nPHASE 4: Validation and Quality\
  \ Checks (30 minutes)\n\n4.1 Verify data completeness:\n   - Check that 2000+ repositories are collected\n   - Verify commit\
  \ histories span at least 2 years for survival analysis\n   - Ensure founder identification is possible for >80% of repos\n\
  \   - Check for data consistency (no missing critical fields)\n\n4.2 Compute preliminary metrics:\n   - Bus factor (minimal\
  \ set of contributors whose departure stops development)\n   - Knowledge redundancy (average pairwise Jaccard similarity\
  \ of file sets)\n   - Founder departure events (repos where founder inactive 12+ months)\n\n4.3 Handle edge cases:\n   -\
  \ Repositories with only 1 contributor (founder = only contributor)\n   - Repositories with no identifiable founder (created\
  \ by organization)\n   - Repositories with incomplete commit history (GitHub API limitations)\n   - Forked repositories\
  \ (exclude or mark appropriately)\n\nFALLBACK STRATEGIES:\n\nFallback 1: If GitHub API rate limit insufficient:\n   - Use\
  \ GitHub Archive (gharchive.org) data from BigQuery or downloaded files\n   - Query for repository events filtered by criteria\n\
  \   - Process JSON event files to extract commit and contributor data\n\nFallback 2: If full commit histories too large:\n\
  \   - Sample top 20 contributors per repository\n   - Collect only last 2 years of commit history\n   - Focus on file modification\
  \ patterns rather than full diffs\n\nFallback 3: If 2000 repos not feasible:\n   - Target 1000 repositories with more comprehensive\
  \ data\n   - Prioritize repositories with clear founder departure events\n   - Use stratified sampling across programming\
  \ languages\n\nTOOLS AND LIBRARIES:\n- PyGithub (github library for Python) OR direct requests to GitHub REST API\n- asyncio\
  \ for parallel API calls\n- pandas for data manipulation\n- json for data export\n- time/backoff for rate limiting\n- tqdm\
  \ for progress tracking\n\nEXECUTION TIMELINE (6 hours total):\n- Hour 1: Phase 1 (evaluate existing datasets)\n- Hour 2-3:\
  \ Phase 2 preparation (authentication, repo discovery)\n- Hour 3-5: Phase 2 execution (data collection with parallel API\
  \ calls)\n- Hour 5-6: Phase 3-4 (structuring, export, validation)\n\nCRITICAL SUCCESS FACTORS:\n1. Obtain GitHub token for\
  \ higher rate limits (5000 vs 60 requests/hour)\n2. Implement efficient parallelization (asyncio, not sequential requests)\n\
  3. Incremental saving to avoid losing progress\n4. Filter repositories early to focus on those with identifiable founders\n\
  5. Balance data completeness vs. API budget constraints"
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

### [12] HUMAN-USER prompt · 2026-08-20 19:56:28 UTC

```
be more exhaustive
```

### [13] SYSTEM-USER prompt · 2026-08-20 20:00:53 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Collect GitHub repo data for OSS survival study
summary: >-
  Collect commit histories, file modifications, and contributor metadata from 2000+ GitHub repositories to study knowledge
  redundancy and project survival after founder departure.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset should contain: (1) Repository metadata (stars, forks, language, creation date, last push), (2) Complete
  commit histories with author information, timestamps, and file modifications, (3) Contributor lists with join dates and
  activity periods, (4) At least 2000 repositories with 100+ stars, 2+ years old, and recent activity, (5) Repositories with
  identifiable founders (original creators) and sufficient commit history to analyze founder departure events, (6) Data structured
  as JSON with one row per commit/file modification event including: repo_id, commit_hash, author_id, timestamp, files_modified,
  file_paths, commit_message, and repository metadata. The dataset should be comprehensive enough to compute knowledge redundancy
  metrics (Jaccard similarity of file modification patterns) and identify founder departure events (12+ months without commits
  after active period).
dataset_search_plan: "PHASE 1: Evaluate Existing Dataset Sources (1 hour)\n\n1.1 Check HuggingFace for pre-existing GitHub\
  \ datasets:\n   - Search HuggingFace Hub for datasets containing GitHub repository data, commit histories, or open-source\
  \ project metadata\n   - Keywords: 'github', 'repository', 'commit', 'open source', 'git', 'software engineering'\n   -\
  \ Promising candidates: GHTorrent dataset, GitHub Archive datasets, software repository mining datasets\n   - Preview top\
  \ 3 candidates to assess data structure and completeness\n   - If suitable dataset found with 2000+ repos and commit-level\
  \ data, download and proceed to Phase 4\n\n1.2 Check for GHTorrent or GHArchive bulk data:\n   - GHTorrent (http://ghtorrent.org/)\
  \ provides MySQL dumps of GitHub data\n   - GHArchive (https://www.gharchive.org/) provides hourly archives of GitHub events\n\
  \   - Assess if these can be queried/downloaded within time constraints\n   - Check if preprocessed versions exist on HuggingFace\
  \ or academic repositories\n\nPHASE 2: GitHub API Data Collection Strategy (2 hours preparation + 3 hours execution)\n\n\
  2.1 Authentication Setup:\n   - Use GitHub Personal Access Token (if available in environment) for 5000 requests/hour limit\n\
  \   - If no token: Implement request throttling for 60 requests/hour (unauthenticated)\n   - Calculate feasible collection\
  \ rate: ~5000 repos with full commit history per hour with authentication\n\n2.2 Repository Discovery:\n   - Search GitHub\
  \ API for repositories matching criteria:\n     * 100+ stars\n     * Created 2+ years ago (before 2024-08-20)\n     * Recently\
  \ active (push event within last 6 months)\n     * Primary language: Python, JavaScript, Java, Go, TypeScript, C++, Ruby\
  \ (popular OSS languages)\n   - Use search API: 'GET /search/repositories?q=stars:>100+created:<2024-08-20+pushed:>2024-02-20&sort=stars&order=desc&per_page=100'\n\
  \   - Paginate through results to collect 2000+ repo URLs\n\n2.3 Data Collection per Repository (parallelized):\n   For\
  \ each repository (implement with asyncio for parallelism):\n   a) Repository metadata: 'GET /repos/{owner}/{repo}'\n  \
  \    - Extract: name, owner, stars, forks, language, created_at, updated_at, default_branch, size\n   \n   b) Contributors\
  \ list: 'GET /repos/{owner}/{repo}/contributors?per_page=100'\n      - Extract: contributor login, contributions count,\
  \ avatar_url\n      - Identify founder: contributor with earliest commit or highest initial contribution\n   \n   c) Commit\
  \ history: 'GET /repos/{owner}/{repo}/commits?per_page=100&since={2_years_ago}'\n      - For each commit: extract sha, author,\
  \ committer, timestamp, message\n      - For commits by top 10 contributors: fetch detailed diff\n   \n   d) Commit details\
  \ with file modifications: 'GET /repos/{owner}/{repo}/commits/{sha}'\n      - Extract: files modified (filename, status,\
  \ additions, deletions)\n      - Only fetch for commits by top contributors to manage API budget\n   \n   e) Identify founder\
  \ departure:\n      - Sort commits by timestamp per contributor\n      - Founder = contributor with first commit or most\
  \ commits in first 6 months\n      - Departure = 12+ months gap in founder's commits after active period\n\n2.4 Incremental\
  \ Saving and Fault Tolerance:\n   - Save data in batches of 50 repositories\n   - Implement checkpointing: resume from last\
  \ saved batch\n   - Handle rate limiting: implement exponential backoff with 403/429 responses\n   - Log failed repositories\
  \ for retry\n\nPHASE 3: Data Structuring and Export (1 hour)\n\n3.1 Transform raw API responses to structured format:\n\
  \   Schema per row (commit/file modification event):\n   {\n     'repo_id': str,  # owner/repo\n     'repo_name': str,\n\
  \     'repo_owner': str,\n     'repo_stars': int,\n     'repo_forks': int,\n     'repo_language': str,\n     'repo_created':\
  \ str,  # ISO timestamp\n     'repo_last_push': str,\n     'commit_sha': str,\n     'commit_timestamp': str,\n     'author_login':\
  \ str,\n     'author_id': str,\n     'is_founder': bool,\n     'files_modified': list,  # list of filenames\n     'file_count':\
  \ int,\n     'commit_message': str,\n     'contributor_join_date': str,  # first commit by this author\n     'contributor_total_commits':\
  \ int\n   }\n\n3.2 Create aggregated views:\n   - Repository-level summary: repo metadata + founder info + contributor count\n\
  \   - Contributor-level summary: per-contributor file modification patterns\n   - Time-series view: monthly commit counts\
  \ per repo for survival analysis\n\n3.3 Export to JSON:\n   - Full dataset: 'github_repo_data_full.json' (all commit events)\n\
  \   - Mini dataset: 'github_repo_data_mini.json' (sample 100 repos)\n   - Preview: 'github_repo_data_preview.json' (5 repos,\
  \ truncated)\n   - Repository summary: 'github_repo_summary.json' (one row per repo)\n\nPHASE 4: Validation and Quality\
  \ Checks (30 minutes)\n\n4.1 Verify data completeness:\n   - Check that 2000+ repositories are collected\n   - Verify commit\
  \ histories span at least 2 years for survival analysis\n   - Ensure founder identification is possible for >80% of repos\n\
  \   - Check for data consistency (no missing critical fields)\n\n4.2 Compute preliminary metrics:\n   - Bus factor (minimal\
  \ set of contributors whose departure stops development)\n   - Knowledge redundancy (average pairwise Jaccard similarity\
  \ of file sets)\n   - Founder departure events (repos where founder inactive 12+ months)\n\n4.3 Handle edge cases:\n   -\
  \ Repositories with only 1 contributor (founder = only contributor)\n   - Repositories with no identifiable founder (created\
  \ by organization)\n   - Repositories with incomplete commit history (GitHub API limitations)\n   - Forked repositories\
  \ (exclude or mark appropriately)\n\nFALLBACK STRATEGIES:\n\nFallback 1: If GitHub API rate limit insufficient:\n   - Use\
  \ GitHub Archive (gharchive.org) data from BigQuery or downloaded files\n   - Query for repository events filtered by criteria\n\
  \   - Process JSON event files to extract commit and contributor data\n\nFallback 2: If full commit histories too large:\n\
  \   - Sample top 20 contributors per repository\n   - Collect only last 2 years of commit history\n   - Focus on file modification\
  \ patterns rather than full diffs\n\nFallback 3: If 2000 repos not feasible:\n   - Target 1000 repositories with more comprehensive\
  \ data\n   - Prioritize repositories with clear founder departure events\n   - Use stratified sampling across programming\
  \ languages\n\nTOOLS AND LIBRARIES:\n- PyGithub (github library for Python) OR direct requests to GitHub REST API\n- asyncio\
  \ for parallel API calls\n- pandas for data manipulation\n- json for data export\n- time/backoff for rate limiting\n- tqdm\
  \ for progress tracking\n\nEXECUTION TIMELINE (6 hours total):\n- Hour 1: Phase 1 (evaluate existing datasets)\n- Hour 2-3:\
  \ Phase 2 preparation (authentication, repo discovery)\n- Hour 3-5: Phase 2 execution (data collection with parallel API\
  \ calls)\n- Hour 5-6: Phase 3-4 (structuring, export, validation)\n\nCRITICAL SUCCESS FACTORS:\n1. Obtain GitHub token for\
  \ higher rate limits (5000 vs 60 requests/hour)\n2. Implement efficient parallelization (asyncio, not sequential requests)\n\
  3. Incremental saving to avoid losing progress\n4. Filter repositories early to focus on those with identifiable founders\n\
  5. Balance data completeness vs. API budget constraints"
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_rhx_UB8HZyTw/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````
