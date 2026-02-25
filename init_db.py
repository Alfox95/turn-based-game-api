from app.database import engine, Base

import app.models
import app.models_game


def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()

print("Tablas creadas correctamente")
