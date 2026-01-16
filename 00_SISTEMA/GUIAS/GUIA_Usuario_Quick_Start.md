# GUIA: Usuário Quick Start

**Navegação Rápida e Decision Trees para Gassen**

**Criado:** 16/Jan/2026
**Versão:** 1.0
**Propósito:** Reduzir fricção, decisão rápida, rotinas claras
**Audiência:** Gassen (usuário, dono do vault)

---

## 🎯 NAVEGAÇÃO RÁPIDA (30 SEGUNDOS)

**O que você quer fazer?**

```
┌──────────────────────────────────────────────────────────┐
│ CRIAR algo novo (arquivo, projeto, nota)                 │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 1: Criar


┌──────────────────────────────────────────────────────────┐
│ ENCONTRAR algo existente (arquivo, informação)           │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 2: Encontrar


┌──────────────────────────────────────────────────────────┐
│ ORGANIZAR vault (limpeza, estrutura, MOCs)               │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 3: Organizar


┌──────────────────────────────────────────────────────────┐
│ SINCRONIZAR (trocar PC, handoff IA, GitHub)              │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 4: Sincronizar


┌──────────────────────────────────────────────────────────┐
│ RESOLVER problema (erro, confusão, lentidão)             │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 5: Troubleshooting


┌──────────────────────────────────────────────────────────┐
│ MANUTENÇÃO periódica (semanal, mensal)                   │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 6: Rotinas
```

---

## SEÇÃO 1: Criar

### Decision Tree: O que criar?

```
Quero criar:

┌─────────────────────────────────────┐
│ NOTA RÁPIDA (captura rápida)        │
└───────────┬─────────────────────────┘
            ▼
        _inbox/ → Processar depois


┌─────────────────────────────────────┐
│ NOTA DE CONHECIMENTO (permanente)   │
└───────────┬─────────────────────────┘
            │
            ▼
    01_CONHECIMENTO/
    ├─ Qual área? (IA, Negócios, Dev Pessoal, etc)
    ├─ Seguir padrão: Area_Subarea_Topico.md
    └─ Atualizar _MOC_Conhecimento.md


┌─────────────────────────────────────┐
│ PROJETO NOVO                        │
└───────────┬─────────────────────────┘
            │
            ▼
    02_PROJETOS/Nome_Projeto/
    ├─ README.md (obrigatório)
    ├─ STATUS_ATUAL.md (obrigatório)
    ├─ planejamento/ checkpoints/ docs/ recursos/ tarefas/ metricas/
    └─ Ver: 02_PROJETOS/_GUIDELINES.md


┌─────────────────────────────────────┐
│ NOTA DE CURSO/LIVE                  │
└───────────┬─────────────────────────┘
            │
            ▼
    03_APRENDIZADO/Nome_Curso/notas/
    ├─ Seguir Sistema 5C
    ├─ Atualizar README.md do curso
    └─ Ver: 03_APRENDIZADO/_GUIDELINES.md


┌─────────────────────────────────────┐
│ TEMPLATE/RECURSO                    │
└───────────┬─────────────────────────┘
            │
            ▼
    04_RECURSOS/
    ├─ TEMPLATES/ → TEMPLATE_Nome.md
    ├─ PROMPTS/ → Prompt_IA_Funcao.md
    └─ CHECKLISTS/ → CHECKLIST_Nome.md


┌─────────────────────────────────────┐
│ NOTA PESSOAL (journal, ideia)       │
└───────────┬─────────────────────────┘
            │
            ▼
    05_PESSOAL/
    ├─ Journal/ → Journal_DDMMMYYYY.md
    ├─ Ideas/ → Idea_Nome.md
    └─ Reflections/ → Reflection_Topico.md
```

### Como Criar (Delegação IA)

**Opção 1: Claude Code (Recomendado para criação estrutural)**

```
"Claude, criar [tipo] sobre [assunto] em [categoria]"

Exemplo:
"Claude, criar projeto KabaK em 02_PROJETOS/ com estrutura completa"
```

**Opção 2: Gemini (Recomendado para processamento massivo)**

```
"Gemini, processar live #23 do Alan Nicolas e criar notas em 03_APRENDIZADO/"

Exemplo:
"Gemini, organizar 50 PDFs da pasta Downloads em 01_CONHECIMENTO/"
```

### Quando Usar Qual IA?

| Tarefa | Claude | Gemini |
|--------|--------|--------|
| Criar projeto completo | ✅ | ❌ |
| Criar template/protocolo | ✅ | ❌ |
| Processar 1 live/PDF | ✅ | ✅ |
| Processar 10+ lives/PDFs | ❌ | ✅ |
| Organizar <10 arquivos | ✅ | ❌ |
| Organizar 50+ arquivos | ❌ | ✅ |
| Decisão estratégica | ✅ | ❌ |

**Ver detalhes:** [[../PADROES/GUIA_Claude_vs_Gemini.md]]

---

## SEÇÃO 2: Encontrar

### Mapa de Pastas - Onde Está O Quê?

```
00_SISTEMA/           → Padrões, protocolos, MOCs, guias
├─ PADROES/          → NOMENCLATURA, ARCHITECTURE_GUIDELINES
├─ PROTOCOLOS/       → PROTOCOLO_*, TROUBLESHOOTING
├─ MOCs/             → Índices master
└─ GUIAS/            → Guias de leitura (este arquivo)

01_CONHECIMENTO/      → Base de conhecimento permanente
├─ IA_Tecnologia/    → IA, LLMs, prompts
├─ Negocios/         → Marketing, vendas, gestão
├─ Desenvolvimento_Pessoal/ → TDAH, produtividade, hábitos
└─ [outras áreas]

02_PROJETOS/          → Projetos ativos
├─ KabaK/            → Projeto KabaK (marca roupa)
├─ Segundo_Cerebro/  → Este vault (meta)
└─ [outros projetos]

03_APRENDIZADO/       → Cursos e estudos
├─ Alan_Nicolas_Academia_Lendaria/ → Lives, episódios, notas
└─ [outros cursos]

04_RECURSOS/          → Templates, prompts, ferramentas
├─ TEMPLATES/        → TEMPLATE_*
├─ PROMPTS/          → Prompt_*
└─ CHECKLISTS/       → CHECKLIST_*

05_PESSOAL/           → Journal, ideias, reflexões
├─ Journal/          → Diário (Journal_DDMMMYYYY.md)
├─ Ideas/            → Ideias (Idea_Nome.md)
└─ Reflections/      → Reflexões

_inbox/               → Captura rápida (processar depois)
```

### Buscar por Tipo

**Documentação de Padrões:**
→ `00_SISTEMA/PADROES/`

**Protocolos e Workflows:**
→ `00_SISTEMA/PROTOCOLOS/`

**Índices (MOCs):**
→ `00_SISTEMA/MOCs/` ou `[Categoria]/_MOC_*.md`

**Projetos:**
→ `02_PROJETOS/Nome_Projeto/`

**Cursos/Lives:**
→ `03_APRENDIZADO/Nome_Curso/`

**Templates:**
→ `04_RECURSOS/TEMPLATES/`

**Notas pessoais:**
→ `05_PESSOAL/`

### Atalhos Obsidian

**Buscar arquivo:**
- `Ctrl+O` → Quick Switcher (buscar por nome)
- `Ctrl+Shift+F` → Buscar em todos arquivos (conteúdo)

**Navegar:**
- `Ctrl+Click` em link → Abrir arquivo
- `Alt+←` → Voltar
- `Alt+→` → Avançar

**Criar:**
- `Ctrl+N` → Novo arquivo
- `Ctrl+Shift+N` → Nova janela

---

## SEÇÃO 3: Organizar

### Limpeza Rápida (Mensal)

**Comando:**
```
"Claude, executar limpeza do vault"

ou

"/limpeza-raiz-vault"  (comando slash)
```

**O que faz:**
- Remove arquivos temporários
- Organiza arquivos soltos na raiz
- Move para pastas corretas (00-05)
- Atualiza MOCs

**Tempo:** 5-10 minutos

### Organizar Inbox (_inbox/)

**Frequência:** Diária (ideal) ou Semanal

**Workflow:**
```
1. Abrir _inbox/
2. Para cada arquivo:
   ├─ É conhecimento? → 01_CONHECIMENTO/
   ├─ É projeto? → 02_PROJETOS/
   ├─ É curso? → 03_APRENDIZADO/
   ├─ É recurso? → 04_RECURSOS/
   └─ É pessoal? → 05_PESSOAL/
3. Atualizar MOCs relevantes
4. _inbox/ deve ficar VAZIO
```

**Delegação:**
```
"Claude, processar arquivos do _inbox/ e organizar nas categorias corretas"
```

### Atualizar MOCs

**Quando:**
- Criou arquivo novo → Atualizar MOC da categoria
- Moveu arquivo → Atualizar MOC de origem + destino
- Deletou arquivo → Remover link do MOC

**Localização dos MOCs:**
```
01_CONHECIMENTO/_MOC_Conhecimento.md
02_PROJETOS/_MOC_Projetos.md
03_APRENDIZADO/_MOC_Aprendizado.md
04_RECURSOS/_MOC_Recursos.md
05_PESSOAL/_MOC_Pessoal.md
```

**Delegação:**
```
"Claude, atualizar _MOC_Conhecimento.md com os 5 novos arquivos que criei"
```

---

## SEÇÃO 4: Sincronizar

### Trocar de PC (Alienware ↔ Desktop)

**Protocolo:**

**Ao SAIR de um PC:**
```
1. Atualizar PC_SYNC_LOG.md (o que fez)
2. Deixar mensagem para o outro PC
3. Aguardar OneDrive sync (2-5 min)
4. Fechar vault
```

**Ao ABRIR no outro PC:**
```
1. LER PC_SYNC_LOG.md PRIMEIRO
2. Ver mensagens para você
3. Continuar trabalho
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_MULTI_PC.md]]

### Handoff entre IAs (Claude → Gemini ou vice-versa)

**Claude delegando para Gemini:**
```
1. Claude atualiza SESSION_LOG.md
2. Claude deixa "Mensagem para Gemini"
3. Gemini lê SESSION_LOG.md ao iniciar
4. Gemini executa tarefa
5. Gemini reporta conclusão
```

**Quando usar:**
- Tarefa >100k tokens → Gemini
- Processamento massivo → Gemini
- Decisão estratégica → Claude
- Planejamento → Claude

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]]

### Sincronizar GitHub

**Cenário 1: Branches do iPhone (claude/*)**

```
Desktop/Alienware:
1. git fetch origin
2. git merge origin/claude/nome-branch
3. git push origin master
4. git push origin --delete claude/nome-branch
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]]

**Cenário 2: Criar issue/PR via Gemini**

```
"Gemini, criar issue no GitHub para documentar sistema X"

Gemini usa: gh issue create --title "..." --body "..."
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_ANTIGRAVITY_GITHUB.md]]

### Decision Tree: Qual Protocolo de Sincronização?

**Ver:** [[../MOCs/MOC_Sincronizacao_Sistemas.md]] (decision tree completo)

```
Trocar PC? → PROTOCOLO_MULTI_PC + PC_SYNC_LOG
Handoff IA? → PROTOCOLO_SINCRONIZACAO_AGENTES + SESSION_LOG
Branches iPhone? → PROTOCOLO_GITHUB_MULTI_DISPOSITIVO
GitHub API? → PROTOCOLO_ANTIGRAVITY_GITHUB
```

---

## SEÇÃO 5: Troubleshooting

### Problemas Comuns

**Ver guia completo:** [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]]

#### Problema 1: Claude não responde (Overload)

**Solução:**
1. Aguardar 5 minutos
2. Tentar novamente
3. Se persistir → Usar Gemini temporariamente

**Horários melhores:** Madrugada (0-6h), Fim de semana

---

#### Problema 2: Gemini quota excedida

**Solução:**
1. Aguardar reset (24h)
2. Dividir trabalho em múltiplos dias
3. Usar Claude para urgente

**Prevenção:** Planejar processamento massivo

---

#### Problema 3: Arquivo no lugar errado

**Solução:**
```
"Claude, mover arquivo X para local correto conforme padrões"
```

Claude vai:
- Consultar NOMENCLATURA.md
- Identificar local correto
- Mover arquivo
- Atualizar MOCs

---

#### Problema 4: Nome de arquivo errado

**Solução:**
```
"Claude, renomear arquivo X para padrão correto"
```

Claude vai:
- Aplicar padrão NOMENCLATURA.md
- Renomear arquivo
- Atualizar links/MOCs

---

#### Problema 5: Vault lento

**Solução:**
1. Aguardar OneDrive sync completo
2. Desabilitar plugins não usados (Obsidian settings)
3. Se >5000 arquivos → Dividir vault

**Delegação:**
```
"Claude, diagnosticar lentidão do vault"
```

---

## SEÇÃO 6: Rotinas

### Diária (5 minutos)

**Manhã:**
- [ ] Processar _inbox/ (captura rápida do dia anterior)
- [ ] Criar Journal_DDMMMYYYY.md (05_PESSOAL/Journal/)
- [ ] Revisar tarefas pendentes (projetos ativos)

**Noite:**
- [ ] Captura rápida em _inbox/ (ideias do dia)
- [ ] Atualizar STATUS_ATUAL.md (projetos ativos)

### Semanal (30 minutos) - Sexta 17h

**Ver protocolo:** [[../PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md]]

**Checklist:**
- [ ] Processar _inbox/ (deve ficar VAZIO)
- [ ] Atualizar projetos ativos (STATUS_ATUAL.md)
- [ ] Atualizar progresso aprendizado (03_APRENDIZADO/)
- [ ] Atualizar STATUS_VAULT.md
- [ ] Criar checkpoint semanal (CHECKPOINT_DDMMMYYYY.md)

**Comando:**
```
"Claude, executar revisão semanal"

ou

"/atualizar-status"  (comando slash)
```

---

### Mensal (1-2 horas) - Último Domingo

**Checklist:**
- [ ] Revisar _inbox/ profundamente
- [ ] Consolidar ideias em 05_PESSOAL/Ideas/
- [ ] Revisar projetos pausados (pausar ou reativar)
- [ ] Atualizar metas e OKRs (se usa)
- [ ] Backup completo do vault
- [ ] Revisar progresso financeiro (se rastreia)

**Comando:**
```
"Claude, executar revisão mensal completa"
```

---

## 🎯 ATALHOS ÚTEIS

### Comandos Slash (Claude Code)

```
/learn          → Ativar contexto aprendizado
/work           → Ativar contexto projetos
/nevoa          → Ativar agente Névoa (orquestração)
/claude-architect → Ativar Claude Architect (padrões)
/marie-kondo    → Ativar Marie Kondo (organização)
/atualizar-status → Atualizar STATUS_VAULT.md
/limpeza-raiz-vault → Limpar raiz do vault
/gemini         → Delegar para Gemini
/validate       → Validar criação de arquivo
```

**Ver lista completa:** `CLAUDE.md` seção "Available Commands"

---

### Arquivos Essenciais (Bookmarks Mentais)

**Leitura Frequente:**
- `CLAUDE.md` - Instruções master para IAs
- `README.md` - Visão geral do vault
- `STATUS_VAULT.md` - Estado atual do vault
- `SESSION_LOG.md` - Comunicação Claude↔Gemini
- `PC_SYNC_LOG.md` - Comunicação Alienware↔Desktop

**Referência:**
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Padrões de nomenclatura
- `00_SISTEMA/PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md` - Resolver problemas
- `00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md` - Índice master

**Projetos:**
- `02_PROJETOS/KabaK/STATUS_ATUAL.md` - Status KabaK
- `02_PROJETOS/KabaK/metricas/DASHBOARD.md` - Métricas KabaK

---

## 💡 DICAS PRÁTICAS

### Dica 1: Use _inbox/ sem Culpa

**Captura rápida > Organização perfeita**

```
✅ CORRETO:
Ideia → _inbox/idea.md → Processar depois

❌ ERRADO:
Ideia → Gastar 10min pensando onde colocar → Esquecer ideia
```

**Processar _inbox/ diariamente (5min) mantém organização.**

---

### Dica 2: Delegue Trabalho Massivo para Gemini

**Gemini = Gratuito (1M tokens)**

```
50 PDFs para organizar → Gemini (R$ 0)
vs
Claude processando tudo → R$ 50-100

Economia: R$ 50-100 por tarefa grande
```

---

### Dica 3: Checkpoint Antes de Grandes Mudanças

**Antes de refatoração grande:**

```
"Claude, criar checkpoint ANTES_REFATORACAO_DDMMMYYYY"
```

**Se algo der errado → Restaurar estado anterior.**

---

### Dica 4: Use MOCs para Navegação Rápida

**Em vez de buscar arquivos um por um:**

```
Abrir _MOC_Conhecimento.md → Ver todos índices de conhecimento
Abrir _MOC_Projetos.md → Ver todos projetos ativos
```

**MOCs = Índice visual do vault**

---

## 📚 REFERÊNCIAS ÚTEIS

**Navegação:**
- Este guia (GUIA_Usuario_Quick_Start.md)
- [[../MOCs/MOC_Padroes_Protocolos_Guidelines.md]] - Índice master

**Padrões:**
- [[../PADROES/NOMENCLATURA.md]] - Como nomear arquivos
- [[../PADROES/GUIA_Claude_vs_Gemini.md]] - Qual IA usar

**Protocolos:**
- [[../PROTOCOLOS/PROTOCOLO_MULTI_PC.md]] - Trocar PC
- [[../PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]] - Handoff IA
- [[../PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md]] - Revisão semanal
- [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] - Resolver problemas

**Guidelines:**
- [[../../02_PROJETOS/_GUIDELINES.md]] - Organizar projetos
- [[../../03_APRENDIZADO/_GUIDELINES.md]] - Processar cursos/lives

**Guias IA:**
- [[GUIA_Leitura_Claude.md]] - Para Claude Code
- [[GUIA_Leitura_Gemini.md]] - Para Gemini/Antigravity

---

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Última atualização:** 16/Jan/2026

**DECISÃO RÁPIDA = MENOS FRICÇÃO = MAIS PRODUTIVIDADE** 🚀✅
