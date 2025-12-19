# 🚀 Deploy: GitHub Pages + Railway

## Arquitetura Escolhida

- **Frontend (Landing Page):** GitHub Pages (gratuito)
- **Backend (Bot + Webhook):** Railway ($5/mês)

---

## 📄 PARTE 1: Deploy Landing Page no GitHub Pages

### Passo 1: Criar Repositório no GitHub

```bash
# Já está com git init feito!
cd d:\Theo\landing-bot-project

# Criar repo no GitHub primeiro (via web):
# 1. Acesse: https://github.com/new
# 2. Nome: landing-bot-frances
# 3. Public ou Private
# 4. Criar repositório

# Conectar repo local ao GitHub
git remote add origin https://github.com/SEU_USUARIO/landing-bot-frances.git
git branch -M main
git push -u origin main
```

### Passo 2: Ativar GitHub Pages

1. No GitHub, vá no repositório
2. **Settings** → **Pages** (menu lateral)
3. **Source:** Deploy from a branch
4. **Branch:** main / (root)
5. Clique em **Save**

✅ Em ~2 minutos, site estará no ar em:
```
https://SEU_USUARIO.github.io/landing-bot-frances/
```

### Alternativa: GitHub Actions (Deploy Automático)

O workflow já está criado em `.github/workflows/deploy.yml`

Após push, o deploy é automático! 🚀

---

## 🤖 PARTE 2: Deploy Backend no Railway

### Passo 1: Preparar Backend para Railway

Criar arquivo `railway.toml`:

```toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "uvicorn webhook_server:app --host 0.0.0.0 --port $PORT"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

### Passo 2: Fazer Commit

```bash
git add railway.toml
git commit -m "Add Railway config"
git push
```

### Passo 3: Deploy no Railway

**Opção A: Via Dashboard (Recomendado)**

1. Acesse: https://railway.app
2. **New Project** → **Deploy from GitHub repo**
3. Selecione: `landing-bot-frances`
4. Railway detecta Python automaticamente

**Opção B: Via CLI**

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Passo 4: Configurar Variáveis de Ambiente

No Railway Dashboard → Variables:

```bash
TELEGRAM_BOT_TOKEN=seu_token_aqui
ADMIN_CHAT_ID=seu_chat_id
MONGODB_URL=mongodb+srv://... (usar o mesmo do Arcsat)
DATABASE_NAME=landing_bot
PORT=8000
ENVIRONMENT=production
```

### Passo 5: Gerar Domínio Público

1. Railway Dashboard → Settings
2. **Generate Domain**
3. Copiar URL (ex: `webhook-server-production.railway.app`)

---

## 🔗 PARTE 3: Conectar Frontend e Backend

### Atualizar landing-page.html

Editar o arquivo com as URLs reais:

```javascript
// Opção 1: Webhook Server (Recomendado)
const WEBHOOK_URL = 'https://seu-webhook.railway.app/webhook/lead';

// Opção 2: Direto Telegram API
const TELEGRAM_BOT_TOKEN = 'SEU_TOKEN';
const TELEGRAM_CHAT_ID = 'SEU_CHAT_ID';
```

### Fazer Commit

```bash
git add landing-page.html
git commit -m "Update: Add production URLs"
git push
```

GitHub Pages atualiza automaticamente em ~1 minuto.

---

## 🧪 PARTE 4: Testar Tudo

### 1. Testar Webhook Server

```bash
curl https://seu-webhook.railway.app/health
# Deve retornar: {"status":"healthy",...}
```

### 2. Testar Landing Page

1. Acesse: `https://seu-usuario.github.io/landing-bot-frances/`
2. Preencha o formulário
3. Verifique notificação no Telegram

### 3. Usar Página de Testes

Acesse: `https://seu-usuario.github.io/landing-bot-frances/test.html`

---

## 📊 Configuração Final

### Domínio Custom (Opcional)

#### GitHub Pages:
1. Compre um domínio (ex: `landing.exemplo.com`)
2. No DNS, adicione:
   ```
   CNAME landing SEU_USUARIO.github.io
   ```
3. No GitHub: Settings → Pages → Custom domain
4. Digite: `landing.exemplo.com`

#### Railway:
1. Settings → Networking
2. Add Custom Domain: `api.exemplo.com`
3. Adicionar DNS:
   ```
   CNAME api railway-provided-url
   ```

---

## 💰 Custos

- **GitHub Pages:** €0/mês (gratuito)
- **Railway:** €5/mês (~$5)
- **Domínio (opcional):** €10-15/ano

**Total: €5/mês (€60/ano)**

---

## 📋 Checklist Completo

### Setup Inicial
- [ ] Repositório criado no GitHub
- [ ] Código pushado
- [ ] GitHub Pages ativado
- [ ] Railway conectado ao repo
- [ ] Variáveis de ambiente configuradas

### Configuração
- [ ] Bot Telegram criado no @BotFather
- [ ] Token e Chat ID obtidos
- [ ] URLs atualizadas na landing page
- [ ] Snapchat Pixel configurado (opcional)

### Deploy
- [ ] Landing page no ar (GitHub Pages)
- [ ] Webhook server no ar (Railway)
- [ ] Testes realizados
- [ ] Formulário funcionando
- [ ] Notificações Telegram OK

### Pós-Deploy
- [ ] Domínio custom configurado (opcional)
- [ ] Analytics configurado
- [ ] Cliente notificado

---

## 🛠️ Comandos Úteis

### Git
```bash
# Status
git status

# Commit e Push
git add .
git commit -m "Update: descrição"
git push

# Ver logs
git log --oneline
```

### Railway CLI
```bash
# Ver logs
railway logs

# Abrir dashboard
railway open

# Variáveis
railway variables
```

---

## ❓ Troubleshooting

### Landing page não carrega:
- Aguarde 2-3 minutos após ativar GitHub Pages
- Verifique Settings → Pages se está ativado
- Branch correta (main) e pasta (root)

### Webhook não responde:
- Verifique logs no Railway
- Teste URL: `curl https://url/health`
- Confira variáveis de ambiente

### Formulário não envia:
- Abra DevTools (F12) → Console
- Verifique erros de CORS
- Confirme URLs corretas no código

---

## 🚀 Próximos Passos

Agora é só:
1. ✅ Obter dados do bot (token + chat ID)
2. ✅ Atualizar landing-page.html
3. ✅ Push para GitHub
4. ✅ Testar!

**Tudo pronto para o deploy!** 🎉
