# Reference Verification Log

## Date: 2026-08-21

## Verification Status Summary

### CRITICAL ERRORS FOUND:

1. **Avelino et al. 2019 paper** - PARTIALLY INCORRECT:
   - **Claimed in research_out.json**: Authors: Avelino, G., Passos, L., Hora, A., Valente, M. T.
   - **ACTUAL AUTHORS (arXiv:1906.08058)**: Avelino, G., Constantinou, E., Valente, M. T., Serebrenik, A.
   - **ERROR**: Passos and Hora are NOT authors of the 2019 abandonment/survival paper
   - **Correct Paper**: "On the abandonment and survival of open source projects: An empirical investigation"
   - **Venue**: Published at ESEM 2019 (not ICSE 2019 as sometimes cited)
   - **DOI**: 10.1109/esem.2019.8870181 (from Crossref search result)
   - **Verification**: ✓ 16% abandonment rate verified, ✓ 41% survival rate verified

2. **Avelino et al. 2016 paper** - CONFUSED WITH 2019 PAPER:
   - **Correct 2016 paper**: "A novel approach for estimating Truck Factors"
   - **Authors**: Avelino, G., Passos, L., Hora, A., Valente, M. T. (THIS is the paper with Passos and Hora)
   - **Venue**: ICPC 2016
   - **DOI**: 10.1109/ICPC.2016.7503718
   - **This is the truck factor measurement paper, NOT the abandonment/survival paper**

3. **Cosentino et al. 2016 paper** - AUTHOR LIST INCORRECT:
   - **Claimed in research_out.json**: Cosentino, V., Colomo-Palacios, R., Caivano, D.
   - **ACTUAL AUTHORS (from searches)**: Cosentino, V., Cánovas Izquierdo, J. L., Cabot, J.
   - **Title**: "Assessing the bus factor of Git repositories" (NOT "from repository data")
   - **Venue**: SANER 2015 (NOT ICPC 2016)
   - **DOI**: 10.1109/saner.2015.7081864
   - **NOTE**: The title "Assessing the bus factor from repository data" may not exist - needs further verification

4. **Write access provisioning 2025 paper** - EXISTS BUT NEEDS VERIFICATION:
   - **Found**: DOI 10.1016/j.respol.2025.105284 in Research Policy 2025
   - **Title**: "Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival"
   - **Status**: DOI fetch returned empty (1 char), needs alternative access method
   - **Relevance to knowledge redundancy**: UNKNOWN - needs full text verification

## Verification Checklist Progress

### Phase 1.1: Core References

- [ ] Avelino et al. 2019 (abandonment/survival) - PARTIALLY VERIFIED (authors incorrect in research_out.json)
- [ ] Cosentino et al. 2016 (bus factor) - INCORRECT (wrong authors, wrong venue, possibly wrong title)
- [ ] Write access provisioning 2025 - FOUND but not fully verified
- [ ] ESEC/FSE 2023 (diversity and survival) - NOT YET VERIFIED

### Phase 1.2: All 23 Sources in research_out.json

NEEDS SYSTEMATIC VERIFICATION - many sources not yet checked

### Phase 1.3: Specific Miscitations

- [ ] Ali et al. 2020 - NOT YET SEARCHED
- [ ] Park & Kwon 2025 - NOT YET SEARCHED

## Next Steps

1. Verify the ESEC/FSE 2023 paper (Source 13 in research_out.json)
2. Search for Ali et al. 2020 and Park & Kwon 2025
3. Systematically verify all 23 sources
4. Correct the reference list
5. Search for peer-reviewed alternatives to non-academic sources
6. Conduct comprehensive literature search for knowledge overlap papers
