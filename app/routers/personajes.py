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
def crear_personaje(personaje: PersonajeCreate, 
                    db: Session = Depends(get_db),
                    current_user: Usuario = Depends(get_current_user)
):
    raza = db.query(Raza).get(personaje.raza_id)
    if not raza:
        raise HTTPException(404, "Raza no existe")
    clase =  db.query(Clase).get(personaje.clase_id)
    if not clase:
        raise HTTPException(404, "Clase no existe")
    

    nuevo = Personaje(
        nombre=personaje.nombre,
        raza_id=personaje.raza_id,
        clase_id=personaje.clase_id,
        usuario_id=current_user.id
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
