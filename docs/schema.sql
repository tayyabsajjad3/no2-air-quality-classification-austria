-- Relational schema for the EEA NO2 air-quality classification experiment.
-- The schema normalizes repeated station, pollutant, unit, aggregation,
-- status, and observation-log values into reference tables.

CREATE TABLE sampling_points (
    sampling_point_id INTEGER PRIMARY KEY,
    sampling_point_code VARCHAR(255) NOT NULL UNIQUE,
    country_code VARCHAR(255),
    station_code VARCHAR(255),
    source_file VARCHAR(255) NOT NULL,
    source_publisher VARCHAR(255) NOT NULL DEFAULT 'European Environment Agency'
);

CREATE TABLE pollutants (
    pollutant_id INTEGER PRIMARY KEY,
    pollutant_name VARCHAR(255) NOT NULL,
    pollutant_formula VARCHAR(255),
    pollutant_uri VARCHAR(255)
);

CREATE TABLE measurement_units (
    unit_id INTEGER PRIMARY KEY,
    unit_code VARCHAR(255) NOT NULL UNIQUE,
    unit_label VARCHAR(255) NOT NULL,
    unit_uri VARCHAR(255)
);

CREATE TABLE aggregation_types (
    aggregation_type_id INTEGER PRIMARY KEY,
    aggregation_code VARCHAR(255) NOT NULL UNIQUE,
    aggregation_label VARCHAR(255) NOT NULL
);

CREATE TABLE validity_flags (
    validity_id INTEGER PRIMARY KEY,
    validity_code INTEGER NOT NULL UNIQUE,
    validity_label VARCHAR(255) NOT NULL
);

CREATE TABLE verification_flags (
    verification_id INTEGER PRIMARY KEY,
    verification_code INTEGER NOT NULL UNIQUE,
    verification_label VARCHAR(255) NOT NULL
);

CREATE TABLE observation_logs (
    observation_log_id INTEGER PRIMARY KEY,
    observation_log_uuid VARCHAR(36) NOT NULL UNIQUE
);

CREATE TABLE measurements (
    measurement_id INTEGER PRIMARY KEY,
    sampling_point_id INTEGER NOT NULL REFERENCES sampling_points(sampling_point_id),
    pollutant_id INTEGER NOT NULL REFERENCES pollutants(pollutant_id),
    unit_id INTEGER NOT NULL REFERENCES measurement_units(unit_id),
    aggregation_type_id INTEGER NOT NULL REFERENCES aggregation_types(aggregation_type_id),
    validity_id INTEGER NOT NULL REFERENCES validity_flags(validity_id),
    verification_id INTEGER NOT NULL REFERENCES verification_flags(verification_id),
    observation_log_id INTEGER NOT NULL REFERENCES observation_logs(observation_log_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    result_time TIMESTAMP,
    value NUMERIC(10, 4) NOT NULL,
    data_capture NUMERIC(10, 4),
    CONSTRAINT measurements_positive_interval CHECK (end_time > start_time),
    CONSTRAINT measurements_non_negative_value CHECK (value >= 0),
    CONSTRAINT measurements_unique_observation UNIQUE (
        sampling_point_id,
        pollutant_id,
        start_time,
        end_time
    )
);

CREATE INDEX idx_measurements_sampling_point
    ON measurements (sampling_point_id);

CREATE INDEX idx_measurements_time
    ON measurements (start_time, end_time);

CREATE INDEX idx_measurements_pollutant
    ON measurements (pollutant_id);
