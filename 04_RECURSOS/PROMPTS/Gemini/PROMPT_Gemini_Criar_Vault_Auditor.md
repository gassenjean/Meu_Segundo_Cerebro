# PROMPT: Criar Skill Antigravity - vault-auditor

**Para:** Gemini 3 Pro (Antigravity)
**Data:** 18/JAN/2026
**Prioridade:** ALTA (Limpeza e auditoria completa do vault)
**Contexto:** Sistema Bi-IA - Qualidade e Conformidade

---

## 🎯 OBJETIVO

Criar skill que faz **varredura completa** no vault, identifica **todos os erros e violações de padrões**, e gera **relatório detalhado** com ações corretivas sugeridas.

**Diferença do architect-linter (planejado):**
- `architect-linter`: Rodará automaticamente, checks rápidos, foco em prevenir novos erros
- `vault-auditor`: Roda sob demanda, análise profunda, foco em corrigir erros existentes

---

## 📋 ESPECIFICAÇÕES DA SKILL

### Metadados

**Nome Técnico:** `vault-auditor`

**Triggers:**
- "auditar vault"
- "varredura completa"
- "verificar erros no vault"
- "health check"

**Versão:** 1.0

---

## 🔍 CATEGORIAS DE VERIFICAÇÃO

### 1. Nomenclatura (CRÍTICO)

**Verificar contra:** `00_SISTEMA/PADROES/NOMENCLATURA.md`

**Checks:**
- [ ] Arquivos com espaços no nome (deve usar `_`)
- [ ] Prefixos incorretos ou ausentes
  - MOC sem `MOC_` ou `_MOC_`
  - Templates sem `TEMPLATE_`
  - Protocolos sem `PROTOCOLO_`
  - Planos sem `PLANO_`
  - Status sem `STATUS_`
  - Checkpoints sem `CHECKPOINT_`
- [ ] Nomes >60 caracteres
- [ ] Caracteres proibidos: `:`, `?`, `*`, `<`, `>`, `|`, `\`, `/`
- [ ] CamelCase incorreto (deve ser: `Categoria_Sub_Topico.md`)
- [ ] Datas em formato errado (deve ser: DDMMMYYYY, ex: 18JAN2026)

### 2. Localização (CRÍTICO)

**Verificar contra:** `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` e Guidelines

**Checks:**
- [ ] Arquivos na raiz que deveriam estar em categorias (01-05)
  - Exceções permitidas: README.md, CLAUDE.md, SESSION_LOG.md, PC_SYNC_LOG.md, STATUS_VAULT.md, CHANGELOG.md
- [ ] Templates fora de `04_RECURSOS/TEMPLATES/`
- [ ] Checklists fora de `04_RECURSOS/CHECKLISTS/`
- [ ] Prompts fora de `04_RECURSOS/PROMPTS/`
- [ ] MOCs de sistema fora de `00_SISTEMA/MOCs/`
- [ ] Protocolos fora de `00_SISTEMA/PROTOCOLOS/`
- [ ] Planos fora de `00_SISTEMA/planejamento/` ou `[projeto]/planejamento/`
- [ ] Checkpoints fora de `00_SISTEMA/CHECKPOINTS/` ou `[projeto]/checkpoints/`

### 3. Estrutura Markdown (IMPORTANTE)

**Checks:**
- [ ] Arquivos .md sem frontmatter YAML (recomendado, não obrigatório)
- [ ] Arquivos .md sem H1 (`# Título`)
- [ ] Múltiplos H1 no mesmo arquivo (deve ter apenas 1)
- [ ] Arquivos vazios (0 bytes ou apenas whitespace)

### 4. Links (IMPORTANTE)

**Checks:**
- [ ] Links quebrados `[[arquivo-inexistente.md]]`
- [ ] Links para arquivos movidos/renomeados
- [ ] Links com path absoluto (deveria ser relativo no Obsidian)

### 5. Organização de Projetos (IMPORTANTE)

**Verificar contra:** `02_PROJETOS/_GUIDELINES.md`

**Para cada pasta em `02_PROJETOS/`:**
- [ ] Tem `README.md`?
- [ ] Tem `STATUS_ATUAL.md`?
- [ ] Tem estrutura mínima (planejamento/, docs/, checkpoints/)?
- [ ] Tem `VALORES_OFICIAIS.md` (se aplicável)?

### 6. Duplicação (ATENÇÃO)

**Checks:**
- [ ] Arquivos com nome idêntico em pastas diferentes (pode ser legítimo, mas flag para revisão)
- [ ] Conteúdo duplicado (hash MD5 igual - pode indicar cópia acidental)

### 7. Arquivos Obsoletos (LIMPEZA)

**Checks:**
- [ ] Arquivos `.bak` >30 dias (podem ser limpos)
- [ ] Pastas `node_modules/` ou `.git/` duplicadas (não deveriam estar no vault)
- [ ] Arquivos temporários (`.tmp`, `.temp`, `~$`)

---

## 📊 RELATÓRIO DE SAÍDA

### Estrutura

**Arquivo:** `00_SISTEMA/RELATORIOS/AUDITORIA_VAULT_[DATA].md`

**Template:**
```markdown
---
data: DD/MMM/YYYY HH:MM
tipo: auditoria-vault
versao-auditor: 1.0
---

# RELATÓRIO: Auditoria Completa do Vault

**Data:** DD/MMM/YYYY HH:MM
**Ferramenta:** vault-auditor v1.0
**Total de arquivos analisados:** [N]
**Duração:** [X] segundos

---

## 📊 RESUMO EXECUTIVO

| Categoria | Total Erros | Severidade |
|-----------|-------------|------------|
| Nomenclatura | [N] | 🔴 CRÍTICO |
| Localização | [N] | 🔴 CRÍTICO |
| Estrutura Markdown | [N] | 🟡 IMPORTANTE |
| Links | [N] | 🟡 IMPORTANTE |
| Organização Projetos | [N] | 🟡 IMPORTANTE |
| Duplicação | [N] | 🟢 ATENÇÃO |
| Arquivos Obsoletos | [N] | 🟢 LIMPEZA |

**Status Geral:** [✅ Saudável / ⚠️ Atenção Necessária / 🔴 Ação Urgente]

---

## 🔴 ERROS CRÍTICOS (Nomenclatura)

### Arquivos com Espaços no Nome ([N] encontrados)

1. `caminho/arquivo com espaços.md`
   - **Problema:** Nome contém espaços
   - **Correção sugerida:** `arquivo_com_espacos.md`
   - **Comando:** `git mv "caminho/arquivo com espaços.md" "caminho/arquivo_com_espacos.md"`

[... mais erros ...]

### Prefixos Incorretos ([N] encontrados)

[... detalhes ...]

---

## 🔴 ERROS CRÍTICOS (Localização)

### Arquivos na Raiz ([N] encontrados)

1. `Arquivo_Perdido.md`
   - **Problema:** Arquivo na raiz do vault
   - **Categoria sugerida:** 01_CONHECIMENTO (baseado em conteúdo/nome)
   - **Ação:** Mover para `01_CONHECIMENTO/[subcategoria]/`

[... mais erros ...]

---

## 🟡 AVISOS (Estrutura Markdown)

[... detalhes ...]

---

## 🟡 AVISOS (Links Quebrados)

[... detalhes ...]

---

## 🟢 LIMPEZA SUGERIDA

### Arquivos .bak Antigos ([N] encontrados)

1. `SESSION_LOG.md.bak_20251215` (34 dias)
   - **Ação:** Pode ser deletado (>30 dias)

[... mais ...]

---

## ✅ CHECKLIST DE CORREÇÃO

**Prioridade CRÍTICA (Fazer Primeiro):**
- [ ] Corrigir [N] arquivos com espaços no nome
- [ ] Corrigir [N] prefixos incorretos
- [ ] Mover [N] arquivos para localização correta

**Prioridade IMPORTANTE (Fazer em Seguida):**
- [ ] Corrigir [N] arquivos sem H1
- [ ] Corrigir [N] links quebrados
- [ ] Completar estrutura de [N] projetos

**Limpeza (Opcional):**
- [ ] Deletar [N] arquivos .bak antigos
- [ ] Revisar [N] arquivos duplicados

---

## 📈 TENDÊNCIAS

**Comparação com última auditoria:**
- [Se existir auditoria anterior, comparar métricas]
- Novos erros: [N]
- Erros corrigidos: [N]
- Status: [Melhorando / Estável / Piorando]

---

**FIM DO RELATÓRIO**
```

---

## 💻 REQUISITOS TÉCNICOS

### Python
- Versão: 3.8+
- Dependências: stdlib (os, re, hashlib, datetime, yaml)
- Encoding: UTF-8

### Performance
- Vault típico: ~2000 arquivos
- Tempo esperado: <60 segundos
- Usar multi-threading se >5000 arquivos (opcional v2.0)

### Lógica de Detecção

**Nomenclatura:**
```python
import re

# Detectar espaços
if ' ' in filename:
    erros.append(...)

# Detectar prefixo
prefixos_validos = ['MOC_', '_MOC_', 'TEMPLATE_', 'PROTOCOLO_', ...]
if categoria_requer_prefixo and not any(filename.startswith(p) for p in prefixos_validos):
    erros.append(...)
```

**Links quebrados:**
```python
# Regex para encontrar [[links]]
links = re.findall(r'\[\[(.+?)\]\]', conteudo)

for link in links:
    if not os.path.exists(resolver_caminho(link)):
        erros.append(...)
```

---

## 🛡️ SAFETY & QUALIDADE

### Modo Read-Only
- [ ] Skill **NUNCA** modifica arquivos automaticamente
- [ ] Apenas **reporta** erros e **sugere** correções
- [ ] Usuário executa correções manualmente (ou via scripts separados)

### Backup
- [ ] Não aplicável (read-only)

### Falsos Positivos
- [ ] Criar arquivo `vault-auditor-exclusions.yaml` (opcional) para listar exceções
- Exemplo: arquivos legítimos na raiz, nomes especiais, etc.

### Encoding
- [ ] UTF-8 sempre
- [ ] Lidar graciosamente com arquivos binários (imagens, PDFs - pular)

---

## 🧪 CASOS DE TESTE

### Teste 1: Vault Limpo
**Input:** Vault 100% conforme padrões
**Expectativa:** Relatório com 0 erros, status "✅ Saudável"

### Teste 2: Vault com Erros Críticos
**Input:**
- 5 arquivos com espaços no nome
- 3 arquivos na raiz
- 2 prefixos incorretos
**Expectativa:**
- Relatório lista os 10 erros
- Severidade: 🔴 CRÍTICO
- Sugestões de correção específicas

### Teste 3: Vault com Links Quebrados
**Input:** 3 arquivos com `[[link-quebrado.md]]`
**Expectativa:** Relatório lista 3 links quebrados com localização exata (arquivo:linha)

### Teste 4: Projeto Incompleto
**Input:** `02_PROJETOS/ProjetoX/` sem `README.md` nem `STATUS_ATUAL.md`
**Expectativa:** Relatório flag ProjetoX como estrutura incompleta

---

## 🗂️ ESTRUTURA DE ARQUIVOS

### Skill
```
.gemini/skills/vault-auditor/
├── skill.md                    # Metadados
├── vault-auditor-exclusions.yaml  # (Opcional) Exceções
└── scripts/
    ├── __init__.py             # Módulo Python
    ├── auditor.py              # Script principal
    ├── checkers/               # Módulos de verificação
    │   ├── nomenclatura.py
    │   ├── localizacao.py
    │   ├── markdown.py
    │   ├── links.py
    │   └── projetos.py
    └── reporter.py             # Gerador de relatório
```

### Saída
```
00_SISTEMA/RELATORIOS/
├── AUDITORIA_VAULT_18JAN2026.md
├── AUDITORIA_VAULT_25JAN2026.md
└── ... (histórico)
```

---

## 🎯 FUNCIONALIDADES OPCIONAIS (v2.0 - Futuro)

- [ ] **Auto-fix mode:** Corrigir automaticamente erros simples (espaços → underscores)
- [ ] **Git integration:** Criar branch com correções + commit
- [ ] **Trend analysis:** Gráficos de evolução de erros ao longo do tempo
- [ ] **Exportar para JSON:** Para integração com outras ferramentas
- [ ] **Obsidian plugin:** Mostrar erros inline no editor

---

## ✅ CHECKLIST DE VALIDAÇÃO

Antes de aprovar a skill:

- [ ] Estrutura de pastas correta
- [ ] skill.md com metadados válidos
- [ ] Script Python roda sem erros
- [ ] Detecta todos os 7 tipos de erros documentados
- [ ] Gera relatório markdown bem formatado
- [ ] Read-only (não modifica nada)
- [ ] Encoding UTF-8
- [ ] Performance aceitável (<60s para 2000 arquivos)
- [ ] Testado com vault real (Meu_Segundo_Cerebro)
- [ ] Zero falsos positivos em exceções documentadas (README.md, etc.)

---

## 🎯 CRITÉRIOS DE SUCESSO

**Após rodar a skill:**
1. Relatório gerado em `00_SISTEMA/RELATORIOS/AUDITORIA_VAULT_[DATA].md`
2. Todos os erros reais identificados
3. Zero falsos positivos (arquivos legítimos não flagados)
4. Sugestões de correção acionáveis (comandos prontos)
5. Tempo de execução <60s
6. Formato markdown legível e bem organizado
7. Checklist pronta para copiar e usar

---

## 📚 REFERÊNCIAS

- Padrões: [[00_SISTEMA/PADROES/NOMENCLATURA.md]]
- Protocolos: [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]]
- Guidelines: `[categoria]/_GUIDELINES.md` (01-05)
- Template base: [[04_RECURSOS/TEMPLATES/TEMPLATE_Criar_Skill_Antigravity.md]]

---

**FIM DO PROMPT**

**Instruções para Gemini:**
1. Criar estrutura `.gemini/skills/vault-auditor/`
2. Implementar checkers modulares (1 por categoria)
3. Implementar gerador de relatório markdown
4. Testar com Meu_Segundo_Cerebro (vault real)
5. Gerar primeiro relatório de auditoria
6. Registrar no SESSION_LOG.md
7. Aguardar validação de Claude Code

**Prioridade:** ALTA (vault precisa estar 100% conforme padrões)
**Ordem sugerida:** Depois de session-log-archiver, antes de validate
