---
created: 2026-01-22T12:00
updated: 2026-01-22T12:00
---
# Projeto: Investigação Contínua Alan Nicolas 🕵️‍♂️

**Status:** 🟢 Operacional (Relógio Suíço Ativo)
**Objetivo:** Transformar o Vault em um organismo que aprende sozinho.

## ⚙️ O "Motor" do Sistema

Este projeto é alimentado pela skill `alan-researcher` (v2.0), que possui um indexador profundo capaz de ler milhares de linhas do seu vault e extrair apenas o "ouro" (Princípios, Workflows, Prompts).

### Componentes Principais

1. **[[CONHECIMENTO_CONSOLIDADO]]**: O "cérebro" gerado automaticamente. Contém todos os conceitos do Alan extraídos do seu vault.
2. **[[PLANO_INVESTIGACAO_CONTINUA]]**: O roteiro de evolução.
3. **Script Indexador**: `.gemini/skills/alan-researcher/scripts/index_alan.py`.

## 🕰️ Como Operar o "Relógio Suíço"

Para manter o sistema atualizado e trabalhando pra você:

### 1. Atualizar o Conhecimento (Click Manual)

Sempre que você adicionar novos arquivos do Alan (cursos, lives) no vault, rode este comando para re-indexar tudo:

```bash
python .gemini/skills/alan-researcher/scripts/index_alan.py
```

### 2. Modo Pesquisa Profunda

Para pedir uma análise usando todo esse contexto consolidado:

```text
/alan-researcher "Com base no CONHECIMENTO_CONSOLIDADO, crie um plano para o KabaK"
```

### 3. Integração com Claude (Bi-IA)

O arquivo `CONHECIMENTO_CONSOLIDADO.md` é salvo num formato que o Claude também entende.

- **Dica:** Peça para o Claude ler este arquivo antes de criar qualquer arquitetura complexa.

## 📊 Status Atual

- **Indexação Inicial:** ✅ Concluída em 22/Jan/2026.
- **Fontes Mapeadas:** `03_APRENDIZADO`, `04_RECURSOS/WORKFLOWS`, `PROMPTS`.
