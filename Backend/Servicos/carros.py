from flask import jsonify, request, Blueprint
from Infraestrutura.context import conexao


carros_bp = Blueprint('carros_bp', __name__)


@carros_bp.route("/buscar-carros", methods=['GET'])
def buscar_carros():
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM CARROS')
        resultado = cursor.fetchall()
        carros = list()
        for carro in resultado:
            carros.append({
                'carroid': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3],
                'cor': carro[4],
                'km': carro[5],
                'preco': carro[6],
                'foto': carro[7]
            })
        cursor.close()
        return jsonify(carros), 200
    except:
        return "Não foi possível buscar os carros !", 500


@carros_bp.route("/buscar-carro/<int:carroid>", methods=['GET'])
def buscar_carro(carroid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM CARROS WHERE carroid = {carroid}")
        resultado = cursor.fetchall()
        carro = list()
        for carros in resultado:
            carro.append({
                'carroid': carros[0],
                'marca': carros[1],
                'modelo': carros[2],
                'ano': carros[3],
                'cor': carros[4],
                'km': carros[5],
                'preco': carros[6],
                'foto': carros[7]
            })
        cursor.close()
        return jsonify(carro), 200
    except:
        return "Não foi possível buscar o carro !", 500


@carros_bp.route("/criar-carro", methods=['POST'])
def criar_carro():
    try:
        cursor = conexao.cursor()
        cursor.execute(
            f"INSERT INTO CARROS(marca, modelo, ano, cor, km, preco, foto) VALUES('{request.json['marca']}','{request.json['modelo']}',"
            f"{request.json['ano']},'{request.json['cor']}',{request.json['km']},{request.json['preco']},'{request.json['foto']}')")
        conexao.commit()
        cursor.close()
        return 'Carro adicionado com sucesso !', 200
    except:
        return 'Não foi possível adicionar o carro', 500


@carros_bp.route("/editar-carro/<int:carroid>", methods=['PUT'])
def editar_carro(carroid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM CARROS WHERE carroid = {carroid}")
        if cursor.fetchone() is None:
            return f'Carro com id: {carroid} não encontrado !', 404
        else:
            cursor.execute(f"UPDATE CARROS SET marca = '{request.json['marca']}', modelo = '{request.json['modelo']}', ano = {request.json['ano']}, cor = '{request.json['cor']}', km = {request.json['km']}, preco = {request.json['preco']}, foto = '{request.json['foto']}' WHERE carroid = {carroid}")
            conexao.commit()
            cursor.close()
            return f'Carro atualizado com sucesso !', 200
    except:
        return 'Não foi possível atualizar o carro !', 500


@carros_bp.route("/deletar-carro/<int:carroid>", methods=['DELETE'])
def deletar_carro(carroid):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM CARROS WHERE carroid = {carroid}")
        if cursor.fetchone() is None:
            return f'Carro com id: {carroid} não encontrado !', 404
        else:
            cursor.execute(f"DELETE FROM CARROS WHERE carroid = {carroid}")
            conexao.commit()
            cursor.close()
            return f'Carro de id: {carroid} excluído com sucesso !', 200
    except:
        return 'Não foi possível concluir a requisição !', 500