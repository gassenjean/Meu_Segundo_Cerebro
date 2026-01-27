---
description: Enables agents to interact with Google Workspace (Calendar, Tasks, Sheets) via structured actions for Google IO.
---

# Google Workspace Skill

This skill allows Agents to request actions in Google Workspace. The Agent does NOT execute the API call directly; instead, it outputs a structured **Action Block** that the `Google IO` system (or a MCP) interprets and executes.

## Protocol

When an Agent needs to perform an action in Google Workspace, it must output a code block with the language `json` and the tag `[GOOGLE_ACTION]`.

### Structure

```json
{
  "service": "calendar | tasks | sheets",
  "action": "create | list | update | delete",
  "payload": {
    // Service-specific fields
  }
}
```

### Services

#### 1. Calendar

Used for scheduling, blocking time (Time Blocking), and checking availability.

**Payload Fields:**

- `summary` (string): Event title.
- `start` (string): ISO 8601 datetime (e.g., "2026-01-26T10:00:00").
- `end` (string): ISO 8601 datetime.
- `description` (string, optional): Details.
- `color` (string, optional): "focus" (red), "family" (green), "faith" (purple), "default" (blue).

**Example:**

```json
{
  "service": "calendar",
  "action": "create",
  "payload": {
    "summary": "Deep Work: KabaK Strategy",
    "start": "2026-01-27T09:00:00",
    "end": "2026-01-27T11:00:00",
    "color": "focus"
  }
}
```

#### 2. Tasks

Used for actionable to-do items, checklists, and follow-ups.

**Payload Fields:**

- `title` (string): Task name.
- `list` (string): "My Tasks" (default), "KabaK", "Família", "Leituras".
- `due` (string, optional): ISO date (YYYY-MM-DD).
- `notes` (string, optional): Context or links.

**Example:**

```json
{
  "service": "tasks",
  "action": "create",
  "payload": {
    "title": "Ler Provérbios 3",
    "list": "Leituras",
    "due": "2026-01-26"
  }
}
```

#### 3. Sheets

Used for logging data (finance, health, metrics).

**Payload Fields:**

- `spreadsheet` (string): "Financeiro", "Saúde", "Hábitos".
- `tab` (string): Sheet name.
- `row` (array): List of values to append.

**Example:**

```json
{
  "service": "sheets",
  "action": "create", // append row
  "payload": {
    "spreadsheet": "Saúde",
    "tab": "Sono",
    "row": ["2026-01-26", "7h30", "Acordou bem"]
  }
}
```

## Agent Usage Instructions

1. **Identify Intent:** If the user asks to "schedule", "remind", "log", or "track", use this skill.
2. **Ask for Missing Info:** If date/time/details are missing, ask the user before generating the action.
3. **Output Action Block:** Generate the JSON block.
4. **Confirm:** Tell the user "Scheduling [Action]..."

## Integration with Managers (iOS Framework)

| Gerente | Usa Service | Casos de Uso |
| ------- | ----------- | ------------ |
| `/coach` | Calendar, Tasks, Sheets | Deep Work, Hábitos, Logs TDAH |
| `/fe` | Calendar, Tasks | Devocionais, Leituras |
| `/familia` | Calendar, Tasks | Datas família, Tarefas casa |
| `/kabak-agent` | Sheets, Calendar | Métricas, Reuniões |
| `/google` | Todos | Orquestra todos os services |

## Hierarquia iOS

```text
/google (Gerente Google)
└── Google Workspace Skill
    ├── Calendar → Coach, Fé, Família
    ├── Tasks → Todos os gerentes
    └── Sheets → Coach, KabaK, Lucas
```

## Recursos Relacionados

- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_GERENTE_GOOGLE.md`
- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_GOOGLE_IO.md`
- `04_RECURSOS/GOOGLE_UNIVERSE/GOOGLE_TOOLS_DATABASE.md`
