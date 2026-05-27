# Entity-Relationship Diagram

```mermaid
erDiagram
    sampling_points ||--o{ measurements : records
    pollutants ||--o{ measurements : describes
    measurement_units ||--o{ measurements : uses
    aggregation_types ||--o{ measurements : aggregates_as
    validity_flags ||--o{ measurements : validates
    verification_flags ||--o{ measurements : verifies
    observation_logs ||--o{ measurements : logs

    sampling_points {
        integer sampling_point_id PK
        varchar sampling_point_code UK
        char country_code
        varchar station_code
        varchar source_file
        varchar source_publisher
    }

    pollutants {
        integer pollutant_id PK
        varchar pollutant_name
        varchar pollutant_formula
        varchar pollutant_uri
    }

    measurement_units {
        integer unit_id PK
        varchar unit_code UK
        varchar unit_label
        varchar unit_uri
    }

    aggregation_types {
        integer aggregation_type_id PK
        varchar aggregation_type_code UK
        varchar aggregation_type_label
    }

    validity_flags {
        integer validity_id PK
        varchar validity_label
        text validity_description
    }

    verification_flags {
        integer verification_id PK
        varchar verification_label
        text verification_description
    }

    observation_logs {
        varchar observation_log_id PK
        timestamp result_time
        numeric data_capture
    }

    measurements {
        bigint measurement_id PK
        integer sampling_point_id FK
        integer pollutant_id FK
        integer unit_id FK
        integer aggregation_type_id FK
        integer validity_id FK
        integer verification_id FK
        varchar observation_log_id FK
        timestamp start_time
        timestamp end_time
        numeric measured_value
    }
```

## 3NF Rationale

The raw EEA files contain hourly NO2 measurements with repeated values for sampling point, pollutant, unit, aggregation type, validity, verification, and observation log. The schema separates these repeated concepts into reference tables and stores the numeric observation itself in `measurements`.

This design avoids update anomalies and keeps each non-key attribute dependent on the key of its own table. For example, the unit label and future unit URI are stored once in `measurement_units`, while each measurement references that unit by key. The `measurements` table keeps only observation-specific facts: time interval, measured value, and references to the related entities.

## Source Data Summary

- Raw files: 16 station-specific Parquet files
- Rows: 140,160 hourly observations
- Sampling points: 16
- Pollutant code: 8, interpreted as nitrogen dioxide (NO2)
- Unit: `ug.m-3`
- Aggregation type: `hour`
- Validity values: `-1`, `1`
- Verification value: `1`
- Time range: 2024-01-01 00:00 to 2024-12-31 00:00
