import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
import subprocess
import sys
import os

from src.model.configs import configs

def download_datasets() -> None:
    cmd_download_train = f"curl {configs.TRAIN_FILE_URL} -o /app/ml_app/data/train.csv"
    cmd_download_test = f"curl {configs.TEST_FILE_URL} -o /app/ml_app/data/test.csv"
    subprocess.call(cmd_download_train, shell=True)
    subprocess.call(cmd_download_test, shell=True)

def load_dataset(*, file_name: str) -> pd.DataFrame:
    if not os.path.exists(f"{configs.DATASET_DIR}/{file_name}"):
        download_datasets()
    _data = pd.read_csv(f"{configs.DATASET_DIR}/{file_name}")
    return _data

def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = "regression_model.pkl"
    save_path = os.path.join(configs.TRAINED_MODEL_DIR, save_file_name)
    joblib.dump(pipeline_to_persist, save_path)

    print("saved pipeline")


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = os.path.join(configs.TRAINED_MODEL_DIR, file_name)
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline