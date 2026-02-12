import random

def frotar(n_frases: int = 1) -> list():

    try:
        with open ("frases.txt" , "r", encoding="utf-8") as f:
            frases = [frase.strip() for frase in f.readlines() if frase.strip()]

        frase_elegida = random.choices (frases, k=n_frases)
        return frase_elegida
    except FileNotFoundError:
        return ["Error en la elección de frase"]
