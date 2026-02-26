from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas_pj import PersonajeCreate, PersonajeOut
from app.models_game import Personaje, Raza, Clase
from app.models import Usuario
from app.auth import get_current_user
from app.game_logic import calcular_stats
from app.services.personaje_service import crear_personaje

router = APIRouter(prefix="/personajes", tags=["Personajes"])

@router.get("/")
def listar_personajes():
    return {"mensaje": "endpoint funcionando"}

# Crear personaje
@router.post("/personajes")
def crea_personaje(datos: PersonajeCreate, 
                    db: Session = Depends(get_db),
                    usuario: Usuario = Depends(get_current_user)
):
    try:
        personaje = crear_personaje(db, datos, usuario)
        return personaje
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

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
