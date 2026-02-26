from sqlalchemy.orm import Session
from app.models_game import Personaje
from app.game_logic.combat import ataque_fisico, ataque_magico


def atacar_fisico(db:Session, atacante_id:Personaje, defensor_id:Personaje):
    atacante = db.query(Personaje).get(atacante_id)
    defensor = db.query(Personaje).get(defensor_id)

    danio = ataque_fisico(atacante, defensor)

    db.commit()
    db.refresh(defensor)

    return {
        "tipo": "fisico",
        "danio": danio,
        "vida_restante": defensor.vida_actual,
        "defensor_vivo": defensor.vivo
    }


def atacar_magico(db:Session, atacante_id:Personaje, defensor_id:Personaje):
    atacante = db.query(Personaje).get(atacante_id)
    defensor = db.query(Personaje).get(defensor_id)

    danio = ataque_magico(atacante, defensor)

    db.commit()
    db.refresh(defensor)

    return {
        "tipo": "magico",
        "danio": danio,
        "vida_restante": defensor.vida_actual,
        "defensor_vivo": defensor.vivo
    }