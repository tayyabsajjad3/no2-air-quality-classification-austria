# OSTrails DMP Evaluation Test Assignment

This document records the WP5 test assignments from the TUWEL file `Automated DMP Evaluation test assignment (2).csv`.

## Group 3 Assignments

| Role | Owner | Assigned metrics |
| --- | --- | --- |
| A | Glent Rembeci | `T-DCSC-026`, `T-DCSC-037`, `T-DCSC-065` |
| B | Somayeh Zeraati | `T-DCSC-058`, `T-DCSC-069`, `T-DCSC-083` |
| C | Muhammed Tayyab | `T-DCSC-001`, `T-DCSC-016`, `T-DCSC-032` |
| D | Sina Sadeghi | `T-DCSC-003`, `T-DCSC-022`, `T-DCSC-090` |

## A/B Work Scope

Because A and B are being covered together, the tests to implement are:

- `T-DCSC-026`
- `T-DCSC-037`
- `T-DCSC-065`
- `T-DCSC-058`
- `T-DCSC-069`
- `T-DCSC-083`

## Implementation Target

These tests must be implemented in the OSTrails shared test repository, not in this NO2 experiment repository:

https://gitlab.tuwien.ac.at/crdm/data-stewardship/dast-2026-ue

The exercise PDF requires following the README of the forked repository and committing the tests there. The final pull request must be named `group-3`.

## Local Implementation Status

The A/B tests have been implemented locally in:

`../dast-2026-ue/groups/group-3/`

The service was verified locally through the required endpoints:

- `GET /tests/:id`
- `POST /assess/test/:id` with each pass/fail example

All six A/B tests returned the expected pass/fail outcomes locally. The remaining step is to push branch `group-3` to the group's GitLab fork and open a merge request against the upstream `submissions` branch.
