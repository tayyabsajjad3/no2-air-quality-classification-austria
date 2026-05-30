# RO-Crate Preparation Notes

The draft `ro-crate-metadata.json` is available in the repository root. The generated-output licence is recorded as CC BY 4.0 unless the verified EEA source-data licence requires a different compatible licence. The DBRepo database DOI has been minted. The local trained model and evaluation outputs are now included in the draft crate. The generated-output deposit has reserved TUWRD DOI `https://doi.org/10.70124/4wqg-7oc34`. The final RO-Crate still needs the TUWRD model DOI after the model file is deposited.

## Entities To Include

| Entity | Current source | Final identifier needed |
| --- | --- | --- |
| Repository | GitHub repository | Zenodo DOI: `https://doi.org/10.5281/zenodo.20465916` |
| Raw EEA input data | `data/raw/*.parquet`, `data/data-inventory.csv` | Source URL and verified input-data licence |
| Database schema | `docs/schema.sql` | DBRepo database URL: `https://test.dbrepo.tuwien.ac.at/database/ed890fa1-154c-4a66-8529-4088c97f68db`; DOI: `https://doi.org/10.82556/3zan-dn41` |
| ER diagram | `docs/er-diagram.md` | Repository path |
| Semantic mapping | `docs/semantic-mapping.md` | Repository path and DBRepo metadata reference |
| Code metadata | `codemeta.json` | Repository path |
| Model card | `docs/model-card.md` | Repository path |
| Trained model | `outputs/models/no2_air_quality_classifier.joblib` | TUWRD model DOI |
| Generated outputs | `outputs/results/`, `outputs/figures/` | Reserved TUWRD DOI: `https://doi.org/10.70124/4wqg-7oc34` |

## Relationships To Model

- The trained model is trained on the DBRepo training dataset/view.
- Generated outputs are produced by the experiment code and trained model.
- The Model Card describes the trained model.
- FAIR4ML metadata describes the trained model and references the Model Card.
- CodeMeta describes the software source code.
- Croissant metadata describes the input dataset.
- TUWRD deposits, the Zenodo DOI, the DBRepo database URL, and the DBRepo DOI are related identifiers for the repository artefacts.
