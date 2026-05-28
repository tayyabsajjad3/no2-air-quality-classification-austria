# DBRepo Metadata Plan

This plan supports T2.1 and T2.2. The DBRepo database and table schemas were created manually in DBRepo on 2026-05-29. Semantic metadata should be added from a Jupyter notebook using the DBRepo REST API once an API token is available, or manually in DBRepo where the table UI exposes concept and unit URI fields. The SQL schema uses DBRepo-compatible data types such as `varchar`, `int`, `decimal`, and `timestamp`; source UUID values are stored as `VARCHAR(36)` because DBRepo's public table-creation type list does not expose a dedicated UUID column type.

## T2.1 Database And Table Metadata

Owner: A

DBRepo database:

- ID: `ed890fa1-154c-4a66-8529-4088c97f68db`
- Name: `no2_air_quality_classification_austria`
- Internal name: `no2_air_quality_classification_austria_jlnb`
- Tables created: `sampling_points`, `pollutants`, `measurement_units`, `aggregation_types`, `validity_flags`, `verification_flags`, `observation_logs`, `measurements`

Recommended database title:

`NO2 Air Quality Classification across Austrian Monitoring Stations`

Recommended database description:

`Hourly nitrogen dioxide (NO2) measurements from Austrian monitoring sampling points, sourced from the European Environment Agency data hub and normalised for a FAIR machine-learning experiment.`

Recommended keywords:

`NO2`, `air quality`, `Austria`, `European Environment Agency`, `environmental monitoring`, `machine learning`, `FAIR data`

Publisher/source note:

The EEA must be credited as the source/publisher of the input data. The student group should be listed as the re-publisher/curator of this DBRepo representation, not as the original data publisher.

## T2.2 Semantic Metadata

Owner: B

The semantic mappings documented in `docs/semantic-mapping.md` should be added to DBRepo attribute metadata. The highest-priority mappings are:

| Table | Attribute | Concept |
| --- | --- | --- |
| `sampling_points` | `sampling_point_code` | `sosa:FeatureOfInterest` / `sosa:Platform` |
| `pollutants` | `pollutant_id`, `pollutant_name` | `sosa:observedProperty`, `CHEBI_33101` |
| `measurements` | `start_time` | `sosa:phenomenonTime`, `time:hasBeginning` |
| `measurements` | `end_time` | `sosa:phenomenonTime`, `time:hasEnd` |
| `measurements` | `result_time` | `sosa:resultTime`, `prov:generatedAtTime` |
| `measurements` | `value` | `sosa:hasSimpleResult` |
| `measurement_units` | `unit_code` | `qudt:unit` |
| `observation_logs` | `observation_log_id` | `prov:Entity` |

Manual DBRepo UI checklist:

1. Open the DBRepo database `ed890fa1-154c-4a66-8529-4088c97f68db`.
2. Open each table and add the concept URI for the attributes listed above where the UI provides a concept field.
3. For unit metadata, add `http://qudt.org/vocab/unit/MicroGM-PER-M3` to the unit URI field for `measurements.value` if DBRepo allows a unit URI on numeric attributes.
4. If DBRepo does not allow editing these fields after table creation, keep this document and `notebooks/dbrepo_setup_template.ipynb` as the required metadata mapping evidence and add the mappings through the REST API once a token is available.
