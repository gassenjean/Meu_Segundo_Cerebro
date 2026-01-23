---
tipo: protocolo
sistema: session-log-v2
versao: 2.0
data: 2026-01-22
---

# 📜 PROTOCOLO SESSION LOG V2.0

**Objetivo:** Manter o `SESSION_LOG.md` leve, legível e útil para colaboração Bi-IA (Claude + Gemini).

---

## 1. 📏 Regra do Limite (15 Entradas)

Para evitar que o arquivo exceda 100KB e consuma janela de contexto desnecessária:

1. **Máximo de Entradas:** O arquivo deve conter no máximo **15 sessões** recentes.
2. **Arquivamento Automático:**
    * Ao atingir 15, as 5 mais antigas devem ser movidas para `00_SISTEMA/LOGS/`.
    * Nome do arquivo: `SESSION_LOG_ARCHIVE_YYYYMMDD.md`.
3. **Responsável:** Agente `session-log-archiver` (Skill) ou execução manual via script.

## 2. 📝 Estrutura da Entrada

Cada nova sessão deve seguir estritamente este formato:

```markdown
## 🟣 [Agente] - [Data/Hora] - [Título Curto]

### Trabalho Realizado
- [Lista de ações]

### Arquivos Criados/Modificados
- [Lista de arquivos]

### Mensagem para [Próximo Agente]
> [Instruções claras ou uso do TEMPLATE_HANDOFF]
```

## 3. 🤝 Handoff (Transição)

Quando houver troca de contexto complexa (ex: sair do PC Trabalho para Casa), **OBRIGATÓRIO** usar o template:
`04_RECURSOS/TEMPLATES/TEMPLATE_HANDOFF.md`.

## 4. 🚫 O que NÃO fazer

* Colocar output de terminal gigante (use arquivos de log separados).
* Duplicar conteúdo de checkpoints (faça apenas o link).
* Deixar a mensagem de handoff vazia ("Continuar trabalho"). Seja específico.

---
*Protocolo ativo a partir de 22/Jan/2026.*
