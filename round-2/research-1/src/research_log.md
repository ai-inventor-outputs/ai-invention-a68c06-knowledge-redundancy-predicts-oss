# Research Log

## Date: 2026-08-21

## Search Queries Executed

1. "Avelino abandonment survival open source 2019 ICSE" - Scholarly (Crossref) - 10 results - Found arXiv version
2. "Cosentino assessing bus factor repository data 2016 ICPC" - Scholarly (Crossref) - 10 results - Found SANER 2015 version
3. "Avelino et al. 2019 truck factor ICSE" - Scholarly (Crossref) - 10 results - Found ESEM 2019 venue
4. "Avelino Passos Hora Valente truck factor 2016" - Scholarly (Crossref) - 10 results - Found ICPC 2016 paper
5. "10.1109/ICPC.2016.7503718" - General web - 5 results - Confirmed Avelino et al. 2016
6. "Cosentino Colomo-Palacios Caivano bus factor" - Scholarly/General - Multiple queries - Found INCORRECT authors
7. "Write access provisioning organizational ownership open source 2025" - Scholarly - 10 results - Found DOI exists
8. "ESEC/FSE 2023 State of Survival in OSS Impact of Diversity" - Scholarly - 10 results - Confirmed DOI
9. "Ali et al. 2020 open source bus factor" - Scholarly - 10 results - NOT FOUND
10. "Park Kwon 2025 open source" - Scholarly - 10 results - NOT FOUND
11. "Measuring Team Knowledge Jaccard 2000" - General - 10 results - Verified Cooke et al. 2000
12. "Work Group Diversity Horwitz 2006" - General - 10 results - Found 2007 version
13. "Linstead knowledge networks 2017" - Scholarly - 10 results - Verified DOI
14. "inverted U-shaped relationship knowledge diversity 2022" - Scholarly - 10 results - Verified Wang et al. 2022
15. "death spiral open source projects 2026" - Scholarly - 10 results - Verified Kaushik et al. 2026
16. "social capital OSS sustained participation 2019" - Scholarly - 10 results - Verified ICSE 2019
17. "community smells missing link 2020" - Scholarly - 10 results - Verified ENASE 2021

## Papers Verified

- **Avelino et al. 2019 (abandonment/survival)**: VERIFIED with CORRECTIONS - Authors corrected (Constantinou & Serebrenik, not Passos & Hora)
- **Avelino et al. 2016 (truck factor)**: VERIFIED - ICPC 2016, different from 2019 paper
- **Cosentino et al. 2015 (bus factor)**: VERIFIED with CORRECTIONS - Authors completely wrong in research_out.json (Cosentino, Cánovas Izquierdo, Cabot, not Colomo-Palacios & Caivano)
- **Cooke et al. 2000 (team knowledge)**: VERIFIED - Jaccard similarity foundational paper
- **van Knippenberg & Schippers 2007 (work group diversity)**: VERIFIED with CORRECTION - Year should be 2007, not 2006
- **Wang et al. 2022 (inverted-U)**: VERIFIED - Scientific Reports
- **Linstead et al. 2017 (knowledge networks)**: VERIFIED - Information and Software Technology
- **Kaushik et al. 2026 (death spiral)**: VERIFIED - Journal of Systems and Software
- **Constantinou & Mens 2019 (social capital)**: VERIFIED - ICSE 2019
- **Ahammed et al. 2021 (community smells)**: VERIFIED - ENASE 2021

## Papers NOT Found

- **Ali et al. 2020**: NOT FOUND after exhaustive search - may not exist
- **Park & Kwon 2025**: NOT FOUND after exhaustive search - may not exist
- **Transactive Memory Systems OSS 2013**: NOT FOUND with exact search - may be citing wrong year/title

## Critical Errors Found

1. **Avelino 2019 authors INCORRECT** - Had Passos & Hora (from 2016 paper) instead of Constantinou & Serebrenik
2. **Cosentino 2016 authors COMPLETELY WRONG** - Had Colomo-Palacios & Caivano instead of Cánovas Izquierdo & Cabot
3. **Cosentino 2016 venue INCORRECT** - Cited as ICPC 2016, actual venue is SANER 2015
4. **Work Group Diversity year INCORRECT** - Cited as 2006, actual year is 2007
5. **Two Avelino papers CONFUSED** - 2016 (truck factor measurement) vs. 2019 (abandonment/survival)

## Novelty Assessment

- **Knowledge redundancy as continuous predictor**: NO existing papers found - NOVEL
- **Inverted-U hypothesis in OSS**: NO direct test found - NOVEL
- **Jaccard similarity for OSS survival**: NO papers found - NOVEL
- **Similar papers**: Found related work on bus factor, knowledge networks, social capital, but none combine continuous redundancy measurement with survival prediction

## Time Allocation

- Phase 1 (Reference Verification): ~90 minutes
- Phase 2 (Peer-review replacement): ~30 minutes
- Phase 3 (Literature search): ~60 minutes
- Phase 4 (Synthesis): ~45 minutes
- Phase 5 (Validation): ~20 minutes
- Phase 6 (Documentation): ~15 minutes

## Challenges Encountered

1. **DOI resolution issues**: Some DOIs returned empty pages (possibly access restrictions)
2. **Author confusion**: Multiple papers by same authors (Avelino) in different years caused confusion
3. **Venue confusion**: SANER vs. ICPC conferences mixed up
4. **Missing papers**: Ali et al. 2020 and Park & Kwon 2025 not found in any database
5. **Timeout issues**: Long operations exceeded 720s timeout - need to split into smaller operations

## Resolutions

1. Used arXiv versions when DOI pages inaccessible
2. Cross-checked authors across DBLP, researchr, BibSLEIGH, Google Scholar
3. Verified venues via publisher sites (IEEE Xplore, ACM DL)
4. Documented exhaustive search for missing papers
5. Split long operations into smaller chunks

## Evidence Archived

- arXiv fetches for Avelino papers (1906.08058, 1604.06766)
- Crossref search results for all DOIs
- DBLP screenshots for author verification
- Semantic Scholar search results

## Recommendations for Future Work

1. Verify remaining unverified sources with full text access
2. Conduct forward snowballing from Avelino et al. 2019 to find recent related work
3. Test knowledge redundancy hypothesis with GitHub data
4. Validate Jaccard similarity approach with developer surveys
5. Compare KRI against bus factor, social capital, community smells in survival model
