---
created: 2026-01-26T11:56
updated: 2026-01-26T11:56
---
# MAPA: Skills Prioritárias (Awesome-Skills)

**Contexto:** Expansão de Capacidades da Névoa (T038)
**Researcher:** Gemini Guardian
**Fonte:** `.agent/skills/skills_index.json`
**Data:** 26/Jan/2026

## 1. Resumo

Analisei o índice de skills disponíveis. De centenas de opções, identifiquei as essenciais para o ecossistema "Mente Lendária" (IA, KabaK, Automação, Conteúdo).

**Total Analisado:** ~80 skills chave (amostra high-value).
**Selecionadas:** 14 Skills de Elite.

## 2. TIER 1 - Essenciais (Ativar Agora)

Estas skills dão superpoderes imediatos para a Névoa gerenciar KabaK e o Vault.

| Skill ID | Categoria | Por que usar? |
| :--- | :--- | :--- |
| `ai-agents-architect` | **IA Core** | Para desenhar os novos agentes do sistema iOS Master. |
| `copywriting` | **Mkt/KabaK** | Essencial para criar anúncios, e-mails e páginas da KabaK. |
| `paid-ads` | **Mkt/KabaK** | Gestão de anúncios (Meta/Google). Crítico para o faturamento. |
| `marketing-ideas` | **Mkt/Estratégia** | Gerador de ideias para campanhas e growth. |
| `content-creator` | **Conteúdo** | Criação de posts, blogs e SEO com "brand voice". |
| `file-organizer` | **Vault/Prod** | Mantém o Segundo Cérebro organizado (a "Marie Kondo" técnica). |
| `concise-planning` | **Produtividade** | Gera checklists atômicos (perfeito para TDAH). |

## 3. TIER 2 - Táticas (Usar sob demanda)

Úteis para projetos específicos que virão em breve.

| Skill ID | Categoria | Uso |
| :--- | :--- | :--- |
| `workflow-automation` | **Automação** | Design de fluxos para n8n/Temporal. |
| `signup-flow-cro` | **KabaK/Growth** | Otimizar a conversão de leads/cadastros. |
| `email-sequence` | **KabaK/CRM** | Criar réguas de relacionamento (pós-venda). |
| `prompt-engineer` | **IA Ops** | Refinar os prompts do sistema Névoa. |
| `research-engineer` | **Estudo** | Modo rigoroso para Deep Research (estudos médicos/técnicos). |
| `youtube-script` | **Conteúdo** | (Se houver no pack) Para roteiros de vídeo. |
| `writing-skills` | **Meta** | Para criar NOVAS skills personalizadas para nós. |

## 4. Skills "Obsidian" (Nota Importante)

Apesar do handoff pedir `obsidian-*`, **não foi encontrada nenhuma skill com este prefixo exato** no índice padrão analisado.
*Porém*, as skills `file-organizer`, `markdown-writer` (implícita) e `content-creator` cobrem 80% do uso do Obsidian.

**Recomendação:** Criar nossa própria skill `obsidian-manager` baseada nos conceitos do Alan Nicolas (`Alan_Nicolas_Dominando_Obsidian.md`).

## 5. Como Ativar

1. **Ler a documentação:** Usar `view_file` no arquivo `.md` da skill (ex: `.agent/skills/skills/ai-agents-architect/SKILL.md`).
2. **Injetar no Contexto:** Quando for realizar uma tarefa (ex: criar anúncio), chamar explicitamente: "Ative a skill `paid-ads`".
3. **Criar Atalhos:** Mapear no `/mapa` ou comandos `/` (ex: `/ads` chama `paid-ads`).

## 6. Próximo Passo

Sugiro criar um arquivo `00_SISTEMA/SKILLS_ATIVAS.md` listando apenas estas selecionadas, com o caminho para o arquivo de instrução de cada uma, para fácil consulta da Névoa.
