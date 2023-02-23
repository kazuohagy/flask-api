from flask import Flask, make_response, jsonify, request
from bd import Nomes

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_name():
    return make_response(
        jsonify(Nomes)
        , 200)

@app.route('/nomes', methods=['POST'])
def create_name():
    nomes = request.json
    Nomes.append(nomes)
    return nomes
app.run()