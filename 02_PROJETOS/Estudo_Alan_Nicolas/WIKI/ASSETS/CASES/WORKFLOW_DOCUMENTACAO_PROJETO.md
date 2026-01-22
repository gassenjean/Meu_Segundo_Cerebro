---
created: 2026-01-22T12:42
updated: 2026-01-22T12:42
---
# WORKFLOW: Documentação de Projeto com IA

**Fonte:** Alan Nicolas (Mentoria)
**Tempo Tradicional:** 4 semanas
**Tempo com Workflow:** 1.5 horas

---

## 🗺️ O MAPA

### 1. MAPEAR (10min)

*Definição estratégica do escopo.*

- Escopo do projeto a documentar
- Audiência (quem vai ler?)
- Nível de detalhe necessário
- Formato desejado (README, wiki, etc)

### 2. ATOMIZAR (15min)

*Quebra em tarefas menores.*

1. Analisar estrutura de pastas
2. Identificar módulos principais
3. Documentar cada módulo separadamente
4. Criar diagramas de arquitetura
5. Escrever guia de setup
6. Criar FAQ de troubleshooting
7. Revisar e consolidar

### 3. PROGRAMAR (5min)

*Setup dos Agentes.*

- **Claude Code:** Análise de código e estrutura
- **Claude 3.5 Sonnet:** Escrita da documentação
- **Mermaid:** Diagramas técnicos

### 4. ATIVAR (1h)

*Execução do Contrato.*

**Prompt / Contrato:**

```markdown
Analise o projeto em [caminho].
Documente cada módulo conforme template padrão.
Crie diagramas em Mermaid para arquitetura.
Pergunte antes de assumir funcionalidade que não está clara.
```

---

## 🧠 Exemplo de Contrato Real

```markdown
## CONTRATO: Claude Code - Documentação de Projeto

### RESPONSABILIDADES
- Analisar código existente
- Gerar documentação técnica
- Criar diagramas de arquitetura

### LIMITES
- NÃO modificar código
- NÃO deletar arquivos
- PERGUNTAR se encontrar inconsistências

### ENTREGÁVEIS
- README.md completo
- Arquitetura em Mermaid diagrams
- Guia de setup para novos devs

### CHECKPOINTS
- Após analisar cada módulo principal
- Após completar cada seção do README
- Antes de finalizar (revisão completa)
```
