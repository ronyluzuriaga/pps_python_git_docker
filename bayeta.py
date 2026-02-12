# Importamos las funciones del nuevo módulo
from mongo_manager import inicializar, consultar

# Inicializamos la BBDD al arrancar (solo insertará si está vacía)
inicializar()

def frotar(n_frases: int) -> list:
    # Delegamos la consulta a MongoDB
    return consultar(n_frases)