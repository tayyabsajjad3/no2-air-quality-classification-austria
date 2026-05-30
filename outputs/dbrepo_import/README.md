# DBRepo Import CSVs

These CSV files were exported from the raw EEA Parquet files after the DBRepo Python import endpoint returned intermittent HTTP 503 during direct notebook data loading:

`data service failed to establish connection to metadata service`

They are loaded with `scripts/load_dbrepo_import_csvs.py`. The script checks existing primary keys and imports only missing rows, so it can be re-run safely without duplicating DBRepo records.

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

Confirmed loaded row counts:

| Table | Rows |
| --- | ---: |
| `sampling_points` | 16 |
| `pollutants` | 1 |
| `measurement_units` | 1 |
| `aggregation_types` | 1 |
| `validity_flags` | 2 |
| `verification_flags` | 1 |
| `observation_logs` | 19 |
| `measurements` | 140,160 |
