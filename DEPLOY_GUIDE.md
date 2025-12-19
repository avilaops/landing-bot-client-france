# 🚀 Guia de Deploy Rápido

## Pré-requisitos
- [ ] Conta GitHub
- [ ] Conta Vercel (login com GitHub)
- [ ] Conta Railway (login com GitHub) ✅ Já tem!
- [ ] Bot Telegram criado no @BotFather

---

## 📝 PASSO 1: Criar Bot no Telegram (5 minutos)

1. Abra o Telegram e procure por **@BotFather**
2. Envie o comando: `/newbot`
3. Escolha um nome: `Landing Page Cliente Francês Bot`
4. Escolha um username: `cliente_frances_landing_bot` (deve terminar em `_bot`)
5. **Copie o TOKEN** que aparece (ex: `123456789:ABCdefGHIjklMNOpqrSTUvwxyz`)
6. Envie uma mensagem para o bot criado
7. Obtenha seu Chat ID:
   ```
   https://api.telegram.org/bot<SEU_TOKEN>/getUpdates
   ```
   Copie o número que aparece em `"chat":{"id":123456789}`

---

## 🌐 PASSO 2: Deploy Landing Page no Vercel (3 minutos)

### Método 1: Via GitHub (Recomendado)

1. **Criar repositório:**
   ```bash
   cd d:\Theo\landing-bot-project
   git init
   git add .
   git commit -m "Initial commit - Landing Page + Bot"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/landing-bot-frances.git
   git push -u origin main
   ```

2. **Deploy no Vercel:**
   - Acesse: https://vercel.com/new
   - Importe o repositório `landing-bot-frances`
   - Configure:
     - **Framework Preset:** Other
     - **Root Directory:** `./`
   - Clique em **Deploy**
   - ✅ Pronto! URL: `https://landing-bot-frances.vercel.app`

### Método 2: Via CLI (Mais Rápido)

```bash
# Instalar Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
cd d:\Theo\landing-bot-project
vercel --prod

# Seguir instruções na tela
```

---

## 🤖 PASSO 3: Deploy Backend no Railway (5 minutos)

### Opção A: Criar novo serviço no projeto existente

1. Acesse: https://railway.app/project/seu-projeto-arcsat
2. Clique em **"New"** → **"GitHub Repo"**
3. Se já tiver repo:
   - Selecione o repositório do projeto
   - **Root Directory:** `/`

4. Se criar novo repo:
   ```bash
   cd d:\Theo\landing-bot-project
   git add webhook_server.py telegram_bot.py requirements.txt
   git commit -m "Add webhook server and bot"
   git push
   ```

5. **Configurar variáveis de ambiente:**
   ```
   TELEGRAM_BOT_TOKEN=seu_token_do_botfather
   ADMIN_CHAT_ID=seu_chat_id
   MONGODB_URL=mongodb+srv://... (copiar do serviço Arcsat)
   DATABASE_NAME=landing_bot
   PORT=8000
   CORS_ORIGINS=https://seu-site.vercel.app
   ```

6. **Railway Settings:**
   - **Start Command:** `uvicorn webhook_server:app --host 0.0.0.0 --port $PORT`
   - Salvar e aguardar deploy

7. **Copiar URL pública:**
   - Settings → Generate Domain
   - Copiar URL (ex: `webhook-server.railway.app`)

### Opção B: Deploy no Render (Gratuito)

1. Acesse: https://render.com
2. New → Web Service
3. Connect GitHub repo
4. Configure:
   - **Name:** landing-bot-webhook
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn webhook_server:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variables (mesmo do Railway)
6. Create Web Service

---

## 🔗 PASSO 4: Conectar Tudo (10 minutos)

### 4.1 Atualizar Landing Page com URLs reais

Edite `landing-page.html`:

```javascript
// Linha ~196 - Atualizar token do bot
const TELEGRAM_BOT_TOKEN = 'SEU_TOKEN_REAL';
const TELEGRAM_CHAT_ID = 'SEU_CHAT_ID_REAL';

// OU usar webhook server (recomendado)
const WEBHOOK_URL = 'https://seu-webhook.railway.app/webhook/lead';
```

### 4.2 Configurar Snapchat Pixel

1. Acesse: https://ads.snapchat.com/
2. Events Manager → Create Pixel
3. Copie o Pixel ID
4. Edite `landing-page.html`:
   ```javascript
   // Linha ~15
   snaptr('init', 'SEU_PIXEL_ID_REAL', {...});
   ```

### 4.3 Fazer commit e redeploy

```bash
git add landing-page.html
git commit -m "Update: Add production URLs and tokens"
git push

# Vercel fará redeploy automático
```

---

## 🧪 PASSO 5: Testar (5 minutos)

### Teste 1: Landing Page
1. Acesse a URL do Vercel
2. Abra DevTools (F12) → Console
3. Preencha formulário
4. Verifique erros no console

### Teste 2: Telegram Bot
```bash
# Localmente primeiro
cd d:\Theo\landing-bot-project
python telegram_bot.py

# No Telegram, enviar /start para o bot
# Deve responder com mensagem de boas-vindas
```

### Teste 3: Webhook Server
```bash
# Testar endpoint
curl https://seu-webhook.railway.app/health

# Deve retornar: {"status":"healthy",...}
```

### Teste 4: Integração Completa
1. Abra a landing page
2. Preencha o formulário
3. Clique em "Enviar"
4. Verifique:
   - ✅ Mensagem de sucesso na tela
   - ✅ Notificação no Telegram
   - ✅ Evento no Snapchat (Events Manager)

---

## 🎯 Checklist Final

- [ ] Bot criado no @BotFather
- [ ] Token e Chat ID obtidos
- [ ] Landing page no Vercel
- [ ] Webhook server no Railway/Render
- [ ] MongoDB conectado
- [ ] URLs atualizadas no código
- [ ] Snapchat Pixel configurado
- [ ] Domínio custom (opcional)
- [ ] Testes completos realizados
- [ ] Cliente notificado

---

## 🔧 Próximos Passos (Pós-Deploy)

### Domínio Custom
1. **Vercel:**
   - Settings → Domains
   - Add domain: `exemplo.com.br`
   - Configurar DNS no Cloudflare

2. **Cloudflare:**
   - DNS → Add Record
   - Type: `CNAME`
   - Name: `@` ou `landing`
   - Content: `cname.vercel-dns.com`

### Monitoramento
- [ ] Configurar UptimeRobot (gratuito)
- [ ] Analytics: Google Analytics ou Plausible
- [ ] Alertas no Telegram

### Melhorias
- [ ] Google Tag Manager
- [ ] Hotjar ou Clarity (heatmaps)
- [ ] A/B testing
- [ ] Email automation

---

## 📞 Suporte

Se algo der errado:
1. Verifique logs no Railway/Render
2. Console do navegador (F12)
3. Teste endpoints manualmente
4. Confira variáveis de ambiente

## 💰 Custos Estimados

- Landing Page (Vercel): **€0/mês**
- Webhook Server (Railway): **€5/mês**
- MongoDB Atlas: **€0/mês** (512MB free)
- Domínio: **€10-15/ano** (opcional)

**Total:** ~€5/mês (€60/ano)
