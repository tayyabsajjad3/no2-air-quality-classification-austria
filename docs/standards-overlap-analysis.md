# T3.11 Standards Overlap and Complementarity Analysis

**Project:** NO2 Air Quality Classification across Austrian Monitoring Stations  
**Owner:** C  
**Date:** 2026-05-29

---

## Overview

This analysis examines the five metadata standards applied in this project:

| Standard | File | Purpose |
|----------|------|---------|
| RO-Crate | `ro-crate-metadata.json` | Describes the entire experiment package and relationships between entities |
| CodeMeta | `codemeta.json` | Describes the software and code |
| FAIR4ML | `docs/fair4ml-metadata.json` | Describes the trained ML model |
| Croissant | `croissant.json` | Describes the input datasets |
| Model Card | `docs/model-card.md` | Human-readable description of the ML model |

---

## Pairwise Comparison

### 1. RO-Crate vs CodeMeta

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `author/creator`, `license`, `url`, `version`, `keywords`, `datePublished` |
| **Unique to RO-Crate** | `@graph` entity relationships, dataset/file hasPart structure, input/output provenance links, conformsTo profile URI |
| **Unique to CodeMeta** | `softwareRequirements`, `runtimePlatform`, `programmingLanguage`, `codeRepository`, `maintainer`, `contIntegration` |
| **Conflicts** | Author representation differs: RO-Crate uses `@type: Person` with `@id`, CodeMeta uses `schema:Person` with `affiliation`. Both can coexist but require careful alignment of ORCID URIs. |

**Discussion:** RO-Crate acts as the container that references the CodeMeta file as one of its entities. CodeMeta provides richer software-specific metadata (dependencies, runtime) that RO-Crate does not model natively. Together they give a complete picture of both the experiment package and the software component.

---

### 2. RO-Crate vs FAIR4ML

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `creator/author`, `license`, `datePublished`, `keywords`, reference to training dataset (via DOI) |
| **Unique to RO-Crate** | Entity relationship graph, file-level provenance, input/output links between datasets and models |
| **Unique to FAIR4ML** | `ml:algorithm`, `ml:hyperparameters`, `ml:evaluationMetrics`, `ml:intendedUse`, `ml:limitations`, `ml:trainingDataCharacteristics` |
| **Conflicts** | Model description: RO-Crate uses `@type: SoftwareApplication` or `File` for model artefacts, while FAIR4ML uses ML-specific types. The model must be referenced consistently across both with the same identifier/DOI. |

**Discussion:** FAIR4ML provides ML-specific provenance that RO-Crate cannot express on its own. RO-Crate references the FAIR4ML file as a metadata entity, creating a two-layer structure where RO-Crate handles package-level provenance and FAIR4ML handles model-level provenance.

---

### 3. RO-Crate vs Croissant

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `license`, `creator`, `url`, `keywords`, `distribution` |
| **Unique to RO-Crate** | Provenance links between datasets and code/models, conformsTo profile, hasPart file graph |
| **Unique to Croissant** | `ml:field` (column-level descriptions), `ml:dataType`, `ml:source`, `ml:transform`, unit references via QUDT URIs, `RecordSet` structure |
| **Conflicts** | Dataset description overlap: both describe the input dataset but at different granularities. RO-Crate describes it at the file level; Croissant describes it at the field/column level. License must be stated consistently in both. |

**Discussion:** Croissant is the most dataset-specific standard — it goes down to column-level descriptions that RO-Crate does not cover. RO-Crate references the Croissant file as a metadata entity. The unit mappings from T2.3 (QUDT URIs) feed directly into Croissant field descriptions.

---

### 4. RO-Crate vs Model Card

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `author`, `license`, training dataset reference, evaluation results |
| **Unique to RO-Crate** | Machine-readable entity graph, DOI/PID references, provenance links |
| **Unique to Model Card** | `out-of-scope uses`, `ethical considerations`, `limitations` (in prose), evaluation metrics table, human-readable narrative sections |
| **Conflicts** | Evaluation metrics: Model Card presents them in a human-readable markdown table; FAIR4ML and RO-Crate reference them as structured data. Values must be identical across all three. |

**Discussion:** The Model Card is the human-readable complement to the machine-readable RO-Crate. RO-Crate references the Model Card file as a `CreativeWork` entity. Together they serve different audiences: machines read RO-Crate, humans read the Model Card.

---

### 5. CodeMeta vs FAIR4ML

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `version`, `author`, `license`, `description`, `url` |
| **Unique to CodeMeta** | `softwareRequirements`, `runtimePlatform`, `programmingLanguage`, `codeRepository`, `contIntegration` |
| **Unique to FAIR4ML** | `ml:algorithm`, `ml:hyperparameters`, `ml:evaluationMetrics`, `ml:intendedUse`, `ml:limitations`, `ml:trainingData` |
| **Conflicts** | Version field: CodeMeta `version` describes the software version; FAIR4ML may reference a model checkpoint version. These are distinct and must not be confused. |

**Discussion:** CodeMeta describes the codebase that produces the model; FAIR4ML describes the model artefact itself. They are complementary with minimal overlap — CodeMeta covers the "how it was built" aspect and FAIR4ML covers the "what it produces" aspect.

---

### 6. CodeMeta vs Croissant

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `license`, `author/creator`, `url` |
| **Unique to CodeMeta** | Software-specific fields: dependencies, runtime, programming language, repository |
| **Unique to Croissant** | Dataset-specific fields: fields/columns, data types, unit URIs, distributions, record sets |
| **Conflicts** | None significant — these two standards cover entirely different artefact types (software vs dataset) and are designed to complement each other. |

**Discussion:** Minimal overlap. CodeMeta and Croissant are the most complementary pair in this project — one describes the code, the other describes the data. They are linked through RO-Crate.

---

### 7. CodeMeta vs Model Card

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | `name`, `description`, `author`, `license`, `version` |
| **Unique to CodeMeta** | Dependencies, runtime, programming language, repository URL |
| **Unique to Model Card** | Intended use, out-of-scope uses, ethical considerations, evaluation results, limitations |
| **Conflicts** | License: both state a license but Model Card may refer to the output data license while CodeMeta refers to the software license. These are intentionally different and must be clearly distinguished. |

**Discussion:** Minor overlap in basic descriptive fields. The license distinction is important — the project uses MIT for code and CC BY 4.0 for output data/models, so each standard must reference the correct license for its artefact type.

---

### 8. FAIR4ML vs Croissant

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | Training dataset reference (via DOI), `name`, `description`, `license` |
| **Unique to FAIR4ML** | Algorithm, hyperparameters, evaluation metrics, intended use, limitations |
| **Unique to Croissant** | Column-level field descriptions, data types, unit URIs, distributions |
| **Conflicts** | Dataset reference: FAIR4ML references the training dataset by DOI; Croissant describes the dataset structure. Both must reference the same dataset consistently. |

**Discussion:** FAIR4ML and Croissant form a natural pair for ML experiments — Croissant describes the input data and FAIR4ML describes what the model learned from it. The DOI link between them is critical for traceability.

---

### 9. FAIR4ML vs Model Card

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | Algorithm name, hyperparameters, evaluation metrics, training dataset reference, intended use, limitations |
| **Unique to FAIR4ML** | Machine-readable structured metadata, ontology references, DOI links |
| **Unique to Model Card** | Human-readable prose narrative, ethical considerations section, out-of-scope uses |
| **Conflicts** | Evaluation metrics: both report the same metrics (precision, recall, F1) but in different formats — structured JSON in FAIR4ML vs markdown table in Model Card. Values must be identical. Discrepancies between the two would be a consistency error. |

**Discussion:** FAIR4ML and Model Card have the highest field overlap of any pair — they both describe the ML model comprehensively. FAIR4ML is the machine-readable version and Model Card is the human-readable version of essentially the same information. The Model Card should be treated as the human-facing summary of the FAIR4ML metadata.

---

### 10. Croissant vs Model Card

| Dimension | Detail |
|-----------|--------|
| **Fields in both** | Dataset name, description, license, creator |
| **Unique to Croissant** | Field/column definitions, data types, unit URIs, distributions, record sets |
| **Unique to Model Card** | Training data narrative, ethical considerations about the data, known biases, out-of-scope uses |
| **Conflicts** | Dataset description may be more detailed in one than the other. The training data section of the Model Card should be consistent with the Croissant dataset description. |

**Discussion:** Croissant provides technical dataset metadata while the Model Card discusses the dataset from the perspective of model training and ethics. They serve different purposes with minimal technical conflict.

---

## Summary Table

| Pair | Shared Fields | Unique to First | Unique to Second | Conflicts |
|------|--------------|-----------------|------------------|-----------|
| RO-Crate vs CodeMeta | name, description, author, license, url, version | entity graph, provenance | softwareRequirements, runtimePlatform | Author representation format |
| RO-Crate vs FAIR4ML | name, description, author, license, dataset DOI | entity graph, file provenance | algorithm, hyperparameters, metrics | Model type representation |
| RO-Crate vs Croissant | name, description, license, creator, url | provenance links, hasPart | field definitions, data types, units | License must be consistent |
| RO-Crate vs Model Card | name, description, author, license, eval results | machine-readable graph | ethical considerations, prose narrative | Evaluation metric values |
| CodeMeta vs FAIR4ML | name, version, author, license | dependencies, runtime | algorithm, metrics, intended use | Version semantics differ |
| CodeMeta vs Croissant | name, description, license, author | software dependencies | column definitions, unit URIs | None significant |
| CodeMeta vs Model Card | name, description, author, license, version | dependencies, runtime | intended use, ethics, limitations | License type (code vs model) |
| FAIR4ML vs Croissant | dataset DOI, name, description, license | algorithm, metrics | field types, unit URIs | Dataset reference must match |
| FAIR4ML vs Model Card | algorithm, hyperparameters, metrics, intended use, limitations | structured machine-readable format | ethical considerations, prose | Metric values must be identical |
| Croissant vs Model Card | dataset name, description, license, creator | field/column definitions | training data narrative, ethics | Dataset description consistency |

---

## Key Findings

**1. RO-Crate is the integration layer.** It does not replace any other standard but acts as the container that references all others. Every other standard (CodeMeta, FAIR4ML, Croissant, Model Card) is referenced as an entity within the RO-Crate graph.

**2. FAIR4ML and Model Card have the highest overlap.** They both describe the ML model comprehensively — FAIR4ML for machines, Model Card for humans. Evaluation metric values must be kept identical across both to avoid inconsistencies.

**3. CodeMeta and Croissant have the lowest overlap.** They describe fundamentally different artefact types (software vs dataset) and are fully complementary with no conflicts.

**4. License management is a cross-cutting concern.** Three different licenses are used in this project — CC BY 4.0 for input data (EEA), MIT for code, and CC BY 4.0 for output data/models. Each standard must reference the correct license for its specific artefact type. Mixing them up is the most likely source of inconsistency.

**5. DOI consistency is critical.** The Zenodo DOI, TUWRD model DOI, and TUWRD dataset DOI must be referenced consistently across all standards that mention them. A mismatch in DOIs across standards would break the provenance chain.

---

## References

- RO-Crate specification: https://www.researchobject.org/ro-crate/
- CodeMeta 2.0: https://codemeta.github.io/
- FAIR4ML: https://fair4ml.com/
- Croissant: https://mlcommons.org/croissant/
- Model Cards: https://modelcards.withgoogle.com/about
