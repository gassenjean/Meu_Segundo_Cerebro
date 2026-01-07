# 📧 Configurar E-mail Automático para Devocionais

Este documento explica como configurar o envio automático de devocionais por e-mail usando GitHub Actions.

---

## 🎯 Como Funciona

Sempre que você (ou Claude) criar um novo devocional e fazer commit/push:
1. GitHub Actions detecta automaticamente o novo arquivo
2. Formata o devocional (remove markdown, frontmatter, etc.)
3. Envia por e-mail para você com assunto formatado
4. Você recebe pronto para copiar/encaminhar no WhatsApp

---

## ⚙️ Configuração (Uma Vez Só)

### Passo 1: Configurar E-mail no GitHub

Vá para: **Seu Repositório** → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Você precisa criar **5 secrets**:

#### 1. `MAIL_SERVER`
- **Valor:** Servidor SMTP do seu provedor
- **Gmail:** `smtp.gmail.com`
- **Outlook/Hotmail:** `smtp-mail.outlook.com`
- **Yahoo:** `smtp.mail.yahoo.com`

#### 2. `MAIL_PORT`
- **Valor:** Porta do servidor SMTP
- **Para TLS (Gmail, Outlook):** `587`
- **Para SSL:** `465`

#### 3. `MAIL_USERNAME`
- **Valor:** Seu e-mail completo
- **Exemplo:** `seuemail@gmail.com`

#### 4. `MAIL_PASSWORD`
- ⚠️ **NÃO use sua senha normal do e-mail!**
- Use "Senha de App" (App Password)

**Como gerar senha de app no Gmail:**
1. Acesse: https://myaccount.google.com/security
2. Ative "Verificação em duas etapas" (se não estiver ativa)
3. Vá em "Senhas de app": https://myaccount.google.com/apppasswords
4. Gere uma senha para "Mail"
5. Copie a senha de 16 caracteres
6. Cole no secret `MAIL_PASSWORD`

**Outlook/Hotmail:**
1. Acesse: https://account.microsoft.com/security
2. Vá em "Advanced security options"
3. Procure "App passwords"
4. Gere uma senha

#### 5. `MAIL_TO`
- **Valor:** E-mail que vai RECEBER o devocional
- **Exemplo:** `seuemail@gmail.com` (pode ser o mesmo ou diferente)

---

### Passo 2: Salvar os Secrets

Para CADA secret acima:
1. Clique em **New repository secret**
2. **Name:** Nome exato do secret (ex: `MAIL_SERVER`)
3. **Value:** O valor correspondente
4. Clique em **Add secret**

Repita para os 5 secrets.

---

## ✅ Testar

Depois de configurar os 5 secrets:

1. Crie um devocional novo (ou peça para Claude criar)
2. Faça commit e push
3. Vá em **Actions** no GitHub
4. Veja o workflow "Enviar Devocional por E-mail" rodando
5. Verifique seu e-mail em alguns minutos

---

## 📧 Formato do E-mail

Você receberá:

**Assunto:**
```
📖 Devocional RPSP - 03 de Janeiro de 2026 - Ações de Graças e Oração
```

**Corpo:**
- Texto limpo (sem markdown)
- Formatado para WhatsApp
- Pronto para copiar e colar
- Sem frontmatter ou metadados técnicos

---

## 🔧 Troubleshooting

### E-mail não chegou?

1. **Verifique o workflow no GitHub:**
   - Vá em **Actions** no repositório
   - Veja se o workflow "Enviar Devocional por E-mail" rodou
   - Se falhou, clique para ver o erro

2. **Erros comuns:**
   - **"Authentication failed":** Senha de app incorreta ou não configurada
   - **"Connection refused":** Server/Port incorretos
   - **"Invalid credentials":** Username está errado

3. **Verifique spam:**
   - Primeiro envio pode cair no spam
   - Marque como "Não é spam" para próximos

4. **Gmail bloqueando?**
   - Certifique-se de usar Senha de App (não a senha normal)
   - Verifique se "Verificação em duas etapas" está ativa

---

## 📝 Manutenção

**Nada!** Uma vez configurado, funciona automaticamente.

Todo devocional novo será enviado por e-mail sem você precisar fazer nada.

---

## 🎓 Arquivos do Sistema

- **Workflow:** `.github/workflows/enviar-devocional.yml`
- **Script:** `.github/scripts/formatar_devocional.py`
- **Docs:** Este arquivo

---

**Criado:** 03/01/2026
**Status:** ✅ Pronto para usar (após configurar secrets)
