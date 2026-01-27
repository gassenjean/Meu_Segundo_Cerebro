# SOP - Protocolo de Integração Antigravity (Segurança de Voo)

**Objetivo:** Garantir zero conflitos com Claude Code e manutenção da integridade do Sistema Operacional Profissional.
**Quando usar:** Obrigatório no início e fim de cada sessão via Antigravity.

---

## 🛫 DECOLAGEM (Workflow `/start`)

### 1. Consciência Situacional
Antes de escrever qualquer código ou texto:
- [ ] Rodar o commando `/start` (via workflow).
- [ ] Ler o `SESSION_LOG.md` (últimas 50 linhas).
- [ ] **Pergunta Chave:** "O Claude deixou alguma instrução pendente para mim?"

### 2. Definição de Escopo Seguro
- [ ] Se o Claude mexeu na pasta `X`, evite mexer na pasta `X` simultaneamente sem validar antes.
- [ ] Se houver dúvida, pergunte ao usuário: "O log mostra que o Claude alterou isso. Posso prosseguir?"

---

## 🛬 ATERRISSAGEM (Workflow `/sync`)

### 1. Validação de Integridade
Antes de fechar (fazer o sync final):
- [ ] Eu quebrei algum link?
- [ ] Eu segui a nomenclatura padrão (`NOMENCLATURA.md`)?
- [ ] Eu coloquei os arquivos nas pastas certas (`ESTRUTURA_PROJETOS.md`)?

### 2. O Handover (Passagem de Bastão)
Ao escrever no `SESSION_LOG.md`:
- [ ] Seja específico: "Criei arquivos X, Y, Z".
- [ ] Seja honesto: "Não terminei a tarefa W".
- [ ] **Deixe Instruções:** Se precisar que o Claude faça algo, use a seção `> Mensagem para Claude`.

---

## 🚨 PROCEDIMENTOS DE EMERGÊNCIA (Conflito Detectado)

Se perceber que ambos editaram o mesmo arquivo:
1. PARE imediatamente.
2. Crie um backup do arquivo atual (`nomedoarquivo_CONFLICT_GEMINI.md`).
3. Notifique o usuário: "Detectei conflito. Salvei minha versão como cópia. Precisamos resolver manual."
