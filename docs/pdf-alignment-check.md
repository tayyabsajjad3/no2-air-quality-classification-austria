# PDF Alignment Check

Date: 2026-05-30

This note checks the current local A/B work against the Part 3 PDF requirements.

## Main Finding

The biggest remaining mismatch is in the TUWRD deposits:

- T3.9 says the trained model must be uploaded as a separate TUWRD deposit.
- T3.10 says the generated/output data must be uploaded as a separate TUWRD deposit.
- The current TUWRD draft shown in the screenshot contains both generated outputs and `no2_air_quality_classifier.joblib` in one record.

That is good evidence that the model file was uploaded, but it is not a strict match to the PDF because the PDF asks for two separate records. The safest fix is to keep the generated-output record for `confusion_matrix.csv`, `confusion_matrix.png`, `model_metrics.json`, and `test_predictions.csv`, then create a second TUWRD record for `no2_air_quality_classifier.joblib`. The local upload packages are now split into `tuwrd-upload-t3-9-model.zip` and `tuwrd-upload-t3-10-generated-data.zip` to support that.

## A Tasks

| Task | PDF match | Note |
| --- | --- | --- |
| T2.1 | Matches locally | Schema, ER diagram, DBRepo DOI, database metadata notes, and import evidence are documented. |
| T3.1 | Matches locally | RO-Crate exists, references the main artefacts, and passes `rocrate-validator 0.9.0` for RO-Crate 1.1 required checks: 38/38 passed, 0 failed. |
| T3.5 | Matches locally | Model Card has the required sections and metric table. Sections were expanded to keep the report student-like but complete. |
| T3.9 | Submitted for review | The separate model-only TUWRD record contains `no2_air_quality_classifier.joblib` and `model-card.md`; DOI `https://doi.org/10.70124/ye7mg-p5v03`. |
| T4.4 | External/manual | Needs the final DMP PDF/A and maDMP JSON, then a single DMP record in the DaSt-2026-final community. TUWEL must receive only `<group_id>-final-dmp-doi.txt` containing the single DOI URL. |
| T5.1 | External/manual | A single group pull request named `group-3` is needed after all group tests are contributed. |
| T5.2 | Matches locally | A tests 026, 037, and 065 are implemented locally. Pass/fail examples were checked through the local service and returned the expected outcomes. |

## B Tasks

| Task | PDF match | Note |
| --- | --- | --- |
| T2.2 | Matches locally | Semantic mapping is documented and DBRepo UI completion notes are present. |
| T2.7 | Prepared locally | Tag `v2.0` exists and release notes are clean. If GitHub has no published release for `v2.0`, create it from `docs/release-notes-v2-draft.md` after pushing the final commit. |
| T3.2 | Matches locally | CodeMeta file exists with pinned dependencies and ORCID authors. |
| T3.6 | Matches locally | Licences are documented for input data, software, and produced outputs. |
| T3.10 | Ready for strict upload | Generated outputs exist locally and a separate `tuwrd-upload-t3-10-generated-data.zip` package plus metadata draft are prepared. A generated-data-only TUWRD record should be used for strict PDF compliance. |
| T4.3 | External/manual | Needs maDMP JSON export from the TU Wien DMP Tool. |
| T4.5 | Complete locally | Comparison note includes the initial DMP DOI and final DMP DOI `https://doi.org/10.70124/pcepy-07563`. |
| T5.3 | Matches locally | B tests 058, 069, and 083 are implemented locally. Pass/fail examples were checked through the local service and returned the expected outcomes. |

## Student-like Wording Check

The documents are written in a clear student-report style: concise explanations, direct evidence, and no exaggerated claims. External actions that depend on community review are stated as submitted for review rather than already curator-approved.

## DMP Tool Access Clarification

The course team clarified that the DMP Tool access bug does not require all contributors to have direct access. One group member can complete the DMP Tool record. The important requirement is that all four group members are listed as contributors in the DMP.
