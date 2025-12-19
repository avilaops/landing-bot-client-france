# 🚀 LeadCapture — Landing Page + Telegram Bot

Landing page moderna com design Apple-style + Bot Telegram para captura de leads.

## ✨ Stack Tecnológico

- **TypeScript** - Type safety e desenvolvimento moderno
- **Vite** - Build ultra-rápido e HMR
- **Iconoir** - Ícones SVG open-source premium
- **FastAPI** - Backend Python para webhooks
- **MongoDB Atlas** - Database cloud
- **Railway** - Deploy backend
- **GitHub Pages** - Deploy frontend

## 🎨 Features

- ✅ Design Apple-inspired com glassmorphism
- ✅ Animações suaves e scroll effects
- ✅ Dark mode automático
- ✅ TypeScript com strict mode
- ✅ Iconoir icons integrados
- ✅ Formulário com validação
- ✅ Snapchat Pixel tracking
- ✅ Responsivo mobile-first
- ✅ Performance otimizada

## 🛠️ Desenvolvimento

```bash
# Instalar dependências
npm install

# Servidor de desenvolvimento (localhost:3000)
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview

# Type checking
npm run type-check
```

## 📦 Estrutura do Projeto

```
landing-bot-client-france/
├── src/
│   ├── main.ts          # Aplicação principal TypeScript
│   ├── style.css        # Estilos globais
│   └── vite-env.d.ts    # Types do Vite
├── index.html           # Entry point
├── package.json         # Dependências e scripts
├── tsconfig.json        # Config TypeScript
├── vite.config.ts       # Config Vite
├── webhook_server.py    # Backend FastAPI
└── telegram_bot.py      # Bot Telegram
```

## 🌐 URLs

- **Frontend (GitHub Pages)**: https://avilaops.github.io/landing-bot-client-france/
- **Backend (Railway)**: https://landing-bot-client-france-production.up.railway.app
- **API Health**: https://landing-bot-client-france-production.up.railway.app/health

## 🚀 Deploy

### Frontend (Automático via GitHub Actions)
Cada push para `main` dispara build e deploy no GitHub Pages.

### Backend (Railway)
Conectado ao GitHub, auto-deploy em cada push.

## 📝 Variáveis de Ambiente

Backend Railway precisa:
- `TELEGRAM_BOT_TOKEN` - Token do BotFather
- `ADMIN_CHAT_ID` - Chat ID do admin
- `MONGODB_URL` - Connection string MongoDB Atlas

## 🎯 Próximos Passos

1. Instalar dependências: `npm install`
2. Rodar dev server: `npm run dev`
3. Obter token do bot do cliente
4. Configurar variáveis no Railway
5. Build e deploy: `npm run build`

## 📄 Licença

MIT © Avila Development

---

**Desenvolvido com ❤️ usando TypeScript + Vite + Iconoir**