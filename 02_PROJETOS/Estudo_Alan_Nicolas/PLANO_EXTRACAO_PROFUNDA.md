---
created: 2026-01-22T12:12
updated: 2026-01-22T12:12
---
# Plano de Extração Profunda: A "Wiki Lendária" 📚

**Objetivo:** Transformar o caos de arquivos dispersos em Manuais Estruturados e Definitivos, enquanto o Claude organiza o KabaK.
**Método:** Processamento em Lote (Batch) via Gemini 1M Context.

## 1. O Conceito: "Minerar a Montanha"

O vault atual tem centenas de notas soltas do Alan. O script anterior (`index_alan.py`) pegou os conceitos-chave. Agora vamos **ler tudo** e reescrever em formato de Livro/Manual.

## 2. Os Entregáveis (Os Manuais)

Vamos gerar 4 artefatos mestres em `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/`:

### 📘 1. O Código de Cultura (Mindset)

*Foco: Princípios, Filosofia, Mentalidade Heroica.*

- **Fontes:** Arquivos "Sobre Mim", "Herói ou Vilão", "Vida Lendária".
- **Output:** `MANUAL_MENTALIDADE_LENDARIA.md`

### 📙 2. O Grimório de Automação (Técnico)

*Foco: n8n, Scripts, Agentes, Prompts.*

- **Fontes:** Pastas de IA, Claude Code, Workflows.
- **Output:** `MANUAL_ENGENHARIA_DE_AGENTES.md`

### 📗 3. O Sistema Operacional (Negócios)

*Foco: Sistema 5C, Gestão de Projetos, PKM.*

- **Fontes:** Notas sobre 5C, Obsidian, Segundo Cérebro.
- **Output:** `MANUAL_GESTAO_CONHECIMENTO.md`

### 📕 4. O Dicionário Lendário (Glossário)

*Foco: Termos específicos (Scaffolding, Janela de Contexto, etc).*

- **Fontes:** Todo o vault.
- **Output:** `GLOSSARIO_UNIFICADO_ALAN.md`

## 3. Estratégia de Execução (Segundo Plano)

1. **Script Agregador (`skills/alan-researcher/scripts/batch_read.py`):**
    - Este script não resume. Ele **concatena** todos os arquivos de um tema em um "super arquivo" temporário.
2. **Processamento Gemini:**
    - Eu (Antigravity) leio esse "super arquivo" (usando meu contexto de 1 milhão de tokens).
    - Eu reescrevo o conteúdo de forma didática e estruturada.
3. **Salvar:**
    - Salvo o resultado final na pasta `WIKI`.

## 4. Próximos Passos (Imediato)

1. [ ] Criar pasta `WIKI` no projeto.
2. [ ] Criar script `batch_read.py`.
3. [ ] Executar extração do **Volume 1: Mentalidade**.
