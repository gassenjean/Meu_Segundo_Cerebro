# HANDOFF: Sync Vault Alan Nicolas

**ID:** T008
**De:** Claude
**Para:** Gemini
**Prioridade:** Alta
**Criado:** 25/Jan/2026 14:30

---

## Missão

Verificar atualizações no vault do Alan Nicolas (mentelendaria.com) e sincronizar com o conteúdo local.

---

## Contexto

Temos **386 arquivos** baixados em `03_APRENDIZADO/Alan_Nicolas_Universe/`:

| Pasta | Arquivos | Conteúdo |
| ----- | -------- | -------- |
| Alan_Cursos_Referencia | 22 | Cursos originais (referência) |
| Alan_Nicolas_Academia_Lendaria | 207 | Episódios Vida Lendária + Lives |
| Alan_Nicolas_Mentoria | 20 | Claude Code para Empresários |
| Alan_Vault_Original | 130 | PKM completo do Alan |

---

## O que falta (Alta Prioridade)

### 1. Gestão IA (27 aulas) - Vagner Campos

- **Módulo:** Formação Lendária 2.0
- **Status local:** 0% extraído
- **Ação:** Verificar se há conteúdo público ou exportável

### 2. IA Avançada (12 aulas)

- **Módulo:** 80-20 da IA
- **Status local:** Pendente
- **Ação:** Verificar estrutura e conteúdo

### 3. Super Agentes IA (8 aulas) - Ramon Toledo

- **Módulo:** Formação Lendária 2.0
- **Status local:** Parcial (conceito criado, aulas não)
- **Ação:** Completar extração

---

## Tarefas

1. **Acessar mentelendaria.com** (use WebFetch se público)
2. **Mapear estrutura atual** do vault dele
3. **Comparar com local** - identificar gaps
4. **Extrair conteúdo faltante** (se acessível)
5. **Atualizar inventário** em `.claude/skills/alan-vault-researcher/INVENTARIO_MENTE_LENDARIA.md`

---

## Onde consolidar

- **Conceitos novos:** `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/`
- **Prompts novos:** `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/ASSETS/PROMPTS/`
- **Aulas estruturadas:** `03_APRENDIZADO/Alan_Nicolas_Universe/Alan_Nicolas_Mentoria/`

---

## Regras de Extração

1. Sintetizar em palavras próprias (não copiar)
2. Citar fonte original
3. Aplicar ao contexto do Gassen
4. Seguir TEMPLATE_EXTRACAO.md

---

## Outputs Esperados

1. **RELATORIO_SYNC_ALAN_25JAN2026.md** - O que foi encontrado/atualizado
2. **Arquivos criados/atualizados** - Lista com paths
3. **Atualização do INVENTARIO** - Percentuais atualizados

---

## Após Conclusão

Atualizar `state.json`:
- Mover T008 para completedTasks
- Adicionar notes com resumo do que foi feito

---

**Boa sorte, Gemini!**
