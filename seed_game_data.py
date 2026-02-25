from app.database import SessionLocal
from app.models_game import Raza, Clase

db = SessionLocal()

def seed_razas():
    razas = [
        Raza(nombre="Lobo", 
             fuerza_mod=2, 
             agilidad_mod=1,
             inteligencia_mod=0, 
             constitucion_mod=2,
             habilidad_especial="Aullido"),
        Raza(nombre="Zorro", 
             fuerza_mod=0, 
             agilidad_mod=2, 
             inteligencia_mod=2,
             constitucion_mod=1,
             habilidad_especial="Astucia"),
        Raza(nombre="Oso", 
             fuerza_mod=3,
             agilidad_mod=0, 
             inteligencia_mod=-1,
             constitucion_mod=3,
             habilidad_especial="Ira primitiva"),
        Raza(nombre="Gato",
             fuerza_mod=0,  
             agilidad_mod=3,
             inteligencia_mod=2,
             constitucion_mod=0,
             habilidad_especial="Paso silencioso"),
        Raza(nombre="Ciervo",
             fuerza_mod=0,  
             agilidad_mod=1, 
             inteligencia_mod=3,
             constitucion_mod=1,
             habilidad_especial="Salto veloz"),
        Raza(nombre="Ardilla",
             fuerza_mod=0,  
             agilidad_mod=4, 
             inteligencia_mod=1,
             constitucion_mod=0,
             habilidad_especial="Reflejos rápidos"),
    ]

    for raza in razas:
        if not db.query(Raza).filter_by(nombre=raza.nombre).first():
            db.add(raza)

    db.commit()


def seed_clases():
    clases = [
        Clase(nombre="Guerrero", vida_base=120, mana_base=20,
              ataque_base=15, precision_base=70, evasion_base=5),

        Clase(nombre="Mago", vida_base=70, mana_base=120,
              ataque_base=20, precision_base=65, evasion_base=10),

        Clase(nombre="Asesino", vida_base=80, mana_base=40,
              ataque_base=18, precision_base=80, evasion_base=20),

        Clase(nombre="Cazador", vida_base=90, mana_base=50,
              ataque_base=16, precision_base=85, evasion_base=15),

        Clase(nombre="Druida", vida_base=95, mana_base=90,
              ataque_base=14, precision_base=75, evasion_base=10),

        Clase(nombre="Bandido", vida_base=85, mana_base=30,
              ataque_base=17, precision_base=78, evasion_base=18),
    ]

    for clase in clases:
        if not db.query(Clase).filter_by(nombre=clase.nombre).first():
            db.add(clase)

    db.commit()


if __name__ == "__main__":
    seed_razas()
    seed_clases()
    print("🌿 Mundo inicial creado.")