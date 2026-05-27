# A/B Task Status

Status date: 2026-05-27

## A Tasks

| Task | Requirement | Owner | Status | Notes |
| --- | --- | --- | --- | --- |
| T2.1 | 3NF schema design, SQL statements, ER diagram, DBRepo table creation, database/table metadata | A | Partially done | `docs/schema.sql`, `docs/er-diagram.md`, `docs/dbrepo-metadata-plan.md`, and `notebooks/dbrepo_setup_template.ipynb` are done. DBRepo table creation and DBRepo metadata still require DBRepo access/API execution. |
| T3.1 | RO-Crate | A | Blocked, prepared | `docs/ro-crate-plan.md` lists required entities and identifiers. Final `ro-crate-metadata.json` needs DOI/deposit/DBRepo links. |
| T3.5 | Model Card | A | Drafted, not final | `docs/model-card.md` has required sections. Final metrics, model details, training DOI, and licence must be filled after training/deposits. |
| T3.9 | Model deposit in TUWRD | A | Blocked | Requires trained model artefact, model metadata, licence, related identifiers, and TUWRD access. |
| T4.4 | Publish final DMP and maDMP in DAMAP/TUWRD | A | Blocked | Requires final DMP PDF from T4.2 and maDMP JSON from T4.3. |
| T5.1 | Fork shared repo and open PR | A | Partially done | The OSTrails repository has been cloned locally and branch `group-3` has been created. Final push/MR still needs to target the group's fork/upstream `submissions` branch. |
| T5.2 | Implement tests A | A | Done locally | Metrics implemented in `../dast-2026-ue/groups/group-3/`: `T-DCSC-026`, `T-DCSC-037`, `T-DCSC-065`. Local endpoint tests pass. |

## B Tasks

| Task | Requirement | Owner | Status | Notes |
| --- | --- | --- | --- | --- |
| T2.2 | Semantic attribute mapping and DBRepo metadata mapping | B | Partially done | `docs/semantic-mapping.md` and the semantic mapping payload in `notebooks/dbrepo_setup_template.ipynb` are done. DBRepo metadata update still requires DBRepo API execution. |
| T2.7 | Second GitHub release | B | Prepared, blocked | `docs/release-notes-v2-draft.md` started. Final release must wait for all WP2 tasks. |
| T3.2 | CodeMeta | B | Drafted, not final | `codemeta.json`, `requirements.txt`, and `docs/codemeta-notes.md` added. ORCIDs and final dependencies still required. |
| T3.6 | Licences | B | Partially done | `LICENSE`, `docs/licences.md`, and `docs/eea-licence-review.md` added. Exact item-level EEA input-data licence should still be checked on the data hub record before final submission. |
| T3.10 | Generated data deposit in TUWRD | B | Blocked | Requires generated outputs, final output-data licence, related identifiers, and TUWRD access. |
| T4.3 | Export and finalise maDMP | B | Blocked | Requires final DMP content and export from TU Wien DMP Tool. |
| T4.5 | Compare initial and final DMP | B | Prepared, blocked | `docs/dmp-comparison-template.md` added and the Part 2 initial DMP DOI is recorded. Final DMP link/content is still required before the comparison can be completed. |
| T5.3 | Implement tests B | B | Done locally | Metrics implemented in `../dast-2026-ue/groups/group-3/`: `T-DCSC-058`, `T-DCSC-069`, `T-DCSC-083`. Local endpoint tests pass. |
