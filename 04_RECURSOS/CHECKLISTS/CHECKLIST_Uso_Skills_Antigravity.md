# ✅ CHECKLIST: Uso de Skills Antigravity

Use este checklist para garantir segurança e efetividade ao usar as automações do Gemini.

---

## 🛫 Pre-Flight (Antes de Executar)

### Segurança Básica

- [ ] **Git Status:** O repositório está limpo (clean) ou com mudanças commitadas?
  - *Evite rodar scripts sobre mudanças não salvas.*
- [ ] **Backup:** Tenho certeza que posso reverter se der errado?
  - *As skills criam `.bak`, mas o git é seu melhor amigo.*
- [ ] **Arquivos Fechados:** Arquivos alvo (Word, Excel) estão fechados?
  - *Evita erros de permissão.*

### Intenção Clara

- [ ] **Qual Skill:** Sei exatamente qual skill quero ativar?
  - *`vault-organizer` (mover arquivos)*
  - *`status-updater` (atualizar métricas)*
  - *`session-logger` (registrar log)*
- [ ] **Contexto:** A raiz do vault (ou o alvo) está pronta?
  - *Ex: Não rodar organizador se a raiz tem arquivos temporários de trabalho que devem ficar lá.*

---

## 🚀 Execução

- [ ] Usei o trigger correto? (Ex: "Organizar vault", "Sync")
- [ ] O Gemini confirmou a execução da ferramenta? (Ícone de ferramenta ou texto "Executando...")

---

## 🛬 Post-Flight (Validação)

### Validação Visual

- [ ] **Log:** Li o relatório gerado pelo Gemini?
  - *Quantos arquivos movidos? Quais erros?*
- [ ] **Arquivos:** Verifiquei se os arquivos foram para onde deviam?
  - *Olhe a pasta `04_RECURSOS` ou a raiz.*
- [ ] **Logs:** O `SESSION_LOG.md` ou `STATUS_VAULT.md` foram atualizados corretamente?

### Se Algo Deu Errado 🛑

- [ ] **Não entre em pânico.**
- [ ] Verifique se foi criado um arquivo `.bak` (Ex: `STATUS_VAULT.md.bak`).
- [ ] Use `git status` para ver o estrago.
- [ ] Use `git restore .` para desfazer tudo (se você seguiu o Pre-Flight e estava clean).
- [ ] Consulte `PROTOCOLO_Troubleshooting_Skills.md`.

---

**Fim do Checklist**
