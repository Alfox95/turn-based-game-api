from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas_pj import PersonajeCreate, PersonajeOut
from app.models_game import Personaje, Raza, Clase
from app.models import Usuario
from app.auth import get_current_user

router = APIRouter(prefix="/personajes", tags=["Personajes"])

@router.get("/")
def listar_personajes():
    return {"mensaje": "endpoint funcionando"}

# Crear personaje
@router.post("/personajes")
def crear_personaje(datos: PersonajeCreate, 
                    db: Session = Depends(get_db),
                    usuario: Usuario = Depends(get_current_user)
):
    raza = db.query(Raza).filter(Raza.id == datos.raza_id).first()
    clase = db.query(Clase).filter(Clase.id == datos.clase_id).first()
    
    if not raza or not clase:
        raise HTTPException(status_code=400, detail="Raza o clase inválida")
    
    fuerza = 5 + raza.fuerza_mod
    agilidad = 5 + raza.agilidad_mod
    inteligencia = 5 + raza.inteligencia_mod
    constitucion = 5 + raza.constitucion_mod
    vida_actual = clase.vida_base

    nuevo = Personaje(
        nombre=datos.nombre,
        usuario_id=usuario.id,
        raza_id=raza.id,
        clase_id=clase.id,
        fuerza=fuerza,
        agilidad=agilidad,
        inteligencia=inteligencia,
        constitucion=constitucion,
        vida_actual=vida_actual,
        energia = clase.energia_base
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar personajes
@router.get("/", response_model=list[PersonajeOut])
def listar_personajes(db: Session = Depends(get_db)):
    return db.query(Personaje).all()

@router.get("/mis-personajes")
def mis_personajes(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    return db.query(Personaje).filter_by(usuario_id=current_user.id).all()
