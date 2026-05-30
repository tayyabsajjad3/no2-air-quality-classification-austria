# Initial vs Final DMP Comparison

This note supports T4.5 by comparing the initial DMP from Part 2 with the final DMP record prepared for WP4.

## Links

- Initial DMP: https://handle.test.datacite.org/10.70124/3gj7h-t2832
- Final DMP: https://doi.org/10.70124/pcepy-07563

## 1. Unrealistic Promises In The Initial DMP

The initial DMP was useful as a first plan, but it treated several FAIR publication steps as simpler than they were in practice. It underestimated the effort needed to coordinate persistent identifiers across GitHub/Zenodo, DBRepo, TUWRD generated outputs, the trained model, and the final DMP record. It also assumed that licensing and reuse decisions could be handled briefly, while the final project required explicit documentation of the EEA source-data terms, generated-output licence, software licence, and reuse conditions.

The initial DMP also did not fully capture the later DBRepo work. The final project required a normalized relational schema, semantic mappings, unit mappings, documented API-based reuse, and checks that the machine-learning workflow could be reproduced from repository/database artefacts rather than only local files. Finally, it did not anticipate how much model documentation would be needed: the final submission includes a Model Card, generated evaluation artefacts, and references to the model and generated-data deposits.

## 2. What The Final DMP Required That The Initial DMP Glossed Over

The final DMP required concrete FAIR implementation evidence, not only planning text. The group had to select and maintain several metadata standards, including RO-Crate, CodeMeta, Croissant, FAIR4ML metadata, and a Model Card. The final plan also had to distinguish the input database, software release, trained model, generated outputs, and DMP itself as related but separate artefacts with separate metadata records and identifiers.

Compared with the initial plan, the final DMP required more detailed provenance and access documentation. The DBRepo database DOI, GitHub/Zenodo software release DOI, generated-data DOI, and final DMP DOI had to be cross-linked. The final DMP also needed contributor identities and ORCIDs, repository relationships, publication dates, licence choices, and a maDMP JSON representation suitable for the TUWRD final DMP record.
