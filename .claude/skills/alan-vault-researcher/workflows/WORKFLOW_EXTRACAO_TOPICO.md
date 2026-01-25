# Workflow: Extrair Tópico Específico

Passo-a-passo para extrair conhecimento do vault do Alan.

---

## Pré-requisitos

- [ ] Tema definido claramente
- [ ] Verificado no inventário se já foi extraído
- [ ] Template de extração disponível

---

## Passos

### 1. Verificar Inventário (1 min)

```bash
# Abrir inventário
Ler: .claude/skills/alan-vault-researcher/INVENTARIO_MENTE_LENDARIA.md

# Verificar se tema já existe
Buscar: [nome do tema]
```

**Se já extraído:** Ir para localização indicada no vault.
**Se pendente:** Continuar para passo 2.

### 2. Pesquisar no Vault Alan (5-10 min)

```bash
# Opção A: WebSearch
WebSearch: "Alan Nicolas [tema] site:mentelendaria.com"

# Opção B: WebFetch (se URL conhecida)
WebFetch: https://mentelendaria.com/[pagina]
Prompt: "Extrair informações sobre [tema]: conceito, princípios, exemplos práticos"
```

### 3. Coletar Informações Brutas

Anotar:
- Definição/conceito central
- Princípios ou regras
- Exemplos práticos mencionados
- Citações relevantes

### 4. Sintetizar (Ética)

Usar template: `assets/templates/TEMPLATE_EXTRACAO.md`

**Regras:**
- Reescrever em palavras próprias
- Máximo 200 palavras por seção
- Citar fonte original
- Aplicar ao seu contexto

### 5. Validar Originalidade

Checklist:
- [ ] Não copiei parágrafos inteiros?
- [ ] Está em minhas palavras?
- [ ] Adicionei minha perspectiva?
- [ ] Citei a fonte?

### 6. Salvar no Vault Local

```text
Localização: 02_PROJETOS/Estudo_Alan_Nicolas/WIKI/conceitos/
Formato: Alan_Nicolas_[Nome_Conceito].md
```

### 7. Atualizar Inventário

```markdown
| [Tema] | conceitos/Alan_Nicolas_[Tema].md | ✅ Extraído | 2026-01-XX |
```

---

## Exemplo Prático

**Tema:** Sistema 5C

```text
1. WebSearch: "Alan Nicolas Sistema 5C site:mentelendaria.com"
2. Coletar: Consumir, Capturar, Conectar, Criar, Compartilhar
3. Sintetizar: Ciclo de vida da informação em 5 etapas...
4. Validar: Original? Sim. Citado? Sim.
5. Salvar: Alan_Nicolas_Sistema_5C.md
6. Atualizar inventário
```

---

## Troubleshooting

| Problema | Solução |
| -------- | ------- |
| Não encontro conteúdo | Tentar variações do termo de busca |
| Página não carrega | Usar Gemini Deep Research |
| Conteúdo muito extenso | Dividir em múltiplas extrações |
| Difícil sintetizar | Focar nos 3 pontos principais |
