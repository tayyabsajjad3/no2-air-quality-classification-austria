# Semantic Mapping

This document describes the semantic mapping for the raw EEA NO2 air-quality measurement attributes used in this experiment. The mappings support the FAIR Findable and Interoperable principles by linking dataset attributes to established ontology concepts.

## Ontologies Used

The main ontology for the observation model is the W3C/OGC Semantic Sensor Network ontology, especially SOSA, because the dataset consists of environmental observations made at monitoring sampling points. OWL-Time is used for start and end timestamps because the observations are hourly time intervals. ChEBI is used for nitrogen dioxide because it provides a curated chemical identifier for NO2, while PROV-O is used for source and observation-log provenance. Unit mappings are listed here for completeness, but the detailed unit mapping belongs to T2.3.

| Prefix | Ontology | Namespace / reference |
| --- | --- | --- |
| `sosa` | Sensor, Observation, Sample, and Actuator ontology | `http://www.w3.org/ns/sosa/` |
| `time` | OWL-Time ontology | `http://www.w3.org/2006/time#` |
| `chebi` | Chemical Entities of Biological Interest | `http://purl.obolibrary.org/obo/CHEBI_` |
| `qudt` | Quantities, Units, Dimensions and Types | `http://qudt.org/schema/qudt/` |
| `unit` | QUDT units | `http://qudt.org/vocab/unit/` |
| `prov` | W3C Provenance Ontology | `http://www.w3.org/ns/prov#` |

## Attribute Mapping

| Raw attribute | Meaning in this dataset | Semantic concept / property | Mapping rationale |
| --- | --- | --- | --- |
| `Samplingpoint` | EEA monitoring sampling point identifier, for example `AT/SPO.09.A23.65511.8.1` | `sosa:FeatureOfInterest`; also modelled as `sosa:Platform` when representing the monitoring station context | The measurement is about air quality at a specific monitoring point. SOSA is appropriate because the dataset consists of observations connected to sampling/monitoring locations. |
| `Pollutant` | Numeric pollutant code. In this dataset the value is always `8`, interpreted as nitrogen dioxide (NO2). | `sosa:observedProperty`; NO2 concept: `chebi:33101` / `http://purl.obolibrary.org/obo/CHEBI_33101` | The pollutant is the observed property of each measurement. ChEBI provides a curated chemical identifier for nitrogen dioxide. |
| `Start` | Start timestamp of the hourly observation interval | `sosa:phenomenonTime` with `time:hasBeginning` | The timestamp marks when the observed environmental phenomenon interval begins. OWL-Time supports interval boundaries. |
| `End` | End timestamp of the hourly observation interval | `sosa:phenomenonTime` with `time:hasEnd` | The timestamp marks when the observed environmental phenomenon interval ends. Together with `Start`, it defines the hourly observation interval. |
| `Value` | Measured NO2 concentration value | `sosa:hasSimpleResult`; quantity kind represented through `qudt:QuantityValue` when paired with unit metadata | The column stores the numeric result of the observation. SOSA `hasSimpleResult` is suitable for direct scalar observation results. |
| `Unit` | Unit of the measured concentration, always `ug.m-3` in the raw files | `qudt:unit`; recommended unit concept: `unit:MicroGM-PER-M3` if accepted by the target metadata system | The unit qualifies the numeric concentration value. Detailed unit validation and fallback unit ontology decisions are handled in T2.3. |
| `AggType` | Temporal aggregation type, always `hour` | `sosa:usedProcedure`; interval duration represented with `time:unitHour` | The value describes the measurement procedure/aggregation over an hourly interval. OWL-Time represents the hour duration, while SOSA can connect the observation to the procedure used. |
| `Validity` | Validity flag for the measurement, values `-1` and `1` | `sosa:Result` quality/status annotation; local controlled vocabulary `validity_flags` | No sufficiently specific standard concept was identified in the source data for the numeric EEA validity flags. The values are therefore normalised into a local controlled vocabulary and attached to the observation result. |
| `Verification` | Verification flag for the measurement, value `1` | `sosa:Result` quality/status annotation; local controlled vocabulary `verification_flags` | The flag describes verification status. It is modelled as a controlled status attribute linked to the observation result because the raw source provides numeric flags rather than ontology IRIs. |
| `ResultTime` | Date/time when the result was produced or reported | `sosa:resultTime`; compatible with `prov:generatedAtTime` | SOSA distinguishes the phenomenon time from the result time. This column describes when the result was available/generated, not when the air was sampled. |
| `DataCapture` | Data capture information; all values are missing in the current raw files | `sosa:Result` quality annotation; candidate relation to data completeness metadata | The attribute appears to describe capture completeness, but it is empty in the current data. It is retained in the schema for provenance and future compatibility. |
| `FkObservationLog` | UUID linking the measurement to an EEA observation log | `prov:Entity`; related through `prov:wasGeneratedBy` / `prov:wasDerivedFrom` | The UUID is provenance metadata for the observation record. PROV-O is appropriate for linking measurement records to their source observation logs. |

## DBRepo Metadata Notes

These mappings were added manually in DBRepo metadata where the table schema UI exposed editable Concept and Measurement Unit fields:

| Table | Column | Recommended semantic annotation |
| --- | --- | --- |
| `sampling_points` | `sampling_point_code` | `sosa:FeatureOfInterest` / `sosa:Platform` |
| `pollutants` | `pollutant_id`, `pollutant_name`, `pollutant_formula` | `sosa:observedProperty`, `CHEBI_33101` |
| `measurement_units` | `unit_code`, `unit_uri` | `qudt:unit` |
| `aggregation_types` | `aggregation_code` | `sosa:usedProcedure`, `time:unitHour` |
| `observation_logs` | `observation_log_id` | `prov:Entity` |
| `measurements` | `start_time` | `sosa:phenomenonTime`, `time:hasBeginning` |
| `measurements` | `end_time` | `sosa:phenomenonTime`, `time:hasEnd` |
| `measurements` | `result_time` | `sosa:resultTime`, `prov:generatedAtTime` |
| `measurements` | `value` | `sosa:hasSimpleResult` |

## Limitations

The EEA raw files encode `Pollutant`, `Validity`, and `Verification` as numeric codes. The pollutant code is mapped to nitrogen dioxide because the project scope and data source describe NO2 measurements, and every raw file uses pollutant code `8`. The exact semantics of `Validity = -1` and `Validity = 1` should be verified against EEA code-list documentation before final DBRepo publication; until then, they are represented as controlled status values rather than over-interpreted ontology concepts.

## References

- W3C/OGC SOSA/SSN: https://www.w3.org/TR/vocab-ssn/
- OWL-Time: https://www.w3.org/TR/owl-time/
- ChEBI nitrogen dioxide, CHEBI:33101: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=33101
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- QUDT: https://qudt.org/
