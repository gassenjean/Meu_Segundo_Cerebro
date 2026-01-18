---
name: session-log-archiver
description: Arquiva entradas antigas do SESSION_LOG.md mantendo apenas as 30 mais recentes.
version: 1.0
triggers:
  - "arquivar session log"
  - "limpar session log"
  - "manter log recente"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Session Log Archiver

Skill responsável por manter o `SESSION_LOG.md` performático e limpo, arquivando automaticamente entradas antigas em arquivos mensais.

## Funcionalidades

- ✅ Analisa o `SESSION_LOG.md` e identifica entradas individuais.
- ✅ Mantém apenas as **30 últimas entradas** no arquivo principal.
- ✅ Move entradas antigas para `00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_[MES]_[ANO].md`.
- ✅ Preserva a ordem cronológica reversa nos arquivos de arquivo.
- ✅ Cria backups automáticos (`.bak`) antes de qualquer modificação.
- ✅ Garante encoding UTF-8 e formatação correta.

## Como Usar

**Linguagem Natural:**

- "Arquivar session log"
- "Limpar o log de sessão"
- "O log está muito grande, pode arquivar?"

## Workflow

1. **Scan:** Lê o `SESSION_LOG.md` e parseia as entradas.
2. **Decisão:** Se houver > 30 entradas, separa as excedentes.
3. **Backup:** Cria `SESSION_LOG.md.bak_[TIMESTAMP]`.
4. **Arquivamento:** Adiciona as entradas excedentes aos arquivos de arquivo mensais correspondentes (criando-os se necessário).
5. **Limpeza:** Reescreve o `SESSION_LOG.md` mantendo apenas o cabeçalho e as 30 entradas recentes.
6. **Relatório:** Exibe quantas entradas foram arquivadas e para onde.

## Script

Executa `scripts/archiver.py` que implementa a lógica segura de arquivamento.
