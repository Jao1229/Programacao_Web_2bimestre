from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import SolicitacaoServico
from app.payment import PaymentService
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "online", "ambiente": "Docker ou Local funcionando!"}

@app.post("/api/pagamento/split", status_code=status.HTTP_201_CREATED)
def processar_pagamento(dados: SolicitacaoServico):
    resultado = PaymentService.criar_pagamento_com_split(
        valor_total=dados.valor_total,
        token_cartao=dados.token_cartao,
        conta_cuidador_id=dados.cuidador_id_gateway
    )
    
    if not resultado["sucesso"]:
        raise HTTPException(status_code=400, detail=resultado["erro"])
        
    return {"mensagem": "Pagamento e split realizados com sucesso!", "detalhes": resultado}