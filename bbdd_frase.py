from pymongo import MongoClient
import random
import json

def conectar():
    client = MongoClient("mongodb://mongo:27017/")  # nombre del contenedor
    db = client["bayeta_db"]
    coleccion = db["frases"]
    return coleccion

def cargar_frases(ruta="frases.txt", primera_carga=True):
    col = conectar()
    if primera_carga and col.count_documents({}) > 0:
        return  # No cargar si ya hay frases y es primera carga
    if ruta.endswith(".txt"):
        with open(ruta, "r", encoding="utf-8") as f:
            frases = [{"texto": linea.strip()} for linea in f if linea.strip()]
        col.insert_many(frases)
    
    if ruta.endswith(".json"):
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            frases = [{"texto": f.strip()} for f in data if f.strip()]
            
        elif isinstance(data, dict) and "frases" in data:
            frases = [{"texto": f.strip()} for f in data["frases"] if f.strip()]

        else:
            raise ValueError("JSON debe ser una lista o un dict con clave 'frases'")
        col.insert_many(frases)
        return
def obtener_frases(n):
    con = conectar()
    frases = list(con.find())
    frases_elegidas = random.sample(frases, k=min(n, len(frases)))
    return [f["texto"] for f in frases_elegidas]

def insertar_frases(lista_frases):
    con = conectar()
    docs = [{"texto": f} for f in lista_frases]
    con.insert_many(docs)