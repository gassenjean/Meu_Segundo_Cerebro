# PROMPT PARA GEMINI: Criar Skill "Vault Organizer"

**Para:** Gemini 3 Pro (Antigravity)
**Tarefa:** Criar primeira Antigravity Skill - Automação de Organização de Vault
**Prioridade:** ⭐⭐⭐⭐⭐ ALTA

---

## CONTEXTO

Você (Gemini) vai criar a **primeira skill Antigravity** do sistema bi-IA. Esta skill é uma conversão da skill Claude Code `/marie-kondo` para automação executável.

**Diferença fundamental:**
- **Claude `/marie-kondo`** = Conhecimento (lê instruções e executa manualmente)
- **Antigravity `vault-organizer`** = Automação (executa script Python automaticamente)

---

## OBJETIVO

Criar skill `vault-organizer` que **automaticamente:**

1. Identifica arquivos fora do lugar (raiz, pastas erradas)
2. Determina localização correta baseado em:
   - Tipo de conteúdo (conhecimento, projeto, recurso, etc)
   - Padrões de nomenclatura (`NOMENCLATURA.md`)
   - Estrutura de categorias (01-05)
3. Move e renomeia arquivos automaticamente
4. Atualiza MOCs relevantes
5. Gera relatório de ações realizadas

---

## ESTRUTURA DA SKILL

Criar em: `.gemini/skills/vault-organizer/`

```
.gemini/skills/vault-organizer/
├── skill.md           # Metadados + Descrição
├── scripts/
│   ├── organizer.py  # Script principal
│   └── utils.py      # Funções auxiliares (se necessário)
└── resources/
    └── patterns.json # Padrões de categorização (se necessário)
```

---

## CONTEÚDO: skill.md

```markdown
---
name: vault-organizer
description: Organiza arquivos automaticamente seguindo padrões do vault (NOMENCLATURA.md)
version: 1.0
triggers:
  - "organizar vault"
  - "marie kondo"
  - "limpar arquivos"
  - "vault organizer"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Vault Organizer

Automação inteligente que organiza arquivos do vault seguindo os padrões definidos em `NOMENCLATURA.md` e `PROTOCOLO_CRIACAO_ARQUIVOS.md`.

## Funcionalidades

- ✅ Identifica arquivos fora do lugar
- ✅ Move para localização correta (01-05 categorias)
- ✅ Renomeia seguindo padrões (CamelCase, underscores)
- ✅ Atualiza MOCs automaticamente
- ✅ Gera relatório detalhado

## Como Usar

**Linguagem Natural:**
- "Organize os arquivos da raiz"
- "Marie Kondo no vault"
- "Limpar arquivos soltos"
- "Organizar PDFs que estão fora do lugar"

**Comando Explícito:**
- `/vault-organizer` (executa scan completo)

## Workflow

1. **Scan:** Identifica arquivos fora do lugar
2. **Análise:** Determina tipo e localização correta
3. **Ação:** Move e renomeia (com confirmação se necessário)
4. **Atualização:** Atualiza MOCs relevantes
5. **Relatório:** Gera resumo de ações realizadas

## Padrões Aplicados

**Lê e aplica:**
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Padrões de nome
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - Workflow
- MOCs de cada categoria (estrutura)

**Categorizações:**
- PDFs de pesquisa → `01_CONHECIMENTO/[Area]/`
- Screenshots de projeto → `02_PROJETOS/[Projeto]/docs/`
- Templates → `04_RECURSOS/TEMPLATES/`
- Ideias pessoais → `05_PESSOAL/Ideas/`

## Script

Executa `scripts/organizer.py` que implementa toda lógica automaticamente.
```

---

## CONTEÚDO: scripts/organizer.py

**Requisitos do script:**

1. **Funções principais:**
   ```python
   def scan_vault(base_path):
       """Escaneia vault e identifica arquivos fora do lugar"""

   def categorize_file(file_path, content_type):
       """Determina categoria correta (01-05)"""

   def determine_location(file_info):
       """Determina localização exata baseado em padrões"""

   def rename_file(old_name):
       """Aplica padrões de nomenclatura (CamelCase, underscores)"""

   def move_and_rename(file_path, new_path):
       """Move arquivo e registra ação"""

   def update_moc(category, file_path):
       """Atualiza MOC relevante com novo arquivo"""

   def generate_report(actions):
       """Gera relatório markdown de ações realizadas"""
   ```

2. **Lógica de categorização:**
   - PDFs técnicos/pesquisa → 01_CONHECIMENTO
   - Documentos de projetos → 02_PROJETOS
   - Materiais de curso → 03_APRENDIZADO
   - Templates/recursos → 04_RECURSOS
   - Notas pessoais/ideias → 05_PESSOAL

3. **Padrões de nomenclatura:**
   - Aplicar CamelCase
   - Substituir espaços por underscores
   - Máximo 60 caracteres
   - Remover caracteres especiais
   - Datas: DDMMMYYYY (17JAN2026)

4. **Safety:**
   - Backup de ações (log)
   - Confirmação para ações críticas
   - Rollback se erro
   - Não deletar nunca, só mover

5. **Output:**
   ```markdown
   # Relatório Vault Organizer - 18/JAN/2026

   ## Resumo
   - Arquivos escaneados: 45
   - Arquivos movidos: 12
   - Arquivos renomeados: 8
   - MOCs atualizados: 3

   ## Ações Detalhadas

   ### Movidos
   1. ✅ pesquisa_marketing.pdf → 01_CONHECIMENTO/Marketing/Marketing_Digital_Pesquisa_2025.pdf
   2. ✅ IMG_20260118.png → 02_PROJETOS/KabaK/docs/reunioes/assets/Reuniao_18JAN2026.png
   [...]

   ### MOCs Atualizados
   - _MOC_Conhecimento.md (+2 arquivos)
   - 02_PROJETOS/KabaK/README.md (+1 screenshot)
   ```

---

## ARQUIVOS DE REFERÊNCIA

**OBRIGATÓRIO ler antes de criar a skill:**

1. `00_SISTEMA/PADROES/NOMENCLATURA.md` - Padrões de nomenclatura
2. `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - Workflow de criação
3. `00_SISTEMA/PROTOCOLOS/PROTOCOLO_DIVISAO_SKILLS_Claude_Antigravity.md` - Como criar skills Antigravity
4. `.claude/skills/marie-kondo/` - Skill original (referência)

**Opcional (contexto):**
- `00_SISTEMA/ANALISES/ANALISE_Antigravity_Skills_Integracao_Sistema_BiIA.md`
- `00_SISTEMA/ANALISES/Pesquisa_Antigravity_Skills_Sistema_Monitoramento.md`

---

## CHECKLIST DE VALIDAÇÃO

Antes de finalizar, verificar:

- [ ] Estrutura de pastas criada (skill.md + scripts/)
- [ ] skill.md completo (metadados + descrição + triggers)
- [ ] Script Python funcional e testado
- [ ] Lógica de categorização implementada
- [ ] Padrões de nomenclatura aplicados corretamente
- [ ] Safety features (backup, confirmação)
- [ ] Relatório markdown gerado corretamente
- [ ] Testado em nova conversa (zero contexto)
- [ ] Ativação via linguagem natural funciona
- [ ] MOCs são atualizados automaticamente

---

## TESTE FINAL

**Criar nova conversa no Antigravity e testar:**

1. Colocar arquivo de teste na raiz: `teste_organizacao.pdf`
2. Dizer: "Organize este arquivo"
3. Verificar se:
   - Skill ativa automaticamente
   - Arquivo é categorizado corretamente
   - Arquivo é movido e renomeado
   - MOC é atualizado
   - Relatório é gerado

---

## ENTREGA

**Salvar skill em:**
`.gemini/skills/vault-organizer/`

**Atualizar SESSION_LOG.md com:**
- Skill criada e testada
- Exemplos de uso
- Próximos passos (criar skill #2: status-updater)

**Avisar Claude Code** que skill está pronta para uso!

---

**Boa sorte, Gemini! Esta é a primeira de muitas skills que vão revolucionar nossa produtividade! 🚀**
