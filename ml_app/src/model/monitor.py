import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab, NumTargetDriftTab

from src.model.datasets.datasets import load_dataset
from src.model.datasets.datasets import load_pipeline
from src.model.configs import configs
from src.model.datasets import validation


def build_data_drift(training_data: pd.DataFrame, test_input_data: pd.DataFrame) -> None:
    data_drift_report = Dashboard(tabs = [DataDriftTab])
    column_mapping = {}

    column_mapping['numerical_features'] = configs.NUMERICALS_LOG_VARS
    column_mapping['categorical_features'] = configs.CATEGORICAL_VARS
    data_drift_report.calculate(training_data, test_input_data, column_mapping=column_mapping)
    data_drift_report.save("/app/ml_app/reports/data_drift_report.html")
    

def build_reports(test_input_data: pd.DataFrame) -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=configs.TRAINING_DATA_FILE)
    training_data = data[configs.FEATURES]
    training_data['target'] = data[configs.TARGET]

    validated_data = validation.validate_inputs(input_data=training_data)
    validated_data = validated_data.fillna(0)
    test_input_data = test_input_data.fillna(0)

    build_data_drift(training_data=validated_data, test_input_data=test_input_data)
