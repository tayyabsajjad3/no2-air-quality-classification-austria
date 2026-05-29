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

## To Add Before Release

- Remaining DBRepo metadata/PID for database and tables.
- SQL view execution and schema-compatibility verification from T2.4/T2.5.
- DBRepo data loading and view verification from T2.5.
- API-based data loading implementation from T2.6.
