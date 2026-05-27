# DBRepo Metadata Plan

This plan supports T2.1 and T2.2. The actual DBRepo updates must be executed from a Jupyter notebook using the DBRepo REST API once the group has DBRepo access credentials and the target database identifier. The SQL schema uses DBRepo-compatible data types such as `serial`, `varchar`, `int`, `decimal`, and `timestamp`; source UUID values are stored as `VARCHAR(36)` because DBRepo's public table-creation type list does not expose a dedicated UUID column type.

## T2.1 Database And Table Metadata

Owner: A

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
| `measurements` | `measured_value` | `sosa:hasSimpleResult` |
| `measurement_units` | `unit_code` | `qudt:unit` |
| `observation_logs` | `observation_log_id` | `prov:Entity` |
| `observation_logs` | `result_time` | `sosa:resultTime`, `prov:generatedAtTime` |
