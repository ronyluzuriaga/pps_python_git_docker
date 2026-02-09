from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, mundo'

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    # Llamamos a la función frotar (que ahora mismo devuelve frases de prueba)
    lista_frases = frotar(n_frases)
    # Devolvemos la lista en formato JSON
    return jsonify({"frases": lista_frases})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)