from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.combat_service import atacar_magico, atacar_fisico

router = APIRouter(prefix="/combat", tags=["Combat"])


@router.post("/fisico")
def ataque_fisico(atacante_id: int, defensor_id: int, db: Session = Depends(get_db)):
    return atacar_fisico(db, atacante_id, defensor_id)


@router.post("/magico")
def ataque_magico(atacante_id: int, defensor_id: int, db: Session = Depends(get_db)):
    return atacar_magico(db, atacante_id, defensor_id)