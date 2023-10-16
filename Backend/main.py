from flask import Flask, jsonify, request
import mysql.connector
# from bd import carros


cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='Veiculo')



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.config['JSON_SORT_KEYS'] = False

@app.route("/",  methods=['GET'])
def get_carros():
    try:
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM CARROS')
        resultado = cursor.fetchall()
        carros = list()
        for carro in resultado:
            carros.append({
                'id': carro[0],
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


@app.route("/buscar/<int:id>",  methods=['GET'])
def get_carro(id):
        try:
            retorno_carro = {}
            for carro in carros:
                if carro['id'] == id:
                    retorno_carro = carro
            return jsonify(retorno_carro), 200
        except:
            return "carro não encontrado !", 404


@app.route("/criar", methods=['POST'])
def create_carros():
    try:
        criar_carro = request.json
        carros.append(criar_carro)
        return jsonify(criar_carro)
    except:
        return "não foi possível adicionar o carro !", 500


@app.route("/editar", methods=['PUT'])
def editar_carro():
        try:
            carro_editado = request.get_json()
            for indice, carro in enumerate(carros):
                if carro['id'] == carro_editado['id']:
                    carros[indice] = carro_editado
                    return jsonify(carro_editado), 200
            return f'Carro com id: {id} não encontrado', 404
        except:
            return 'Não foi possível editar o carro', 500


@app.route("/deletar/<int:id>", methods=['DELETE'])
def deletar_carro(id):
    try:
        for carro in carros:
            if carro['id'] == id:
                carros.remove(carro)
                return jsonify(f'O carro  de id: {carro} foi deletado com sucesso'), 200
        return f'Carro com id: {id} não encontrado', 404
    except:
        return 'não foi possível deletar o carro', 500


if __name__ == '__main__':
    app.run(debug=True)
