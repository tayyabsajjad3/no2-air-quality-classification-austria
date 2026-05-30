# NO2 Air Quality Classification across Austrian Monitoring Stations

[![DOI](https://zenodo.org/badge/1230137926.svg)](https://doi.org/10.5281/zenodo.20432795)

---

## Abstract

This project classifies nitrogen dioxide (NO2) air quality levels across Austrian monitoring stations using hourly measurements from the European Environment Agency (EEA) collected in 2024. A Random Forest binary classifier predicts whether NO2 concentrations are elevated (>= 40 µg/m³) or normal (< 40 µg/m³) based on temporal and station features. The experiment is fully documented and published following FAIR data science principles, including a normalised DBRepo database, ontology-mapped metadata, and standardised metadata artefacts (RO-Crate, CodeMeta, FAIR4ML, Croissant, Model Card).

---

## Contributors

| Role | Name | ORCID |
|------|------|-------|
| Owner A | Sina Sadeghi | [0009-0008-1996-4666](https://orcid.org/0009-0008-1996-4666) |
| Owner B | Glent Rembeci | [0009-0003-3981-8301](https://orcid.org/0009-0003-3981-8301) |
| Owner C | Muhammed Tayyab Sajjad | [0009-0000-6631-8482](https://orcid.org/0009-0000-6631-8482) |
| Owner D | Somayeh Zeraati | [0009-0001-3666-0911](https://orcid.org/0009-0001-3666-0911) |

---

## Licences

Three separate licences apply to different artefact categories in this project:

**Input data:** The raw EEA NO2 measurements are reused under **CC BY 4.0**. The data must be cited with the original EEA data hub record, access date, and provenance information. See `docs/eea-licence-review.md` for the full licence review.

**Software / code:** All scripts, notebooks, and source code in this repository are licensed under the **MIT Licence**. See `LICENSE` for the full licence text. The MIT licence is compatible with the CC BY 4.0 input data licence.

**Produced / output data:** Trained models, predictions, evaluation figures, and generated datasets are released under **CC BY 4.0**. See `docs/licences.md` for the full licence decision record.

---

## Data Source

- Source: European Environment Agency (EEA)
- Data hub: https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d
- Access date: 18 March 2026
- Format: Parquet files (raw data)
- Raw files: 16 station-specific Parquet files in `data/raw/`
- Data inventory: `data/data-inventory.csv`

---

## Requirements and Installation

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

```bash
git clone https://github.com/tayyabsajjad3/no2-air-quality-classification-austria.git
cd no2-air-quality-classification-austria
pip install -r requirements.txt
```

### Dependencies

Key dependencies (all pinned in `requirements.txt`):

- `pandas` — data manipulation
- `scikit-learn` — machine learning
- `matplotlib` — visualisation
- `pyarrow` — Parquet file reading
- `requests` — DBRepo API calls
- `python-dotenv` — environment variable management
- `dbrepo` — DBRepo Python client

---

## Step-by-Step Reproduction Instructions

### Option 1 — From local Parquet files

```bash
# 1. Train the model from raw EEA Parquet files
python scripts/train_no2_classifier.py

# Outputs:
# outputs/models/no2_air_quality_classifier.joblib
# outputs/results/model_metrics.json
# outputs/results/test_predictions.csv
# outputs/figures/confusion_matrix.png
```

### Option 2 — From DBRepo (FAIR reimplementation)

```bash
# 1. Set up environment variables
cp .env.example .env
# Edit .env with your DBRepo credentials

# 2. Load data from DBRepo
python scripts/load_dbrepo_import_csvs.py

# 3. Run the experiment using DBRepo views
python src/data_ingestion/ingest_dbrepo.py
```

### DBRepo Configuration

Create a `.env` file in the repo root:

```
TU_USERNAME=your_dbrepo_username
TU_PASSWORD=your_dbrepo_password
```

---

## Inputs and Outputs

### Inputs

| File | Description |
|------|-------------|
| `data/raw/SPO.09.*.parquet` | 16 EEA Parquet files with hourly NO2 measurements from Austrian stations |
| `data/data-inventory.csv` | Inventory of all raw data files |

### Outputs

| File | Description |
|------|-------------|
| `outputs/models/no2_air_quality_classifier.joblib` | Trained Random Forest classifier |
| `outputs/results/model_metrics.json` | Evaluation metrics (accuracy, precision, recall, F1) |
| `outputs/results/test_predictions.csv` | Model predictions on the test set |
| `outputs/results/confusion_matrix.csv` | Confusion matrix in CSV format |
| `outputs/figures/confusion_matrix.png` | Confusion matrix visualisation |

---

## Baseline Model

The model classifies NO2 measurements as `elevated` (>= 40 µg/m³) or `normal` (< 40 µg/m³). The measured NO2 value is used only to create the target label and is not used as an input feature.

**Features used:** `hour`, `month`, `weekday`, `Validity`, `Verification`, `data_capture_missing`, `Samplingpoint`

**Test-set metrics:**

| Metric | Value |
|--------|-------|
| Accuracy | 0.8005 |
| Precision (elevated) | 0.2107 |
| Recall (elevated) | 0.7251 |
| F1 (elevated) | 0.3266 |

The model is a FAIR baseline, not a production air-quality classifier.

---

## File Organisation

### data/
- Raw datasets: original EEA Parquet filenames retained in `data/raw/` to preserve provenance
- Raw data documentation: `data/raw/README.md`
- Raw data inventory: `data/data-inventory.csv`
- Processed datasets: `processed_<dataset-name>.csv`

### src/
- Data ingestion scripts: `ingest_<source>.py`
- Preprocessing scripts: `preprocess_<step>.py`
- Modeling scripts: `model_<algorithm>.py`
- Evaluation scripts: `evaluate_<metric>.py`

### outputs/
- Figures: `fig_<description>.png`
- Models: `model_<name>.joblib`
- Results: `results_<experiment>.csv`

### docs/
- Documentation files (reports, metadata, model cards)
- Database schema: `docs/schema.sql`
- Entity-relationship diagram: `docs/er-diagram.md`
- Semantic attribute mapping: `docs/semantic-mapping.md`
- Unit mapping: `docs/unit-mapping.md`
- Standards overlap analysis: `docs/standards-overlap-analysis.md`
- FAIR4ML metadata: `docs/fair4ml-metadata.json`

### Configuration files
- `config_<purpose>.yaml`

All file names follow lowercase naming with underscores for consistency.

---

## SQL Views (T2.4)

The following SQL views are defined in `docs/views.sql`:

- **`view_no2_classification_features`**: Primary feature table with flattened NO2 measurements and an `elevated_no2_label` target variable based on `Value >= 40 µg/m³`
- **`view_balanced_pollution_samples`**: Class-balanced sample combining normal and elevated NO2 events
- **`view_regional_daily_aggregates`**: Daily aggregates (average, max, min) per station for temporal trend features

---

## DBRepo API (T2.6)

- **Base URL**: `https://test.dbrepo.tuwien.ac.at`
- **Database ID**: `ed890fa1-154c-4a66-8529-4088c97f68db`
- **DBRepo DOI**: `https://doi.org/10.82556/3zan-dn41`
- **Endpoints used**: `/api/v1/database/ed890fa1-154c-4a66-8529-4088c97f68db/view/<view_name>/data`
- **Authentication**: None required (publicly accessible database)
- **Data loading**: `python scripts/load_dbrepo_import_csvs.py`
- **Implementation**: `src/data_ingestion/ingest_dbrepo.py`
- **Configuration**: `DBREPO_BASE_URL`, `DBREPO_DATABASE_ID`, optional `DBREPO_API_TOKEN`

Loaded DBRepo row counts: `sampling_points` 16, `pollutants` 1, `measurement_units` 1, `aggregation_types` 1, `validity_flags` 2, `verification_flags` 1, `observation_logs` 19, `measurements` 140,160.

---

## Metadata and Documentation

| File | Description |
|------|-------------|
| `CITATION.cff` | Citation metadata referencing Zenodo DOI |
| `codemeta.json` | CodeMeta 2.0 software metadata |
| `ro-crate-metadata.json` | RO-Crate experiment package metadata |
| `croissant.json` | Croissant dataset metadata |
| `docs/fair4ml-metadata.json` | FAIR4ML model metadata |
| `docs/model-card.md` | Human-readable model card |
| `docs/unit-mapping.md` | Unit of measurement ontology mappings (T2.3) |
| `docs/semantic-mapping.md` | Attribute semantic mappings (T2.2) |
| `docs/standards-overlap-analysis.md` | Standards overlap analysis (T3.11) |
| `docs/licences.md` | Licence decision record |

---

## Zenodo DOI (T3.8)

[![DOI](https://zenodo.org/badge/1230137926.svg)](https://doi.org/10.5281/zenodo.20432795)

A `CITATION.cff` file is available in the repository root, referencing the Zenodo DOI.

---

## TUWRD Deposits

- Generated data deposit DOI: `https://doi.org/10.70124/4wqg-7oc34`
- Model deposit: to be added after upload
- DBRepo DOI: `https://doi.org/10.82556/3zan-dn41`
