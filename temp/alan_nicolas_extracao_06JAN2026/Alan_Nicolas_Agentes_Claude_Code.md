# Alan_Nicolas_Agentes_Claude_Code

## Fonte Original

- URL: <https://mentelendaria.com/IA/Claude+Code/agents/README>
- Autor: Alan Nicolas
- Data acesso: 06/01/2026
- Seção: IA/Claude Code/Agents

## Conceito Aprendido

Agentes Claude Code são versões especializadas da IA, configuradas com `systemPrompt` (identidade/expertise), `tools` (capacidades) e `temperature` (criatividade) específicas. Diferente do uso genérico ("faça tudo"), agentes são "funcionários especialistas" (ex: um Arquiteto de Backend vs. um Revisor de Texto). O segredo da eficiência é a **especialização**: definir claramente quem o agente é e o que ele *não* deve fazer.

**Princípio central:** Não use um generalista para trabalho de especialista. Crie personas focadas com ferramentas restritas para máxima precisão.

**Como funciona:**
Você define um arquivo de configuração (ex: `meu-agente.js` ou via prompt de sistema) onde estabelece:

1. **Identidade:** "Você é um especialista em X".
2. **Restrições:** "Sempre faça Y, nunca faça Z".
3. **Ferramentas:** Acesso apenas ao necessário (ex: `read_file`, mas não `execute_command`).
O workflow ideal envolve: Pesquisar -> Pensar (`think`) -> Delegar para Agente -> Testar.

**Por que é importante:**
Resolve o problema de respostas alucinadas ou genéricas. Um agente focado erra menos, segue padrões de código (linting) rigorosamente e produz resultados prontos para produção mais rápido do que um prompt genérico iterativo.

## Aplicação ao Contexto Gassen

### 🪙 DeFi (Lucas)

**Problema resolvido:** Erros em cálculos de yield ou análise de smart contracts superficial.
**Como aplicar:**

1. Criar agente **"DeFi Auditor"**: Especialista em ler Solidity e encontrar vulnerabilidades.
2. Ferramentas restritas: Apenas leitura de código e acesso a docs de segurança (sem escrita).
3. System Prompt focado em "Paranóia de Segurança" e "Checklist de Auditoria".
**Exemplo prático:** "DeFi Auditor, analise este contrato de Staking e liste apenas riscos de Reentrancy e Overflow."

### 🧠 TDAH (Coach/Elena)

**Problema resolvido:** Paralisia por análise ao tentar estruturar projetos complexos.
**Como aplicar:**

1. Criar agente **"Secretária Executiva"**: Especialista em quebrar tarefas grandes em micro-passos.
2. Temperatura baixa (0.2) para ser extremamente objetiva e não "criativa demais".
3. Output forçado: Lista de checkbox simples.
**Exemplo prático:** "Secretária, tenho que entregar o projeto KabaK. Quebre em tarefas de 15 minutos para agora."

### 📈 Tráfego (Pedro)

**Problema resolvido:** Variação na qualidade dos copys e falta de padrão na "Voz da Marca".
**Como aplicar:**

1. Criar agente **"Copywriter KabaK"**: Treinado com os melhores anúncios anteriores (few-shot learning no prompt).
2. Regra rígida: "Nunca use clichês de marketing digital, use linguagem direta e premium."
3. Ferramenta: Acesso ao banco de "Hooks Vencedores".
**Exemplo prático:** "Copywriter, gere 3 variações de manchete para este criativo, mantendo o tom provocativo da marca."

## Conexões Vault Existente

### Conceitos Relacionados

- [[Conhecimento_IA_Agentes_vs_Prompts]] - Diferença teórica entre prompt único e agente persistente.
- [[MOC_Claude_Code]] - Onde os agentes técnicos habitam.
- [[Skill_Criacao_Personas]] - Metodologia para definir a "alma" do agente.

### Aplicações Cruzadas

- Combinar o agente **DeFi Auditor** com [[Google_Sheets_Investimentos]] para automatizar análise de risco.
- Usar o agente **Secretária Executiva** para alimentar o [[MOC_Projetos]] semanalmente.

## Diferenças da Fonte Original

**O que adaptei:**

- Original: Foco em código JS (`module.exports`). → Adaptado: Foco conceitual aplicável tanto em código quanto em prompts de sistema manuais (Antigravity/Claude).
- Original: Exemplos de desenvolvimento (`backend-architect`). → Adaptado: Agentes de negócio (Auditor, Secretária, Copywriter).
- Original: Estrutura técnica rígida. → Adaptado: Foco na "Mentalidade de Especialização" para o usuário.

**Por que adaptei:**

- O Gassen usa IA não só para codar, mas como "Segundo Cérebro" operacional. Agentes conceituais são mais valiosos que apenas scripts JS neste momento de estruturação.

## Implementação Prática

### Próximos Passos

- [ ] Definir a "Job Description" do Agente Auditor DeFi (Lucas).
- [ ] Criar um prompt de sistema fixo para a "Secretária Biônica" (Elena).
- [ ] Testar a criação de um agente simples via Claude Code (`/agent create`).

### Métricas de Sucesso

- [ ] Criação de 3 agentes especializados funcionais no próximo mês.
- [ ] Redução de 30% no tempo de refação de copys e códigos.

### Recursos Necessários

- Acesso ao Claude Code CLI.
- Biblioteca de Prompts (para treinar os agentes).

---

**Tags:** #alan-nicolas #mentelendaria #ia #agentes #claude-code #automacao
**Status:** 📥 Aguardando Validação Claude

---
*Inspirado em metodologia Alan Nicolas (mentelendaria.com)*
*Adaptado para contexto: DeFi + TDAH + Tráfego Pago*
*Este conteúdo é uma SÍNTESE ORIGINAL, não cópia do material fonte*
