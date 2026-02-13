from flask import Flask, jsonify, request
from bayeta import frotar, anadir
from bbdd_frase import cargar_frases
import json

app = Flask(__name__)

FORM_HTML = """ 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Añadir frases</title>
</head> 
<body> 
    <h1>Subir archivo JSON de frases</h1> 
    <form action="/add" method="POST" enctype="multipart/form-data">
        <label for="file">Selecciona un archivo JSON:</label><br><br>
        <input type="file" id="file" name="file" accept=".json" required><br><br> 
        <button type="submit">Subir y cargar frases</button>
    </form> 
    <p>O usa la API enviando JSON a este mismo endpoint.</p>
</body>
</html> 
"""

cargar_frases("frases.txt", primera_carga=True)

@app.route("/")
def hola():
    return "Hola, mundo"

@app.route("/frotar/<int:n_frases>")
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return app.response_class(
        response=json.dumps(frases, ensure_ascii=False, indent=2), 
        mimetype="application/json")

@app.route("/add", methods=['GET', 'POST'])
def endpoint_add():
    if request.method == 'GET': 
        return FORM_HTML
    
    if "file" in request.files: 
        file = request.files["file"] 
    
        if file.filename == "": 
            return jsonify({"error": "Archivo vacío"}), 400 
    
        if not file.filename.endswith(".json"): 
            return jsonify({"error": "El archivo debe ser .json"}), 400 
    # Guardar temporalmente 
        ruta = "/tmp/" + file.filename 
        file.save(ruta) # Cargar frases desde archivo JSON 
        cargar_frases(ruta, primera_carga=False)

        return jsonify({"message": "Frases añadidas correctamente"}), 200

    # --- JSON API --- 
    data = request.get_json() 
    if not data or "frases" not in data: 
        return jsonify({"error": "debes enviar un json con una clave 'frases'"}), 400 
    if not isinstance(data["frases"], list): 
        return jsonify({"error": "la clave 'frases' debe ser una lista"}), 400 
    anadir(data["frases"]) 
    return jsonify({"message": "Frases añadidas correctamente"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
