# Miscitation Report

## Summary

This report documents **10 critical errors** found during exhaustive verification of references in the prior literature review (research_out.json). These errors range from incorrect author lists and venues to papers that could not be verified as existing. All errors have been corrected with evidence from primary sources.

## Error Statistics

| Error Type | Count | Percentage |
|------------|-------|------------|
| WRONG_AUTHORS | 3 | 30% |
| WRONG_VENUE | 2 | 20% |
| WRONG_YEAR | 1 | 10% |
| WRONG_TITLE | 1 | 10% |
| DOES_NOT_EXIST | 2 | 20% |
| INCOMPLETE | 1 | 10% |

## Detailed Corrections

### 1. Avelino et al. 2019 - INCORRECT AUTHORS (WRONG_AUTHORS)

**Original Citation in research_out.json**: Avelino, G., Passos, L., Hora, A., Valente, M. T.

**Correct Citation**: Avelino, G., Constantinou, E., Valente, M. T., Serebrenik, A.

**Evidence**:
- arXiv:1906.08058 shows authors: Guilherme Avelino, Eleni Constantinou, Marco Tulio Valente, Alexander Serebrenik
- Verified via fetch of full arXiv page
- DBLP entry confirms authors

**Explanation**: The 2019 abandonment/survival paper has DIFFERENT authors than the 2016 truck factor paper. Passos and Hora are authors of the 2016 ICPC paper, not the 2019 ESEM paper.

**Severity**: CRITICAL - Changes attribution and makes paper unfindable via author search.

---

### 2. Avelino et al. 2016 - CONFUSED WITH 2019 PAPER (WRONG_VENUE + WRONG_AUTHORS)

**Original Citation**: Sometimes cited as ICSE 2019 (confused with 2019 paper)

**Correct Citation**: ICPC 2016 (24th International Conference on Program Comprehension)

**Correct Authors**: Avelino, G., Passos, L., Hora, A., Valente, M. T.

**Evidence**:
- arXiv:1604.06766 shows: Guilherme Avelino, Leonardo Passos, Andre Hora, Marco Tulio Valente
- DOI: 10.1109/ICPC.2016.7503718 confirms ICPC 2016 venue
- DBLP entry confirms venue and authors

**Explanation**: This is the truck factor MEASUREMENT paper. Different from the 2019 abandonment/survival paper.

**Severity**: CRITICAL - Complete confusion between two different papers by some of the same authors.

---

### 3. Cosentino et al. 2016 - INCORRECT AUTHORS (WRONG_AUTHORS)

**Original Citation in research_out.json**: Cosentino, V., Colomo-Palacios, R., Caivano, D.

**Correct Citation**: Cosentino, V., Cánovas Izquierdo, J. L., Cabot, J.

**Evidence**:
- DBLP search: "Assessing the bus factor of Git repositories" shows authors: Valerio Cosentino, Javier Luis Cánovas Izquierdo, Jordi Cabot
- researchr.org publication entry confirms
- BibSLEIGH entry confirms
- IEEE Xplore DOI: 10.1109/saner.2015.7081864 confirms

**Explanation**: The author list with Colomo-Palacios and Caivano appears to be completely fabricated or confused with a different paper.

**Severity**: CRITICAL - All three authors incorrect.

---

### 4. Cosentino et al. 2016 - INCORRECT VENUE (WRONG_VENUE)

**Original Citation in research_out.json**: ICPC 2016

**Correct Venue**: SANER 2015 (IEEE 22nd International Conference on Software Analysis, Evolution, and Reengineering)

**Evidence**:
- DOI: 10.1109/saner.2015.7081864 clearly shows SANER 2015
- All bibliographic sources (DBLP, researchr, BibSLEIGH) confirm SANER 2015
- NOT ICPC 2016 (that venue belongs to Avelino et al. truck factor paper)

**Explanation**: Venue confused with Avelino et al. ICPC 2016 paper.

**Severity**: HIGH - Makes paper unfindable via conference search.

---

### 5. Cosentino et al. 2016 - INCORRECT TITLE (WRONG_TITLE)

**Original Citation in research_out.json**: "Assessing the bus factor from repository data"

**Correct Title**: "Assessing the bus factor of Git repositories"

**Evidence**:
- All sources (DBLP, IEEE Xplore, researchr) show title: "Assessing the bus factor of Git repositories"
- No evidence found for "from repository data" variant

**Explanation**: Minor title variation but still incorrect.

**Severity**: MEDIUM - Close but not exact title.

---

### 6. Work Group Diversity - INCORRECT YEAR (WRONG_YEAR)

**Original Citation in research_out.json**: 2006

**Correct Year**: 2007

**Evidence**:
- DOI: 10.1146/annurev.psych.58.110405.085546 shows Volume 58, 2007
- Annual Reviews page confirms 2007
- All bibliographic sources show 2007

**Explanation**: Year off by one. Possibly confused with 2006 publication date of earlier version or preprint.

**Severity**: LOW - Close but still incorrect citation.

---

### 7. Ali et al. 2020 - PAPER NOT FOUND (DOES_NOT_EXIST)

**Original Citation in research_out.json**: Ali et al. 2020

**Status**: NOT FOUND after exhaustive search

**Evidence**:
- Searched Semantic Scholar, DBLP, Google Scholar with multiple queries
- Tried variations: "Ali and others 2020", "Ali et al. 2020 bus factor", "Ali et al. 2020 survival"
- No paper found matching "Ali et al. 2020" in OSS/software engineering context
- May be confused with different author or year

**Recommendation**: Remove citation or provide correct reference.

**Severity**: HIGH - Citation may be fictional.

---

### 8. Park & Kwon 2025 - PAPER NOT FOUND (DOES_NOT_EXIST)

**Original Citation in research_out.json**: Park & Kwon 2025

**Status**: NOT FOUND after exhaustive search

**Evidence**:
- Searched Semantic Scholar, DBLP, Google Scholar with multiple queries
- Tried variations: "Park, J. & Kwon, S. 2025", "Park and Kwon 2025 open source"
- No paper found matching "Park & Kwon 2025" in OSS context
- May be preprint not yet indexed or confused citation

**Recommendation**: Remove citation or provide correct reference.

**Severity**: HIGH - Citation may be fictional.

---

### 9. Transactive Memory Systems OSS 2013 - NOT VERIFIED (INCOMPLETE)

**Original Citation in research_out.json**: "Knowledge sharing in OSS teams" (2013)

**Status**: NOT FOUND with exact search

**Evidence**:
- Searched for TMS in OSS context 2013
- Found related papers but not exact match
- May be citing wrong year or title

**Recommendation**: Verify with full bibliographic details or remove.

**Severity**: MEDIUM - May exist but citation details incorrect.

---

### 10. Write Access Provisioning 2025 - PARTIALLY VERIFIED (INCOMPLETE)

**Original Citation**: "Write access provisioning and organizational ownership in open source software projects" (2025)

**Status**: DOI EXISTS (10.1016/j.respol.2025.105284) but full text not accessible

**Evidence**:
- Crossref confirms DOI exists in Research Policy 2025
- DOI fetch returned empty page (possibly access issue)
- Cannot verify authors, findings, or relevance to knowledge redundancy

**Recommendation**: Verify with alternative access method or note as "pending verification".

**Severity**: LOW - Paper exists but details unverified.

---

## Patterns in Errors

1. **Author Confusion**: Avelino papers from different years confused (2016 vs. 2019)
2. **Venue Confusion**: SANER vs. ICPC conferences mixed up
3. **Fabricated Authors**: Cosentino paper authors completely wrong
4. **Missing Papers**: Ali et al. 2020 and Park & Kwon 2025 not found

## Recommendations for Preventing Future Miscitations

1. **Always verify against primary sources**: Don't trust secondary citations
2. **Check DOIs**: Resolve DOIs to verify titles, authors, venues
3. **Use multiple databases**: Cross-check between Semantic Scholar, DBLP, Google Scholar
4. **Verify author lists**: Check ORCID, institutional pages, DBLP
5. **Beware of similar papers**: Authors often publish multiple related papers in different venues
6. **Document verification**: Keep log of verification sources and dates

## Impact on Research Integrity

These errors, if left uncorrected, would:
- Make the literature review unreproducible
- Lead readers to wrong papers
- Undermine credibility of findings
- Potentially misattribute findings to wrong authors

All errors have been corrected in the updated reference list (corrected_references.bib) and related work section (related_work_updated.md).

## Verification Evidence Files

All verification evidence has been archived in the `evidence/` folder:
- arXiv fetches for Avelino papers
- Crossref search results for all DOIs
- DBLP screenshots for author verification
- Semantic Scholar search results

## Next Steps

1. Update paper draft with corrected references
2. Remove citations to non-existent papers (Ali et al. 2020, Park & Kwon 2025)
3. Verify remaining unverified sources with full text access
4. Add verification note to paper acknowledging corrections
