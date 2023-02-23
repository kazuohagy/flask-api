from flask import Flask, make_response, jsonify, request
from bd import Nomes

app = Flask(__name__)

#Consultar todos os resultados
@app.route("/", methods=['GET'])
def get_name():
    return make_response(
        jsonify(Nomes)
        , 200)
#Consultar um resultado
@app.route('/nomes/<int:id>', methods=['GET'])
def consultar_nome(id):
    for Nome in Nomes:
        if Nome['id'] == id:
            return jsonify(Nome)
        

#Editar um resultado
@app.route('/nomes/<int:id>', methods=['PUT'])
def editar_nome(id):
    for Nome in Nomes:
        if Nome['id'] == id:
            Nome['name'] = request.json['name']
            Nome['email'] = request.json['email']
            Nome['senha'] = request.json['senha']
            return jsonify(Nome)
#Criar um resultado
@app.route('/nomes', methods=['POST'])
def create_name():
    nomes = request.json
    Nomes.append(nomes)
    return nomes

#Excluir um resultado
@app.route('/nomes/<int:id>', methods=['DELETE'])
def delete_name(id):
    for Nome in Nomes:
        if Nome['id'] == id:
            Nomes.remove(Nome)
            return jsonify(Nome)
app.run()