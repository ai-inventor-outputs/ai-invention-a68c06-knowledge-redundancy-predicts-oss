# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `iter1_924aa01cf43b` — Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 15:08:33 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: OSS Survival Literature Review Plan
summary: >-
  Comprehensive literature review plan to validate novelty of knowledge redundancy hypothesis and identify methodological
  approaches for measuring OSS survival, bus factor, and knowledge redundancy.
runpod_compute_profile: cpu_light
question: >-
  What is the current state of research on OSS project survival prediction, how is bus factor measured, and what constructs
  similar to knowledge redundancy exist in the literature that would validate or challenge the proposed inverted-U hypothesis?
research_plan: |-
  ## Phase 1: Identify and Retrieve Key Papers (45 minutes)

  ### Step 1.1: Search for Primary References
  Execute the following searches using aii-web-tools (scholarly mode preferred):

  1. **Avelino et al. (2019)** - 'On the abandonment and survival of open source projects'
     - Search query: "On the abandonment and survival of open source projects" Avelino 2019
     - Target: Find PDF or full text version

  2. **Cosentino et al. (2016)** - 'Assessing the bus factor from repository data'
     - Search query: "Assessing the bus factor from repository data" Cosentino 2016
     - Target: Understand bus factor algorithm

  3. **ESEC/FSE 2023** - 'The State of Survival in OSS: The Impact of Diversity'
     - Search query: "State of Survival in OSS" ESEC FSE 2023 diversity
     - Target: Find diversity metrics and survival definitions

  4. **2025 Write Access Paper** - 'Write access provisioning and organizational ownership'
     - Search query: "write access provisioning" open source 2025
     - Target: Governance factors in OSS survival

  ### Step 1.2: Retrieve and Extract Key Information
  For each paper found:
  1. Fetch the abstract, introduction, and methodology sections
  2. Use fetch_grep to extract:
     - **Survival definition**: How is project survival operationalized? (pattern: survival definition|project survival|abandonment)
     - **Bus factor measurement**: How is bus factor calculated? (pattern: bus factor|critical contributor)
     - **Control variables**: What variables are controlled for? (pattern: control|covariate|adjust)
     - **Statistical methods**: What analysis methods are used? (pattern: Cox|survival analysis|regression)

  **Deliverable**: Create papers_summary.md with 2-3 paragraph summary per paper.

  ## Phase 2: Synthesize Measurement Approaches (50 minutes)

  ### Step 2.1: Bus Factor vs. Knowledge Redundancy Analysis
  Search and read:
  - Query: bus factor measurement algorithm git repository Cosentino
  - Fetch Cosentino (2016) methodology section
  - Use fetch_grep to extract algorithm details: pattern: algorithm|computation|measure

  **Key analysis**: Create comparison table showing differences between bus factor and knowledge redundancy.

  ### Step 2.2: Knowledge/Expertise Measurement Methods
  Search for methods to infer expertise from git history:
  - Query 1: developer expertise git history file modification patterns
  - Query 2: Jaccard similarity expertise overlap measurement
  - Query 3: measuring knowledge overlap in teams organizational psychology

  Synthesize findings on file modification patterns, code authorship, and discussion participation.

  **Deliverable**: Create measurement_approaches.md with 3+ methods and recommendations.

  ### Step 2.3: Survival Definitions in OSS Literature
  Search for survival operationalization:
  - Query: open source project survival definition metrics
  - Review Avelino (2019) for survival criteria
  - Extract using fetch_grep: pattern: survival|abandonment|active development

  Create survival definition options: activity-based, trend-based, or hybrid.

  **Deliverable**: Recommend specific survival definition with justification.

  ## Phase 3: Identify Control Variables and Confounds (40 minutes)

  ### Step 3.1: Known Predictors of OSS Survival
  Search for factors affecting OSS survival:
  - Query: open source project success factors predictors
  - Review ESEC/FSE 2023 for diversity and other factors
  - Extract control variables using fetch_grep: pattern: control|covariate|confound

  Compile list of potential control variables:
  - **Project-level**: size, age, popularity, language, domain
  - **Contributor-level**: count, diversity, contribution frequency
  - **Technical**: complexity, dependency count, test coverage
  - **Social**: community engagement, governance structure

  ### Step 3.2: Statistical Methods for Survival Analysis
  Search for appropriate statistical methods:
  - Query: Cox proportional hazards model survival analysis software
  - Query: survival analysis open source GitHub projects

  Verify assumptions and implementation for Cox model with quadratic term.

  **Deliverable**: Create statistical_approach.md with recommended model.

  ## Phase 4: Validate Novelty and Identify Gaps (30 minutes)

  ### Step 4.1: Direct Literature Search on Knowledge Redundancy in OSS
  Search specifically for knowledge redundancy or similar constructs:
  - Query: "knowledge redundancy" open source software
  - Query: "expertise overlap" open source
  - Query: "knowledge overlap" GitHub

  If no direct matches found, search broader terms like team redundancy or transactive memory systems.

  ### Step 4.2: Gap Analysis
  Based on literature review, articulate:
  1. What existing work measures (bus factor, diversity, governance)
  2. What existing work misses (degree of knowledge overlap)
  3. How knowledge redundancy differs (structure vs. count)
  4. Why inverted-U is plausible (theoretical grounding)

  **Deliverable**: Create novelty_validation.md with 3-5 specific gaps.

  ## Phase 5: Synthesize and Write Final Report (35 minutes)

  ### Step 5.1: Write research_report.md
  Structure:
  1. **Executive Summary** (1 paragraph)
  2. **Literature Review** (3-4 pages): OSS Survival, Bus Factor, Knowledge Redundancy, Related Constructs
  3. **Methodological Recommendations** (2-3 pages): Measurement, Survival Definition, Controls, Statistics
  4. **Gap Analysis and Novelty** (1-2 pages)
  5. **Bibliography**

  ### Step 5.2: Create research_out.json
  Output structure:
  - answer: Comprehensive 2-3 paragraph summary
  - sources: Array of objects with title, authors, year, url, key_findings
  - follow_up_questions: Array of 3-5 questions

  ## Time Budget and Parallelization

  **Total estimated time**: 200 minutes (3h 20min) - within 3h budget if parallelized.

  **Parallelization opportunities**:
  - Phase 1 searches can be parallelized (4 independent searches)
  - Phase 3.1 and 3.2 can be parallelized

  **Critical path**: Phase 1 -> Phase 2 -> Phase 4 -> Phase 5 (must be sequential)

  **Risk mitigation**:
  - If papers not freely available, use pre-prints or conference abstracts
  - If searches return too many results, filter by citation count (>10 citations)
  - If time runs short, prioritize: Phase 1 -> Phase 2.1 -> Phase 4 -> Phase 5

  ## Execution Checklist

  Before starting execution, verify:
  - [ ] aii-web-tools skill is accessible
  - [ ] Scholarly search mode works
  - [ ] fetch_grep works on at least one PDF
  - [ ] Output directory is writable

  During execution, track:
  - [ ] Papers found and summarized (4 primary papers)
  - [ ] Measurement approaches synthesized (bus factor, knowledge redundancy)
  - [ ] Control variables identified (10+ variables)
  - [ ] Statistical approach defined (Cox model with quadratic term)
  - [ ] Novelty validated (3+ gaps identified)
  - [ ] Final report written (research_report.md)
  - [ ] Output JSON created (research_out.json)
explanation: >-
  This research is critical for validating the novelty of the knowledge redundancy hypothesis and ensuring the methodology
  is sound. Without a thorough literature review, we risk: (1) rediscovering known results, (2) using suboptimal measurement
  approaches, (3) failing to control for known confounds, and (4) misinterpreting results due to methodological flaws. The
  executor needs specific search queries, paper retrieval strategies, extraction patterns (fetch_grep), and output specifications
  to conduct this research efficiently within the 3-hour time budget. This plan provides step-by-step instructions with parallelization
  opportunities and risk mitigation strategies.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 15:08:33 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-tools · 2026-08-21 15:08:41 UTC

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

### [4] HUMAN-USER prompt · 2026-08-21 15:15:15 UTC

```
be more exhaustive
```

### [5] HUMAN-USER prompt · 2026-08-21 15:27:05 UTC

```
be more exhaustive
```

### [6] HUMAN-USER prompt · 2026-08-21 15:28:08 UTC

```
be more exhaustive
```

### [7] HUMAN-USER prompt · 2026-08-21 15:34:59 UTC

```
be more exhaustive
```

### [8] SYSTEM-USER prompt · 2026-08-21 15:37:45 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: OSS Survival Literature Review Plan
summary: >-
  Comprehensive literature review plan to validate novelty of knowledge redundancy hypothesis and identify methodological
  approaches for measuring OSS survival, bus factor, and knowledge redundancy.
runpod_compute_profile: cpu_light
question: >-
  What is the current state of research on OSS project survival prediction, how is bus factor measured, and what constructs
  similar to knowledge redundancy exist in the literature that would validate or challenge the proposed inverted-U hypothesis?
research_plan: |-
  ## Phase 1: Identify and Retrieve Key Papers (45 minutes)

  ### Step 1.1: Search for Primary References
  Execute the following searches using aii-web-tools (scholarly mode preferred):

  1. **Avelino et al. (2019)** - 'On the abandonment and survival of open source projects'
     - Search query: "On the abandonment and survival of open source projects" Avelino 2019
     - Target: Find PDF or full text version

  2. **Cosentino et al. (2016)** - 'Assessing the bus factor from repository data'
     - Search query: "Assessing the bus factor from repository data" Cosentino 2016
     - Target: Understand bus factor algorithm

  3. **ESEC/FSE 2023** - 'The State of Survival in OSS: The Impact of Diversity'
     - Search query: "State of Survival in OSS" ESEC FSE 2023 diversity
     - Target: Find diversity metrics and survival definitions

  4. **2025 Write Access Paper** - 'Write access provisioning and organizational ownership'
     - Search query: "write access provisioning" open source 2025
     - Target: Governance factors in OSS survival

  ### Step 1.2: Retrieve and Extract Key Information
  For each paper found:
  1. Fetch the abstract, introduction, and methodology sections
  2. Use fetch_grep to extract:
     - **Survival definition**: How is project survival operationalized? (pattern: survival definition|project survival|abandonment)
     - **Bus factor measurement**: How is bus factor calculated? (pattern: bus factor|critical contributor)
     - **Control variables**: What variables are controlled for? (pattern: control|covariate|adjust)
     - **Statistical methods**: What analysis methods are used? (pattern: Cox|survival analysis|regression)

  **Deliverable**: Create papers_summary.md with 2-3 paragraph summary per paper.

  ## Phase 2: Synthesize Measurement Approaches (50 minutes)

  ### Step 2.1: Bus Factor vs. Knowledge Redundancy Analysis
  Search and read:
  - Query: bus factor measurement algorithm git repository Cosentino
  - Fetch Cosentino (2016) methodology section
  - Use fetch_grep to extract algorithm details: pattern: algorithm|computation|measure

  **Key analysis**: Create comparison table showing differences between bus factor and knowledge redundancy.

  ### Step 2.2: Knowledge/Expertise Measurement Methods
  Search for methods to infer expertise from git history:
  - Query 1: developer expertise git history file modification patterns
  - Query 2: Jaccard similarity expertise overlap measurement
  - Query 3: measuring knowledge overlap in teams organizational psychology

  Synthesize findings on file modification patterns, code authorship, and discussion participation.

  **Deliverable**: Create measurement_approaches.md with 3+ methods and recommendations.

  ### Step 2.3: Survival Definitions in OSS Literature
  Search for survival operationalization:
  - Query: open source project survival definition metrics
  - Review Avelino (2019) for survival criteria
  - Extract using fetch_grep: pattern: survival|abandonment|active development

  Create survival definition options: activity-based, trend-based, or hybrid.

  **Deliverable**: Recommend specific survival definition with justification.

  ## Phase 3: Identify Control Variables and Confounds (40 minutes)

  ### Step 3.1: Known Predictors of OSS Survival
  Search for factors affecting OSS survival:
  - Query: open source project success factors predictors
  - Review ESEC/FSE 2023 for diversity and other factors
  - Extract control variables using fetch_grep: pattern: control|covariate|confound

  Compile list of potential control variables:
  - **Project-level**: size, age, popularity, language, domain
  - **Contributor-level**: count, diversity, contribution frequency
  - **Technical**: complexity, dependency count, test coverage
  - **Social**: community engagement, governance structure

  ### Step 3.2: Statistical Methods for Survival Analysis
  Search for appropriate statistical methods:
  - Query: Cox proportional hazards model survival analysis software
  - Query: survival analysis open source GitHub projects

  Verify assumptions and implementation for Cox model with quadratic term.

  **Deliverable**: Create statistical_approach.md with recommended model.

  ## Phase 4: Validate Novelty and Identify Gaps (30 minutes)

  ### Step 4.1: Direct Literature Search on Knowledge Redundancy in OSS
  Search specifically for knowledge redundancy or similar constructs:
  - Query: "knowledge redundancy" open source software
  - Query: "expertise overlap" open source
  - Query: "knowledge overlap" GitHub

  If no direct matches found, search broader terms like team redundancy or transactive memory systems.

  ### Step 4.2: Gap Analysis
  Based on literature review, articulate:
  1. What existing work measures (bus factor, diversity, governance)
  2. What existing work misses (degree of knowledge overlap)
  3. How knowledge redundancy differs (structure vs. count)
  4. Why inverted-U is plausible (theoretical grounding)

  **Deliverable**: Create novelty_validation.md with 3-5 specific gaps.

  ## Phase 5: Synthesize and Write Final Report (35 minutes)

  ### Step 5.1: Write research_report.md
  Structure:
  1. **Executive Summary** (1 paragraph)
  2. **Literature Review** (3-4 pages): OSS Survival, Bus Factor, Knowledge Redundancy, Related Constructs
  3. **Methodological Recommendations** (2-3 pages): Measurement, Survival Definition, Controls, Statistics
  4. **Gap Analysis and Novelty** (1-2 pages)
  5. **Bibliography**

  ### Step 5.2: Create research_out.json
  Output structure:
  - answer: Comprehensive 2-3 paragraph summary
  - sources: Array of objects with title, authors, year, url, key_findings
  - follow_up_questions: Array of 3-5 questions

  ## Time Budget and Parallelization

  **Total estimated time**: 200 minutes (3h 20min) - within 3h budget if parallelized.

  **Parallelization opportunities**:
  - Phase 1 searches can be parallelized (4 independent searches)
  - Phase 3.1 and 3.2 can be parallelized

  **Critical path**: Phase 1 -> Phase 2 -> Phase 4 -> Phase 5 (must be sequential)

  **Risk mitigation**:
  - If papers not freely available, use pre-prints or conference abstracts
  - If searches return too many results, filter by citation count (>10 citations)
  - If time runs short, prioritize: Phase 1 -> Phase 2.1 -> Phase 4 -> Phase 5

  ## Execution Checklist

  Before starting execution, verify:
  - [ ] aii-web-tools skill is accessible
  - [ ] Scholarly search mode works
  - [ ] fetch_grep works on at least one PDF
  - [ ] Output directory is writable

  During execution, track:
  - [ ] Papers found and summarized (4 primary papers)
  - [ ] Measurement approaches synthesized (bus factor, knowledge redundancy)
  - [ ] Control variables identified (10+ variables)
  - [ ] Statistical approach defined (Cox model with quadratic term)
  - [ ] Novelty validated (3+ gaps identified)
  - [ ] Final report written (research_report.md)
  - [ ] Output JSON created (research_out.json)
explanation: >-
  This research is critical for validating the novelty of the knowledge redundancy hypothesis and ensuring the methodology
  is sound. Without a thorough literature review, we risk: (1) rediscovering known results, (2) using suboptimal measurement
  approaches, (3) failing to control for known confounds, and (4) misinterpreting results due to methodological flaws. The
  executor needs specific search queries, paper retrieval strategies, extraction patterns (fetch_grep), and output specifications
  to conduct this research efficiently within the 3-hour time budget. This plan provides step-by-step instructions with parallelization
  opportunities and risk mitigation strategies.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_qtJqn5LVU5LN/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [9] HUMAN-USER prompt · 2026-08-21 15:37:45 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [10] SYSTEM-USER prompt · 2026-08-21 15:49:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This research reviews academic literature to understand what makes open-source software projects survive when founders leave, finding that knowledge concentration (bus factor) is critical but the right amount of knowledge overlap among developers may follow an inverted-U shape where both too little and too much redundancy harm survival.' is too long (at most 250 characters, got 338)
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
