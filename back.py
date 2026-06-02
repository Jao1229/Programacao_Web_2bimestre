from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Cuidadores de Plantas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


plantas_db = [
    {"id": 1, "nome": "Samambaia", "dono": "Alice", "rega": "3 vezes por semana", "status": "Saudável"},
    {"id": 2, "nome": "Suculenta", "dono": "Bruno", "rega": "1 vez por semana", "status": "Precisa de sol"}
]


class Planta(BaseModel):
    nome: str
    dono: str
    rega: str
    status: str


@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Cuidadores de Plantas! 🌱"}

@app.get("/api/plantas", response_model=List[dict])
def listar_plantas():
    return plantas_db


@app.post("/api/plantas", status_code=201)
def cadastrar_planta(planta: Planta):
    nova_planta = planta.dict()
    nova_planta["id"] = len(plantas_db) + 1
    plantas_db.append(nova_planta)
    return {"mensagem": "Planta cadastrada com sucesso!", "planta": nova_planta}
