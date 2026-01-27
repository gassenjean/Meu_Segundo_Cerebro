# Mapa de Skills Disponíveis

**Criado:** 27/Jan/2026
**Fonte:** `.agent/skills/skills/` (244 skills)
**Status:** Mapeado para ativação

---

## Skills Priorizadas para Ativação

### Tier 1 - Marketing/KabaK (ALTA PRIORIDADE)

| Skill | Path | Uso |
| ----- | ---- | --- |
| `copywriting` | `.agent/skills/skills/copywriting/SKILL.md` | Copy para anúncios e landing pages |
| `content-creator` | `.agent/skills/skills/content-creator/SKILL.md` | Posts e SEO |
| `email-sequence` | `.agent/skills/skills/email-sequence/SKILL.md` | Réguas de email |
| `analytics-tracking` | `.agent/skills/skills/analytics-tracking/SKILL.md` | Métricas e tracking |
| `ab-test-setup` | `.agent/skills/skills/ab-test-setup/SKILL.md` | Testes A/B |
| `competitor-alternatives` | `.agent/skills/skills/competitor-alternatives/SKILL.md` | Intel competitiva |

### Tier 2 - Produtividade/TDAH

| Skill | Path | Uso |
| ----- | ---- | --- |
| `concise-planning` | `.agent/skills/skills/concise-planning/SKILL.md` | Checklists atômicos |
| `file-organizer` | `.agent/skills/skills/file-organizer/SKILL.md` | Organização de arquivos |
| `brainstorming` | `.agent/skills/skills/brainstorming/SKILL.md` | Ideação |

### Tier 3 - Agentes/Automação

| Skill | Path | Uso |
| ----- | ---- | --- |
| `ai-agents-architect` | `.agent/skills/skills/ai-agents-architect/SKILL.md` | Desenhar agentes |
| `agent-memory-systems` | `.agent/skills/skills/agent-memory-systems/SKILL.md` | Memória persistente |
| `autonomous-agents` | `.agent/skills/skills/autonomous-agents/SKILL.md` | Agentes autônomos |
| `dispatching-parallel-agents` | `.agent/skills/skills/dispatching-parallel-agents/SKILL.md` | Paralelização |
| `conversation-memory` | `.agent/skills/skills/conversation-memory/SKILL.md` | Contexto |

### Tier 4 - Desenvolvimento

| Skill | Path | Uso |
| ----- | ---- | --- |
| `app-builder` | `.agent/skills/skills/app-builder/SKILL.md` | Criar apps |
| `api-patterns` | `.agent/skills/skills/api-patterns/SKILL.md` | Padrões de API |
| `architecture` | `.agent/skills/skills/architecture/SKILL.md` | Arquitetura |
| `github-workflow-automation` | `.agent/skills/skills/github-workflow-automation/SKILL.md` | GitHub Actions |

---

## Outras Skills Úteis (244 total)

### Segurança

- `api-security-best-practices`
- `aws-penetration-testing`
- `cloud-penetration-testing`
- `ethical-hacking-methodology`

### Frontend

- `frontend-design`
- `frontend-dev-guidelines`
- `react-best-practices`
- `tailwindcss`

### Backend

- `backend-dev-guidelines`
- `database-design`
- `docker-expert`
- `aws-serverless`

### Integração

- `hubspot-integration`
- `stripe-integration`
- `firebase`
- `supabase`

---

## Como Ativar uma Skill

Para ativar uma skill no Claude Code:

```bash
# Opção 1: Copiar para .claude/skills/
cp -r .agent/skills/skills/copywriting .claude/skills/

# Opção 2: Referenciar inline
# Quando precisar, dizer: "Use a skill copywriting de .agent/skills/skills/"
```

---

## Conexão com iOS

| Gerente | Skills Recomendadas |
| ------- | ------------------- |
| /kabak-agent | copywriting, content-creator, email-sequence, analytics-tracking |
| /coach | concise-planning, file-organizer |
| /alan | ai-agents-architect, agent-memory-systems |
| /marie-kondo | file-organizer, architecture |

---

## Próximos Passos

1. [ ] Copiar skills Tier 1 para `.claude/skills/`
2. [ ] Testar copywriting com KabaK
3. [ ] Testar concise-planning com Coach
4. [ ] Documentar uso

---

**Responsável:** Névoa 7.0
**Delegado para:** Gemini (cópia em massa)
