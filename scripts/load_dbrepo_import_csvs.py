import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from dbrepo.RestClient import RestClient


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs" / "dbrepo_import"

ENDPOINT = "https://test.dbrepo.tuwien.ac.at"
DATABASE_ID = "ed890fa1-154c-4a66-8529-4088c97f68db"

TABLES = [
    ("sampling_points", "b277e2ed-1fab-4ac3-962b-b1e82026ae5e", "01_sampling_points.csv", "sampling_point_id"),
    ("pollutants", "13dec6c5-5c0d-4a98-9973-b862c10b4e49", "02_pollutants.csv", "pollutant_id"),
    ("measurement_units", "b1afdf57-ff37-4452-94e3-77c28bafc4b3", "03_measurement_units.csv", "unit_id"),
    ("aggregation_types", "868cdaaa-c961-4833-af05-6b9cc5f7c904", "04_aggregation_types.csv", "aggregation_type_id"),
    ("validity_flags", "4b62c1b0-295b-4697-8c91-f61f075c8348", "05_validity_flags.csv", "validity_id"),
    ("verification_flags", "2e096722-778b-4f12-a236-5f32ad9556e4", "06_verification_flags.csv", "verification_id"),
    ("observation_logs", "c51d477c-db84-4fae-b03c-3e7fb9c9be61", "07_observation_logs.csv", "observation_log_id"),
    ("measurements", "0082a413-69b5-40a3-ac29-a7243961312d", "08_measurements.csv", "measurement_id"),
]


def load_client() -> RestClient:
    load_dotenv(ROOT / ".env")
    username = os.getenv("TU_USERNAME")
    password = os.getenv("TU_PASSWORD")
    if not username or not password:
        raise RuntimeError("Set TU_USERNAME and TU_PASSWORD in .env before running this script.")
    return RestClient(endpoint=ENDPOINT, username=username, password=password)


def get_existing_ids(client: RestClient, table_id: str, pk_column: str) -> set:
    try:
        data = client.get_table_data(database_id=DATABASE_ID, table_id=table_id, size=1_000_000)
    except Exception as exc:
        print(f"  existing rows could not be read, treating as empty ({type(exc).__name__}: {exc})")
        return set()

    if pk_column not in data.columns:
        return set()
    return set(data[pk_column].dropna().astype(str))


def import_missing_rows(client: RestClient, name: str, table_id: str, csv_name: str, pk_column: str) -> None:
    csv_path = OUTPUT_DIR / csv_name
    frame = pd.read_csv(csv_path)
    existing_ids = get_existing_ids(client, table_id, pk_column)
    if existing_ids:
        frame = frame[~frame[pk_column].astype(str).isin(existing_ids)].reset_index(drop=True)

    if frame.empty:
        print(f"{name}: no missing rows")
        return

    chunk_size = int(os.getenv("DBREPO_IMPORT_CHUNK_SIZE", "5000"))
    print(f"{name}: importing {len(frame):,} missing rows")
    for start in range(0, len(frame), chunk_size):
        chunk = frame.iloc[start : start + chunk_size].copy()
        client.import_table_data(database_id=DATABASE_ID, table_id=table_id, dataframe=chunk)
        end = min(start + len(chunk), len(frame))
        print(f"  imported {end:,}/{len(frame):,}")


def main() -> None:
    client = load_client()
    client.get_database(database_id=DATABASE_ID)
    for table in TABLES:
        import_missing_rows(client, *table)


if __name__ == "__main__":
    main()
