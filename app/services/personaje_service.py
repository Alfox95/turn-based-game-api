from sqlalchemy.orm import Session
from fastapi import Depends

from app.auth import get_current_user
from app.models import Usuario
from app.models_game import Personaje, Raza, Clase
from app.schemas.schemas_pj import PersonajeCreate
from app.game_logic import calcular_stats


def crear_personaje(db: Session, 
                    data: PersonajeCreate, 
                    usuario: Usuario = Depends(get_current_user)):
    
    raza = db.query(Raza).filter(Raza.id == data.raza_id).first()
    clase = db.query(Clase).filter(Clase.id == data.clase_id).first()

    if not raza or not clase:
        raise ValueError("Raza o clase inválida")

    # 2️⃣ crear personaje base
    personaje = Personaje(
        nombre=data.nombre,
        usuario_id=usuario.id,
        raza_id=raza.id,
        clase_id=clase.id,       
    )

    db.add(personaje)
    db.commit()
    db.refresh(personaje)

    stats = calcular_stats(personaje, raza, clase)

    personaje.vida = stats["vida"]
    personaje.mana = stats["mana"]
    personaje.fuerza = stats["fuerza"]
    personaje.agilidad = stats["agilidad"]
    personaje.inteligencia = stats["inteligencia"]
    personaje.constitucion = stats["constitucion"]
    personaje.energia = stats["energia"]
    personaje.ataque = stats["ataque"]
    personaje.magia = stats["magia"]
    personaje.defensa = stats["defensa"]
    personaje.evasion = stats["evasion"]
    personaje.precision = stats["precision"]

    db.commit()
    db.refresh(personaje)

    return personaje