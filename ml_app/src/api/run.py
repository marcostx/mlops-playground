from src.api.app import create_app
from src.api.config import DevelopmentConfig
# from flasgger import Swagger, LazyJSONEncoder


application = create_app(
    config_object=DevelopmentConfig)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
