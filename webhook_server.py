"""
Servidor FastAPI para receber webhooks da landing page
e enviar notificações via Telegram Bot
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from datetime import datetime
import os
from dotenv import load_dotenv
import httpx
import logging

# Carregar variáveis de ambiente
load_dotenv()

# Configuração
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="Landing Page Webhook Server",
    description="Recebe leads da landing page e envia para Telegram",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class LeadData(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    message: str | None = None
    source: str | None = None


class LeadResponse(BaseModel):
    success: bool
    message: str
    lead_id: str | None = None


# Armazenamento em memória (em produção, usar MongoDB)
leads_storage = []


@app.get("/")
async def root():
    """Health check"""
    return {
        "status": "online",
        "service": "Landing Page Webhook Server",
        "version": "1.0.0",
        "environment": ENVIRONMENT
    }


@app.get("/health")
async def health_check():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "total_leads": len(leads_storage)
    }


@app.post("/webhook/lead", response_model=LeadResponse)
async def receive_lead(lead: LeadData):
    """
    Recebe lead da landing page e envia notificação para Telegram
    """
    try:
        # Adicionar timestamp
        lead_dict = lead.model_dump()
        lead_dict['timestamp'] = datetime.utcnow().isoformat()
        lead_dict['lead_id'] = f"LEAD-{len(leads_storage) + 1:04d}"

        # Armazenar lead
        leads_storage.append(lead_dict)

        # Enviar notificação para Telegram
        await send_telegram_notification(lead_dict)

        logger.info(f"Lead recebido e processado: {lead.email}")

        return LeadResponse(
            success=True,
            message="Lead recebido com sucesso",
            lead_id=lead_dict['lead_id']
        )

    except Exception as e:
        logger.error(f"Erro ao processar lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao processar lead")


async def send_telegram_notification(lead_data: dict):
    """Envia notificação para o Telegram"""

    if not TELEGRAM_BOT_TOKEN or not ADMIN_CHAT_ID:
        logger.warning("Token ou Chat ID do Telegram não configurado")
        return

    message = f"""
🎯 NOUVEAU LEAD !

👤 Nom: {lead_data['name']}
📧 Email: {lead_data['email']}
📱 Téléphone: {lead_data.get('phone', 'Non renseigné')}
🏢 Entreprise: {lead_data.get('company', 'Non renseigné')}
💬 Message: {lead_data.get('message', 'Aucun message')}

🆔 ID: {lead_data['lead_id']}
🕐 Date: {datetime.fromisoformat(lead_data['timestamp']).strftime('%d/%m/%Y %H:%M')}
🔗 Source: {lead_data.get('source', 'Landing Page')}

Total de leads: {len(leads_storage)}
    """

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": ADMIN_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            logger.info("Notificação enviada para Telegram com sucesso")
    except Exception as e:
        logger.error(f"Erro ao enviar notificação para Telegram: {e}")


@app.get("/leads")
async def get_leads(limit: int = 10):
    """Retorna os últimos leads"""
    return {
        "total": len(leads_storage),
        "leads": leads_storage[-limit:]
    }


@app.get("/stats")
async def get_stats():
    """Retorna estatísticas dos leads"""
    today = datetime.utcnow().date()

    today_leads = [
        l for l in leads_storage
        if datetime.fromisoformat(l['timestamp']).date() == today
    ]

    return {
        "total_leads": len(leads_storage),
        "today_leads": len(today_leads),
        "last_lead": leads_storage[-1] if leads_storage else None,
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
