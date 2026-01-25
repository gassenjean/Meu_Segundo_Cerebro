# PROMPT: Criar Skill Antigravity - session-log-archiver

**Para:** Gemini 3 Pro (Antigravity)
**Data:** 18/JAN/2026
**Prioridade:** ALTA (SESSION_LOG.md está com 2656 linhas - muito longo!)
**Contexto:** Sistema Bi-IA - Manutenção de Logs

---

## 🎯 OBJETIVO

Criar skill que automatiza o arquivamento de entradas antigas do SESSION_LOG.md, mantendo apenas as últimas 30-50 entradas ativas e movendo o histórico antigo para arquivo de backup mensal.

---

## 📋 ESPECIFICAÇÕES DA SKILL

### Metadados

**Nome Técnico:** `session-log-archiver`

**Triggers:**
- "arquivar session log"
- "limpar session log"
- "manter log recente"

**Versão:** 1.0

---

## 🔧 FUNCIONALIDADES OBRIGATÓRIAS

### 1. Leitura e Análise
- [ ] Ler SESSION_LOG.md completo
- [ ] Identificar entradas individuais (cada entrada começa com `## 🟣` ou `## 🔵`)
- [ ] Contar total de entradas
- [ ] Extrair timestamp de cada entrada (formato: DD/MMM/YYYY)

### 2. Lógica de Arquivamento

**Critério:** Manter apenas as **últimas 30 entradas** no SESSION_LOG.md ativo

**Arquivamento:**
- Entradas antigas (31+) vão para: `00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_[MES]_[ANO].md`
- Exemplo: `SESSION_LOG_ARQUIVO_JAN_2026.md`
- Se arquivo do mês já existir, **append** (não sobrescrever)

### 3. Estrutura do Arquivo de Arquivo

**Template:**
```markdown
---
criado: [DATA_PRIMEIRA_ENTRADA]
atualizado: [DATA_ULTIMA_ENTRADA]
tags:
  - log-archive
  - session-history
periodo: [MES]/[ANO]
---

# SESSION LOG - Arquivo [MES]/[ANO]

**Total de entradas:** [N]
**Período:** [DATA_INICIO] a [DATA_FIM]

---

[ENTRADAS ANTIGAS AQUI - EM ORDEM CRONOLÓGICA REVERSA]
```

### 4. Atualização do SESSION_LOG.md

- [ ] Manter header original (frontmatter + título + metadados)
- [ ] Manter seção "CONTEXTO ATUAL DO VAULT" (se existir)
- [ ] Manter seção "MENSAGEM PARA CLAUDE/GEMINI" (se existir)
- [ ] Manter apenas últimas 30 entradas
- [ ] Adicionar nota no topo indicando quantas entradas foram arquivadas

**Nota exemplo:**
```markdown
> 📦 **Última limpeza:** 18/JAN/2026 - 200 entradas arquivadas em `00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_JAN_2026.md`
```

---

## 🛡️ SAFETY & QUALIDADE

### Backup
- [ ] Criar backup completo: `SESSION_LOG.md.bak_[TIMESTAMP]` ANTES de qualquer modificação
- [ ] Manter último backup (.bak) sempre

### Validação
- [ ] Verificar que arquivo de arquivo foi criado com sucesso
- [ ] Verificar que SESSION_LOG.md resultante tem exatamente 30 entradas (ou menos se total < 30)
- [ ] Verificar encoding UTF-8
- [ ] Meses em PT-BR (JAN, FEV, MAR, ABR, MAI, JUN, JUL, AGO, SET, OUT, NOV, DEZ)

### Preview & Confirmação
- [ ] Mostrar preview:
  - Total de entradas atuais: X
  - Entradas a arquivar: Y
  - Entradas a manter: 30
  - Arquivo destino: `SESSION_LOG_ARQUIVO_[MES]_[ANO].md`
- [ ] Solicitar confirmação do usuário (ou modo --auto se confiante)

---

## 🧪 CASOS DE TESTE

### Teste 1: Arquivo Grande (>100 entradas)
**Input:** SESSION_LOG.md com 150 entradas
**Expectativa:**
- Manter últimas 30 no SESSION_LOG.md
- Arquivar 120 entradas mais antigas em `SESSION_LOG_ARQUIVO_[MES]_[ANO].md`
- Backup criado

### Teste 2: Arquivo Pequeno (<30 entradas)
**Input:** SESSION_LOG.md com 20 entradas
**Expectativa:**
- Nenhuma ação (mensagem: "SESSION_LOG.md já está enxuto (20 entradas). Nada a arquivar.")

### Teste 3: Múltiplos Meses
**Input:** SESSION_LOG.md com entradas de DEZ/2025, JAN/2026, FEV/2026
**Expectativa:**
- Entradas de DEZ/2025 → `SESSION_LOG_ARQUIVO_DEZ_2025.md`
- Entradas antigas de JAN/2026 → `SESSION_LOG_ARQUIVO_JAN_2026.md`
- Últimas 30 permanecem no SESSION_LOG.md

### Teste 4: Arquivo de Arquivo Já Existe
**Input:** `SESSION_LOG_ARQUIVO_JAN_2026.md` já existe com 50 entradas
**Expectativa:**
- Append (adicionar) novas entradas arquivadas ao arquivo existente
- Atualizar header (atualizado: [NOVA_DATA], total entradas: 50+X)

---

## 🗂️ ESTRUTURA DE ARQUIVOS

### Skill
```
.gemini/skills/session-log-archiver/
├── skill.md               # Metadados
└── scripts/
    ├── __init__.py        # Módulo Python
    ├── archiver.py        # Script principal
    └── parser.py          # Parser de entradas (opcional)
```

### Arquivos de Destino
```
00_SISTEMA/LOGS/
├── SESSION_LOG_ARQUIVO_JAN_2026.md
├── SESSION_LOG_ARQUIVO_FEV_2026.md
└── ... (um por mês conforme necessário)
```

---

## 💻 REQUISITOS TÉCNICOS

### Python
- Versão: 3.8+
- Dependências: stdlib (re, os, datetime, shutil)
- Encoding: UTF-8 sempre

### Lógica de Parsing

**Identificar início de entrada:**
```python
import re

# Regex para detectar entrada
pattern = r'^## (🟣|🔵) .+ - (\d{2}/\w{3}/\d{4})'
```

**Extração de mês/ano:**
```python
# Exemplo: "18/JAN/2026" -> MES="JAN", ANO="2026"
from datetime import datetime
```

---

## 📊 RELATÓRIO DE SAÍDA

**Formato:**
```
📦 SESSION LOG ARQUIVAMENTO

📋 Estatísticas:
   - Total de entradas analisadas: 150
   - Entradas mantidas (ativas): 30
   - Entradas arquivadas: 120

📁 Arquivos criados/atualizados:
   - 00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_DEZ_2025.md (50 entradas)
   - 00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_JAN_2026.md (70 entradas)

💾 Backup:
   - SESSION_LOG.md.bak_20260118_163000

✅ SESSION_LOG.md reduzido de 2656 para ~800 linhas
```

---

## ✅ CHECKLIST DE VALIDAÇÃO

Antes de aprovar a skill:

- [ ] Estrutura de pastas correta (.gemini/skills/session-log-archiver/)
- [ ] skill.md com metadados válidos (YAML)
- [ ] Script Python roda sem erros
- [ ] Backup automático funciona
- [ ] Parsing de entradas correto (identifica 🟣 e 🔵)
- [ ] Arquivamento por mês funciona
- [ ] Append em arquivo existente funciona
- [ ] Encoding UTF-8 preservado
- [ ] Meses em PT-BR
- [ ] Preview antes de executar
- [ ] Relatório de saída claro
- [ ] Testado com SESSION_LOG.md real (2656 linhas)

---

## 🎯 CRITÉRIOS DE SUCESSO

**Após rodar a skill:**
1. SESSION_LOG.md tem ≤ 30 entradas (últimas)
2. Entradas antigas estão arquivadas em `00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_*.md`
3. Backup `.bak` existe
4. Nenhuma entrada perdida (total antes = mantidas + arquivadas)
5. Formatação markdown preservada
6. Header e metadados preservados

---

## 📚 REFERÊNCIAS

- Template base: [[04_RECURSOS/TEMPLATES/TEMPLATE_Criar_Skill_Antigravity.md]]
- Padrão similar: session-logger (inserção no SESSION_LOG.md)
- Estrutura SESSION_LOG.md: Frontmatter YAML + Entradas com emoji 🟣/🔵

---

**FIM DO PROMPT**

**Instruções para Gemini:**
1. Criar estrutura `.gemini/skills/session-log-archiver/`
2. Implementar `archiver.py` com lógica completa
3. Testar com SESSION_LOG.md atual (2656 linhas)
4. Registrar criação no SESSION_LOG.md (ironia: última entrada antes de arquivar!)
5. Aguardar validação de Claude Code

**Prioridade:** ALTA (log muito longo dificulta leitura e pode causar problemas de performance)