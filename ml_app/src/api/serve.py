from flask import Blueprint, request, jsonify
from flasgger import Swagger, LazyJSONEncoder
from flasgger.utils import swag_from
from src.model.test import make_prediction

from src.api.config import get_logger

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    ---
    description: Health check endpoint
    responses:
        200:
            description: the system is ok
    """
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@prediction_app.route('/predict/regression', methods=['POST'])
@swag_from("/app/ml_app/src/api/swagger_conf.yml")
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        result = make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions')[0]
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version})
