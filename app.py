from flask import Flask, jsonify, request
from bayeta import frotar, anadir

app = Flask(__name__)

@app.route("/frotar/<int:n_frases>")
def endpoint_frotar(n_frases):
    return jsonify(frotar(n_frases))

@app.route("/frotar/add", methods=["POST"])
def endpoint_add():
    data = request.get_json()
    frases = data.get("frases", [])
    anadir(frases)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
