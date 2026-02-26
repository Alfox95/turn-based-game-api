from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.routers import usuarios, personajes, combat
from app.auth import router as auth_router

app = FastAPI()

# Routers
app.include_router(usuarios.router)
app.include_router(personajes.router)
app.include_router(combat.router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"mensaje": "Backend Python funcionando"}