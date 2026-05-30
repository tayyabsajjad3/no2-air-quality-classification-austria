# Release Notes Draft: v2.0

This draft supports T2.7. It should be finalised only after all WP2 work is complete.

## Added

- Raw EEA NO2 Parquet files under `data/raw/`.
- Raw data documentation in `data/raw/README.md`.
- Machine-readable raw data inventory in `data/data-inventory.csv`.
- 3NF relational schema in `docs/schema.sql`.
- Entity-relationship diagram and 3NF rationale in `docs/er-diagram.md`.
- Semantic attribute mapping in `docs/semantic-mapping.md`.
- Visible DBRepo database and manually created table schemas for the normalised 3NF model.
- SQL view definitions draft in `docs/views.sql`.
- Code citation metadata in `CITATION.cff` with Zenodo DOI `10.5281/zenodo.20432795`.
- Croissant dataset metadata in `croissant.json`.
- Licence decision record selecting CC BY 4.0 for generated outputs, subject to final source-licence compatibility verification.
- DBRepo database DOI `10.82556/3zan-dn41`.
- DBRepo CSV import fallback files in `outputs/dbrepo_import/`.
- Idempotent DBRepo loading script in `scripts/load_dbrepo_import_csvs.py`.
- Loaded DBRepo tables with 140,160 measurement rows and all lookup/reference rows.
- Baseline NO2 elevated-class classifier in `outputs/models/no2_air_quality_classifier.joblib`.
- Reproducible model training script in `scripts/train_no2_classifier.py`.
- Evaluation outputs in `outputs/results/` and `outputs/figures/confusion_matrix.png`.

## To Add Before Release

- SQL view execution and schema-compatibility verification from T2.4/T2.5.
- API-based data loading implementation from T2.6.
- TUWRD model DOI and generated-output DOI after final deposit.
