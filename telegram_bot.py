"""
Bot Telegram pour tracking de conversions
Landing Page → Telegram notifications
"""
import os
import logging
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID', 'YOUR_CHAT_ID')

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Armazenamento simples de leads (em produção, usar banco de dados)
leads_db = []


class TelegramBot:
    """Bot Telegram para gerenciar leads"""

    def __init__(self, token: str):
        self.token = token
        self.bot = Bot(token=token)
        self.application = Application.builder().token(token).build()
        self._register_handlers()

    def _register_handlers(self):
        """Registra os handlers de comandos"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("stats", self.stats_command))
        self.application.add_handler(CommandHandler("leads", self.leads_command))
        self.application.add_handler(CommandHandler("today", self.today_command))

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        welcome_message = """
🤖 Bot de Tracking de Conversions

Bienvenue ! Je suis votre assistant de suivi des leads.

Commandes disponibles:
/help - Afficher l'aide
/stats - Statistiques globales
/leads - Liste des derniers leads
/today - Leads d'aujourd'hui

Je vous notifierai automatiquement à chaque nouveau lead !
        """
        await update.message.reply_text(welcome_message)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /help"""
        help_text = """
📚 Aide - Commandes disponibles:

/start - Démarrer le bot
/stats - Voir les statistiques
/leads - Liste des 10 derniers leads
/today - Leads reçus aujourd'hui

💡 Le bot vous notifie automatiquement quand un nouveau lead arrive via la landing page.
        """
        await update.message.reply_text(help_text)

    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /stats - Estatísticas gerais"""
        total_leads = len(leads_db)

        today = datetime.now().date()
        today_leads = len([l for l in leads_db if datetime.fromisoformat(l['timestamp']).date() == today])

        stats_message = f"""
📊 Statistiques Globales

📈 Total de leads: {total_leads}
📅 Aujourd'hui: {today_leads}
🎯 Taux de conversion: {(today_leads/max(total_leads, 1)*100):.1f}%

Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        """
        await update.message.reply_text(stats_message)

    async def leads_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /leads - Lista últimos leads"""
        if not leads_db:
            await update.message.reply_text("Aucun lead enregistré pour le moment.")
            return

        recent_leads = leads_db[-10:]  # Últimos 10

        message = "📋 10 derniers leads:\n\n"
        for i, lead in enumerate(reversed(recent_leads), 1):
            message += f"{i}. {lead['name']} - {lead['email']}\n"
            message += f"   📱 {lead.get('phone', 'N/A')} | 🏢 {lead.get('company', 'N/A')}\n"
            message += f"   🕐 {lead['timestamp']}\n\n"

        await update.message.reply_text(message)

    async def today_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /today - Leads de hoje"""
        today = datetime.now().date()
        today_leads = [l for l in leads_db if datetime.fromisoformat(l['timestamp']).date() == today]

        if not today_leads:
            await update.message.reply_text("Aucun lead aujourd'hui.")
            return

        message = f"📅 Leads d'aujourd'hui ({len(today_leads)}):\n\n"
        for i, lead in enumerate(today_leads, 1):
            message += f"{i}. {lead['name']} - {lead['email']}\n"
            message += f"   📱 {lead.get('phone', 'N/A')}\n"
            message += f"   💬 {lead.get('message', 'N/A')[:50]}...\n\n"

        await update.message.reply_text(message)

    async def send_lead_notification(self, lead_data: dict):
        """Envia notificação de novo lead para o admin"""
        message = f"""
🎯 NOUVEAU LEAD !

👤 Nom: {lead_data['name']}
📧 Email: {lead_data['email']}
📱 Téléphone: {lead_data.get('phone', 'Non renseigné')}
🏢 Entreprise: {lead_data.get('company', 'Non renseigné')}
💬 Message: {lead_data.get('message', 'Aucun message')}

🕐 Date: {lead_data['timestamp']}
🔗 Source: {lead_data.get('source', 'Landing Page')}

Total de leads: {len(leads_db)}
        """

        try:
            await self.bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                text=message,
                parse_mode='HTML'
            )
            logger.info(f"Notification envoyée pour lead: {lead_data['email']}")
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de notification: {e}")

    def add_lead(self, lead_data: dict):
        """Adiciona lead ao banco de dados"""
        lead_data['timestamp'] = datetime.now().isoformat()
        leads_db.append(lead_data)
        logger.info(f"Lead ajouté: {lead_data['name']} - {lead_data['email']}")

    def run(self):
        """Inicia o bot"""
        logger.info("Bot Telegram démarré...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Função principal"""
    if TELEGRAM_BOT_TOKEN == 'YOUR_BOT_TOKEN':
        print("⚠️ ERRO: Configure TELEGRAM_BOT_TOKEN no arquivo .env")
        return

    bot = TelegramBot(TELEGRAM_BOT_TOKEN)
    bot.run()


if __name__ == '__main__':
    main()
