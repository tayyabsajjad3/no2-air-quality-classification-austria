# Licence Decisions

This document records the licence decisions for the three artefact categories required by T3.6.

## Input Data

The input data consists of nitrogen dioxide (NO2) monitoring measurements downloaded from the European Environment Agency (EEA) data hub. The raw Parquet files are retained under their original EEA filenames in `data/raw/` to preserve provenance.

The EEA legal notice states that, unless otherwise indicated, EEA materials are published under a CC-BY licence. The EEA data policy also states that data made available by EEA can be accompanied by item-specific licences or third-party reuse conditions.

The source-specific EEA metadata factsheet for the data hub record used in this project was checked on 2026-05-29. It lists the licence as Creative Commons Attribution 4.0 International (CC BY 4.0) and the copyright holder as the European Environment Agency. Therefore, the raw input data is documented as EEA-sourced CC BY 4.0 material. The group does not claim authorship over the raw data; the EEA source, access date, file inventory, and provenance must remain cited.

## Software / Code

The software and documentation created by this group are licensed under the MIT License. MIT was selected because it is a permissive open-source licence, is widely understood, and allows reuse, modification, and redistribution of the project code with minimal restrictions.

The MIT License applies to original code and software documentation in this repository. It does not override the licence or reuse terms of the EEA input data.

## Produced / Output Data

Produced artefacts such as trained models, predictions, evaluation tables, and generated figures should be licensed separately from the software. The selected output-data licence for this project is Creative Commons Attribution 4.0 International (CC BY 4.0), unless the verified EEA input-data licence imposes a more restrictive or share-alike requirement.

The final TU Wien Research Data Repository deposits for the model and generated data must state the selected output-data licence explicitly. The same licence should be referenced in the README, RO-Crate, FAIR4ML metadata, Model Card, and deposit metadata.

## Current Status

| Artefact category | Proposed licence | Status |
| --- | --- | --- |
| Input data | CC BY 4.0, EEA as source/copyright holder | Verified from the source-specific EEA metadata factsheet on 2026-05-29 |
| Software/code | MIT License | Added as `LICENSE` |
| Produced/output data | CC BY 4.0, unless input licence requires otherwise | Selected for generated outputs; verify source compatibility before TUWRD deposits |
