# Landing Page + Bot Telegram + Snapchat Integration

## 🚀 Projeto Cliente Francês

Sistema completo de landing page com tracking de conversões via Telegram Bot e Snapchat Pixel.

## 📦 Estrutura do Projeto

```
landing-bot-project/
├── landing-page.html      # Landing page responsiva
├── telegram_bot.py        # Bot Telegram para tracking
├── webhook_server.py      # Servidor FastAPI para webhooks
├── requirements.txt       # Dependências Python
├── .env.example          # Exemplo de variáveis de ambiente
└── README.md             # Este arquivo
```

## 🔧 Configuração

### 1. Criar Bot no Telegram

1. Fale com [@BotFather](https://t.me/botfather) no Telegram
2. Use o comando `/newbot`
3. Escolha um nome e username para o bot
4. Copie o token fornecido

### 2. Obter Chat ID

```bash
# Envie uma mensagem para o bot e execute:
curl https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

### 3. Configurar Snapchat Pixel

1. Acesse [Snapchat Ads Manager](https://ads.snapchat.com/)
2. Vá em Events Manager → Create Pixel
3. Copie o Pixel ID
4. Cole no arquivo `landing-page.html`

### 4. Instalar Dependências

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente

```bash
# Copiar exemplo
cp .env.example .env

# Editar .env com seus dados
TELEGRAM_BOT_TOKEN=seu_token_aqui
ADMIN_CHAT_ID=seu_chat_id_aqui
SNAPCHAT_PIXEL_ID=seu_pixel_id_aqui
```

## 🚀 Execução

### Executar Bot Telegram

```bash
python telegram_bot.py
```

### Executar Servidor Webhook (opcional)

```bash
uvicorn webhook_server:app --reload --port 8000
```

### Testar Landing Page

Abra `landing-page.html` no navegador ou use um servidor local:

```bash
# Python
python -m http.server 8080

# Node.js
npx serve .
```

## 📊 Funcionalidades

### Landing Page
- ✅ Design responsivo (mobile, tablet, desktop)
- ✅ Formulário de captura de leads
- ✅ Animações suaves
- ✅ Otimizada para conversão
- ✅ Snapchat Pixel integrado
- ✅ Tracking de eventos

### Bot Telegram
- ✅ Notificações instantâneas de novos leads
- ✅ Comandos para visualizar estatísticas
- ✅ Lista de leads recentes
- ✅ Dashboard de métricas
- ✅ Armazenamento de dados

### Comandos Disponíveis

- `/start` - Iniciar o bot
- `/help` - Mostrar ajuda
- `/stats` - Estatísticas globais
- `/leads` - Lista dos 10 últimos leads
- `/today` - Leads de hoje

## 🔒 Segurança

- Token do bot deve estar em arquivo `.env` (nunca commitar)
- HTTPS obrigatório em produção
- Validação de dados no formulário
- Rate limiting no servidor

## 🚀 Deploy

### Frontend (Landing Page)

**Vercel:**
```bash
vercel --prod
```

**Netlify:**
```bash
netlify deploy --prod
```

### Backend (Bot Telegram)

**Railway:**
```bash
railway up
```

**Heroku:**
```bash
git push heroku main
```

## 📈 Tracking e Analytics

### Eventos Snapchat Rastreados:
- `PAGE_VIEW` - Visualização da página
- `SIGN_UP` - Submissão do formulário

### Dados Capturados:
- Nome completo
- Email
- Telefone
- Empresa
- Mensagem
- Timestamp
- URL de origem

## 💰 Modelo de Cobrança

**Setup Inicial:** €1.900
- Landing page completa
- Bot Telegram configurado
- Snapchat Pixel integrado
- Deploy em produção
- Documentação

**Mensalidade:**
- Meses 1-3: €400/mês (suporte premium)
- Meses 4+: €300/mês (manutenção)

**Inclui:**
- Hospedagem gerenciada
- Manutenção do bot
- Ajustes (até 2h/mês)
- Suporte técnico
- Analytics mensais

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript puro
- **Backend:** Python 3.11+
- **Bot:** python-telegram-bot
- **Servidor:** FastAPI
- **Tracking:** Snapchat Pixel
- **Deploy:** Vercel/Netlify + Railway

## 📞 Suporte

Para questões técnicas ou suporte:
- Email: [seu-email]
- Telegram: [@seu-telegram]
- Tempo de resposta: 24h (dias úteis)

## 📝 Changelog

### v1.0.0 - 19/12/2025
- ✅ Landing page inicial
- ✅ Bot Telegram básico
- ✅ Integração Snapchat Pixel
- ✅ Sistema de notificações
- ✅ Comandos de estatísticas

## 📄 Licença

© 2025 - Projeto proprietário do cliente
