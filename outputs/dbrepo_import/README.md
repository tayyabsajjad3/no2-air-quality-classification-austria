# DBRepo Import CSV Fallback

These CSV files were exported from the raw EEA Parquet files after the DBRepo Python import endpoint returned HTTP 503 during data loading:

`data service failed to establish connection to metadata service`

Import order:

1. `01_sampling_points.csv`
2. `02_pollutants.csv`
3. `03_measurement_units.csv`
4. `04_aggregation_types.csv`
5. `05_validity_flags.csv`
6. `06_verification_flags.csv`
7. `07_observation_logs.csv`
8. `08_measurements.csv`

The files include integer IDs, so the measurement table can keep the same foreign-key references as the DBRepo schema.
