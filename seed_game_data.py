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
             fuerza_mod=1, 
             agilidad_mod=2, 
             inteligencia_mod=2,
             constitucion_mod=1,
             habilidad_especial="Astucia"),
        Raza(nombre="Oso", 
             fuerza_mod=3,
             agilidad_mod=-1, 
             inteligencia_mod=-1,
             constitucion_mod=3,
             habilidad_especial="Ira primitiva"),
        Raza(nombre="Gato",
             fuerza_mod=0,  
             agilidad_mod=3,
             inteligencia_mod=2,
             constitucion_mod=1,
             habilidad_especial="Paso silencioso"),
        Raza(nombre="Ciervo",
             fuerza_mod=0,  
             agilidad_mod=1, 
             inteligencia_mod=3,
             constitucion_mod=1,
             habilidad_especial="Salto veloz"),
        Raza(nombre="Mono",
             fuerza_mod=-1,  
             agilidad_mod=1, 
             inteligencia_mod=4,
             constitucion_mod=0,
             habilidad_especial="Concentración")
    ]

    for raza in razas:
        if not db.query(Raza).filter_by(nombre=raza.nombre).first():
            db.add(raza)

    db.commit()


def seed_clases():
    clases = [
        Clase(
            nombre="Guerrero",
            multiplicador_daño_fisico=1.2,
            multiplicador_daño_magico=0.55,
            bonus_precision=0.85,
            bonus_evasion=0.05,
            ataque_por_nivel=3,
            magia_por_nivel=0.5,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.7,
            mana_por_inteligencia=0.5
        ),

        Clase(
            nombre="Mago",
            multiplicador_daño_fisico=0.85,
            multiplicador_daño_magico=1.3,
            bonus_precision=0.7,
            bonus_evasion=0.05,
            ataque_por_nivel=0.75,
            magia_por_nivel=3,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.4,
            mana_por_inteligencia=2.5
        ),

        Clase(
            nombre="Asesino",
            multiplicador_daño_fisico=1.3,
            multiplicador_daño_magico=0.95,
            bonus_precision=0.85,
            bonus_evasion=0.2,
            ataque_por_nivel=2.5,
            magia_por_nivel=1.5,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.35,
            mana_por_inteligencia=1.5
        ),

        Clase(
            nombre="Cazador",
            multiplicador_daño_fisico=1.15,
            multiplicador_daño_magico=0.9,
            bonus_precision=0.8,
            bonus_evasion=0.1,
            ataque_por_nivel=2,
            magia_por_nivel=1,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.5,
            mana_por_inteligencia=1
        ),

        Clase(
            nombre="Druida",
            multiplicador_daño_fisico=0.9,
            multiplicador_daño_magico=1.2,
            bonus_precision=0.8,
            bonus_evasion=0.1,
            ataque_por_nivel=1,
            magia_por_nivel=2,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.4,
            mana_por_inteligencia=2
        ),

        Clase(
            nombre="Paladin",
            multiplicador_daño_fisico=1.1,
            multiplicador_daño_magico=1.0,
            bonus_precision=0.0,
            bonus_evasion=0.1,
            ataque_por_nivel=2,
            magia_por_nivel=1,
            defensa_por_nivel=1,
            energia_por_nivel=10,
            vida_por_constitucion=0.5,
            mana_por_inteligencia=1.0
        )
    ]

    for clase in clases:
        if not db.query(Clase).filter_by(nombre=clase.nombre).first():
            db.add(clase)

    db.commit()


if __name__ == "__main__":
    seed_razas()
    seed_clases()
    print("🌿 Mundo inicial creado.")