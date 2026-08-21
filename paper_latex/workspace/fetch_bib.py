import json

# References from the paper
references = [
    {"title": "On the abandonment and survival of open source projects: An empirical investigation", "author": "Avelino", "year": 2019},
    {"title": "Assessing the bus factor of Git repositories", "author": "Cosentino", "year": 2015},
    {"title": "Going farther together: The impact of social capital on sustained participation in open source", "author": "Qiu", "year": 2019},
    {"title": "A comparative study of algorithms for estimating truck factor", "author": "Ferreira", "year": 2019},
    {"title": "What can OSS mailing lists tell us?", "author": "Rigby", "year": 2007},
    {"title": "Bus factor in practice", "author": "Jabrayilzade", "year": 2022},
    {"arxiv": "2508.09828", "author": "Piccolo", "year": 2025},
    {"title": "Turnover in open-source projects: The case of core developers", "author": "Ferreira", "year": 2020},
    {"title": "Is this GitHub project maintained?", "author": "Coelho", "year": 2020},
    {"title": "Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival", "author": "Miller", "year": 2025},
    {"title": "The state of survival in OSS: The impact of diversity", "author": "Choudhary", "year": 2023},
    {"title": "Transactive memory systems 1985-2010: An integrative framework of key dimensions", "author": "Ren", "year": 2011},
    {"title": "A degree-of-knowledge model to capture source code familiarity", "author": "Fritz", "year": 2010},
    {"title": "Transactive memory: A contemporary analysis of the group mind", "author": "Wegner", "year": 1985},
    {"title": "lifelines: Survival analysis in Python", "author": "Davidson-Pilon", "year": 2019},
]

# Output references as JSON for the skill script
print(json.dumps({"references": references}))
