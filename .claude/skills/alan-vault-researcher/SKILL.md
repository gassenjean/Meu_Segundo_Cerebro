---
name: alan-vault-researcher
description: Pesquisa e inventário do vault Mente Lendária (Alan Nicolas). Use para mapear conteúdo, extrair temas específicos, e sincronizar com o Segundo Cérebro.
version: 1.0.0
argument-hint: "/alan-vault inventario | /alan-vault extrair [tema] | /alan-vault sync"
---

# Alan Vault Researcher

Sistema completo para pesquisa e extração ética do vault do Alan Nicolas (mentelendaria.com).

---

## Quando Usar

- Descobrir o que existe no vault do Alan
- Extrair conhecimento sobre tema específico
- Sincronizar novidades com seu Segundo Cérebro
- Verificar o que já foi extraído vs pendente

---

## Comandos

```bash
/alan-vault inventario     # Ver mapa completo do conteúdo
/alan-vault extrair [tema] # Extrair tema específico
/alan-vault sync           # Verificar novidades
/alan-vault status         # Ver progresso da extração
```

---

## Fluxo de Extração

```text
1. INVENTÁRIO
   └── Consultar INVENTARIO_MENTE_LENDARIA.md

2. ESCOLHER TEMA
   └── Identificar seção/tópico desejado

3. PESQUISAR
   └── WebSearch + mentelendaria.com
   └── Coletar informações brutas

4. SINTETIZAR (Ética)
   └── Usar TEMPLATE_EXTRACAO.md
   └── Síntese em palavras próprias
   └── Citar fonte original

5. VALIDAR
   └── Verificar originalidade
   └── Aplicar ao contexto pessoal

6. INTEGRAR
   └── Salvar no vault local
   └── Atualizar inventário (status: extraído)
```

---

## Protocolo de Extração Ética

**OBRIGATÓRIO:** Toda extração deve seguir estas regras:

1. **Síntese, não cópia** - Reescrever em palavras próprias
2. **Citar fonte** - Sempre incluir URL original
3. **Aplicar contexto** - Adaptar para seu uso (DeFi, TDAH, etc.)
4. **Documentar diferenças** - O que mudou da fonte original

**Template obrigatório:** `assets/templates/TEMPLATE_EXTRACAO.md`

---

## Inventário

**Arquivo principal:** `INVENTARIO_MENTE_LENDARIA.md`

Contém:
- Mapa de todas as seções do vault Alan
- URLs conhecidas
- Status de cada item (pendente/extraído/obsoleto)
- Prioridade de extração

---

## Conteúdo Já Extraído

| Item | Localização no Vault | Status |
| ---- | -------------------- | ------ |
| Manual Mentalidade Lendária | `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/` | ✅ |
| Manual Engenharia de Agentes | `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/` | ✅ |
| Manual Gestão Conhecimento | `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/` | ✅ |
| Dicionário Lendário | `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/` | ✅ |
| 99+ Prompts | `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/ASSETS/PROMPTS/` | ✅ |
| 4 Checkpoints Aula 1 | `02_PROJETOS/Estudo_Alan_Nicolas/` | ✅ |
| Método 5C | `02_PROJETOS/Estudo_Alan_Nicolas/Alan_Nicolas_Metodo_5C.md` | ✅ |
| Metodologia Criação | `02_PROJETOS/Estudo_Alan_Nicolas/Alan_Nicolas_Metodologia_Criacao.md` | ✅ |

---

## Templates

| Template | Uso |
| -------- | --- |
| `TEMPLATE_EXTRACAO.md` | Formato padrão para nova extração |
| `TEMPLATE_INVENTARIO.md` | Registro de item no inventário |
| `TEMPLATE_SINTESE.md` | Síntese final para vault local |

---

## Workflows

| Workflow | Quando Usar |
| -------- | ----------- |
| `WORKFLOW_INVENTARIO.md` | Atualizar mapa do vault Alan |
| `WORKFLOW_EXTRACAO_TOPICO.md` | Extrair tema específico |
| `WORKFLOW_SINCRONIZACAO.md` | Verificar novidades |

---

## Integração com Gemini

Para extrações em massa (>50k tokens):

1. Preparar handoff com `/gemini-handoff`
2. Usar prompt de deep research
3. Validar resultado com Claude
4. Integrar ao vault

**Referência:** `.claude/skills/gemini-handoff/SKILL.md`

---

## Referências

- `references/urls_conhecidas.md` - URLs mapeadas do vault Alan
- `references/estrutura_vault_alan.md` - Arquitetura do mentelendaria.com
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_EXTRACAO_ETICA.md` - Protocolo completo

---

## Métricas

| Métrica | Valor |
| ------- | ----- |
| Seções mapeadas | Ver inventário |
| Itens extraídos | 8+ manuais/docs |
| Prompts coletados | 99+ |
| Última atualização | 2026-01-25 |
