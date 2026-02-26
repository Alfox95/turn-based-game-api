
from app.models_game import Personaje, Clase, Raza

import random

BASE_VIDA = 20
BASE_MANA = 10
BASE_ENERGIA = 50
BASE_ATAQUE = 10
BASE_MAGIA = 10


def calcular_stats(personaje: Personaje, raza: Raza, clase: Clase):
    nivel = personaje.nivel

    fuerza = 10 + raza.fuerza_mod
    agilidad = 10 + raza.agilidad_mod
    inteligencia = 10 + raza.inteligencia_mod
    constitucion = 10 + raza.constitucion_mod

    vida = BASE_VIDA
    for _ in range(nivel - 1):
        vida += constitucion * random.uniform(
            clase.vida_por_constitucion * 0.8,
            clase.vida_por_constitucion * 1.2
        )

    mana = BASE_MANA + (nivel - 1) * inteligencia * clase.mana_por_inteligencia
    energia = BASE_ENERGIA + (nivel - 1) * clase.energia_por_nivel
    ataque = (BASE_ATAQUE + clase.ataque_por_nivel * nivel) * clase.multiplicador_daño_fisico
    magia = (BASE_MAGIA + clase.magia_por_nivel * nivel) * clase.multiplicador_daño_magico
    defensa = clase.defensa_por_nivel * nivel
    evasion = clase.bonus_evasion + (agilidad * 5 / 1000)
    precision = clase.bonus_precision + (agilidad * 5 / 1000)

    return {
        "fuerza": fuerza,
        "agilidad": agilidad,
        "inteligencia": inteligencia,
        "constitucion": constitucion,
        "vida": round(vida),
        "mana": round(mana),
        "energia": energia,
        "ataque": round(ataque, 2),
        "magia": round(magia, 2),
        "defensa": round(defensa, 2),
        "evasion": round(evasion, 3),
        "precision": round(precision, 3)
    }