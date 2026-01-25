---
criado: 2025-11-28T08:05:00-03:00
atualizado: 2025-11-28T09:05:00-03:00
status: AGUARDANDO_VALIDACAO
---

# 📦 INVENTÁRIO DE CONHECIMENTO & RECURSOS (Fase 1)

Este documento lista **apenas** os itens de Conhecimento, Aprendizado e Recursos identificados nos vaults antigos para migração imediata.

---

## 1. 🎓 CURSOS & APRENDIZADO (Destino: `03_APRENDIZADO`)

| Nome                       | Origem                                                                     | Ação Proposta                                                      |
| :------------------------- | :------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| **Formação Lendária 2025** | `Segunda_Mente.../Formação_Lendária_2025`                                  | Migrar como Curso Principal.                                       |
| **Subido Tráfego 3K**      | `Segunda_Mente.../Subido_Trafego_3K`                                       | Migrar para `03_APRENDIZADO/Subido_Trafego`.                       |
| **Alan Vault Download**    | `Segunda_Mente.../_ul/alan_vault_download`                                 | **OURO:** Conteúdo bruto do vault do Alan. Migrar como Referência. |
| **Engenharia de Prompts**  | `Segunda_Mente.../_ul/alan_vault_download/Cursos_Engenharia de Prompts...` | Migrar para `03_APRENDIZADO/Engenharia_Prompts`.                   |
| **Dominando Obsidian**     | `Segunda_Mente.../_ul/alan_vault_download/Cursos_Dominando Obsidian...`    | Migrar para `03_APRENDIZADO/Dominando_Obsidian`.                   |
| **Zona de Genialidade**    | `Segunda_Mente.../_ul/alan_vault_download/Cursos_Zona de Genialidade...`   | Migrar para `03_APRENDIZADO/Zona_Genialidade`.                     |
| **Curso Claude Code**      | `Vault_Novo/Claude Code Projects/claude curso`                             | Migrar para `03_APRENDIZADO/Claude_Code`.                          |
| **DeFi Journey**           | `Segunda_Mente.../DEFIVERSO_Journey`                                       | Migrar para `03_APRENDIZADO/DeFi_Journey`.                         |

## 2. 🧠 BASE DE CONHECIMENTO (Destino: `01_CONHECIMENTO`)

| Nome                         | Origem                                                                           | Ação Proposta                                                                                 |
| :--------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Mentes Inquietas (TDAH)**  | `Segunda_Mente.../Sua_Mente.../Recursos/Mentes Inquietas`                        | **Encontrado:** 15 Capítulos (Markdown). Migrar para `01_CONHECIMENTO/TDAH_Mentes_Inquietas`. |
| **Cultivo Medicinal**        | `Segunda_Mente.../Nebo_Cloud` (Arquivos Cultivo)                                 | Migrar para `01_CONHECIMENTO/Cultivo_Medicinal`.                                              |
| **Guia Skills Agentes**      | `Segunda_Mente.../GUIA_SKILLS_AGENTES.md`                                        | Migrar para `01_CONHECIMENTO/IA_Agentes`.                                                     |
| **Manual TDAH Família**      | `Segunda_Mente.../TDAH_SUPERPODER...`                                            | Migrar para `01_CONHECIMENTO/TDAH_Produtividade`.                                             |
| **Apocalipse (Estudo)**      | `Segunda_Mente.../Sua_Mente.../Recursos/Deus/Apocalipse`                         | Migrar para `01_CONHECIMENTO/Espiritualidade/Apocalipse`.                                     |
| **Devocionais & Espiritual** | `Segunda_Mente.../Automacao_Devocionais` e `_ul/.../Filosofia & Espiritualidade` | Migrar para `01_CONHECIMENTO/Espiritualidade`.                                                |
| **Livros Diversos**          | `Segunda_Mente.../Sua_Mente.../Recursos/Livros`                                  | Migrar para `01_CONHECIMENTO/Livros_Resumos`.                                                 |
| **Marketing & Copy**         | `_ul/alan_vault_download/MOC - Marketing & Copy.md`                              | Migrar para `01_CONHECIMENTO/Marketing`.                                                      |

## 3. 🛠️ RECURSOS & FERRAMENTAS (Destino: `04_RECURSOS`)

| Nome                 | Origem                                    | Ação Proposta                                                        |
| :------------------- | :---------------------------------------- | :------------------------------------------------------------------- |
| **n8n Templates**    | `Segunda_Mente.../n8n templates`          | Mover para `04_RECURSOS/TEMPLATES/n8n` (Arquivo Morto Inicialmente). |
| **Copilot Prompts**  | `Segunda_Mente.../copilot-custom-prompts` | Mover para `04_RECURSOS/PROMPTS`.                                    |
| **Scrapers Scripts** | `Segunda_Mente.../_ul/*.js`               | Mover para `04_RECURSOS/SCRIPTS`.                                    |

---

## 4. 🤖 AGENTES AUXILIARES (Fase 5)

Vamos criar personas para auxiliar na gestão do conhecimento:

1.  **Elena Vasquez (Produtividade/TDAH):**
    - _Função:_ Organizar notas de TDAH, Mentes Inquietas e rotinas.
    - _Origem:_ Baseada no `TDAH_SUPERPODER_MANUAL`.

2.  **Pedro Sobral (Tráfego):**
    - _Função:_ Gerir conhecimento de Tráfego Pago (Subido, KabaK).
    - _Origem:_ Baseado no `Subido_Trafego_3K`.

3.  **Alan Nicolas (IA/Automação):**
    - _Função:_ Gerir scripts, n8n e estrutura do vault.
    - _Origem:_ Baseado no `Formação_Lendária` e `alan_vault_download`.

4.  **Dr. Green (Cultivo):**
    - _Função:_ Especialista em Cultivo Medicinal.
    - _Origem:_ Baseado nos arquivos do `Nebo_Cloud`.

5.  **Lucas Amoedo (DeFi):**
    - _Função:_ Especialista em Cripto e DeFi.
    - _Origem:_ Baseado no `DEFIVERSO_Journey`.

---

## 5. ⚠️ ITENS IGNORADOS (Fase 2 - Projetos)

- `KabaK_Build_Project`
- `Gabriele Confecções`
- `Agronegócio`

---

**Status:** Aguardando validação final para execução.
