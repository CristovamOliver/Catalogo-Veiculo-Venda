from flask import jsonify, Blueprint
from Infraestrutura.context import conexao

usuarios_bp = Blueprint('usuarios_bp', __name__)


@usuarios_bp.route("/buscar-usuarios", methods=['GET'])
def get_usuarios():
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM USUARIO')
        resultado = cursor.fetchall()
        usuarios = list()
        for usuario in resultado:
            usuarios.append({
                'usuarioid': usuario[0],
                'usuario': usuario[1],
                'senha': usuario[2],
                'categoria': usuario[3],
            })
        return jsonify(usuarios), 200
    except:
        return "Nenhum usuário encontrado !", 404