from app.models_game import Personaje
from app.game_logic.resources import normalizar_recursos


atacante : Personaje
defensor : Personaje

def calcular_danio_fisico(atacante: Personaje, defensor : Personaje):
    danio = atacante.ataque - defensor.defensa * 0.3
    return max(1, int(danio))


def calcular_danio_magico(atacante : Personaje, defensor : Personaje):
    poder = atacante.magia
    #resistencia = defensor.resistencia_magica * 0.4
    danio = poder #- resistencia
    return max(2, int(danio))


def ataque_fisico(atacante : Personaje, defensor : Personaje):
    if atacante.energia_actual < 5:
        raise ValueError("No tienes energía suficiente")

    atacante.energia_actual -= 5

    danio = calcular_danio_fisico(atacante, defensor)
    defensor.vida_actual -= danio

    normalizar_recursos(defensor)
    normalizar_recursos(atacante)

    return danio


def ataque_magico(atacante : Personaje, defensor : Personaje):
    if atacante.mana_actual < 10:
        raise ValueError("No tienes mana suficiente")

    if atacante.energia_actual < 3:
        raise ValueError("No tienes energía suficiente")

    atacante.mana_actual -= 10
    atacante.energia_actual -= 3

    danio = calcular_danio_magico(atacante, defensor)
    defensor.vida_actual -= danio

    normalizar_recursos(defensor)
    normalizar_recursos(atacante)

    return danio