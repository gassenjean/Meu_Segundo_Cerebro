---
criado: 2026-01-18T15:15:00-03:00
atualizado: 2026-01-18T15:15:00-03:00
tags:
  - plano
  - fase-7
  - protocolos
  - skills-antigravity
status: planejamento
---

# PLANO: Fase 7.3 - Protocolos de Uso (Antigravity Skills)

**Fase:** 7.3 - Protocolos
**Status:** Planejamento
**Pré-requisito:** Fase 7.2 COMPLETA ✅
**Próximo:** Fase 7.4 - Conversão Top 7

---

## 🎯 OBJETIVO

Criar documentação completa de uso, manutenção e troubleshooting para as 3 skills Antigravity aprovadas, estabelecendo protocolos claros para garantir uso efetivo e resolução de problemas.

---

## 📋 ESCOPO

### O Que Será Criado

**1. Protocolo de Uso das Skills**
- Quando usar cada skill
- Como triggerar corretamente
- Workflow típico de cada skill
- Boas práticas
- Casos de uso reais

**2. Guia de Troubleshooting**
- Problemas comuns e soluções
- Diagnóstico de erros
- Logs de debug
- Fallback manual se skill falhar

**3. Documentação de Edge Cases**
- Cenários especiais
- Limitações conhecidas
- Workarounds
- O que fazer quando...

**4. Templates de Prompts para Skills Futuras**
- Template padrão para criar novas skills
- Checklist de especificações
- Estrutura de validação
- Padrões de código Python

**5. Protocolo de Manutenção**
- Como atualizar uma skill existente
- Versionamento
- Testes de regressão
- Changelog

---

## 📁 ARQUIVOS A CRIAR

### 1. Protocolos (00_SISTEMA/PROTOCOLOS/)

**PROTOCOLO_Uso_Skills_Antigravity.md** (~8KB estimado)
- Seções:
  - Visão geral
  - Skill #1: vault-organizer (quando usar, como usar, exemplos)
  - Skill #2: status-updater (quando usar, como usar, exemplos)
  - Skill #3: session-logger (quando usar, como usar, exemplos)
  - Workflow típico (diagramas)
  - Boas práticas
  - Checklist de uso

**PROTOCOLO_Troubleshooting_Skills.md** (~6KB estimado)
- Seções:
  - Diagnóstico geral
  - Problemas comuns por skill
  - Códigos de erro
  - Logs de debug (como ler)
  - Fallback manual
  - Quando reportar bug vs. quando é uso incorreto
  - Checklist de diagnóstico

**PROTOCOLO_Manutencao_Skills.md** (~5KB estimado)
- Seções:
  - Como atualizar skill existente
  - Versionamento semântico (1.0 → 1.1 → 2.0)
  - Testes de regressão
  - Changelog (como documentar)
  - Backup antes de atualizar
  - Rollback se der problema

### 2. Guias (00_SISTEMA/GUIAS/)

**GUIA_Edge_Cases_Skills.md** (~5KB estimado)
- Seções:
  - Cenários especiais vault-organizer
  - Cenários especiais status-updater
  - Cenários especiais session-logger
  - Limitações conhecidas
  - Workarounds
  - Quando NÃO usar a skill

### 3. Templates (04_RECURSOS/TEMPLATES/)

**TEMPLATE_Criar_Skill_Antigravity.md** (~10KB estimado)
- Seções:
  - Checklist de especificações
  - Template skill.md (metadados)
  - Template script Python (estrutura base)
  - Padrões de código
  - Funções obrigatórias
  - Safety requirements
  - Exemplo completo

**TEMPLATE_Prompt_Gemini_Nova_Skill.md** (~8KB estimado)
- Seções:
  - Estrutura do prompt
  - Contexto necessário
  - Especificações técnicas
  - Checklist de validação
  - Exemplo de prompt real (session-logger como referência)

### 4. Checklists (04_RECURSOS/CHECKLISTS/)

**CHECKLIST_Uso_Skills_Antigravity.md** (~3KB estimado)
- Checklist antes de usar skill
- Checklist após executar skill
- Checklist de validação do resultado
- Checklist de troubleshooting

---

## 🔄 WORKFLOW DE CRIAÇÃO

### Etapa 1: Análise (1h)
- [ ] Revisar as 3 skills aprovadas
- [ ] Listar casos de uso reais
- [ ] Identificar edge cases (testes práticos)
- [ ] Documentar problemas encontrados (se houver)

### Etapa 2: Protocolos (2h)
- [ ] Criar PROTOCOLO_Uso_Skills_Antigravity.md
- [ ] Criar PROTOCOLO_Troubleshooting_Skills.md
- [ ] Criar PROTOCOLO_Manutencao_Skills.md

### Etapa 3: Guias e Templates (2h)
- [ ] Criar GUIA_Edge_Cases_Skills.md
- [ ] Criar TEMPLATE_Criar_Skill_Antigravity.md
- [ ] Criar TEMPLATE_Prompt_Gemini_Nova_Skill.md
- [ ] Criar CHECKLIST_Uso_Skills_Antigravity.md

### Etapa 4: Integração (1h)
- [ ] Atualizar MOC_Skills_BiIA.md com links
- [ ] Atualizar MOC_Padroes_Protocolos_Guidelines.md
- [ ] Atualizar CLAUDE.md (referência aos protocolos)
- [ ] Atualizar GEMINI.md (referência aos templates)

### Etapa 5: Validação (30min)
- [ ] Testar uso de pelo menos 1 skill seguindo protocolo
- [ ] Validar que documentação está clara
- [ ] Verificar links funcionando
- [ ] Criar checkpoint

**Tempo Total Estimado:** 6-7 horas

---

## 📊 MÉTRICAS DE SUCESSO

### Completude
- [ ] 7 arquivos criados (3 protocolos + 1 guia + 2 templates + 1 checklist)
- [ ] MOCs atualizados com referências
- [ ] Links internos funcionando

### Qualidade
- [ ] Cada skill tem seção dedicada em pelo menos 2 documentos
- [ ] Pelo menos 3 exemplos reais de uso por skill
- [ ] Pelo menos 5 edge cases documentados
- [ ] Template testado com criação de skill fictícia

### Utilidade
- [ ] Protocolo pode ser seguido sem contexto adicional
- [ ] Troubleshooting resolve pelo menos 80% dos problemas comuns
- [ ] Template reduz tempo de criação de nova skill em 50%

---

## 🎯 CONTEÚDO PRIORITÁRIO

### Must Have (Obrigatório)

**PROTOCOLO_Uso_Skills_Antigravity.md:**
- Quando usar cada skill (decisão clara)
- Como triggerar (linguagem natural correta)
- Workflow típico (passo a passo)
- Exemplos reais (3 por skill)

**PROTOCOLO_Troubleshooting_Skills.md:**
- Skill não ativa quando deveria (diagnóstico)
- Skill falha ao executar (logs, erros)
- Resultado incorreto (validação)
- Fallback manual (o que fazer)

**TEMPLATE_Criar_Skill_Antigravity.md:**
- Estrutura skill.md completa
- Template script Python base
- Funções obrigatórias documentadas
- Exemplo completo funcional

### Should Have (Importante)

**GUIA_Edge_Cases_Skills.md:**
- Vault muito grande (>50k arquivos)
- Encoding issues (caracteres especiais)
- Git não disponível
- Permissões de arquivo

**TEMPLATE_Prompt_Gemini_Nova_Skill.md:**
- Seções obrigatórias do prompt
- Como especificar funcionalidades
- Como criar checklist de validação

### Could Have (Desejável)

**PROTOCOLO_Manutencao_Skills.md:**
- Versionamento
- Testes de regressão
- Changelog

**CHECKLIST_Uso_Skills_Antigravity.md:**
- Pre-flight checks
- Post-execution validation

---

## 🔗 DEPENDÊNCIAS

### Arquivos de Referência
- MOC_Skills_BiIA.md (criado ✅)
- .gemini/skills/vault-organizer/ (criado ✅)
- .gemini/skills/status-updater/ (criado ✅)
- .gemini/skills/session-logger/ (criado ✅)
- SESSION_LOG.md (ativo ✅)
- STATUS_VAULT.md (ativo ✅)

### Protocolos Relacionados
- PROTOCOLO_CRIACAO_ARQUIVOS.md (nomenclatura)
- PROTOCOLO_SINCRONIZACAO_AGENTES.md (comunicação bi-IA)

### Skills Claude Code
- /validate (usar antes de criar)
- /sync (registrar progresso)

---

## 📝 CONTEÚDO ESPECÍFICO

### PROTOCOLO_Uso_Skills_Antigravity.md

**Estrutura:**

```markdown
# PROTOCOLO: Uso de Skills Antigravity

## Visão Geral

Sistema de skills executáveis que automatizam tarefas do vault.

## Skill #1: vault-organizer

### Quando Usar
- Arquivos fora do lugar (raiz do vault)
- Após baixar múltiplos arquivos
- Limpeza semanal
- Após migração de conteúdo

### Quando NÃO Usar
- Arquivos já organizados
- Estrutura complexa que requer decisão manual
- Documentos temporários que serão apagados

### Como Usar

**Trigger:** "organizar vault" ou "marie kondo"

**Workflow:**
1. Gemini detecta trigger
2. Skill escaneia raiz do vault
3. Categoriza arquivos (PDFs, imagens, etc.)
4. Move para pastas corretas
5. Gera relatório

**Exemplo Real:**
```
Usuário: "Organizar vault"
Gemini: [Detecta trigger]
        [Skill ativa]
        [Move 5 PDFs para 04_RECURSOS/]
        [Move 3 PNGs para 04_RECURSOS/]
        [Gera relatório]
        "✅ 8 arquivos organizados!"
```

### Validação do Resultado
- Raiz do vault limpa?
- Arquivos nas pastas corretas?
- Relatório gerado?
- MOCs atualizados (se necessário)?

## Skill #2: status-updater

[Mesmo formato]

## Skill #3: session-logger

[Mesmo formato]

## Workflow Típico (Todas Skills)

[Diagrama Mermaid]

## Boas Práticas

1. Sempre ler relatório gerado
2. Validar resultado antes de commit
3. Ter backup recente (skills criam automático)
4. Usar modo dry-run se incerto

## Checklist de Uso

### Antes de Usar Skill
- [ ] Sei exatamente o que quero fazer?
- [ ] Skill correta para o caso?
- [ ] Backup recente existe?
- [ ] Vault em estado consistente (git)?

### Depois de Usar Skill
- [ ] Resultado esperado?
- [ ] Relatório faz sentido?
- [ ] MOCs atualizados (se relevante)?
- [ ] Commit (se tudo OK)?
```

### PROTOCOLO_Troubleshooting_Skills.md

**Estrutura:**

```markdown
# PROTOCOLO: Troubleshooting Skills Antigravity

## Diagnóstico Geral

### Skill Não Ativa

**Sintoma:** Trigger não funciona

**Diagnóstico:**
1. Spelling correto? ("sync" não "sinc")
2. Trigger exato ou similar?
3. Gemini entendeu comando?

**Solução:**
- Usar trigger exato da documentação
- Reformular: "Por favor, execute session-logger"
- Fallback: Executar script manualmente

### Skill Falha ao Executar

**Sintoma:** Erro durante execução

**Diagnóstico:**
1. Ler mensagem de erro
2. Verificar logs (output do script)
3. Verificar pré-requisitos (git, encoding, etc.)

**Solução:**
- Verificar pré-requisitos
- Executar com --dry-run
- Reportar erro com contexto completo

### Resultado Incorreto

**Sintoma:** Skill executa mas resultado errado

**Diagnóstico:**
1. Comparar com backup automático
2. Ler relatório gerado
3. Verificar se entendeu comando corretamente

**Solução:**
- Restaurar backup
- Reformular comando
- Executar manualmente com mais controle

## Problemas Comuns por Skill

### vault-organizer

**Problema:** Moveu arquivo para pasta errada

**Causa:** Categorização incorreta

**Solução:**
1. Mover manualmente
2. Reportar caso (melhorar heurística)

### status-updater

**Problema:** Métricas incorretas

**Causa:** Heurística não considerou caso específico

**Solução:**
1. Atualizar manualmente STATUS_VAULT.md
2. Reportar caso (ajustar cálculo)

### session-logger

**Problema:** Git não detecta mudanças

**Causa:** Git não disponível ou repo não inicializado

**Solução:**
1. Verificar: `git status` funciona?
2. Inicializar repo se necessário
3. Usar modo manual (argumentos CLI)

## Códigos de Erro

[Lista de erros comuns com explicações]

## Fallback Manual

### Como Executar Skill Manualmente

**vault-organizer:**
```bash
cd .gemini/skills/vault-organizer/scripts
python organizer.py
```

**status-updater:**
```bash
cd .gemini/skills/status-updater/scripts
python updater.py
```

**session-logger:**
```bash
cd .gemini/skills/session-logger/scripts
python logger.py "mensagem opcional"
```

## Quando Reportar Bug

**Bug real:**
- Erro Python (traceback)
- Comportamento inesperado consistente
- Dados corrompidos

**Uso incorreto:**
- Trigger errado
- Expectativa incorreta
- Caso não suportado

## Checklist de Diagnóstico

- [ ] Li mensagem de erro completamente?
- [ ] Verifiquei pré-requisitos (git, python, encoding)?
- [ ] Tentei modo dry-run?
- [ ] Consultei documentação da skill?
- [ ] Verifiquei backup automático?
- [ ] Tentei fallback manual?
```

---

## 🚀 EXECUÇÃO

### Agente Responsável

**Claude Code** - Criação de protocolos (conhecimento estratégico)
**Gemini** - Pode auxiliar com exemplos de uso (se delegado)

### Timing

**Quando executar:** Logo após aprovação deste plano
**Duração:** 1 sessão (6-7h) ou 2 sessões (3-4h cada)
**Prioridade:** ALTA (bloqueia Fase 7.4)

### Validação

**Critério de aprovação:**
- [ ] 7 arquivos criados
- [ ] Cada skill documentada em pelo menos 3 documentos
- [ ] Pelo menos 10 exemplos reais de uso (total)
- [ ] Pelo menos 10 edge cases documentados
- [ ] Template testado com skill fictícia
- [ ] MOCs atualizados
- [ ] Checkpoint criado

---

## 📋 CHECKPOINT

**Ao finalizar Fase 7.3:**

Criar: `CHECKPOINT_18JAN2026_Fase_7_3_Protocolos.md`

**Conteúdo:**
- Resumo dos 7 arquivos criados
- Exemplos de uso documentados
- Edge cases descobertos
- Aprendizados
- Próximo: Fase 7.4 (Conversão Top 7)

---

## 🎯 IMPACTO ESPERADO

### Benefícios

**Curto Prazo:**
- Uso efetivo das 3 skills (redução de erros)
- Troubleshooting rápido (economia de tempo)
- Documentação clara (zero ambiguidade)

**Médio Prazo:**
- Criação rápida de novas skills (template pronto)
- Manutenção fácil (protocolos claros)
- Onboarding facilitado (se outros usarem vault)

**Longo Prazo:**
- Sistema escalável (até 7 skills ou mais)
- Qualidade consistente (padrões definidos)
- Conhecimento preservado (documentação completa)

### Métricas

- Tempo para usar skill corretamente: -50%
- Tempo para resolver erro: -70%
- Tempo para criar nova skill: -50%
- Erros de uso: -80%

---

**Versão:** 1.0
**Criado:** 18/JAN/2026
**Status:** Planejamento
**Aprovação:** Pendente

---

**PRONTO PARA EXECUÇÃO!** 🚀
