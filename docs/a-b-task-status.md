# A/B Task Status

Status date: 2026-05-29

## Owner A

| Task | Requirement | Status | Notes |
| --- | --- | --- | --- |
| T2.1 | 3NF schema, SQL statements, ER diagram, DBRepo database/table creation, database/table metadata | Mostly done | `docs/schema.sql`, `docs/er-diagram.md`, and `docs/dbrepo-metadata-plan.md` are done. The visible DBRepo database `ed890fa1-154c-4a66-8529-4088c97f68db` and all eight table schemas were created manually. Remaining work is table/database metadata enrichment through DBRepo metadata fields/API. |
| T3.1 | RO-Crate | Prepared, blocked | `docs/ro-crate-plan.md` lists entities and now includes the DBRepo database URL. Final RO-Crate still needs final repository DOI, model DOI, generated-data DOI, licences, and final artefact filenames. |
| T3.5 | Model Card | Drafted, blocked | `docs/model-card.md` contains the required structure. Final model details and metrics depend on the trained model and evaluation results. |
| T3.9 | Model deposit in TUWRD | Blocked | Requires final trained model artefact, model metadata, licence, related identifiers, and TUWRD deposit access. |
| T4.4 | Publish final DMP and maDMP in DAMAP/TUWRD | Blocked | Requires final DMP PDF and maDMP JSON from WP4. |
| T5.1 | Fork shared OSTrails repository and open PR/MR | Locally done, submission blocked | `../dast-2026-ue` contains branch `group-3` and commit `5f33b19`. Push is blocked by GitLab 403 and fork creation is blocked by namespace project limit. |
| T5.2 | Implement assigned A tests | Done locally | Implemented `T-DCSC-026`, `T-DCSC-037`, and `T-DCSC-065` in `../dast-2026-ue/groups/group-3/`. Local endpoint tests passed. |

## Owner B

| Task | Requirement | Status | Notes |
| --- | --- | --- | --- |
| T2.2 | Semantic attribute mapping and DBRepo metadata mapping | Prepared, next actionable | `docs/semantic-mapping.md` and `docs/dbrepo-metadata-plan.md` are aligned with the created DBRepo schema. Next step is adding semantic metadata in DBRepo, preferably via API token/notebook or manually where the UI supports concept/unit URI fields. |
| T2.7 | Second GitHub release | Prepared, blocked | `docs/release-notes-v2-draft.md` has been updated with the completed DBRepo table setup. Final release must wait for the remaining WP2 tasks owned by C/D. |
| T3.2 | CodeMeta | Drafted, blocked | `codemeta.json`, `requirements.txt`, and `docs/codemeta-notes.md` are present. ORCIDs must be collected from group members before final submission. |
| T3.6 | Licences | Mostly done | `LICENSE`, `docs/licences.md`, and `docs/eea-licence-review.md` document the code, input-data, and produced-data licence decisions. Exact EEA item-level licence still needs source-record confirmation before final submission. |
| T3.10 | Generated data deposit in TUWRD | Blocked | Requires generated output artefacts, final output-data licence, related identifiers, and TUWRD deposit access. |
| T4.3 | Export and finalise maDMP | Blocked | Requires final DMP content and export from the TU Wien DMP Tool. |
| T4.5 | Compare initial and final DMP | Prepared, blocked | `docs/dmp-comparison-template.md` records the comparison structure and the initial DMP link. Final DMP content is still required. |
| T5.3 | Implement assigned B tests | Done locally | Implemented `T-DCSC-058`, `T-DCSC-069`, and `T-DCSC-083` in `../dast-2026-ue/groups/group-3/`. Local endpoint tests passed. |
