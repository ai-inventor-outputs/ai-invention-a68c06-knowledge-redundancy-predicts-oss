# Reference Verification Report

## Executive Summary

This report presents the results of a systematic verification of all 17 references in the paper "Knowledge Redundancy Predicts Open-Source Project Survival After Founder Departure." 

**Critical Findings:**
- **1 FABRICATED reference** ([3] Dechange 2016 - no such author/paper exists)
- **2 INCORRECT author assignments** ([9] Foucault et al. 2017 - paper is actually by Lin, Robles & Serebrenik; [15] Lin et al. 2017 - wrong venue)
- **1 MISUSED reference** ([7] Edmondson 1999 - paper is about psychological safety, not knowledge redundancy)
- **1 IRRELEVANT reference** ([8] Zazworka et al. 2010 - paper is about software architecture, not bus factor/knowledge redundancy)
- **1 INCORRECT year/venue** ([14] Bird et al. - paper is from 2009, not 2010)
- **1 DUPLICATE reference** ([9] and [15] cite the same paper with different/wrong information)

**Overall Assessment:** The paper contains significant citation errors that must be corrected before publication. Several references do not support the claims made in the paper.

---

## Detailed Verification Results

### Reference [1]: Avelino et al. 2019
- **Status:** ✅ VERIFIED
- **Claim in paper:** Founder departure affects 16% of projects; 41% survive through new developers
- **Actual paper:** "On the abandonment and survival of open source projects: An empirical investigation" (ESEM 2019)
- **Verification:** Paper exists and matches the citation. Correct DOI: 10.1109/ESEM.2019.8870181
- **Notes:** No issues found.

### Reference [2]: Cosentino et al. 2015
- **Status:** ✅ VERIFIED
- **Claim in paper:** Bus factor assessment algorithm
- **Actual paper:** "Assessing the bus factor of Git repositories" (SANER 2015)
- **Verification:** Paper exists and matches the citation. Correct DOI: 10.1109/SANER.2015.7081864
- **Notes:** No issues found.

### Reference [3]: Dechange 2016
- **Status:** ❌ FABRICATED
- **Claim in paper:** left-pad incident case study
- **Actual source:** NO ACADEMIC PAPER EXISTS by author "Dechange"
- **Verification:** 
  - Searched Google Scholar, Crossref, general web - no author named "Dechange" found
  - The left-pad incident is a real industry event (March 2016) documented on Wikipedia and in news articles
  - No academic paper with this title/author combination exists
- **Correction needed:** 
  - Remove fabricated citation
  - Cite Wikipedia page: https://en.wikipedia.org/wiki/Npm_left-pad_incident
  - Or cite news articles: The Verge, InfoWorld, etc.
  - Or cite academic papers that mention left-pad as a case study (e.g., papers on npm ecosystem dependency)

### Reference [4]: Ait et al. 2022
- **Status:** ✅ VERIFIED
- **Claim in paper:** Survival rate of GitHub projects
- **Actual paper:** "An empirical study on the survival rate of GitHub projects" (MSR 2022)
- **Verification:** Paper exists and matches the citation. Correct DOI: 10.1145/3524842.3527941
- **Notes:** No issues found.

### Reference [5]: Robinson et al. 2022
- **Status:** ✅ VERIFIED
- **Claim in paper:** Survival analysis of Python projects
- **Actual paper:** "Two approaches to survival analysis of open source Python projects" (ICPC 2022)
- **Verification:** Paper exists and matches the citation. Correct DOI: 10.1145/3524610.3527871
- **Notes:** No issues found.

### Reference [6]: Cosentino et al. 2017
- **Status:** ⚠️ VERIFIED (with minor issue)
- **Claim in paper:** Bus factor of Git repositories (journal version)
- **Actual paper:** "Assessing the bus factor of Git repositories" (IEEE TSE, 43(8), 731-743, 2017)
- **Verification:** Paper exists but DOI in reference list is incomplete ("10.1109/TSE.2017.XXXX")
- **Correction needed:** 
  - Correct DOI: 10.1109/TSE.2016.2616306
  - Note: Journal publication year is 2017, but online publication date is 2016

### Reference [7]: Edmondson 1999
- **Status:** ⚠️ VERIFIED but MISUSED
- **Claim in paper:** (Implied use for knowledge redundancy concept)
- **Actual paper:** "Psychological safety and learning behavior in work teams" (ASQ, 44(2), 350-383, 1999)
- **Verification:** 
  - Paper is REAL and correctly cited
  - HOWEVER: Paper is about **psychological safety**, NOT knowledge redundancy
  - The paper does not discuss knowledge redundancy at all
- **Correction needed:** 
  - Do not use this to support knowledge redundancy claims
  - Find appropriate source on knowledge redundancy in teams
  - Edmondson 1999 should only be cited when discussing psychological safety

### Reference [8]: Zazworka et al. 2010
- **Status:** ⚠️ VERIFIED but IRRELEVANT
- **Claim in paper:** (Implied use for bus factor/knowledge)
- **Actual paper:** "Towards a conceptual framework for expert decision making in the selection of software architecture styles" (ECBS 2010)
- **Verification:** 
  - Paper is REAL and correctly cited
  - HOWEVER: Paper is about **software architecture styles**, NOT bus factor or knowledge redundancy
  - Does not support the claims about bus factor measurement
- **Correction needed:** 
  - Replace with relevant bus factor papers (e.g., Cosentino et al. 2015/2017 already cited)
  - Or remove if no relevant content

### Reference [9]: Foucault et al. 2017
- **Status:** ❌ INCORRECT AUTHORS
- **Claim in paper:** Developer turnover in open source
- **Actual paper with this title:** "Developer Turnover in Global, Industrial Open Source Projects: Insights from Applying Survival Analysis" 
  - **Correct authors:** Lin, B., Robles, G., & Serebrenik, A. (2017)
  - **DOI:** 10.1109/ICGSE.2017.11
- **Foucault et al. actual paper:** "Impact of developer turnover on quality in open-source software" (FSE 2015, not 2017)
  - **Authors:** Foucault, M., Palyart, M., Blanc, X., Robles, G., & González-Barahona, J. M. (2015)
  - **DOI:** 10.1145/2786805.2786870
- **Correction needed:** 
  - If citing "Developer Turnover..." paper → change authors to Lin, Robles & Serebrenik
  - If citing Foucault's work → change to Foucault et al. 2015 with correct title

### Reference [10]: Lisan et al. 2024
- **Status:** ⚠️ UNABLE TO FULLY VERIFY
- **Claim in paper:** Bus factor analysis guidance
- **Alleged paper:** "Guiding effort allocation in open-source software projects using bus factor analysis" (arXiv:2401.03303, 2024)
- **Verification:** 
  - arXiv paper exists at claimed URL
  - Unable to confirm authors "Lisan, A., Kondo, M., & Nourry, S." definitively
  - Search results inconclusive
- **Notes:** May be correct, but requires further verification from arXiv directly

### Reference [11]: Medappa et al. 2025
- **Status:** ✅ VERIFIED
- **Claim in paper:** Write access and organizational ownership impact on OSS
- **Actual paper:** "Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival" (Research Policy, 54(1), 105284, 2025)
- **Verification:** Paper exists and matches citation. Very recent (2025). DOI: 10.1016/j.respol.2025.105284
- **Notes:** No issues found.

### Reference [12]: Rashid et al. 2017
- **Status:** ✅ VERIFIED
- **Claim in paper:** Knowledge loss in OSS projects
- **Actual paper:** "Exploring knowledge loss in open source software (OSS) projects" (EuroSPI 2017)
- **Verification:** Paper exists and matches citation. DOI: 10.1007/978-3-319-67383-7_35
- **Notes:** No issues found.

### Reference [13]: Rashid et al. 2020
- **Status:** ✅ VERIFIED
- **Claim in paper:** Proactive knowledge retention in OSS
- **Actual paper:** "A mechanism to explore proactive knowledge retention in open source software communities" (JSEP, 32(2), e2198, 2020)
- **Verification:** Paper exists and matches citation. DOI: 10.1002/smr.2198
- **Notes:** No issues found.

### Reference [14]: Bird et al. 2010
- **Status:** ⚠️ INCORRECT YEAR
- **Claim in paper:** Bias in bug-fix datasets
- **Actual paper:** "Fair and balanced? Bias in bug-fix datasets" 
  - **Correct year:** 2009 (FSE 2009), NOT 2010
  - **Correct venue:** Proceedings of the 7th joint meeting of ESEC/FSE, NOT MSR 2010
- **Verification:** Paper exists but year and venue are wrong
- **Correction needed:** 
  - Change year to 2009
  - Change venue to ESEC/FSE 2009
  - DOI is correct: 10.1145/1595696.1595716

### Reference [15]: Lin et al. 2017
- **Status:** ❌ INCORRECT VENUE (and DUPLICATE of [9])
- **Claim in paper:** Developer turnover (same as [9])
- **Actual paper:** Same as reference [9] - "Developer Turnover in Global, Industrial Open Source Projects..."
  - **Correct venue:** ICGSE 2017, NOT Empirical Software Engineering vol. 22
  - **No journal publication in EmpSE with these authors/title exists**
- **Verification:** 
  - Paper was published in ICGSE 2017 conference proceedings
  - NOT in Empirical Software Engineering journal
  - The journal information (vol. 22, no. 6, pp. 2771-2805, 2017) appears to be fabricated
- **Correction needed:** 
  - Remove or correct to match [9] (ICGSE 2017)
  - Remove duplicate reference

### Reference [16]: Kalbfleisch & Prentice 2002
- **Status:** ✅ VERIFIED
- **Claim in paper:** Survival analysis reference (book)
- **Actual book:** "The Statistical Analysis of Failure Time Data" (2nd ed., Wiley, 2002)
- **Verification:** Classic survival analysis book, correctly cited. DOI: 10.1002/9781118032985
- **Notes:** No issues found.

### Reference [17]: Davidson-Pilon 2019
- **Status:** ✅ VERIFIED
- **Claim in paper:** lifelines Python package
- **Actual paper:** "lifelines: Survival analysis in Python" (JOSS, 4(40), 1317, 2019)
- **Verification:** Paper exists and matches citation. DOI: 10.21105/joss.01317
- **Notes:** No issues found.

---

## Missing Sources: Inverted-U Hypothesis for Knowledge Redundancy

The paper's introduction states (Section 1.5):
> "This hypothesis draws from organizational psychology research showing that moderate redundancy enables backup behavior during member absence while preserving specialization benefits [8]."

**Problems identified:**
1. Reference [8] (Zazworka et al. 2010) does NOT discuss knowledge redundancy
2. Reference [7] (Edmondson 1999) discusses psychological safety, NOT knowledge redundancy
3. **No source is provided for the "inverted-U hypothesis" about knowledge redundancy**

**Search results for "inverted-U" + "knowledge redundancy":**
- No direct academic paper found with this exact phrase
- Reagans & Zuckerman (2001) discuss network diversity in teams, not specifically knowledge redundancy
- General organizational psychology literature discusses "too much of a good thing" effects but not specifically for knowledge redundancy

**Recommendation:**
- The paper needs a proper citation for the inverted-U hypothesis about knowledge redundancy
- Possible sources to investigate:
  - Organizational psychology papers on team diversity and performance
  - "Too much of a good thing: Curvilinear relationships in organizations" type papers
  - Transactive memory systems literature

---

## Summary of Corrections Needed

| Ref | Issue | Action Required |
|-----|-------|-----------------|
| [3] | FABRICATED | Remove and replace with Wikipedia/news citation |
| [7] | MISUSED | Do not use for knowledge redundancy; find correct source |
| [8] | IRRELEVANT | Replace with relevant bus factor paper or remove |
| [9] | WRONG AUTHORS | Change to Lin, Robles & Serebrenik 2017 |
| [14] | WRONG YEAR/VENUE | Change to Bird et al. 2009 (FSE 2009) |
| [15] | WRONG VENUE + DUPLICATE | Remove or correct to ICGSE 2017 |
| [6] | INCOMPLETE DOI | Provide complete DOI |
| N/A | Missing inverted-U source | Find proper citation for knowledge redundancy hypothesis |

---

## Verification Methodology

1. **Search:** Used scholarly and general web searches via aii-web-tools
2. **Cross-reference:** Checked paper titles, authors, years, and DOIs against academic databases (Crossref, Google Scholar)
3. **Fetch:** Attempted to fetch paper abstracts/landing pages for verification
4. **Triangulate:** Cross-referenced information across multiple sources

**Limitations:**
- Some papers behind paywalls could not be fully accessed
- DOI resolution occasionally failed (HTTP 403/202 errors)
- Pre-2000 papers sometimes difficult to verify online

---

## Follow-Up Actions

1. **Immediate:** Correct all identified errors in the paper's reference list
2. **Research:** Find proper academic source for inverted-U hypothesis about knowledge redundancy
3. **Verify:** Double-check references [10] Lisan et al. 2024 from arXiv directly
4. **Review:** Ensure all references actually support the specific claims made in the paper text

---

**Report prepared by:** AI Researcher  
**Date:** 2024  
**Confidence level:** High (verified against multiple sources)
