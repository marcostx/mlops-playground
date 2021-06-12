import io
import json
import math
import os

from src.model.configs import configs
from src.model.datasets.datasets import load_dataset


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200

def test_prediction_endpoint(flask_test_client):
    # Given
    test_data = load_dataset(file_name=configs.TESTING_DATA_FILE)
    post_json = test_data[0:1].to_json(orient='records')

    # When
    response = flask_test_client.post('/predict/regression',
                                      json=post_json)

    # Then
    assert response.status_code == 200