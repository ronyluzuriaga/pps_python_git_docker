from pymongo import MongoClient
import random

def conectar():
    client = MongoClient("mongodb://mongo:27017/")  # nombre del contenedor
    db = client["bayeta_db"]
    coleccion = db["frases"]
    return coleccion

def cargar_frases(ruta="frases.txt"):
    col = conectar()
    if col.count_documents({}) == 0:
        with open(ruta, "r", encoding="utf-8") as f:
            frases = [{"texto": linea.strip()} for linea in f if linea.strip()]
        col.insert_many(frases)

def obtener_frases(n):
    con = conectar()
    frases = list(con.find())
    frases_elegidas = random.sample(frases, k=min(n, len(frases)))
    return [f["texto"] for f in frases_elegidas]

def insertar_frases(lista_frases):
    con = conectar()
    docs = [{"texto": f} for f in lista_frases]
    con.insert_many(docs)