from flask import Flask
from flasgger import Swagger, LazyJSONEncoder
from flasgger.utils import swag_from

from src.api.serve import prediction_app
from src.api.config import get_logger


_logger = get_logger(logger_name=__name__)


def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    flask_app = Flask('api')
    swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    swagger = Swagger(flask_app, config=swagger_config)
    flask_app.config.from_object(config_object)

    # import blueprints
    flask_app.register_blueprint(prediction_app)
    _logger.debug('Application instance created')

    return flask_app
