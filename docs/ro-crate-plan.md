# RO-Crate Preparation Notes

The draft `ro-crate-metadata.json` is available in the repository root. The generated-output licence is recorded as CC BY 4.0 unless the verified EEA source-data licence requires a different compatible licence. The final RO-Crate cannot be completed until the group has the trained model deposit DOI, generated-data deposit DOI, Muhammed Tayyab's ORCID, DBRepo PID, and final artefact filenames. The current Zenodo DOI and DBRepo database identifier are already included in the draft crate.

## Entities To Include

| Entity | Current source | Final identifier needed |
| --- | --- | --- |
| Repository | GitHub repository | Zenodo DOI: `https://doi.org/10.5281/zenodo.20432795` |
| Raw EEA input data | `data/raw/*.parquet`, `data/data-inventory.csv` | Source URL and verified input-data licence |
| Database schema | `docs/schema.sql` | DBRepo database URL: `https://test.dbrepo.tuwien.ac.at/database/ed890fa1-154c-4a66-8529-4088c97f68db` |
| ER diagram | `docs/er-diagram.md` | Repository path |
| Semantic mapping | `docs/semantic-mapping.md` | Repository path and DBRepo metadata reference |
| Code metadata | `codemeta.json` | Repository path |
| Model card | `docs/model-card.md` | Repository path |
| Trained model | `outputs/models/` | TUWRD model DOI |
| Generated outputs | `outputs/results/`, `outputs/figures/` | TUWRD generated-data DOI |

## Relationships To Model

- The trained model is trained on the DBRepo training dataset/view.
- Generated outputs are produced by the experiment code and trained model.
- The Model Card describes the trained model.
- FAIR4ML metadata describes the trained model and references the Model Card.
- CodeMeta describes the software source code.
- Croissant metadata describes the input dataset.
- TUWRD deposits, the Zenodo DOI, and the DBRepo database URL are related identifiers for the repository artefacts.
