# Model Card

This Model Card is prepared as the required T3.5 structure. It must be completed after the final trained model, training dataset DOI, evaluation results, and output-data licence are available.

## Model Description

This project aims to train a machine learning model for classifying nitrogen dioxide (NO2) air-quality levels across Austrian monitoring stations. The input data consists of hourly NO2 measurements from the European Environment Agency for 2024. The final model artefact, algorithm, software version, and hyperparameters must be recorded here after training is complete.

## Intended Use

The intended use of the model is to support reproducible analysis of NO2 air-quality classes in the selected Austrian monitoring-station dataset. It is intended for educational open-science demonstration, FAIR data stewardship practice, and reproducible environmental data analysis. It should be used together with the documented data source, preprocessing steps, and evaluation metadata.

## Out-of-Scope Uses

The model is not intended for regulatory air-quality enforcement decisions. It is not intended to provide real-time public-health warnings or replace official monitoring and reporting by environmental authorities. It should not be applied to other pollutants, countries, years, or station networks without validating that the data distribution and class definitions are compatible.

## Training Data

The training data is derived from EEA NO2 hourly measurement files stored in `data/raw/`. The current raw dataset contains 16 station-specific Parquet files and 140,160 hourly observations. The repository DOI is `https://doi.org/10.5281/zenodo.20432795`, and the DBRepo database is `https://test.dbrepo.tuwien.ac.at/database/ed890fa1-154c-4a66-8529-4088c97f68db`. The final version of this section must reference the exact DBRepo training view or TUWRD training-data deposit once those are complete.

## Evaluation Results

The final evaluation metrics must be filled in after model training and testing are complete. The table below records the required structure for classification metrics. The values must be generated from the final reproducible pipeline, not entered manually from an intermediate run.

| Metric | Value | Notes |
| --- | --- | --- |
| Precision | To be added | Required after final evaluation |
| Recall | To be added | Required after final evaluation |
| F1 score | To be added | Required after final evaluation |

## Limitations

The model is limited by the coverage of the selected 2024 EEA station files and may not generalise outside the included monitoring points. The raw data currently covers NO2 only, so the model does not represent broader multi-pollutant air quality without additional data. The interpretation of validity and verification flags should be confirmed against EEA documentation before final conclusions are drawn.

## Ethical Considerations

Air-quality analysis can influence public interpretation of environmental risk, so the model output must be presented with clear uncertainty and scope limitations. The project should avoid implying official authority or regulatory validity unless the results are independently validated. The model should be documented transparently so that users can inspect the input data, preprocessing, assumptions, and evaluation results.

## Licence

The software code is licensed under the MIT License. Produced artefacts such as the trained model and generated outputs are selected for release under CC BY 4.0, unless the verified EEA source-data licence requires a different compatible licence. The final model deposit must state the selected output-data licence explicitly.
