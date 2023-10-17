from flask import Flask
from Servicos.carros import carros_bp
from Servicos.usuarios import usuarios_bp


app = Flask(__name__)
app.register_blueprint(carros_bp)
app.register_blueprint(usuarios_bp)



if __name__ == '__main__':
    app.run(debug=True)
