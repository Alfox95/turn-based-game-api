from pydantic import BaseModel

class PersonajeCreate(BaseModel):
    nombre: str
    raza_id: int
    clase_id: int
    nivel: int = 1

class PersonajeOut(PersonajeCreate):
    id: int
