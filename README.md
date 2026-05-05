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

---

## File Organisation

This repository follows a structured naming convention:

### data/

* Raw datasets: `raw_<dataset-name>.parquet`
* Processed datasets: processed_<dataset-name>.csv

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

### Configuration files

* config_<purpose>.yaml

All file names follow lowercase naming with underscores for consistency.

---

## Technologies Used

* Python
* pandas
* scikit-learn
* matplotlib

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

To be defined in later stages (WP3).
