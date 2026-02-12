import os
from pymongo import MongoClient

# --- 1. INSTANCIACIÓN ---
def instanciar():
    # Detectamos si estamos en Docker usando una variable de entorno.
    # Si no existe la variable, usamos 'localhost' (para cuando pruebas en tu PC sin Docker)
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    
    cliente_mongo = MongoClient(mongo_uri)
    bd = cliente_mongo['bayeta']
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return frases_auspiciosas

# --- 2. INICIALIZACIÓN ---
def inicializar():
    coleccion = instanciar()
    
    # Comprobamos que no se haya inicializado previamente
    if coleccion.count_documents({}) == 0:
        print("Inicializando Base de Datos desde fichero...")
        try:
            # Leemos el fichero de texto en lugar de la lista 'hardcodeada'
            with open("frases.txt", "r", encoding="utf-8") as f:
                # Creamos la lista de diccionarios que pide Mongo: {"frase": "texto..."}
                datos = [{"frase": linea.strip()} for linea in f.readlines() if linea.strip()]
            
            if datos:
                coleccion.insert_many(datos)
                print(f"Se han insertado {len(datos)} frases.")
        except FileNotFoundError:
            print("Error: No se encuentra el fichero frases.txt")

# --- 3. CONSULTA ---
def consultar(n_frases: int) -> list:
    coleccion = instanciar()
    
    # Obtener frases aleatorias usando el framework de agregación de Mongo
    pipeline = [{'$sample': {'size': n_frases}}]
    cursor = coleccion.aggregate(pipeline)
    
    # Extraemos solo el texto de la frase para devolver una lista limpia de strings
    lista_frases = [documento['frase'] for documento in cursor]
    
    return lista_frases