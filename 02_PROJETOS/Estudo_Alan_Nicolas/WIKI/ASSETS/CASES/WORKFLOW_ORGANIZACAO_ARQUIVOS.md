---
created: 2026-01-22T12:43
updated: 2026-01-22T12:43
---
# WORKFLOW: Organização de Arquivos com IA

**Fonte:** Alan Nicolas (Mentoria)
**Tempo Tradicional:** infinito (procrastinação)
**Tempo com Workflow:** 10 minutos (resolvido)

> **"O primeiro caso de uso universal. Todo mundo tem uma pasta Downloads bagunçada."**

---

## 🗺️ O MAPA

### 1. MAPEAR (2min)

- Qual pasta organizar? (Desktop, Downloads, Documentos)
- Critérios de organização (por tipo, por data, por projeto)
- O que pode ser deletado? (duplicados, prints temporários)

### 2. ATOMIZAR (3min)

1. Auditar conteúdo da pasta
2. Criar estrutura de pastas ideal
3. Mover arquivos para categorias
4. Identificar e sugerir deleção de duplicados
5. Validar organização final

### 3. PROGRAMAR (1min)

*Ferramenta:* **Claude Code** (no terminal, com acesso local).

### 4. ATIVAR (10min)

**Prompt Básico:**

```bash
claude "Gostaria que você organizasse o meu desktop colocando os arquivos nas pastas ideais."
```

**Prompt Avançado (Downloads):**

```markdown
Organize minha pasta Downloads:

1. Crie estrutura de pastas por tipo (Documentos, Imagens, Vídeos, Instaladores, etc)
2. Mova arquivos para pastas apropriadas
3. Identifique arquivos duplicados
4. Me mostre prints/capturas de tela recentes e pergunte se posso deletar
5. Encontre arquivos com mais de 6 meses que provavelmente não preciso mais

Antes de deletar QUALQUER coisa, me pergunte.
Faça com cuidado e atenção aos detalhes.
```

---

## 🛡️ Sistema de Permissões (1-2-3)

- **Claude:** "Posso mover estes 45 PDFs para pasta Documentos/PDFs?"
- **Você:** `1` (Sim, vá em frente)

- **Claude:** "Posso deletar estes prints?"
- **Você:** `2` (Proponha a lista primeiro)

- **Claude:** "Posso apagar seu TCC?"
- **Você:** `3` (NÃO! Abortar)
