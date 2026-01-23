# 🦅 Workflows Adaptados: O Método MAPA no Sistema Bi-IA

**Fonte:** `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/ASSETS/CASES/`
**Adaptação:** Antigravity (Gemini) + Claude Code
**Metodologia:** MAPA (Mapear, Atomizar, Programar, Ativar)

---

## 🧠 Conceito Central: MAPA no Antigravity

Adaptamos o framework do Alan para nossas ferramentas nativas:

1. **Mapear:** Uso de `list_dir`, `view_file_outline` e `task_boundary` (Planning).
2. **Atomizar:** Quebra em checklist no `task.md`.
3. **Programar:** Definição de ferramentas (`tool_use`) e agentes (Prompts).
4. **Ativar:** Execução via `run_command` ou `write_to_file`.

---

## 🚀 Workflow 1: Criação de Curso (Deep Content)

*De 40h para 2h com Contexto Infinito.*

### 1. MAPEAR (Gemini)

* **Ação:** Ler material bruto (PDFs, Transcrições) usando janela de 1M tokens.
* **Ferramenta:** `view_file` (em arquivos gigantes).
* **Prompt:** *Ultimate Course Framework Extractor* (Ver `ANALISE_PROMPTS_UTEIS.md`).

### 2. ATOMIZAR (Planejamento)

* **Ação:** Criar `implementation_plan.md`.
* **Estrutura:** Definir Módulos > Aulas > Assets.

### 3. PROGRAMAR (Claude/Antigravity)

* **Ação:** Criar estrutura de arquivos vazios ou esboços.
* **Prompt:** "Crie a estrutura de pastas e arquivos markdown para o curso X baseada no plano."

### 4. ATIVAR (Curso)

* **Ação:** Iterar arquivo por arquivo preenchendo conteúdo.
* **Diferencial:** Usar `view_file` no material fonte específico para cada aula para evitar alucinação.

---

## 📑 Workflow 2: Documentação de Projeto (Auto-Docs)

*A "Segunda Cérebro" que se auto-documenta.*

### 1. MAPEAR (Audit)

* **Ação:** Escanear o diretório do projeto.
* **Ferramenta:** `find_by_name` (listar todos .md, .py, .js).
* **Output:** Árvore de arquivos para contexto.

### 2. ATOMIZAR

* **Ação:** Identificar clusters de arquivos (ex: "Backend", "Frontend", "Docs").
* **Artifact:** Atualizar `task.md` com tarefas de documentação por cluster.

### 3. PROGRAMAR (Contrato)

* **Ação:** Definir padrão em `00_SISTEMA/PADROES/NOMENCLATURA.md`.
* **Prompt:** "Analise este código e gere um README.md técnico focando em [Audiência]."

### 4. ATIVAR (Documentação)

* **Ação:** `write_to_file` gerando os documentos.
* **Loop Ralph:** Verificar se links funcionam e se a nomenclatura está `NOMENCLATURA.md` compliant.

---

## 🧹 Workflow 3: Organização de Arquivos (Guardian)

*O "Zelador Cibernético".*

### 1. MAPEAR (Diagnóstico)

* **Ação:** Identificar arquivos fora do padrão (espaços, sem prefixo).
* **Ferramenta:** `list_dir` na raiz ou pastas alvo.
* **Critério:** Violar `00_SISTEMA/PADROES/NOMENCLATURA.md`.

### 2. ATOMIZAR (Plano de Ação)

* **Ação:** Criar lista de movimentos (De -> Para).
* **Segurança:** Se > 10 arquivos, criar `implementation_plan.md` para aprovação humana.

### 3. PROGRAMAR (Permissões 1-2-3)

* **Nível 1 (Read):** Apenas relatar (Log).
* **Nível 2 (Propose):** Criar script `.sh` ou `.ps1` de movimentação e pedir *human approval* (`run_command` com `SafeToAutoRun: false`).
* **Nível 3 (Execute):** Mover arquivos temporários ou logs automaticamente (`SafeToAutoRun: true`).

### 4. ATIVAR (Organização)

* **Ação:** Executar script de limpeza.
* **Finalização:** Atualizar `_MOC` da área afetada.

---

## 🔑 A Chave da Permissão (1-2-3) Adaptação

O sistema 1-2-3 do Alan mapeia diretamente para nossas ferramentas:

* **Nível 1:** `view_file`, `list_dir` (Seguro).
* **Nível 2:** `write_to_file`, `run_command` (Requer supervisão/plano).
* **Nível 3:** `// turbo` workflows (Autônomo).

---
> *Adaptação gerada pelo Agente Antigravity em 22/Jan/2026*
