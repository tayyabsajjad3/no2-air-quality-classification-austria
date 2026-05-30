# A/B Final Check

Date: 2026-05-30

This note records the final local check for the A and B tasks. It is written as evidence for the group report and should not replace the required TUWEL text-file submissions.

## Owner A

| Task | Status | Evidence |
| --- | --- | --- |
| T2.1 DBRepo schema design | Complete locally | `docs/schema.sql`, `docs/er-diagram.md`, `docs/dbrepo-metadata-plan.md`, DBRepo DOI `10.82556/3zan-dn41` |
| T3.1 RO-Crate | Complete locally | `ro-crate-metadata.json`; validator report in `docs/validation/ro-crate-validator-output.json` shows 38/38 required checks passed |
| T3.5 Model Card | Complete locally | `docs/model-card.md`, linked to `outputs/models/no2_air_quality_classifier.joblib` |
| T3.9 Model TUWRD deposit | Ready for strict upload | `tuwrd-upload-t3-9-model.zip` contains the model file and metadata draft for a separate model-only TUWRD record |
| T4.4 Final DMP publication | External/manual | Needs final DMP PDF/A and maDMP JSON to be published as one DMP record; TUWEL should receive only the single DOI URL |
| T5.1 Group pull request | External/manual | One group pull request named `group-3` is required after all tests are contributed |
| T5.2 Tests A | Complete locally | Metrics 026, 037, and 065 return expected pass/fail results in the local OSTrails service |

## Owner B

| Task | Status | Evidence |
| --- | --- | --- |
| T2.2 Semantic mapping | Complete locally | `docs/semantic-mapping.md` and DBRepo metadata notes |
| T2.7 Second GitHub release | Prepared locally | `v2.0` tag exists; clean release notes are in `docs/release-notes-v2-draft.md` |
| T3.2 CodeMeta | Complete locally | `codemeta.json` includes name, version, authors with ORCIDs, licence, dependencies, and repository URL |
| T3.6 Licences | Complete locally | `docs/licences.md` and `docs/eea-licence-review.md` document software, source-data, and generated-output licence decisions |
| T3.10 Generated data TUWRD deposit | Ready for strict upload | `tuwrd-upload-t3-10-generated-data.zip` contains only generated-output files and metadata draft for a separate generated-data TUWRD record |
| T4.3 maDMP export | External/manual | Needs the TU Wien DMP Tool maDMP JSON export |
| T4.5 DMP comparison | Prepared locally | `docs/dmp-comparison-template.md`; final comparison needs the final DMP DOI/link |
| T5.3 Tests B | Complete locally | Metrics 058, 069, and 083 return expected pass/fail results in the local OSTrails service |

## Student-Style Claim Check

The local documents avoid claiming that external publication steps are already finished. For T3.9 and T3.10, the repository now clearly separates what is complete locally from what still needs publication in TUWRD. This is safer than saying the deposits are fully complete before the final TUWRD records are published.
