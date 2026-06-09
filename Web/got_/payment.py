import stripe
from app.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentService:
    @staticmethod
    def criar_pagamento_com_split(valor_total: float, token_cartao: str, conta_cuidador_id: str):
        try:
            
            taxa_plataforma = int(amount_cents * 0.15)
            
            charge = stripe.Charge.create(
                amount=amount_cents,
                currency="brl",
                source=token_cartao,
                description="Serviço de Cuidador de Plantas",
                application_fee_amount=taxa_plataforma,  # O que fica para sua plataforma
                transfer_data={
                    "destination": conta_cuidador_id,   # Conta do cuidador que receberá o resto
                },
            )
            return {"sucesso": True, "transaction_id": charge.id, "status": charge.status}
            
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}