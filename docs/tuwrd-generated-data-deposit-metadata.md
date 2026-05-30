# TUWRD Generated Data Deposit Metadata Draft

This note is a copy-ready metadata draft for the separate T3.10 TUWRD record.

## Record Type

Dataset

## Title

Generated outputs for NO2 Air Quality Classification across Austrian Monitoring Stations

## Files

- `model_metrics.json`
- `test_predictions.csv`
- `confusion_matrix.csv`
- `confusion_matrix.png`

## Description

Generated output files from the baseline NO2 air-quality classification experiment. The deposit contains evaluation metrics, test-set predictions, a confusion-matrix table, and a confusion-matrix figure produced from EEA Austria NO2 hourly measurement data for an educational FAIR Data Science project.

The input EEA NO2 measurement data were normalized in DBRepo and used to train and evaluate a baseline RandomForestClassifier. The threshold for the educational target label was Value >= 40 ug/m3. The generated data are outputs of the model evaluation workflow and should be interpreted as course-project artefacts, not as an operational air-quality service.

The related DBRepo database and normalized source tables are available via DOI: https://doi.org/10.82556/3zan-dn41.

## Keywords

NO2; air quality; Austria; EEA; machine learning; generated data; model evaluation; confusion matrix; DBRepo

## Licence

Creative Commons Attribution 4.0 International

## Related Works

- References: DBRepo source database, DOI `10.82556/3zan-dn41`, resource type Dataset.
- IsSupplementedBy: trained model deposit, DOI `10.70124/ye7mg-p5v03`, resource type Software.

## Contributor Note

List all four group members as contributors. Direct DMP Tool access is not required for every contributor, according to the course clarification.
