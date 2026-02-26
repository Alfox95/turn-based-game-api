from app.models_game import Personaje

def normalizar_recursos(personaje: Personaje):
    # Vida
    if personaje.vida_actual > personaje.vida_max:
        personaje.vida_actual = personaje.vida_max

    if personaje.vida_actual <= 0:
        personaje.vida_actual = 0
        personaje.vivo = False
    else:
        personaje.vivo = True

    # Mana
    if personaje.mana_actual > personaje.mana_max:
        personaje.mana_actual = personaje.mana_max

    if personaje.mana_actual < 0:
        personaje.mana_actual = 0

    # Energía
    if personaje.energia_actual > personaje.energia_max:
        personaje.energia_actual = personaje.energia_max

    if personaje.energia_actual < 0:
        personaje.energia_actual = 0
