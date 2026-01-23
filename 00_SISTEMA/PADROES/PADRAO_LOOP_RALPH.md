# PADRÃO: Loop Ralph

**Origem:** Sistema Alan Nicolas
**Propósito:** Verificação automática de conclusão de tarefas

---

## Conceito

> "Não seja o imbecil que aperta sim."
> — Alan Nicolas

O Loop Ralph garante que toda tarefa seja verificada antes de ser considerada concluída.

```
1. Tarefa iniciada
2. Aguarda conclusão
3. Verifica: completou?
   ├── SIM → Notifica + próxima tarefa
   └── NÃO → Continua de onde parou
4. Repete até sucesso
```

---

## Implementação Padrão

### Verificação Mínima (Obrigatória)

Toda skill/gerente DEVE verificar:

```markdown
- [ ] Ação foi executada?
- [ ] Resultado existe?
- [ ] Resultado está correto?
- [ ] SESSION_LOG foi atualizado?
```

### Verificações por Tipo

#### Movimentação de Arquivos
```markdown
- [ ] Arquivo de destino existe?
- [ ] Arquivo de origem foi removido?
- [ ] Caminho está correto?
- [ ] Nomenclatura correta?
- [ ] MOC foi atualizado?
```

#### Criação de Arquivos
```markdown
- [ ] Arquivo foi criado?
- [ ] Localização correta?
- [ ] Nomenclatura correta?
- [ ] Conteúdo não está vazio?
- [ ] MOC foi atualizado?
```

#### Edição de Arquivos
```markdown
- [ ] Arquivo ainda existe?
- [ ] Edição foi aplicada?
- [ ] Backup foi criado (se crítico)?
- [ ] Formato válido (markdown)?
```

#### Delegação
```markdown
- [ ] Skill/gerente respondeu?
- [ ] Tarefa foi aceita?
- [ ] Resultado foi retornado?
- [ ] Resultado está correto?
```

---

## Fluxo de Verificação

```
┌──────────────────────────────────────────────────────────────┐
│                        TAREFA                                │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│                      EXECUTAR                                │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│               LOOP RALPH (VERIFICAR)                         │
│                                                              │
│   Para cada item da checklist:                               │
│   ├── PASSOU? → Continua                                     │
│   └── FALHOU? → PARA + ALERTA                                │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
              ┌───────────┴───────────┐
              │                       │
         TUDO OK               ALGUM FALHOU
              │                       │
              ↓                       ↓
┌─────────────────────┐   ┌─────────────────────┐
│  TAREFA CONCLUÍDA   │   │  REVERTER + ALERTAR │
│  Notificar usuário  │   │  Mostrar o que falhou│
│  Próxima tarefa     │   │  Sugerir correção    │
└─────────────────────┘   └─────────────────────┘
```

---

## Código de Verificação (Pseudo)

```python
def loop_ralph(tarefa, verificacoes):
    """
    Executa Loop Ralph após tarefa.
    Retorna True se passou, False se falhou.
    """
    resultado = executar(tarefa)

    for verificacao in verificacoes:
        if not verificacao(resultado):
            reverter(tarefa)
            alertar(f"Falha: {verificacao.nome}")
            return False

    registrar_session_log(tarefa, "SUCESSO")
    return True
```

---

## Integração com Gerentes

### Névoa (Master)
```
Delega para gerente
→ Loop Ralph: gerente respondeu?
→ Loop Ralph: tarefa concluída?
```

### Gerentes
```
Delega para skill
→ Loop Ralph: skill respondeu?
→ Loop Ralph: resultado correto?
```

### Skills
```
Executa ação
→ Loop Ralph: ação executada?
→ Loop Ralph: resultado existe?
```

---

## Níveis de Criticidade

| Nível | Ação se Falhar | Exemplo |
|-------|----------------|---------|
| CRÍTICO | Reverter + Parar | Mover arquivo crítico |
| ALTO | Reverter + Alertar | Editar MOC |
| MÉDIO | Alertar + Continuar | Atualizar SESSION_LOG |
| BAIXO | Logar + Continuar | Atualizar métricas |

---

## Timeouts

```
Ação simples:      30 segundos
Ação complexa:     2 minutos
Bulk operation:    10 minutos
Delegação Gemini:  5 minutos
```

Se timeout → ALERTAR + SUGERIR retry.

---

## Exemplos de Uso

### Guardian
```
/guardian fix
→ Propõe correção
→ Usuário aprova
→ Executa
→ LOOP RALPH:
  - [ ] Arquivo de destino existe? ✅
  - [ ] Arquivo de origem removido? ✅
  - [ ] Nome correto? ✅
  - [ ] MOC atualizado? ✅
→ SUCESSO
```

### Falha Detectada
```
/marie-kondo organizar "pasta/"
→ Move arquivo X para Y
→ LOOP RALPH:
  - [ ] Arquivo de destino existe? ❌ FALHOU
→ REVERTER
→ ALERTAR: "Falha ao mover arquivo X. Destino não existe."
→ SUGERIR: "Verificar se pasta Y existe"
```

---

## Anti-Patterns

**NUNCA:**
- Pular verificação
- Assumir que funcionou
- Ignorar falhas
- Continuar após erro crítico

**SEMPRE:**
- Verificar cada ação
- Reverter se falhou
- Alertar usuário
- Registrar no log

---

## Onde Usar

| Componente | Usa Loop Ralph? |
|------------|-----------------|
| Névoa | ✅ SIM |
| Gerentes | ✅ SIM |
| Guardian | ✅ SIM |
| Skills com modificação | ✅ SIM |
| Skills read-only | ❌ Opcional |

---

**Versão:** 1.0
**Criado:** 22/JAN/2026
**Origem:** Alan Nicolas (Conceito Ralph)
**Status:** PADRÃO OFICIAL

**"Não seja o imbecil que aperta sim."**
