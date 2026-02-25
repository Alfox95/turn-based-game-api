from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


from app.database import Base

class Raza(Base):
    __tablename__ = "razas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    fuerza_mod = Column(Integer, default=0)
    agilidad_mod = Column(Integer, default=0)
    inteligencia_mod = Column(Integer, default=0)
    constitucion_mod = Column(Integer, default=0)

    habilidad_especial = Column(String, nullable=True)

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    vida_base = Column(Integer)
    mana_base = Column(Integer)
    ataque_base = Column(Integer)
    magico_base = Column(Integer)
    precision_base = Column(Integer)
    evasion_base = Column(Integer)

class Personaje(Base):
    __tablename__ = "personajes"

    usuario = relationship("Usuario", back_populates="personajes")

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, unique=True, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    raza_id = Column(Integer, ForeignKey("razas.id"))
    clase_id = Column(Integer, ForeignKey("clases.id"))

    nivel = Column(Integer, default=1)
    experiencia = Column(Integer, default=0)

    fuerza = Column(Integer, default=10)
    agilidad = Column(Integer, default=10)
    inteligencia = Column(Integer, default=10)
    constitucion = Column(Integer, default=10)
    #energia = Column(Integer, default= 10)

    vida_actual = Column(Integer, default= 20)
    mana_actual = Column(Integer, default=20)

class Habilidad(Base):
    __tablename__ = "habilidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    tipo = Column(String)  # daño, buff, curación
    poder = Column(Integer)
    costo_mana = Column(Integer)

class PersonajeHabilidad(Base):
    __tablename__ = "personaje_habilidades"

    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    habilidad_id = Column(Integer, ForeignKey("habilidades.id"))

