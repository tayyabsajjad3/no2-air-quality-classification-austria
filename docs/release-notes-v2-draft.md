# Release Notes Draft: v2.0

This draft supports T2.7. It records the main changes since the first project release and can be used as the body of the second GitHub release.

## Added

- Raw EEA NO2 Parquet files under `data/raw/`.
- Raw data documentation in `data/raw/README.md`.
- Machine-readable raw data inventory in `data/data-inventory.csv`.
- 3NF relational schema in `docs/schema.sql`.
- Entity-relationship diagram and 3NF rationale in `docs/er-diagram.md`.
- Semantic attribute mapping in `docs/semantic-mapping.md`.
- Visible DBRepo database and manually created table schemas for the normalized 3NF model.
- DBRepo database DOI `10.82556/3zan-dn41`.
- DBRepo CSV import fallback files in `outputs/dbrepo_import/`.
- Idempotent DBRepo loading script in `scripts/load_dbrepo_import_csvs.py`.
- Loaded DBRepo tables with measurement and lookup/reference rows.
- SQL view definitions draft in `docs/views.sql`.
- API-based DBRepo ingestion implementation in `src/data_ingestion/ingest_dbrepo.py`.
- Code citation metadata in `CITATION.cff` with Zenodo DOI `10.5281/zenodo.20465449`.
- CodeMeta software metadata in `codemeta.json`.
- Croissant dataset metadata in `croissant.json`.
- Licence decision record selecting CC BY 4.0 for generated outputs and MIT for project code.
- Baseline NO2 elevated-class classifier in `outputs/models/no2_air_quality_classifier.joblib`.
- Reproducible model training script in `scripts/train_no2_classifier.py`.
- Evaluation outputs in `outputs/results/` and `outputs/figures/confusion_matrix.png`.
- Model Card in `docs/model-card.md`.
- RO-Crate metadata in `ro-crate-metadata.json`.
- RO-Crate validation reports in `docs/validation/`.
- Reserved TUWRD generated-output DOI `10.70124/4wqg-7oc34`.
- Separate TUWRD metadata drafts for the model deposit and generated-data deposit.

## Notes

- The local repository contains the trained model and generated outputs needed for the TUWRD records.
- The final GitHub release should use tag `v2.0` and should point to the current repository state after the final A/B updates are pushed.
- The separate TUWRD model DOI should be added later once the model-only TUWRD record is published by the team/reviewer.
