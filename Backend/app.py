from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from Servicos.carros import carros_bp
from Servicos.usuarios import usuarios_bp


app = Flask(__name__)


SWAGGER_URL = ''
API_URL = '/static/swagger.json'


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Catálogo de Veículos"
    },
)


app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(carros_bp)
app.register_blueprint(usuarios_bp)


if __name__ == '__main__':
    app.run(debug=True)