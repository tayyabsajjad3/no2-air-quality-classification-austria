# NO2 Air Quality Classification across Austrian Monitoring Stations

## Project Description

This project focuses on classifying nitrogen dioxide (NO2) air quality levels across Austrian monitoring stations using environmental data provided by the European Environment Agency (EEA). The dataset consists of hourly measurements collected in 2024 and includes pollutant concentrations, timestamps, and station identifiers.

The goal is to build a machine learning model that predicts air quality classes based on environmental measurements.

---

## Data Source

* Source: European Environment Agency (EEA)
* Data hub: https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d
* Access date: 18 March 2026
* Format: Parquet files (raw data)
* Raw files: 16 station-specific Parquet files in `data/raw/`
* Data inventory: `data/data-inventory.csv`

---

## File Organisation

This repository follows a structured naming convention:

### data/

* Raw datasets: original EEA Parquet filenames are retained in `data/raw/` to preserve provenance.
* Raw data documentation: `data/raw/README.md`
* Raw data inventory: `data/data-inventory.csv`
* Processed datasets: `processed_<dataset-name>.csv`

### src/

* Data ingestion scripts: ingest_<source>.py
* Preprocessing scripts: preprocess_<step>.py
* Modeling scripts: model_<algorithm>.py
* Evaluation scripts: evaluate_<metric>.py

### outputs/

* Figures: fig_<description>.png
* Models: model_<name>.joblib
* Results: results_<experiment>.csv

### docs/

* Documentation files (reports, metadata, model cards)
* Database schema: `docs/schema.sql`
* Entity-relationship diagram: `docs/er-diagram.md`
* Semantic attribute mapping: `docs/semantic-mapping.md`

### Configuration files

* config_<purpose>.yaml

All file names follow lowercase naming with underscores for consistency.

---

## Technologies Used

* Python
* pandas
* scikit-learn
* matplotlib
* pyarrow
* requests
* python-dotenv

Dependencies are pinned in `requirements.txt`.

---

## Project Structure

The workflow includes:

1. Data ingestion from EEA source
2. Data preprocessing and cleaning
3. Feature engineering
4. Model training and evaluation
5. Result generation and visualization

---

## License

The software/code in this repository is licensed under the MIT License; see `LICENSE`.

Input data from the European Environment Agency is reused under the CC BY 4.0 licence identified in the source-specific EEA metadata factsheet. The raw data remains EEA-sourced material and must be cited with the original data hub record, access date, and provenance information. Produced artefacts such as trained models, predictions, and figures are selected for CC BY 4.0 release. The licence decision record is documented in `docs/licences.md`.

---

## SQL Views (T2.4)

The following SQL views are defined in `docs/views.sql` to de-normalize data into accessible formats for the ML pipeline:

*   **`view_no2_classification_features`**: A primary feature table that flattens raw NO2 measurements with sampling point details, suitable for direct ML input. It includes a `high_pollution_label` as a target variable.
*   **`view_balanced_pollution_samples`**: Provides a class-balanced sample of NO2 measurements, useful for addressing class imbalance in ML training. It combines a subsample of normal pollution events with all high pollution events.
*   **`view_regional_daily_aggregates`**: Exposes engineered trend features by aggregating daily NO2 values (average, max, min) per station, providing temporal context.

---

## DBRepo API (T2.6)

The experiment's data loading and retrieval are documented for DBRepo. Table loading is handled through an idempotent CSV loader because direct notebook imports intermittently returned HTTP 503 from the DBRepo test instance.

*   **Base URL**: `https://test.dbrepo.tuwien.ac.at`
*   **Database ID**: `ed890fa1-154c-4a66-8529-4088c97f68db`
*   **DBRepo DOI**: `https://doi.org/10.82556/3zan-dn41`
*   **Data loading**: `python scripts/load_dbrepo_import_csvs.py`
*   **Implementation**: `src/ingest_dbrepo.py`
*   **Configuration**: `DBREPO_BASE_URL`, `DBREPO_DATABASE_ID`, optional `DBREPO_API_TOKEN`, and optional `DBREPO_VIEW_DATA_PATH_TEMPLATE`

Loaded DBRepo row counts: `sampling_points` 16, `pollutants` 1, `measurement_units` 1, `aggregation_types` 1, `validity_flags` 2, `verification_flags` 1, `observation_logs` 19, and `measurements` 140,160.

---

## Zenodo DOI (T3.8)

[![DOI](https://zenodo.org/badge/1230137926.svg)](https://doi.org/10.5281/zenodo.20432795)

A `CITATION.cff` file is available in the repository root, referencing the Zenodo DOI.

---

## Metadata And Documentation

DBRepo database: https://test.dbrepo.tuwien.ac.at/database/ed890fa1-154c-4a66-8529-4088c97f68db
DBRepo DOI: https://doi.org/10.82556/3zan-dn41

* CodeMeta draft: `codemeta.json`
* RO-Crate metadata draft: `ro-crate-metadata.json`
* CodeMeta notes: `docs/codemeta-notes.md`
* Licence decisions: `docs/licences.md`
* EEA licence review: `docs/eea-licence-review.md`
* Model Card draft: `docs/model-card.md`
* RO-Crate preparation notes: `docs/ro-crate-plan.md`
* DBRepo metadata plan: `docs/dbrepo-metadata-plan.md`
* DBRepo notebook template: `notebooks/dbrepo_setup_template.ipynb`
* OSTrails test assignment: `docs/ostrails-test-assignment.md`
