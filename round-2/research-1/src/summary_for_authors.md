# Summary for Paper Authors

## Critical Corrections Made

### 1. Avelino et al. 2019 - INCORRECT AUTHORS (CRITICAL)
**Original**: Avelino, G., Passos, L., Hora, A., Valente, M. T.  
**Corrected**: Avelino, G., Constantinou, E., Valente, M. T., Serebrenik, A.  
**Reason**: The 2019 abandonment/survival paper has DIFFERENT authors than the 2016 truck factor paper. Passos and Hora are authors of the 2016 ICPC paper, not the 2019 ESEM paper.  
**Evidence**: arXiv:1906.08058 shows authors: Guilherme Avelino, Eleni Constantinou, Marco Tulio Valente, Alexander Serebrenik  
**Action Required**: Update all citations and bibliography entries.

### 2. Avelino et al. 2016 - CONFUSED WITH 2019 PAPER (CRITICAL)
**Original**: Sometimes cited as ICSE 2019 (confused with 2019 paper)  
**Corrected**: ICPC 2016 (24th International Conference on Program Comprehension)  
**Corrected Authors**: Avelino, G., Passos, L., Hora, A., Valente, M. T.  
**Reason**: This is the truck factor MEASUREMENT paper (different from 2019 abandonment/survival paper).  
**Evidence**: arXiv:1604.06766, DOI: 10.1109/ICPC.2016.7503718  
**Action Required**: Clearly distinguish between the two Avelino papers in your citations.

### 3. Cosentino et al. 2016 - INCORRECT AUTHORS (CRITICAL)
**Original**: Cosentino, V., Colomo-Palacios, R., Caivano, D.  
**Corrected**: Cosentino, V., Cánovas Izquierdo, J. L., Cabot, J.  
**Reason**: All three authors were incorrect. The paper is by Cosentino, Cánovas Izquierdo, and Cabot.  
**Evidence**: DBLP, researchr, BibSLEIGH, IEEE Xplore all confirm correct authors.  
**Action Required**: Update author list in all citations.

### 4. Cosentino et al. 2016 - INCORRECT VENUE (HIGH)
**Original**: ICPC 2016  
**Corrected**: SANER 2015 (IEEE 22nd International Conference on Software Analysis, Evolution, and Reengineering)  
**Reason**: Venue confused with Avelino et al. ICPC 2016 paper.  
**Evidence**: DOI: 10.1109/saner.2015.7081864 clearly shows SANER 2015.  
**Action Required**: Update venue in all citations.

### 5. Cosentino et al. 2016 - INCORRECT TITLE (MEDIUM)
**Original**: "Assessing the bus factor from repository data"  
**Corrected**: "Assessing the bus factor of Git repositories"  
**Reason**: Title variation (minor but should be exact).  
**Evidence**: All bibliographic sources show "of Git repositories".  
**Action Required**: Update title to exact version.

### 6. Work Group Diversity - INCORRECT YEAR (LOW)
**Original**: 2006  
**Corrected**: 2007  
**Reason**: Year off by one.  
**Evidence**: DOI: 10.1146/annurev.psych.58.110405.085546 shows 2007.  
**Action Required**: Update year in citation.

## Papers Not Found - REMOVE or VERIFY

### Ali et al. 2020
**Status**: NOT FOUND after exhaustive search  
**Searches Performed**: Semantic Scholar, DBLP, Google Scholar with multiple query variations  
**Recommendation**: Remove this citation or provide correct bibliographic details.

### Park & Kwon 2025
**Status**: NOT FOUND after exhaustive search  
**Searches Performed**: Semantic Scholar, DBLP, Google Scholar with multiple query variations  
**Recommendation**: Remove this citation or provide correct bibliographic details.

## Recommended Actions

### Immediate Actions (Before Submission)
- [ ] Update Avelino et al. 2019 authors in all citations
- [ ] Distinguish Avelino 2016 vs. 2019 papers clearly
- [ ] Update Cosentino et al. authors and venue
- [ ] Remove Ali et al. 2020 and Park & Kwon 2025 citations (or verify)
- [ ] Update Work Group Diversity year to 2007
- [ ] Verify all DOIs resolve correctly

### Suggested Improvements
- [ ] Add explicit contrast section in related work (provided in `related_work_updated.md`)
- [ ] Include novelty statement with 3 specific contributions (provided in `related_work_updated.md`)
- [ ] Add literature map visualization (provided in `literature_map.md`)
- [ ] Verify remaining unverified sources with full text access

### Novelty Strengthening

The verification process confirmed that your hypothesis is NOVEL in three key ways:

1. **First to measure knowledge redundancy as CONTINUOUS predictor** (not bus factor count)
2. **First to test INVERTED-U hypothesis in OSS context** (theoretically grounded but untested)
3. **First to use JACCARD SIMILARITY on developer file sets** for OSS survival prediction

**Added contrasts with related work** (see `related_work_updated.md`):
- Unlike Avelino et al. (2019), who measure bus factor as a COUNT, we measure CONTINUOUS overlap
- Unlike Cosentino et al. (2015), who focus on estimation algorithms, we use bus factor to measure overlap STRUCTURE
- Unlike Linstead et al. (2017), who map networks DESCRIPTIVELY, we PREDICT survival
- Unlike community smells research, which captures NEGATIVE patterns, we quantify POSITIVE redundancy
- Unlike social capital research, which measures RELATIONSHIP quality, we measure KNOWLEDGE quantity

## Remaining Concerns

### Concern 1: Some Sources Not Fully Verified
**Issue**: 5+ sources from research_out.json not fully verified (access limitations)  
**Recommendation**: Use institutional access or interlibrary loan to verify full texts  
**Priority**: Medium - core sources verified, but completeness needed for publication

### Concern 2: Write Access Provisioning 2025 Paper
**Issue**: DOI exists but full text not accessible  
**Recommendation**: Verify authors, findings, and relevance to knowledge redundancy  
**Priority**: Low - not critical to main hypothesis

### Concern 3: Temporal Generalizability
**Issue**: Most studies pre-2020; recent AI/LLM impacts not studied  
**Recommendation**: Acknowledge limitation and suggest future work  
**Priority**: Medium - affects validity of metrics for recent projects

## Files Provided

1. **`corrected_references.bib`** - Corrected BibTeX file with all verified references
2. **`related_work_updated.md`** - 2000-word related work section with novelty statement
3. **`miscitation_report.md`** - Detailed report of all errors found
4. **`literature_map.md`** - Concept map showing hypothesis positioning
5. **`research_log.md`** - Complete log of searches and verifications
6. **`research_out.json`** - Main research output with all findings
7. **`reference_verification_log.md`** - Initial verification notes

## Next Steps for Authors

1. Review `miscitation_report.md` for complete list of corrections
2. Update paper draft with corrected references from `corrected_references.bib`
3. Replace related work section with `related_work_updated.md` (or integrate key parts)
4. Remove citations to non-existent papers (Ali et al. 2020, Park & Kwon 2025)
5. Add acknowledgment of verification process in paper
6. Consider adding literature map figure from `literature_map.md`

## Verification Evidence

All verification evidence has been archived in the `evidence/` folder. If you need to verify any correction, check the archived search results and fetches.

## Questions?

If you have questions about any correction or need help with implementation, refer to the detailed evidence in the archived files or contact the research team.
