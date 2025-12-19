# 🎯 Instruções para o Cliente - Bot Telegram

## 📱 Criar seu Bot no Telegram (5 minutos)

### Passo 1: Falar com o BotFather

1. **Abra o Telegram** (celular ou desktop)
2. Procure por: **@BotFather**
3. Clique em **START** ou envie `/start`

### Passo 2: Criar o Bot

Digite o comando:
```
/newbot
```

O BotFather vai fazer algumas perguntas:

**1. "Alright, a new bot. How are we going to call it?"**
```
Landing Page Cliente Bot
```
(Você pode escolher qualquer nome)

**2. "Good. Now let's choose a username for your bot."**
```
cliente_landing_bot
```
(Deve terminar em `_bot` e ser único)

### Passo 3: Guardar o Token

Você vai receber uma mensagem assim:

```
Done! Congratulations on your new bot.

Use this token to access the HTTP API:
1234567890:ABCdefGHIjklMNOpqrSTUvwxyz123456789

For a description of the Bot API, see this page: 
https://core.telegram.org/bots/api
```

**⚠️ IMPORTANTE:** Copie esse TOKEN e guarde em lugar seguro!

Envie para mim:
- ✅ Token do bot
- ✅ Link do bot (ex: t.me/cliente_landing_bot)

### Passo 4: Obter seu Chat ID

1. **Envie qualquer mensagem** para o bot que você acabou de criar (ex: "Olá")

2. **Abra este link no navegador:**
```
https://api.telegram.org/bot<SEU_TOKEN>/getUpdates
```
Substitua `<SEU_TOKEN>` pelo token que recebeu

3. Você verá algo assim:
```json
{
  "ok": true,
  "result": [{
    "update_id": 123456,
    "message": {
      "chat": {
        "id": 987654321,
        ...
      }
    }
  }]
}
```

4. **Copie o número** que aparece em `"chat": {"id": 987654321}`

Envie para mim:
- ✅ Seu Chat ID

---

## 🎨 Snapchat Pixel (Opcional - 10 minutos)

Se você quiser tracking no Snapchat Ads:

### Passo 1: Acessar Snapchat Ads Manager

1. Acesse: https://ads.snapchat.com/
2. Faça login
3. Vá em **Events Manager** (menu lateral esquerdo)

### Passo 2: Criar Pixel

1. Clique em **Create Pixel**
2. Escolha um nome: `Landing Page Conversions`
3. Clique em **Create**

### Passo 3: Copiar Pixel ID

Você verá algo como:
```
Pixel ID: abc123def456
```

**Copie esse ID** e envie para mim.

---

## 📧 O que enviar para mim

Depois de criar tudo, me envie:

```
✅ Bot Token: 1234567890:ABCdefGHIjklMNOpqrSTUvwxyz
✅ Chat ID: 987654321
✅ Link do Bot: t.me/cliente_landing_bot
✅ Snapchat Pixel ID (opcional): abc123def456
```

Com essas informações, vou:
1. Configurar tudo nos servidores
2. Fazer deploy da landing page
3. Testar toda a integração
4. Te enviar o link final!

---

## ❓ Dúvidas Comuns

**Q: O username do bot já está em uso**
A: Escolha outro nome único, ex: `cliente_landing_2024_bot`

**Q: Não encontro o Chat ID**
A: Certifique-se de enviar uma mensagem para o bot primeiro

**Q: Preciso do Snapchat Pixel?**
A: Não é obrigatório. Só se quiser medir conversões no Snapchat Ads

**Q: Quanto tempo leva?**
A: Com suas informações, deploy completo em 30 minutos!

---

## 🚀 Próximos Passos

Após você me enviar os dados:
1. ✅ Configuração completa (30 min)
2. ✅ Deploy da landing page
3. ✅ Testes de integração
4. ✅ Envio do link final
5. ✅ Tutorial de uso

**Estou aguardando suas informações!** 🎯
