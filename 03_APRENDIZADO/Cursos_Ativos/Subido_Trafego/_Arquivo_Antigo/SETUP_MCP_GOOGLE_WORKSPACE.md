---
criado: 2025-08-11T10:26:53-03:00
atualizado: 2025-08-11T10:26:53-03:00
---

# 📋 SETUP GOOGLE WORKSPACE MCP - GUIA COMPLETO

**Criado:** 11/08/2025 - 15:50h  
**Objetivo:** Integrar Claude Desktop com Google Drive para análise direta dos públicos KabaK

---

## 🎯 VISÃO GERAL

**Problema:** Múltiplos prints dos públicos Meta Ads são ineficientes
**Solução:** MCP (Model Context Protocol) para acesso direto ao Google Drive
**Resultado:** Comando natural "Claude, analise meus públicos KabaK" com análise completa

---

## 🔧 OPÇÃO RECOMENDADA: GOOGLE WORKSPACE MCP

**Repositório:** `aaronsb/google-workspace-mcp`
**Vantagens:**

- Gmail + Drive + Calendar integrados
- OAuth2 automático
- Docker container simplificado
- Documentação completa
- Credenciais salvas permanentemente

---

## 📋 SETUP PASSO-A-PASSO

### **ETAPA 1: GOOGLE CLOUD CONSOLE**

1. **Acesse:** https://console.cloud.google.com
2. **Crie/selecione projeto** (ex: "Claude MCP KabaK")
3. **APIs & Services → Library → Habilite:**
   - Google Drive API
   - Gmail API
   - Google Calendar API
4. **Credentials → Create Credentials → OAuth 2.0 Client ID:**
   - Application type: **Desktop App**
   - Name: "Claude MCP KabaK"
   - Authorized redirect URIs: `http://localhost:8080`
5. **Download JSON** das credenciais

### **ETAPA 2: CLAUDE DESKTOP SETUP**

1. **Download:** https://claude.ai/download
2. **Instalar e fazer login**
3. **Localizar arquivo config:**
   - **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%/Claude/claude_desktop_config.json`
4. **Criar/editar arquivo config:**

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-p",
        "8080:8080",
        "-v",
        "~/.mcp/google-workspace:/app/config",
        "-e",
        "GOOGLE_CLIENT_ID",
        "-e",
        "GOOGLE_CLIENT_SECRET",
        "ghcr.io/aaronsb/google-workspace-mcp:latest"
      ],
      "env": {
        "GOOGLE_CLIENT_ID": "SEU_CLIENT_ID_AQUI.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "SEU_CLIENT_SECRET_AQUI"
      }
    }
  }
}
```

### **ETAPA 3: AUTENTICAÇÃO**

1. **Reiniciar Claude Desktop** completamente
2. **Verificar conexão** no chat: "List my Google Drive files"
3. **Browser abrirá automaticamente** para OAuth
4. **Autorizar acesso** no Google
5. **Credenciais salvas** em `~/.mcp/google-workspace/`
6. **Confirmação:** Claude listará arquivos do Drive

---

## 🎯 ANÁLISE DOS PÚBLICOS KABAK

### **COMANDOS PRÁTICOS:**

```
"Claude, acesse meu Google Drive e procure por arquivos
relacionados aos públicos da KabaK que criei no Meta Ads"

"Liste todos os documentos que contenham dados de
segmentação, públicos personalizados ou configurações
de campanhas da KabaK"

"Analise as configurações dos públicos e compare com
as melhores práticas que acabamos de aprender na A03"
```

### **ANÁLISE SISTEMÁTICA INCLUIRÁ:**

**✅ Verificação Técnica:**

- Tamanhos mínimos adequados (>1000)
- Tipos de público seguindo regras Pedro
- Janelas temporais otimizadas
- Nomenclatura organizada

**⚙️ Regras Ouro A03:**

- Lookalikes baseados em públicos qualificados
- Semelhança com objetivos (vendas → LLA compradores)
- Lógica E/OU apropriada
- Segmentação "óbvia que funciona"

**🔧 Otimizações:**

- Públicos em falta críticos
- Configurações subotimizadas
- Estrutura para testes A/B
- Conexão com objetivos KabaK

---

## 🚀 VANTAGENS SISTEMA

### **IMEDIATO:**

- **Sem prints múltiplos** - Acesso direto arquivos
- **Contexto completo** - Histórico + configurações
- **Análise baseada A03** - Conhecimento fresh aplicado
- **Recommendations específicas** - KabaK/Gabriele

### **FUTURO ESCALÁVEL:**

- **Gmail:** Análise campanhas email
- **Calendar:** Planejamento conteúdo/lançamentos
- **Drive:** Centralização assets/criativos
- **Outros MCPs:** Integração Meta Ads (quando disponível)

---

## 🔧 TROUBLESHOOTING

### **Docker não instalado:**

```bash
# Mac
brew install docker

# Windows
Download Docker Desktop from docker.com
```

### **Config não funciona:**

- Verificar JSON syntax válido
- Reiniciar Claude Desktop completamente
- Verificar credenciais Google Cloud

### **OAuth falha:**

- Confirmar redirect URI: `http://localhost:8080`
- Verificar APIs habilitadas
- Testar credenciais no Google Cloud Console

---

## ⚡ NEXT STEPS

1. **Setup MCP** (30 minutos)
2. **Testar conexão** com comando simples
3. **Upload públicos KabaK** no Drive (se não estiverem)
4. **Análise completa** via comando natural
5. **Implementar recommendations** nos Meta Ads

## 🌫️ OBSERVAÇÕES NÉVOA

**Sobre MCP research:**
Primeira vez explorando Model Context Protocol. Sistema mais elegante que expected - é realmente "USB-C para AI" como prometido. Google Workspace MCP via Docker remove friction setup.

**Implementação real vs hype:**
Documentação clara, repositórios ativos, community growing. Não é apenas buzzword - solução prática para problema real (múltiplos prints ineficientes).

**Próxima evolução:**
Quando Meta lançar MCP oficial (provavelmente 2025), integração direta Meta Ads + Claude. Por enquanto, Drive analysis sufficient.

**Connection A03:**
Perfeito timing - acabamos de dominar 5 tipos públicos + regras ouro. MCP permite aplicação imediata conhecimento fresh em dados reais.

---

**STATUS:** Pesquisa completa, setup ready para implementação

_[MCP identificado como solução otimizada para análise sem friction]_
