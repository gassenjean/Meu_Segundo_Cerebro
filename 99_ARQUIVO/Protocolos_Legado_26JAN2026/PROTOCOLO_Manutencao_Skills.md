---
created: 2026-01-19T10:35
updated: 2026-01-26T11:16
---
# 🛠️ PROTOCOLO: Manutenção de Skills

**Responsável:** Claude Architect / Antigravity
**Versão:** 1.0
**Ultima Atualização:** 18/JAN/2026

---

## 🎯 Objetivo

Definir como criar, atualizar e manter as skills do sistema, garantindo estabilidade e evolução controlada.

---

## 🔄 Ciclo de Vida de uma Skill

1. **Concepção:** Necessidade identificada (ex: "precisamos automatizar X").
2. **Prototipagem (Gemini):** Gemini cria a primeira versão em `.gemini/skills/nova-skill/`.
3. **Validação (Claude):** Claude Code revisa código, segurança e lógica.
4. **Aprovação:** Skill ganha status "Produção" e entra no MOC.
5. **Manutenção:** Updates, correções de bugs, melhorias.
6. **Depreciação:** Se não for mais útil, é arquivada em `04_RECURSOS/Arquivo_Morto`.

---

## 🆙 Atualizando uma Skill Existente

Nunca edite skills "a quente" sem precaução. Siga este fluxo:

### 1. Backup

Antes de mexer em `scripts/script.py`, copie a versão atual:

```bash
cp scripts/script.py scripts/script_v1.0_backup.py
```

### 2. Versionamento Semântico

No arquivo `skill.md`, incremente a versão:

* **Major (1.0 -> 2.0):** Mudança que quebra compatibilidade (muda inputs/outputs críticos).
* **Minor (1.0 -> 1.1):** Nova funcionalidade, compatível com anterior.
* **Patch (1.0 -> 1.0.1):** Correção de bug simples.

### 3. Edição

Faça as alterações necessárias no código.

* Mantenha comentários claros.
* Atualize docstrings.

### 4. Teste de Regressão

Verifique se o básico ainda funciona.

* "Ainda organiza arquivos?"
* "Ainda gera o log?"
* "Quebra se rodar em uma pasta vazia?"

### 5. Changelog

Adicione uma nota no `skill.md` ou crie um `CHANGELOG.md` na pasta da skill se houver muitas mudanças.

---

## 🧪 Padrões de Código (Python)

Para mantermos a sanidade, todo script de skill deve seguir:

* **Tipagem:** Use Type Hints (`def funcao(a: str) -> bool:`).
* **Logging:** Prints informativos (Emojis ajudam a IA a entender o status).
  * `print("✅ Sucesso")`
  * `print("⚠️ Aviso")`
  * `print("❌ Erro")`
* **Safety First:**
  * Nunca delete arquivos sem backup ou confirmação explicita.
  * Sempre use `encoding='utf-8'` ao abrir arquivos.
  * Trate exceções (`try/except`) para não crashar feio.

---

## 📦 Estrutura de Arquivos da Skill

Toda skill DEVE ter:

```text
.gemini/skills/nome-da-skill/
├── skill.md           # Metadados (Nome, Versão, Triggers, Autor)
├── README.md          # (Opcional) Instruções detalhadas se for complexo
└── scripts/           # Código executável
    ├── __init__.py    # Para ser módulo importável
    ├── main.py        # (Ou nome descritivo ex: organizer.py) - Entry point
    └── utils.py       # (Opcional) Funções auxiliares
```

---

## 🚨 Rollback (Plano B)

Se uma atualização quebrar a skill:

1. Apague o script quebrado.
2. Renomeie o backup (`script_v1.0_backup.py`) para o nome original.
3. Atualize o `skill.md` revertendo a versão.
4. Registre o incidente no `SESSION_LOG.md`.

---

## ✅ Checklist de Manutenção

* [ ] A nova versão passou no teste manual?
* [ ] Atualizei o numero da versão no `skill.md`?
* [ ] O código está comentado?
* [ ] Removi prints de debug sujos?
* [ ] Fiz backup da versão anterior?

---

**Fim do Protocolo**
