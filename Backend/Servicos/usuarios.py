from flask import jsonify, request, Blueprint
from Infraestrutura.context import conexao


usuarios_bp = Blueprint('usuarios_bp', __name__)


@usuarios_bp.route("/buscar-usuarios", methods=['GET'])
def buscar_usuarios():
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
        cursor.close()
        return jsonify(usuarios), 200
    except:
        return "Não foi possível concluir a requisição !", 500


@usuarios_bp.route("/buscar-usuario/<int:usuarioid>", methods=['GET'])
def buscar_usuario(usuarioid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM USUARIO WHERE usuarioid = {usuarioid}")
        resultado = cursor.fetchall()
        usuarios = list()
        for usuario in resultado:
            usuarios.append({
                'usuarioid': usuario[0],
                'usuario': usuario[1],
                'senha': usuario[2],
                'categoria': usuario[3],
            })
        cursor.close()
        return jsonify(usuarios), 200
    except:
        return "Não foi possível concluir a requisição !", 500


@usuarios_bp.route("/criar-usuario", methods=['POST'])
def criar_usuario():
    try:
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO USUARIO(usuario, senha, categoria) VALUES('{request.json['usuario']}','{request.json['senha']}',"
            f"{request.json['categoria']})")
        conexao.commit()
        cursor.close()
        return 'Usuário adicionado com sucesso !', 200
    except:
        return "Não foi possível concluir a requisição !", 500


@usuarios_bp.route("/editar-usuario/<int:usuarioid>", methods=["PUT"])
def editar_usuario(usuarioid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM USUARIO WHERE usuarioid = {usuarioid}")
        if cursor.fetchone() is None:
            return f'Usuário com id: {usuarioid} não encontrado !', 404
        else:
            cursor.execute(f"UPDATE USUARIO SET usuario = '{request.json['usuario']}', senha = '{request.json['senha']}', categoria = {request.json['categoria']} WHERE usuarioid = {usuarioid}")
            conexao.commit()
            cursor.close()
            return 'Usuário atualizado com sucesso !', 200
    except:
        return "Não foi possível concluir a requisição !", 500


@usuarios_bp.route("/deletar-usuario/<int:usuarioid>", methods=["DELETE"])
def deletar_usuario(usuarioid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM USUARIO WHERE usuarioid = {usuarioid}")
        if cursor.fetchone() is None:
            return f'Usuário com id: {usuarioid} não encontrado !', 404
        else:
            cursor.execute(f"DELETE FROM USUARIO WHERE usuarioid = {usuarioid}")
            conexao.commit()
            cursor.close()
            return f'Usuário com id: {usuarioid} excluído com sucesso !', 200
    except:
        return 'Não foi possível concluir a requisição !', 500