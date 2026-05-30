# Final A/B Status Report

Date: 2026-05-30

This report summarises the final local status of Owner A and Owner B tasks for the NO2 Air Quality Classification across Austrian Monitoring Stations project.

## Owner A

| Task | Status | Evidence / remaining action |
| --- | --- | --- |
| T2.1 DBRepo schema design | Complete for submission | `docs/schema.sql`, `docs/er-diagram.md`, and `docs/dbrepo-metadata-plan.md` document the 3NF schema, DBRepo database, table schemas, and metadata. The DBRepo database DOI is `https://doi.org/10.82556/3zan-dn41`. |
| T3.1 RO-Crate | Complete locally, pending final publication activation | `ro-crate-metadata.json` includes the repository, DBRepo DOI, Zenodo DOI, trained model, generated outputs, and TUWRD generated-output DOI `https://doi.org/10.70124/4wqg-7oc34`. If the TUWRD DOI changes after final publication, update the identifier. |
| T3.5 Model Card | Complete locally, pending final publication activation | `docs/model-card.md` documents the baseline RandomForest model, train/test split, evaluation metrics, limitations, and related generated-output DOI. |
| T3.9 Model deposit in TUWRD | Partly done, strict PDF issue remains | The model file `outputs/models/no2_air_quality_classifier.joblib` was uploaded to the TUWRD draft. However, the PDF asks for the model deposit to be separate from the generated-data deposit, so a separate model record is still needed for a strict match. Final publication requires team/reviewer permission. |
| T4.4 DAMAP/TUWRD export and publish | External/manual | Requires the final DMP PDF from T4.2 and final maDMP JSON from T4.3. The publication step is manual in DAMAP/TUWRD. |
| T5.1 Fork and pull request | External/manual | Local group-3 tests are implemented in `../dast-2026-ue/groups/group-3/`. Final MR/PR depends on GitLab/fork access. |
| T5.2 Implement tests A | Complete locally | `T-DCSC-026`, `T-DCSC-037`, and `T-DCSC-065` are implemented and were locally checked with pass/fail examples. |

## Owner B

| Task | Status | Evidence / remaining action |
| --- | --- | --- |
| T2.2 Semantic mapping | Complete for submission | `docs/semantic-mapping.md` and `docs/dbrepo-metadata-plan.md` document the semantic mappings and DBRepo UI completion notes. |
| T2.7 Second GitHub release | Prepared | `docs/release-notes-v2-draft.md` is ready as release notes. The actual GitHub release should be created after the group confirms final DOI/publication state. |
| T3.2 CodeMeta | Complete | `codemeta.json`, `requirements.txt`, and `docs/codemeta-notes.md` are available and aligned with the repository DOI. |
| T3.6 Licences | Complete for submission | `LICENSE`, `docs/licences.md`, and `docs/eea-licence-review.md` document MIT for software and CC BY 4.0 for EEA input/generated outputs. |
| T3.10 Generated data deposit in TUWRD | Ready for team publication, but should stay separate | The TUWRD draft contains `confusion_matrix.csv`, `confusion_matrix.png`, `model_metrics.json`, and `test_predictions.csv`; it also currently contains `no2_air_quality_classifier.joblib`. Reserved DOI: `https://doi.org/10.70124/4wqg-7oc34`. For strict PDF compliance, the model file should be moved/copied to a separate model deposit and this record should remain the generated-output dataset deposit. |
| T4.3 Export and finalise maDMP | External/manual | Requires export from the TU Wien DMP Tool. |
| T4.5 Compare initial and final DMP | Prepared, final DMP required | `docs/dmp-comparison-template.md` is prepared. It can be completed once the final DMP PDF/export exists. |
| T5.3 Implement tests B | Complete locally | `T-DCSC-058`, `T-DCSC-069`, and `T-DCSC-083` are implemented and were locally checked with pass/fail examples. |

## Remaining Team Actions

1. Create or keep a separate TUWRD model deposit for `outputs/models/no2_air_quality_classifier.joblib`, because T3.9 and T3.10 are required to be separate deposits.
2. Complete TUWRD publication/review for the generated-output record and the separate model record.
3. Export the final DMP PDF and maDMP JSON from the TU Wien DMP Tool.
4. Publish the final DMP/maDMP record if required by T4.4.
5. Complete the DMP comparison once the final DMP is available.
6. Create the final GitHub release after DOI/publication state is confirmed.
7. Complete the GitLab MR/PR if required by WP5 and if access is available.
