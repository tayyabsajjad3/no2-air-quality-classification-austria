"""Train the baseline NO2 classifier used in the project.

The NO2 value is only used to make the elevated/not elevated label. I keep it
out of the input features, otherwise the model would basically get the answer.
The label is for this exercise and should not be read as an official air-quality
decision rule.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
MODEL_DIR = ROOT / "outputs" / "models"
RESULTS_DIR = ROOT / "outputs" / "results"
FIGURES_DIR = ROOT / "outputs" / "figures"

# Add src to python path to import our DBRepo ingestor
sys.path.append(str(ROOT / "src"))
from ingest_dbrepo import fetch_view_data

THRESHOLD_UG_M3 = 40.0
RANDOM_STATE = 42


def get_data_from_dbrepo() -> tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    print("Loading data via DBRepo API...")
    df = fetch_view_data("view_no2_classification_features")
    
    feature_columns = [
        "hour",
        "month",
        "weekday",
        "validity",
        "verification",
        "data_capture_missing",
        "samplingpoint",
    ]
    metadata_columns = ["measurement_id", "samplingpoint", "start_time", "value"]
    
    # Ensure types are correct after JSON deserialization
    df[feature_columns] = df[feature_columns].apply(pd.to_numeric, errors='ignore')
    df["target_elevated_no2"] = pd.to_numeric(df["target_elevated_no2"])
    
    return df[feature_columns], df["target_elevated_no2"], df[metadata_columns]


def build_pipeline() -> Pipeline:
    categorical_features = ["samplingpoint"]
    numeric_features = ["hour", "month", "weekday", "validity", "verification", "data_capture_missing"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("station", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("numeric", "passthrough", numeric_features),
        ]
    )

    classifier = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        class_weight="balanced",
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )

    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", classifier),
        ]
    )


def main() -> None:
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    x, y, metadata = get_data_from_dbrepo()
    train_idx, test_idx = train_test_split(
        x.index,
        test_size=0.2,
        stratify=y,
        random_state=RANDOM_STATE,
    )
    x_train = x.loc[train_idx]
    x_test = x.loc[test_idx]
    y_train = y.loc[train_idx]
    y_test = y.loc[test_idx]
    metadata_test = metadata.loc[test_idx].reset_index(drop=True)

    pipeline = build_pipeline()
    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)

    metrics = {
        "model_name": "no2_air_quality_classifier",
        "algorithm": "RandomForestClassifier",
        "target": f"Value >= {THRESHOLD_UG_M3} ug/m3",
        "target_note": "The measured Value column is used to create the label but is not used as a model feature.",
        "features_used": list(x.columns),
        "threshold_ug_m3": THRESHOLD_UG_M3,
        "random_state": RANDOM_STATE,
        "rows_total": int(len(x)),
        "rows_train": int(len(x_train)),
        "rows_test": int(len(x_test)),
        "positive_rows_total": int(y.sum()),
        "positive_rate_total": float(y.mean()),
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "classification_report": classification_report(
            y_test,
            y_pred,
            target_names=["normal", "elevated"],
            zero_division=0,
            output_dict=True,
        ),
    }

    model_path = MODEL_DIR / "no2_air_quality_classifier.joblib"
    metrics_path = RESULTS_DIR / "model_metrics.json"
    predictions_path = RESULTS_DIR / "test_predictions.csv"
    confusion_csv_path = RESULTS_DIR / "confusion_matrix.csv"
    confusion_png_path = FIGURES_DIR / "confusion_matrix.png"

    joblib.dump(pipeline, model_path)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    predictions = metadata_test.copy()
    predictions["actual_elevated_no2"] = y_test.to_numpy()
    predictions["predicted_elevated_no2"] = y_pred
    predictions.to_csv(predictions_path, index=False)

    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
    pd.DataFrame(
        cm,
        index=["actual_normal", "actual_elevated"],
        columns=["predicted_normal", "predicted_elevated"],
    ).to_csv(confusion_csv_path)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["normal", "elevated"],
    )
    display.plot(cmap="Blues", values_format="d")
    plt.title("NO2 Classifier Confusion Matrix")
    plt.tight_layout()
    plt.savefig(confusion_png_path, dpi=160)
    plt.close()

    print(f"Saved model to {model_path.relative_to(ROOT)}")
    print(f"Saved metrics to {metrics_path.relative_to(ROOT)}")
    print(json.dumps({k: metrics[k] for k in ['accuracy', 'precision', 'recall', 'f1']}, indent=2))


if __name__ == "__main__":
    main()
