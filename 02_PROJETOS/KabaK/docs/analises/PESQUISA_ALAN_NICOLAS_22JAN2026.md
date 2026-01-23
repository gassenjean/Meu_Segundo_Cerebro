---
created: 2026-01-22T11:52
updated: 2026-01-22T11:52
---
# PESQUISA ALAN NICOLAS: Padrões e Metodologias 🧠

**Data:** 22/Jan/2026
**Origem:** Pesquisa Browser (mentelendaria.com) + Contexto Local (Alan Universe)
**Objetivo:** Extrair padrões para reorganização do Projeto KabaK.

## 1. Estrutura do Vault (Padrão Lendário)

Baseado na análise do site ao vivo e do vault local, a estrutura recomendada segue a lógica MOC (Map of Content) + Pastas Funcionais.

### Estrutura Ideal Identificada

```
00_SISTEMA/          (Meta-sistema, MOCs, Padrões)
01_CONHECIMENTO/     (Conceitos teóricos, Wiki)
02_PROJETOS/         (Projetos ativos com fim definido)
03_APRENDIZADO/      (Cursos, Lives, Anotações)
04_RECURSOS/         (Templates, Prompts, Workflows)
05_PESSOAL/          (Diário, Identidade)
```

**Aplicação no KabaK:**
O projeto KabaK deve residir em `02_PROJETOS/KabaK/` e possuir um MOC interno (`_MOC_KabaK.md`) que linka para seus documentos principais.

## 2. Metodologia 5C

O framework central para gestão de conhecimento e projetos é o 5C:

1. **CONSUMIR**: Entrada de dados (Reuniões, Pesquisas).
2. **CAPTURAR**: Registrar bruto em `_inbox` ou notas de reunião.
3. **CONECTAR**: Linkar com `VALORES_OFICIAIS.md` e outros projetos.
4. **CRIAR**: Gerar Briefings, Planilhas e Planos de Ação.
5. **COMPARTILHAR**: Enviar para Sócios (Sansom, Dr. Alexandre).

**Insight para KabaK:**
Atualmente temos muito "CRIAR" (docs) mas o "CONECTAR" está falho (fontes de verdade duplicadas).

## 3. Padrões de Automação e Skills

A pesquisa identificou que o Alan utiliza **Agentes Especializados** para funções repetitivas.

### Padrão de Skill Identificado

- **Pasta:** `.gemini/skills/nome-skill/`
- **Componentes:**
  - `SKILL.md`: Instruções claras e modo de uso.
  - `prompts/`: Personas específicas (System Prompts).
  - `scripts/`: Código Python/Bash para execução pesada.
  - `references/`: Dados estáticos de apoio.

**Recomendação para Skill KabaK v2.0:**
Deve seguir exatamente esta estrutura folders, separando a lógica (script) da personalidade (prompt).

## 4. Integração Bi-IA (Claude + Gemini)

O vault do Alan sugere uma divisão clara:

- **Gemini (1M tokens):** Processamento massivo (ler livros, logs inteiros, "Capturar").
- **Claude (Raciocínio):** Arquitetura, código complexo, "Conectar" e "Criar".

**No KabaK:**

- Usar Gemini para ler os 7 docs de reunião e consolidar.
- Usar Claude para estruturar o MOC e validar a lógica financeira.

## 5. Ações Imediatas (Baseado na Pesquisa)

1. [ ] **Criar `_MOC_KabaK.md`**: Essencial para navegação (Padrão Alan).
2. [ ] **Consolidar Fontes**: Aplicar o "Consolidar" do 5C para eliminar as 8 planilhas.
3. [ ] **Adotar Persona Consultor**: Usar a nova skill `alan-researcher` para auditar as decisões do projeto.

---
*Gerado via Skill Alan Researcher (v1.0)*
