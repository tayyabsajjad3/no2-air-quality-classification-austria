# Group 3 review notes for Group 5 DMP and published artefacts

Review target: Group 5  
Review record: https://test.researchdata.tuwien.ac.at/records/v888d-r0r44  
Prepared by: Group 3, A/B contribution draft  

## A - GitHub repository and Zenodo/software publication

Checked artefacts:
- GitHub repository: https://github.com/gevzak/predicting-urban-traffic-congestion
- Zenodo concept/version DOI from README and CITATION.cff: https://doi.org/10.5281/zenodo.20365705 and https://doi.org/10.5281/zenodo.20403050
- TUWRD model record linked from the DMP: https://test.researchdata.tuwien.ac.at/records/0wpaq-xkp80
- TUWRD generated-output record linked from the DMP: https://test.researchdata.tuwien.ac.at/records/4bcm8-dcj47

Findings:
- The GitHub repository is public and has a clear structure with README.md, LICENSE, CITATION.cff, codemeta.json, croissant.json, ro-crate-metadata.json, docs/model-card.md, source folders, notebooks, output/model artefacts, and validation reports.
- The README includes a Zenodo DOI badge and the CITATION.cff contains the concept DOI and a version DOI. The Zenodo API record resolves and lists an archived software release zip with MIT licensing.
- The software licence is available in the repository root as LICENSE, and the citation metadata is present in CITATION.cff. This is consistent with the expected GitHub and Zenodo publication requirements.
- The linked TUWRD model deposit exists as a separate model/software-related record and includes model artefacts such as config_mlp_v1.yaml, mlp_classifier_v1.json, mlp_model.keras, and scaler.pkl.
- The linked generated-output TUWRD deposit exists separately and includes evaluation outputs such as classification_report.csv, confusion_matrix.png, confusion_matrix_data.csv, metrics.json, and performance_metrics.png.
- Minor issue: the README still contains a placeholder text, "[Insert TUWRD Model DOI Link from T3.9]", even though the model DOI is available through the DMP/TUWRD record. This should be corrected for full consistency.

Suggested contribution to final review:
- Metadata standard artefacts and software publication are mostly complete and verifiable. The main remaining issue is a small documentation consistency problem in the README placeholder.

## B - DMP and maDMP

Checked artefacts:
- DMP TUWRD record: https://test.researchdata.tuwien.ac.at/records/v888d-r0r44
- DMP PDF file: DMP-FINAL_Predicting_Urban_Traffic_Congestion_Levels_using_Multi-Layer_Perceptrons_on_SDCC_SCOOT_Data.pdf
- maDMP JSON file: maDMP-FINAL_Predicting_Urban_Traffic_Congestion_Levels_using_Multi-Layer_Perceptrons_on_SDCC_SCOOT_Data.json

Findings:
- The DMP record is published/open in TUWRD and contains both required files: the human-readable DMP PDF and the machine-actionable maDMP JSON.
- The DMP PDF follows the FWF DMP structure and includes administrative information, data management responsibilities, produced/reused datasets, metadata and documentation, data quality control, storage/backup, publication and preservation, legal aspects, and ethical aspects.
- The DMP describes the SDCC SCOOT traffic dataset, DBRepo reuse, GitHub/Zenodo software publication, TUWRD model and generated-output deposits, and metadata standards such as RO-Crate, CodeMeta, FAIR4ML, Croissant, and Model Cards.
- The maDMP JSON is syntactically valid JSON and contains an RDA-style top-level dmp object with contact, contributors, cost, created/modified dates, project information, ethical issue status, and five dataset entries with distributions.
- Minor issue: some maDMP dataset entries are not directly human-readable when parsed through simple JSON access because titles are not exposed as straightforward title fields. This does not make the JSON invalid, but it reduces clarity for machine/actionable review.

Suggested contribution to final review:
- The FWF DMP completeness is strong because all major template sections are present. The maDMP is technically usable at the JSON level, but a stricter RDA schema validation and clearer dataset labels would improve confidence.

## Suggested ratings from A/B evidence only

- (a) Completeness of all FWF DMP fields: 3/3
- (c) Correctness of metadata standard artefacts, from A-side evidence: 2/3 to 3/3. Suggested final rating: 2/3 if the README placeholder is counted as a consistency issue.
- (d) maDMP technical validity: 2/3
- (e) Consistency between DMP text and published artefacts, from A/B evidence: 2/3 because the major artefacts exist, but the README placeholder and the generated-output resource type/detail should be checked by the full group.

## Pending for C/D before final PDF

- C should still verify DBRepo through the browser/UI or API because the downloaded static HTML page does not expose tables/views/semantic annotations without JavaScript.
- D should verify metadata standard artefacts in detail, especially RO-Crate, CodeMeta, FAIR4ML, Croissant, and Model Card content against the DMP text.
