# Alan_Nicolas_Metodologia_Claude_Obsidian

## Fonte Original

- URL: https://mentelendaria.com (Conhecimento/IA/Claude + Obsidian MOC)
- Autor: Alan Nicolas
- Data acesso: 30/12/2025

## Conceito Aprendido

A metodologia de Alan Nicolas não trata Claude e Obsidian como ferramentas separadas, mas como um **Ecossistema Integrado**.

1.  **Obsidian AI-Ready:** A estrutura de pastas e MOCs é desenhada para que a IA _consiga ler_. Nomes padronizados, links claros e metadados (YAML) não são apenas para organização humana, mas para dar contexto rico ao Claude.
2.  **Agentes Especialistas (Roles):** O Claude nunca é usado como "Generalista". Ele sempre assume um chapéu (Role). Existem **31 Agentes**, com destaque para a categoria de **Arquitetura** (Backend, Database, Solution Architect).
3.  **Community Prompts:** Uso de prompts validados pela comunidade "Legendary". O destaque é o **Salesperson**, que segue um framework rígido de 8 passos (Hook, Agitation, Value, etc).

## Aplicação ao Contexto Gassen

### DeFi (Lucas)

- **Obsidian:** Usar Dataview para criar dashboards de tokens. "Quais moedas estou holdando que caíram 20%?" (Dataview responde rápido).
- **Claude:** Criar um Role `/defi-analyst` que só analisa Whitepapers seguindo um checklist de segurança.

### TDAH (Coach/Elena)

- **Obsidian:** O uso de **Templater** é obrigatório para reduzir a fricção de entrada. O Gassen não deve criar notas do zero. Digita `/nota` e o template já vem com os campos certos.
- **Claude:** O agente `/coach` já implementado está alinhado, mas pode ser melhorado com os princípios de "Hell Yeah or No" descobertos na fase anterior.

### Tráfego (Pedro)

- **Framework Salesperson:** A estrutura de 8 passos descoberta (Hook -> Agitation -> ... -> Close) deve ser o _Standard_ para todos os criativos da KabaK.
- **Implementação:** Criar um template no Obsidian chamado `TEMPLATE_Sales_Copy.md` que obriga a preencher os 8 passos.

## Conexões Vault Existente

- [[00_SISTEMA/AGENTES/PERFIL_ALAN_MIRROR.md]] - Atualizar com os novos Roles.
- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Validar se nossa nomenclatura é "AI-Readable".
- [[04_RECURSOS/TEMPLATES/]] - Onde os novos templates devem morar.

## Diferenças da Fonte Original

- Alan usa muitos plugins visuais (Canvas, Excalidraw).
- Adaptação Gassen: Manter foco em Texto/Markdown e Dataview para performance e compatibilidade com o Claude Code (que lê texto melhor que imagens).

## Implementação Prática

- [ ] Criar o Prompt do Agente `/salesperson` copiando o framework de 8 passos.
- [ ] Instalar/Configurar plugin **Dataview** se não estiver ativo.
- [ ] Revisar a pasta `00_SISTEMA` para garantir que o Claude entenda a hierarquia (MOCs claros).

---

_Inspirado em metodologia Alan Nicolas (mentelendaria.com)_
_Adaptado para contexto: DeFi + TDAH + Tráfego Pago_
