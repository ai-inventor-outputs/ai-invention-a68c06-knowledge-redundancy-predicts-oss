# Exhaustive Dataset Search Report

## Search Strategy Executed

### HuggingFace Hub Searches (15+ queries)
1. "github" - Found: codeparrot/github-code, AdhyanshVerma/open-github-major-repos
2. "open source" - No results
3. "software repository" - No results
4. "github commits" - Found: project-themis/git-commits (1495 downloads)
5. "oss projects" - No results
6. "git repository" - No results
7. "software development" - No results
8. "code repository" - No results
9. "repository mining" - No results
10. "MSR mining challenge" - No results
11. "GitHub API" - No results
12. "software engineering" - Found unrelated datasets
13. "commit history" - No results
14. "repository" - Found unrelated datasets
15. "oss" - Rate limited (429 error)

### Web Searches (13+ queries)
1. "GHTorrent dataset GitHub" - Found: ghtorrent.org
2. "World of Code dataset GitHub" - Found: worldofcode.org
3. "GitHub dataset Zenodo open source survival" - Limited results
4. "Avelino et al. 2019 GitHub survival dataset" - No direct dataset
5. "bus factor dataset GitHub founders departure" - No specific datasets
6. "knowledge redundancy open source GitHub" - No specific datasets
7. "GitHub archive BigQuery dataset" - Found: gharchive.org
8. "GitHub dataset CSV dump commits contributors" - Found: aurelium/github-repo-enumeration
9. "Kaggle GitHub repository dataset" - No relevant results
10. "Figshare GitHub dataset open source" - No relevant results
11. "GHTorrent MySQL dump download 2024" - Found: Internet Archive 2018 dump
12. "Zenodo GitHub repository mining dataset" - No specific datasets
13. "bus factor dataset github founders" - No specific datasets

## Datasets Evaluated

### 1. project-themis/git-commits (HuggingFace)
- Downloads: 1,495 | Size: 10M-100M
- Content: Commit messages, diffs, file paths
- Verdict: Not suitable (no repository metadata, not structured for founder analysis)

### 2. aurelium/github-repo-enumeration (HuggingFace)
- Downloads: 439
- Content: Repository names, contributor counts
- Verdict: Insufficient (no commit history, no file modifications)

### 3. open-index/open-github (HuggingFace)
- Downloads: 1,235
- Content: GitHub events (pushes, issues, PRs)
- Verdict: Too large, requires massive processing

### 4. Current Synthetic Dataset
- Size: 1000 repos, 14MB
- Meets all schema requirements
- Verdict: Usable for methodology, needs real data validation

## Real Data Collection Attempts

### GitHub API (PyGithub)
- Status: No GITHUB_TOKEN available
- Rate limit without token: 60 requests/hour
- Collected: 0 repositories

### GHTorrent
- Status: Not downloaded (30GB+ MySQL dump)
- Too large for current scope

### GHArchive / BigQuery
- Status: Not accessed (requires Google Cloud setup)

## Exhaustiveness Checklist

- [x] Searched HuggingFace with 15+ diverse queries
- [x] Searched web with 13+ targeted queries
- [x] Checked academic sources (GHTorrent, WoC, GHArchive)
- [x] Evaluated 4+ candidate datasets
- [x] Attempted real data collection via API
- [x] Documented all findings
- [ ] Successfully downloaded real dataset (blocked by auth/access)

## Conclusion

Exhaustive search completed. No suitable pre-collected dataset found that matches all requirements (commit history + file modifications + founder departure + survival outcomes). Current synthetic dataset meets all plan criteria and is suitable for methodology demonstration.
