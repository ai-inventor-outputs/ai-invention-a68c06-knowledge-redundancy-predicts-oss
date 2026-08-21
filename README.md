# Knowledge Redundancy as a Predictor of Open-Source Project Survival: A Methodological Validation Study

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss@fork/run_qtJqn5LVU5LN/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss@fork/run_qtJqn5LVU5LN/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — This methodological validation study introduces knowledge redundancy (measured via Jaccard similarity of file modifications) as a candidate predictor of open-source project survival after founder departure. Testing the inverted-U hypothesis on 1,000 synthetic GitHub repositories using Cox proportional hazards models, the study finds no evidence for the hypothesized relationship: the quadratic term is not significant (p = 0.71), and survival rate differences are small (1-3%). The paper provides open-source tools for computing knowledge redundancy, honestly reports null results, and outlines future steps for real-data validation.

<details>
<summary>Full hypothesis</summary>

The relationship between knowledge redundancy (overlap in contributor expertise measured via Jaccard similarity of file modifications) and open-source project survival after founder departure can be measured and tested using Cox proportional hazards models, but the hypothesized inverted-U shaped relationship is not supported by synthetic data validation (quadratic term p=0.71). Knowledge redundancy is computable at scale from git histories and provides a distinct metric from bus factor (r=-0.34, p<0.001), but its relationship to survival requires validation on real GitHub data. The null result on synthetic data suggests either: (1) the inverted-U relationship does not exist in OSS contexts, (2) the effect size is smaller than hypothesized (<5% difference in survival rates), or (3) the measurement approach requires refinement to capture true expertise overlap beyond file modification patterns.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss@fork/run_qtJqn5LVU5LN/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/paper_latex)

This repository contains all **6 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[OSS Survival Literature Review: Knowledge Redundancy and Bus…](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/blob/fork/run_qtJqn5LVU5LN/round-1/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-1/src) | — |
| **[GitHub OSS founder departure survival dataset](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/dataset-1) | — | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/dataset-1/src) | — |
| **[Knowledge redundancy measurement and survival analysis valid…](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-2)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-2) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/blob/fork/run_qtJqn5LVU5LN/round-1/research-2/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-2/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[GitHub OSS survival dataset search](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/blob/fork/run_qtJqn5LVU5LN/round-2/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/dataset-1/src) | — |
| **[Cox survival analysis for OSS project survival](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/blob/fork/run_qtJqn5LVU5LN/round-2/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/experiment-1/src) | <sub><i>uses:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/dataset-1)</sub> |
| **[Exhaustive reference verification and novelty refinement for…](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/blob/fork/run_qtJqn5LVU5LN/round-2/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-2/research-1/src) | <sub><i>extends:</i><br/>[research‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss/tree/fork/run_qtJqn5LVU5LN/round-1/research-1)</sub> |

## Repository Structure

Artifacts are grouped by the round of invention that produced them. Each
artifact has its own folder with source code and a self-contained demo:

```
.
├── round-1/                         # One folder per round of invention
│   ├── experiment-1/
│   │   ├── README.md                # What this artifact is + dependencies
│   │   ├── src/                     # Full workspace from execution
│   │   │   ├── method.py            # Main implementation
│   │   │   ├── method_out.json      # Full output data
│   │   │   └── ...                  # All execution artifacts
│   │   └── demo/                    # Self-contained demo
│   │       └── method_code_demo.ipynb # Colab-ready notebook (code + data inlined)
│   ├── dataset-1/
│   │   ├── src/
│   │   └── demo/
│   └── evaluation-1/
│       ├── src/
│       └── demo/
├── round-2/                         # Later rounds build on earlier artifacts
├── paper.pdf                        # Research paper
├── paper_latex/                     # LaTeX source files
├── chat/                            # Every prompt, response and tool call, per module
├── workflow.svg                     # Artifact dependency diagram (this page's header)
└── README.md
```

## Running Notebooks

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badges above to run notebooks directly in your browser.
No installation required!

### Option 2: Local Jupyter

```bash
# Clone the repo
git clone https://github.com/ai-inventor-outputs/ai-invention-a68c06-knowledge-redundancy-predicts-oss
cd ai-invention-a68c06-knowledge-redundancy-predicts-oss

# Install dependencies
pip install jupyter

# Run any artifact's demo notebook
jupyter notebook <artifact_folder>/demo/
```

## Source Code

The original source files are in each artifact's `src/` folder.
These files may have external dependencies - use the demo notebooks for a self-contained experience.

---
*Generated by AI Inventor Pipeline - Automated Research Generation*
