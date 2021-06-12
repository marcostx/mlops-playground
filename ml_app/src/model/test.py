import numpy as np
import pandas as pd

from src.model.datasets.datasets import load_pipeline
from src.model.datasets import validation
from src.model.configs import configs
from src.model.monitor import build_reports


pipeline_file_name = "regression_model.pkl"
_model_pipeline = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    validated_data = validation.validate_inputs(input_data=data)
    prediction = _model_pipeline.predict(validated_data[configs.FEATURES])
    validated_data['target'] = prediction
    
    # model monitoring
    build_reports(validated_data)

    output = np.exp(prediction)
    response = {"predictions": output}

    return response