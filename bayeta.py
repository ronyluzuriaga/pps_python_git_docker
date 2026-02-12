from bbdd_frase import obtener_frases, insertar_frases

def frotar(n_frases: int = 1) -> list:
    return obtener_frases(n_frases)

def anadir(frases: list):
    insertar_frases(frases)
