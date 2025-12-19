# 🚀 Landing Page + Bot Telegram - Cliente Francês

Système complet de landing page avec tracking de conversions via Telegram Bot et Snapchat Pixel.

## 🌐 Demo Live

**Landing Page:** https://avilaops.github.io/landing-bot-client-france/

**Test Suite:** https://avilaops.github.io/landing-bot-client-france/test.html

## 📦 Fonctionnalités

### Landing Page
- ✅ Design responsif moderne
- ✅ Formulaire de capture de leads
- ✅ Animations fluides
- ✅ Optimisée pour la conversion
- ✅ SEO friendly

### Bot Telegram
- ✅ Notifications instantanées des nouveaux leads
- ✅ Commandes de gestion (/stats, /leads, /today)
- ✅ Dashboard de métriques
- ✅ Stockage des données

### Intégrations
- ✅ Snapchat Pixel pour tracking
- ✅ Webhook server (FastAPI)
- ✅ MongoDB pour persistance
- ✅ Analytics en temps réel

## 🛠️ Stack Technique

**Frontend:**
- HTML5, CSS3, JavaScript
- GitHub Pages (hosting)

**Backend:**
- Python 3.11+
- FastAPI (webhook server)
- python-telegram-bot
- MongoDB Atlas
- Railway (hosting)

## 📋 Structure du Projet

```
├── landing-page.html          # Page principale
├── index.html                 # Redirection
├── test.html                  # Suite de tests
├── webhook_server.py          # Serveur webhook FastAPI
├── telegram_bot.py            # Bot Telegram
├── requirements.txt           # Dépendances Python
├── railway.toml               # Config Railway
└── .github/workflows/         # CI/CD GitHub Actions
```

## 🚀 Déploiement

### Frontend (GitHub Pages)
Déployé automatiquement via GitHub Actions à chaque push sur `main`.

### Backend (Railway)
1. Connecter le repo sur Railway
2. Configurer les variables d'environnement
3. Deploy automatique

## 📊 Configuration

Variables d'environnement requises:
```env
TELEGRAM_BOT_TOKEN=your_token
ADMIN_CHAT_ID=your_chat_id
MONGODB_URL=your_mongodb_url
DATABASE_NAME=landing_bot
```

## 📖 Documentation

- [SETUP.md](./SETUP.md) - Guide de configuration
- [DEPLOY_RAILWAY_GITHUB.md](./DEPLOY_RAILWAY_GITHUB.md) - Guide de déploiement
- [PLATAFORMAS.md](./PLATAFORMAS.md) - Options de plateformes
- [INSTRUCOES_CLIENTE.md](./INSTRUCOES_CLIENTE.md) - Instructions client

## 💰 Coûts

- **GitHub Pages:** €0/mois (gratuit)
- **Railway:** €5/mois
- **MongoDB Atlas:** €0/mois (free tier 512MB)
- **Total:** ~€5/mois

## 🧪 Tests

Accédez à la page de tests: https://avilaops.github.io/landing-bot-client-france/test.html

Tests disponibles:
1. Health check webhook server
2. Connexion bot Telegram
3. Soumission de lead de test
4. Chargement Snapchat Pixel

## 📞 Support

Pour questions ou support technique, consultez la documentation ou créez une issue.

## 📄 Licence

© 2025 - Projet propriétaire du client

---

**Status:** ✅ Production Ready | 🚀 Live at https://avilaops.github.io/landing-bot-client-france/
