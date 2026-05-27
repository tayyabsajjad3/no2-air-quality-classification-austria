# RO-Crate Preparation Notes

The final `ro-crate-metadata.json` cannot be completed until the group has the final GitHub/Zenodo DOI, DBRepo entry URL, trained model deposit DOI, generated-data deposit DOI, selected licences, and final artefact filenames.

## Entities To Include

| Entity | Current source | Final identifier needed |
| --- | --- | --- |
| Repository | GitHub repository | Zenodo DOI after GitHub-Zenodo release |
| Raw EEA input data | `data/raw/*.parquet`, `data/data-inventory.csv` | Source URL and verified input-data licence |
| Database schema | `docs/schema.sql` | DBRepo database/table URL |
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
- TUWRD deposits and Zenodo DOI are related identifiers for the repository artefacts.
