# PDF Alignment Check

Date: 2026-05-30

This note checks the current local A/B work against the Part 3 PDF requirements.

## Main Finding

The biggest remaining mismatch is in the TUWRD deposits:

- T3.9 says the trained model must be uploaded as a separate TUWRD deposit.
- T3.10 says the generated/output data must be uploaded as a separate TUWRD deposit.
- The current TUWRD draft shown in the screenshot contains both generated outputs and `no2_air_quality_classifier.joblib` in one record.

That is good evidence that the model file was uploaded, but it is not a strict match to the PDF because the PDF asks for two separate records. The safest fix is to keep the generated-output record for `confusion_matrix.csv`, `confusion_matrix.png`, `model_metrics.json`, and `test_predictions.csv`, then create a second TUWRD record for `no2_air_quality_classifier.joblib`.

## A Tasks

| Task | PDF match | Note |
| --- | --- | --- |
| T2.1 | Mostly matches | Schema, ER diagram, DBRepo DOI, and metadata are documented. The PDF preferred notebook/API table creation; the project documents manual DBRepo creation plus API/CSV loading fallback. |
| T3.1 | Mostly matches | RO-Crate exists and references main artefacts. A full `ro-crate-validator` output is still needed for strict compliance. |
| T3.5 | Matches locally | Model Card has the required sections and metric table. Sections were expanded to keep the report student-like but complete. |
| T3.9 | Partly matches | Model file was uploaded, but the PDF requires a separate model deposit from T3.10. |
| T4.4 | External/manual | Needs final DMP PDF and maDMP JSON, then TUWRD/DAMAP publication by the team. |
| T5.1 | External/manual | Needs final group MR/PR when GitLab/fork access is available. |
| T5.2 | Matches locally | A tests are implemented locally and pass/fail examples were checked. |

## B Tasks

| Task | PDF match | Note |
| --- | --- | --- |
| T2.2 | Mostly matches | Semantic mapping is documented and DBRepo UI completion notes are present. |
| T2.7 | Prepared | Release notes are ready, but final GitHub release should wait until the group confirms final DOI/publication state. |
| T3.2 | Matches locally | CodeMeta file exists with pinned dependencies and ORCID authors. |
| T3.6 | Matches locally | Licences are documented for input data, software, and produced outputs. |
| T3.10 | Partly matches | Generated outputs were uploaded, but the record also contains the model file; strict PDF compliance wants generated outputs and model as separate deposits. |
| T4.3 | External/manual | Needs maDMP JSON export from the TU Wien DMP Tool. |
| T4.5 | Prepared, final DMP needed | Comparison template exists; it needs the final DMP before it can be completed. |
| T5.3 | Matches locally | B tests are implemented locally and pass/fail examples were checked. |

## Student-like Wording Check

The documents are written in a clear student-report style: concise explanations, direct evidence, and no exaggerated claims. The remaining external actions are stated honestly instead of being hidden. The only thing to avoid in the final submission is claiming that T3.9 and T3.10 are fully complete if the model and generated outputs remain in one TUWRD record.

## DMP Tool Access Clarification

The course team clarified that the DMP Tool access bug does not require all contributors to have direct access. One group member can complete the DMP Tool record. The important requirement is that all four group members are listed as contributors in the DMP.
