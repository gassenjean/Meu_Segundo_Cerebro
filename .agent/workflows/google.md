---
description: Ativar Gerente Google (Orquestrador Ecossistema)
---

# Gerente Google - Orquestrador Ecossistema

Esta workflow ativa o **Gerente de Plataforma Google** para orquestrar automações, dados e IA.

1. Carregar contexto do Gerente Google:
   - `view_file c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\04_RECURSOS\PROMPTS\Agentes_Sistema\PROMPT_GERENTE_GOOGLE.md`
   - `view_file c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\04_RECURSOS\GOOGLE_TOOLS_DATABASE.md` (se existir, caso contrário ignora)

2. Ler estado atual:
   - `view_file c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\.bi-ia\state.json`

3. **Orquestração:**
   - Adote a persona definida em `PROMPT_GERENTE_GOOGLE.md`.
   - Verifique se há tarefas pendentes em `state.json` para o Gerente Google.
   - Pergunte ao usuário qual squad acionar (IA, Automação, Dados, Research, Criação).
