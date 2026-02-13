from urllib import request
from flask import Flask, jsonify
from bayeta import frotar, anadir

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola, mundo"

@app.route("/frotar/<int:n_frases>")
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

@app.route("/add/", methods=['POST'])
def endpoint_add():
    data = request.get_json()

    if not data or 'frases' not in data:
        return jsonify({"error": "debes enviar un json con una clave 'frases'"}), 400

    n_frase = data['frases']

    if not isinstance(n_frase, list):
        return jsonify({"error": "la clave 'frases' debe ser una lista"}), 400
    
    anadir(n_frase)
    return jsonify({"message": "Frases añadidas correctamente"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
