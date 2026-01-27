# 🔧 PROTOCOLO: Troubleshooting Skills Antigravity

**Responsável:** Antigravity (Gemini)
**Versão:** 1.0
**Ultima Atualização:** 18/JAN/2026

---

## 🎯 Objetivo

Diagnosticar e resolver problemas comuns na execução das skills automáticas do Gemini.

---

## 🔍 Diagnóstico Geral

### 1. Skill Não Ativa (Gemini não executa)

**Sintoma:** Você pede "Organizar vault" e o Gemini apenas responde com texto, sem rodar a ferramenta.

**Causas Prováveis:**

* Ambiguidade no prompt.
* Gemini entrou em modo "conversa" e esqueceu que tem ferramentas.
* Erro na chamada da ferramenta (o modelo tentou mas falhou silenciosamente).

**Solução:**

1. **Seja Explicito:** Use o comando de barra fake (ex: `/organizar`) ou diga "Execute a skill vault-organizer".
2. **Verifique o Contexto:** Se a conversa está muito longa, ele pode ter perdido o contexto das skills. Reinicie a sessão.

### 2. Skill Falha com Erro (Crash)

**Sintoma:** O Gemini tenta executar, aparece "Running...", mas retorna um erro vermelho ou texto de traceback Python.

**Diagnóstico:**

* Leia a última linha do erro (Ex: `FileNotFoundError`, `PermissionError`).
* Verifique se o script existe em `.gemini/skills/...`.

**Solução:**

1. **Dry Run:** Peça para rodar em modo de teste se disponível.
2. **Fallback Manual:** Se for urgente, rode o script via terminal (veja seção Fallback).

### 3. Resultado Incorreto (Lógica Errada)

**Sintoma:** A skill rodou com sucesso, mas fez algo errado (moveu arquivo errado, calculou métrica errada).

**Solução:**

1. **Undo/Restore:** Use o backup `.bak` gerado pela skill.
2. **Reporte:** Documente o edge case em `GUIA_Edge_Cases_Skills.md` para melhorarmos o script depois.

---

## 🐛 Problemas Comuns por Skill

### 🧹 vault-organizer

| Sintoma | Causa | Solução |
|---------|-------|---------|
| Moveu arquivo importante para `Arquivo_Morto` | Classificação agressiva | Mova de volta manualmente e adicione exceção no script futuramente. |
| Não moveu nada | Arquivos não bateram nas regras | Verifique se as extensões (.pdf, .jpg) estão cobertas nas regras. |
| Erro de Permissão | Arquivo aberto em outro programa | Feche arquivos (Word, PDF Reader) antes de organizar. |

### 📊 status-updater

| Sintoma | Causa | Solução |
|---------|-------|---------|
| Zerou o arquivo STATUS_VAULT | Erro gravíssimo de I/O | **RESTAURE O BACKUP IMEDIATAMENTE** (`STATUS_VAULT.md.bak`). |
| Progresso travado em X% | Heurística fixa | O script calcula progresso baseado em regras rígidas. Se quiser mudar, edite `metrics.py`. |
| Duplicou seções | Regex falhou ao achar marcadores | Verifique se alguém editou manualmente os marcadores `<!-- status:start -->`. |

### 📝 session-logger

| Sintoma | Causa | Solução |
|---------|-------|---------|
| "Git not found" | Git não instalado ou não no PATH | Instale Git ou verifique PATH. |
| Não detectou mudanças | Alterações não salvas ou .gitignore | Verifique se salvou os arquivos. Verifique se não está no .gitignore. |
| Encoding estranho (caracteres quebrados) | Windows CP1252 vs UTF-8 | Script força UTF-8, mas editor pode estar abrindo errado. Verifique configurações do editor. |

---

## 🚨 Fallback Manual (Linha de Comando)

Se o Gemini estiver "burro" ou as ferramentas falharem, você pode (e deve) rodar os scripts manualmente via terminal. É Python puro.

**Pré-requisitos:** Python 3 instalado.

### Executar Vault Organizer

```powershell
cd .gemini/skills/vault-organizer/scripts
python organizer.py
```

### Executar Status Updater

```powershell
cd .gemini/skills/status-updater/scripts
python updater.py
```

*Dica: Verifique `metrics.py` se quiser ver apenas os dados sem atualizar.*

### Executar Session Logger

```powershell
cd .gemini/skills/session-logger/scripts
python logger.py "Mensagem manual de log"
```

---

## 📜 Logs e Debug

* As skills geralmente imprimem logs no stdout (o que o Gemini vê).
* Se precisar de mais detalhes, procure por arquivos `.log` dentro da pasta `scripts/` (se a skill implementar logging em arquivo).

---

## ✅ Checklist de Diagnóstico

* [ ] Li a mensagem de erro inteira?
* [ ] O arquivo alvo existe e não está bloqueado?
* [ ] Tenho permissão de escrita na pasta?
* [ ] O Python está instalado e funcionando (`python --version`)?
* [ ] O Git está funcionando (`git status`)?
* [ ] Tentei rodar manualmente via terminal para isolar se é erro da IA ou do Script?

---

**Fim do Protocolo**
