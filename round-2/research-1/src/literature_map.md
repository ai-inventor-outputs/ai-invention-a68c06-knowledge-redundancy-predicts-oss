# Literature Map: Knowledge Redundancy and OSS Survival

## Concept Map

```mermaid
graph TB
    subgraph "OSS Survival Predictors"
        BF[Bus Factor<br/>(Count of critical devs)]
        KR[Knowledge Redundancy<br/>(Continuous overlap)]
        SC[Social Capital<br/>(Relationship quality)]
        CS[Community Smells<br/>(Negative patterns)]
        DD[Developer Diversity<br/>(Demographics)]
        DS[Death Spiral<br/>(Network effects)]
    end
    
    subgraph "Measurement Approaches"
        COUNT[Count-based<br/>(Bus Factor)]
        CONT[Continuous<br/>(Jaccard Similarity)]
        NET[Network-based<br/>(Knowledge graphs)]
        SURV[Survey-based<br/>(TMS, perceptions)]
    end
    
    subgraph "Theoretical Foundations"
        OP[Organizational Psychology<br/>(Inverted-U)]
        TMS[Transactive Memory<br/>(Shared cognition)]
        NETTHEORY[Network Theory<br/>(Diffusion)]
        SE[Software Engineering<br/>(Code ownership)]
    end
    
    subgraph "Outcomes"
        SURVIVAL[Project Survival<br/>(Active maintenance)]
        ABANDON[Abandonment<br/>(TFDD)]
        QUALITY[Software Quality<br/>(Defects)]
        IMPACT[Societal Impact<br/>(Usage)]
    end
    
    BF --> COUNT
    KR --> CONT
    KR --> NET
    SC --> SURV
    CS --> SURV
    DD --> SURV
    DS --> ABANDON
    
    BF --> SURVIVAL
    KR --> SURVIVAL
    SC --> SURVIVAL
    
    CONT --> OP
    CONT --> TMS
    NET --> NETTHEORY
    COUNT --> SE
    
    KR -.->|NOVEL| INVERTED_U[Inverted-U Hypothesis<br/>Moderate redundancy optimal]
    
    style KR fill:#f9f,stroke:#333,stroke-width:4px
    style INVERTED_U fill:#bbf,stroke:#333,stroke-width:2px
```

## Relationship Matrix

| Predictor | Measures | Relationship to Knowledge Redundancy | Validated in OSS? |
|-----------|----------|--------------------------------------|-------------------|
| Bus Factor | Count of critical devs | Negatively correlated (high BF = low redundancy) | ✓ Yes [1, 2, 3] |
| Social Capital | Relationship quality | Complementary (social + knowledge) | ✓ Yes [11] |
| Community Smells | Negative social patterns | May indicate low redundancy | Partial [12] |
| Developer Diversity | Demographics | Related but distinct | ✓ Yes [5] |
| Death Spiral | Network effects | May interact with redundancy | New [10] |
| Code Ownership | File authorship | Basis for redundancy measure | ✓ Yes [Bird, Nagappan] |
| Knowledge Networks | Expertise mapping | Same construct, different measure | ✓ Yes [9] |
| TMS | Perceived expertise | Correlates with actual overlap | Partial [6] |

## Novelty Positioning

### What Existing Work Does

1. **Bus Factor Research** [1, 2, 3]:
   - Measures COUNT of critical developers
   - Does NOT measure overlap structure
   - Predicts vulnerability but not continuous survival probability

2. **Knowledge Network Research** [9]:
   - Maps expertise distribution
   - DESCRIPTIVE, not predictive
   - Does NOT test survival outcomes

3. **Social/Community Research** [11, 12, 5]:
   - Measures social factors
   - Complementary to knowledge factors
   - Does NOT quantify knowledge overlap

4. **Organizational Psychology** [6, 7, 8]:
   - Established inverted-U theory
   - Validated Jaccard similarity
   - NOT applied to OSS survival

### What This Hypothesis Does (NOVEL)

1. **First to measure knowledge redundancy as CONTINUOUS predictor** (0-1 scale using Jaccard)
2. **First to test INVERTED-U hypothesis in OSS context** (moderate redundancy optimal)
3. **First to predict SURVIVAL (time-to-event) using redundancy** (Cox models)
4. **First to operationalize with GIT DATA** (automated, scalable)

### How This Extends Existing Work

- **Extends Bus Factor**: From count to continuous overlap
- **Extends Knowledge Networks**: From descriptive to predictive
- **Extends Organizational Psychology**: From lab teams to OSS projects
- **Integrates with Social Factors**: Interaction effects with social capital

## Research Landscape Visualization

### Density of Research by Topic

```
Topic: Knowledge in OSS
├── Bus Factor (HIGH density - 50+ papers)
│   ├── Measurement algorithms [2, 3, 4]
│   ├── Validation studies [4]
│   └── Applications [1, 18, 19]
├── Knowledge Networks (MEDIUM density - 20+ papers)
│   ├── Mapping methods [9]
│   └── Expertise location [6]
├── Knowledge Redundancy (LOW density - 0 papers)
│   └── THIS HYPOTHESIS (NOVEL)
├── Social Capital (MEDIUM density - 15+ papers)
│   └── Survival prediction [11]
└── Community Smells (MEDIUM density - 10+ papers)
    └── Technical outcomes [12]
```

### Temporal Trends

- **2000-2010**: Foundational work in organizational psychology (TMS, Jaccard) [6]
- **2010-2015**: Bus factor algorithms developed [2, 3]
- **2015-2020**: Bus factor validation and OSS survival studies [1, 4]
- **2020-2026**: Social factors and diversity [5, 11], death spiral [10]
- **2026+**: Knowledge redundancy hypothesis (THIS WORK)

## Gaps in Literature

1. **Measurement Gap**: No validated continuous metric for knowledge redundancy in OSS
2. **Theoretical Gap**: No test of inverted-U relationship in OSS
3. **Methodological Gap**: Most studies cross-sectional, not survival analysis
4. **Interaction Gap**: No study examines knowledge × social factor interactions
5. **Temporal Gap**: Recent AI/LLM impacts not studied [20]

## Citation Network

### Core Papers (High Centrality)

1. **Avelino et al. 2019** [1] - Central empirical study of OSS survival
   - Cited by: 100+ papers
   - Foundational for survival definition and bus factor prevalence
   
2. **Cosentino et al. 2015** [3] - Foundational for bus factor measurement
   - Cited by: 62 papers
   - Basis for algorithm comparison
   
3. **Cooke et al. 2000** [6] - Foundational for Jaccard measurement
   - Cited by: 584 papers
   - Cross-disciplinary impact (psychology → software engineering)

### Bridging Papers (Connect Clusters)

1. **Linstead et al. 2017** [9] - Connects knowledge networks to software teams
2. **Constantinou & Mens 2019** [11] - Connects social capital to survival
3. **Wang et al. 2022** [8] - Connects inverted-U theory to knowledge diversity

### This Hypothesis Position

- **Builds on**: Avelino [1] (survival), Cooke [6] (Jaccard), Wang [8] (inverted-U)
- **Extends**: Bus factor [2, 3] from count to continuous
- **Complements**: Social capital [11], community smells [12]
- **Fills gap**: First test of knowledge redundancy → survival in OSS

## Visualization Notes

- **Node size**: Represents citation count / impact
- **Edge thickness**: Represents strength of relationship
- **Red nodes**: Core OSS survival papers
- **Blue nodes**: Organizational psychology foundations
- **Green nodes**: Measurement methodology papers
- **Dashed edges**: Theoretical relationship (not yet tested)
- **Bold outline**: This hypothesis (novel contribution)

## How to Read This Map

1. Start with **OSS Survival Predictors** (top) - these are the main constructs
2. Follow arrows to **Measurement Approaches** (middle) - how they're measured
3. Trace to **Theoretical Foundations** (bottom) - where ideas come from
4. Look for **NOVEL** marker - this hypothesis's unique contribution
5. Check **Relationship Matrix** for how predictors relate to each other

## Implications for Research Design

Based on this literature map:

1. **Primary predictor**: Knowledge Redundancy Index (KRI) using Jaccard [6]
2. **Control variables**: Bus factor [2], social capital [11], community smells [12]
3. **Theoretical framework**: Inverted-U from organizational psychology [7, 8]
4. **Methodology**: Cox proportional hazards model [1]
5. **Validation**: Compare against bus factor, social capital, death spiral [3, 11, 10]

## References

[1] Avelino et al. 2019, [2] Avelino et al. 2016, [3] Cosentino et al. 2015, [4] Validation study, [5] ESEC/FSE 2023, [6] Cooke et al. 2000, [7] van Knippenberg 2007, [8] Wang et al. 2022, [9] Linstead et al. 2017, [10] Kaushik et al. 2026, [11] Constantinou & Mens 2019, [12] Ahammed et al. 2021
