import decimal
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "outputs" / "dbrepo_import"


def normalize_decimal(value):
    if isinstance(value, decimal.Decimal):
        return float(value)
    return value


def load_raw_data() -> pd.DataFrame:
    parquet_files = sorted(RAW_DATA_DIR.glob("*.parquet"))
    if not parquet_files:
        raise FileNotFoundError(f"No parquet files found in {RAW_DATA_DIR}")

    frames = []
    for path in parquet_files:
        frame = pd.read_parquet(path)
        frame["source_file"] = path.stem
        frames.append(frame)

    data = pd.concat(frames, ignore_index=True)
    for column in data.columns:
        if data[column].dtype == object:
            data[column] = data[column].apply(normalize_decimal)
    return data


def with_ids(frame: pd.DataFrame, id_column: str) -> pd.DataFrame:
    frame = frame.reset_index(drop=True).copy()
    frame.insert(0, id_column, range(1, len(frame) + 1))
    return frame


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_data = load_raw_data()

    sampling_points = (
        all_data[["Samplingpoint", "source_file"]]
        .drop_duplicates()
        .rename(columns={"Samplingpoint": "sampling_point_code"})
        .reset_index(drop=True)
    )
    sampling_points["country_code"] = "AT"
    sampling_points["station_code"] = sampling_points["source_file"]
    sampling_points["source_publisher"] = "European Environment Agency"
    sampling_points = with_ids(
        sampling_points[
            [
                "sampling_point_code",
                "country_code",
                "station_code",
                "source_file",
                "source_publisher",
            ]
        ],
        "sampling_point_id",
    )

    pollutants = (
        all_data[["Pollutant"]]
        .drop_duplicates()
        .rename(columns={"Pollutant": "pollutant_id"})
        .reset_index(drop=True)
    )
    pollutants["pollutant_name"] = "Nitrogen Dioxide"
    pollutants["pollutant_formula"] = "NO2"
    pollutants["pollutant_uri"] = "http://dd.eionet.europa.eu/vocabulary/aq/pollutant/8"

    measurement_units = (
        all_data[["Unit"]]
        .drop_duplicates()
        .rename(columns={"Unit": "unit_code"})
        .reset_index(drop=True)
    )
    measurement_units["unit_label"] = "Microgram Per Cubic Metre"
    measurement_units["unit_uri"] = "http://qudt.org/vocab/unit/MicroGM-PER-M3"
    measurement_units = with_ids(measurement_units, "unit_id")

    aggregation_types = (
        all_data[["AggType"]]
        .drop_duplicates()
        .rename(columns={"AggType": "aggregation_code"})
        .reset_index(drop=True)
    )
    aggregation_types["aggregation_label"] = aggregation_types["aggregation_code"]
    aggregation_types = with_ids(aggregation_types, "aggregation_type_id")

    validity_flags = (
        all_data[["Validity"]]
        .drop_duplicates()
        .rename(columns={"Validity": "validity_code"})
        .reset_index(drop=True)
    )
    validity_flags["validity_label"] = validity_flags["validity_code"].astype(str)
    validity_flags = with_ids(validity_flags, "validity_id")

    verification_flags = (
        all_data[["Verification"]]
        .drop_duplicates()
        .rename(columns={"Verification": "verification_code"})
        .reset_index(drop=True)
    )
    verification_flags["verification_label"] = verification_flags["verification_code"].astype(str)
    verification_flags = with_ids(verification_flags, "verification_id")

    observation_logs = (
        all_data[["FkObservationLog"]]
        .drop_duplicates()
        .rename(columns={"FkObservationLog": "observation_log_uuid"})
        .reset_index(drop=True)
    )
    observation_logs = with_ids(observation_logs, "observation_log_id")

    sp_map = dict(zip(sampling_points["sampling_point_code"], sampling_points["sampling_point_id"]))
    unit_map = dict(zip(measurement_units["unit_code"], measurement_units["unit_id"]))
    agg_map = dict(zip(aggregation_types["aggregation_code"], aggregation_types["aggregation_type_id"]))
    val_map = dict(zip(validity_flags["validity_code"], validity_flags["validity_id"]))
    ver_map = dict(zip(verification_flags["verification_code"], verification_flags["verification_id"]))
    obs_map = dict(zip(observation_logs["observation_log_uuid"], observation_logs["observation_log_id"]))

    measurements = pd.DataFrame()
    measurements.insert(0, "measurement_id", range(1, len(all_data) + 1))
    measurements["sampling_point_id"] = all_data["Samplingpoint"].map(sp_map)
    measurements["pollutant_id"] = all_data["Pollutant"]
    measurements["unit_id"] = all_data["Unit"].map(unit_map)
    measurements["aggregation_type_id"] = all_data["AggType"].map(agg_map)
    measurements["validity_id"] = all_data["Validity"].map(val_map)
    measurements["verification_id"] = all_data["Verification"].map(ver_map)
    measurements["observation_log_id"] = all_data["FkObservationLog"].map(obs_map)
    measurements["start_time"] = pd.to_datetime(all_data["Start"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
    measurements["end_time"] = pd.to_datetime(all_data["End"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
    measurements["result_time"] = pd.to_datetime(all_data["ResultTime"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
    measurements["value"] = pd.to_numeric(all_data["Value"], errors="coerce")
    measurements["data_capture"] = pd.to_numeric(all_data["DataCapture"], errors="coerce")

    tables = {
        "01_sampling_points.csv": sampling_points,
        "02_pollutants.csv": pollutants,
        "03_measurement_units.csv": measurement_units,
        "04_aggregation_types.csv": aggregation_types,
        "05_validity_flags.csv": validity_flags,
        "06_verification_flags.csv": verification_flags,
        "07_observation_logs.csv": observation_logs,
        "08_measurements.csv": measurements,
    }

    for filename, table in tables.items():
        table.to_csv(OUTPUT_DIR / filename, index=False)
        print(f"{filename}: {len(table):,} rows")

    print(f"\nExported DBRepo import CSVs to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
