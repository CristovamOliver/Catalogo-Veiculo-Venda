from flask import jsonify, request, Blueprint
from Infraestrutura.context import conexao

carros_bp = Blueprint('carros_bp', __name__)


@carros_bp.route("/buscar-carros", methods=['GET'])
def get_carros():
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
        return jsonify(carros), 200
    except:
        return "Nenhum carro encontrado !", 404


@carros_bp.route("/buscar/<int:carroid>", methods=['GET'])
def get_carro(carroid):
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
        return jsonify(carro), 200
    except:
        return 'Carro não encontrado !', 404


@carros_bp.route("/criar", methods=['POST'])
def create_carros():
    try:
        cursor = conexao.cursor()
        # region [QUERY]
        query_insert = (
            f"INSERT INTO CARROS(marca, modelo, ano, cor, km, preco, foto) VALUES('{request.json['marca']}','{request.json['modelo']}',"
            f"'{request.json['ano']}','{request.json['cor']}','{request.json['km']}','{request.json['preco']}','{request.json['foto']}')")
        # endregion
        cursor.execute(query_insert)
        conexao.commit()
        return 'Carro adicionado com sucesso !', 200
    except:
        return 'Não foi adicionar o carro', 500


# @carros_bp.route("/editar", methods=['PUT'])
# def editar_carro():
#         try:
#             cursor = conexao.cursor()
#             cursor.execute(f"UPDATE CARROS SET address = 'Canyon 123' WHERE address = 'Valley 345 {}")
#             resultado = cursor.fetchall()
#             return jsonify(carro), 200
#             return f'Carro com id: {id} não encontrado', 404
#         except:
#             return 'Não foi possível editar o carro', 500


@carros_bp.route("/deletar/<int:carroid>", methods=['DELETE'])
def deletar_carro(carroid):
    try:
        cursor = conexao.cursor()
        if carroid is None:
            return f'Carro com id: {carroid} não encontrado !', 404
        else:
            cursor.execute(f"DELETE FROM CARROS WHERE carroid = {carroid}")
            return f'Carro com id: {carroid} excluído com sucesso !', 200
        conexao.commit()
    except:
        return 'Não foi possível deletar o carro !', 500