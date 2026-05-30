# TUWRD Model Deposit Metadata Draft

Use this draft for the separate TUWRD deposit required for T3.9. The generated-output deposit has reserved DOI `https://doi.org/10.70124/4wqg-7oc34`. The exercise PDF says the trained-model deposit and generated-output deposit must be separate records, so uploading the model file into the generated-output record alone is not enough for a strict match.

## File

Upload:

- `outputs/models/no2_air_quality_classifier.joblib`

## Basic Information

Digital Object Identifier:

- Select `No, I need one`

Resource type:

- `Software` if available
- otherwise `Dataset`

Title:

`Baseline model for NO2 Air Quality Classification across Austrian Monitoring Stations`

Publication date:

`2026-05-30`

Creators:

- Zeraati, Somayeh (TU Wien)
- Rembeci, Glent (TU Wien)
- Sadeghi, Sina (TU Wien)
- Tayyab, Muhammed (TU Wien)

Description:

`Trained baseline RandomForestClassifier model for the NO2 Air Quality Classification across Austrian Monitoring Stations project. The model predicts an educational elevated-NO2 class using time, station, validity, verification, and data-capture metadata. The measured NO2 value is used only to create the target label (Value >= 40 ug/m3) and is not used as an input feature. The related generated-output deposit contains the evaluation metrics, test predictions, confusion-matrix table, and confusion-matrix figure.`

Licence:

- `Creative Commons Attribution 4.0 International`

Keywords:

- `NO2`
- `air quality`
- `Austria`
- `machine learning`
- `RandomForestClassifier`
- `FAIR data`
- `DBRepo`

Language:

- `English`

Publisher:

- `TU Wien`

## Alternate Identifiers

- Identifier: `10.5281/zenodo.20465916`
  Scheme: `DOI`
  Use for the software repository release.

- Identifier: `10.82556/3zan-dn41`
  Scheme: `DOI`
  Use for the DBRepo database.

- Identifier: `10.70124/4wqg-7oc34`
  Scheme: `DOI`
  Use for the generated-output deposit.

## Related Works

- Relation: `References`
  Identifier: `10.5281/zenodo.20465916`
  Scheme: `DOI`
  Resource type: `Software`

- Relation: `Is supplement to`
  Identifier: `10.70124/4wqg-7oc34`
  Scheme: `DOI`
  Resource type: `Dataset`

- Relation: `Is derived from`
  Identifier: `10.82556/3zan-dn41`
  Scheme: `DOI`
  Resource type: `Dataset`

## Final Step

After publishing, copy the final model DOI back into:

- `README.md`
- `docs/model-card.md`
- `docs/ro-crate-plan.md`
- `ro-crate-metadata.json`
- `docs/release-notes-v2-draft.md`
