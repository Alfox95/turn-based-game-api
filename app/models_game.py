from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database import Base
from app.models import Usuario

class Raza(Base):
    __tablename__ = "razas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    fuerza_mod = Column(Integer, default=0)
    agilidad_mod = Column(Integer, default=0)
    inteligencia_mod = Column(Integer, default=0)
    constitucion_mod = Column(Integer, default=0)

    habilidad_especial = Column(String, nullable=True)

    personajes = relationship("Personaje", back_populates="raza")

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    # 🔹 Multiplicadores constantes
    multiplicador_daño_fisico = Column(Float, default=1.0)
    multiplicador_daño_magico = Column(Float, default=1.0)

    bonus_precision = Column(Float, default=0.0)
    bonus_evasion = Column(Float, default=0.0)

    # 🔹 Progresión por nivel
    ataque_por_nivel = Column(Float, default=0.0)
    magia_por_nivel = Column(Float, default=0.0)
    defensa_por_nivel = Column(Float, default=0.0)
    energia_por_nivel = Column(Float, default=10.0)

    vida_por_constitucion = Column(Float, default=0.5)
    mana_por_inteligencia = Column(Float, default=1.0)

    def __repr__(self):
        return f"<Clase {self.nombre}>"

    personajes = relationship("Personaje", back_populates="clase")

class Personaje(Base):
    __tablename__ = "personajes"

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
    energia = Column(Integer, default= 10)

    vida = Column(Integer, default= 20)
    mana = Column(Integer, default=20)
    ataque = Column(Float)
    magia = Column(Float)
    defensa = Column(Float)
    evasion = Column(Float)
    precision = Column(Float)


    usuario = relationship("Usuario", back_populates="personajes")
    raza = relationship("Raza", back_populates="personajes")
    clase = relationship("Clase", back_populates="personajes")

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

