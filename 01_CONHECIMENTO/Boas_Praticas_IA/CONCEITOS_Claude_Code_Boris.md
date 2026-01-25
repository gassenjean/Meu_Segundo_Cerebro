---
created: 2026-01-25T12:27
updated: 2026-01-25T12:27
---
# CONCEITOS: 13 Dicas de Boris (Criador do Claude Code)

**Fonte:** Boris (Creator of Claude Code) - Como_o_criador_do_Claude_Code_usa_a_pr_pria_ferramenta___13_ (2).pdf
**Categoria:** Táticas / Workflow / Melhores Práticas
**Tags:** #claude-code #workflow #produtividade #boris

---

## 1. Paralelismo Extremo (5 Clouds)

### O Que É

Rodar múltiplas instâncias (clouds) do Claude Code em paralelo. Boris menciona abrir o terminal e numerar: 1, 2, 3, 4, 5.

### Por Que Importa

Aumenta drasticamente o throughput. Enquanto uma instância processa ou compila, você interage com outra.

### Como Aplicar

1. Abra 5 terminais.
2. Inicie 5 sessões independentes.
3. Atribua tarefas distintas (ex: T1=Frontend, T2=Backend, T3=Testes).
4. Use notificações do sistema para saber quando cada uma termina.

---

## 2. Ambiente Híbrido (15 Instâncias)

### O Que É

Usar instâncias locais combinadas com instâncias na nuvem (`cloud.ai`). Boris roda de 5 a 10 na nuvem + 5 locais, totalizando até 15 "trabalhadores" simultâneos.

### Aplicação no Bi-IA

Podemos simular isso rodando múltiplos terminais locais com diferentes perfis de agentes (Névoa, Gerentes), permitindo que trabalhem em paralelo em diferentes partes do Vault.

---

## 3. Opus 4.5 + Thinking (O Cérebro)

### O Que É

Uso exclusivo do modelo Opus 4.5 com "Thinking Mode" ativado para **tudo**.

### Por Que Importa

"Apesar de ser maior e mais lento que o SONNET, ele considera mais rápido no final das contas porque os resultados são mais objetivos." A qualidade do raciocínio evita o loop de tentativa e erro ("churn").

### Como Aplicar

No arquivo de configuração, forçar o uso dos modelos de raciocínio mais fortes disponíveis para tarefas de planejamento e arquitetura.

---

## 4. CLAUDE.md Compartilhado (Memória Coletiva)

### O Que É

Um único arquivo `CLAUDE.md` na raiz do repositório que serve como memória viva de todo o time. Não use múltiplos arquivos espalhados.

### Como Aplicar

"Qualquer vez que alguém vê alguma coisa do cloud que está agindo de maneira incorreta, eles adicionam no cloud.md." É a fonte da verdade evolutiva. Se a IA erra, corrija no MD, não só no chat.

---

## 5. @Claude no Code Review

### O Que É

Invocar o Claude diretamente nos comentários de Pull Requests/Code Reviews.

### Como Aplicar

Marcar `@Claude` no review para que ele:

1. Analise a mudança.
2. Adicione novas regras descobertas ao `CLAUDE.md` automaticamente.
Isso cria um ciclo virtuoso onde o Code Review melhora a IA para o futuro.

---

## 6. Plan Mode (Shift+Tab+Tab) - OBRIGATÓRIO

### O Que É

O modo de planejamento dedicado. Boris começa **a maioria** das sessões assim.

### Por Que Importa

"Um bom plano é realmente importante... você consegue ter um resultado em um one shot." Evita que a IA saia escrevendo código sem direção.

### Aplicação no Bi-IA

Isso valida nossa estratégia de exigir `implementation_plan.md` (PLANNING mode) antes de qualquer `EXECUTION`. É a diferença entre um júnior e um sênior.

---

## 7. Slash Commands para Workflows Repetitivos

### O Que É

Criar atalhos (`/comando`) para tarefas que você faz muitas vezes ao dia (inner loop workflows).

### Exemplo Concreto

`commit-push-pr`: Um comando que roda git status, pre-computa informações e faz o push, economizando digitação e tempo de contexto.

### Como Aplicar

Mapear tudo que fazemos >3x ao dia e transformar em um comando em `.claude/commands/`.

---

## 8. Sub-agents Especializados

### O Que É

Uso regular de "sub-agentes" para tarefas específicas pós-codificação.

- **Code Simplifier:** Simplifica o código após o Claude terminar.
- **Verify App:** Testa a aplicação end-to-end.

### Aplicação no Bi-IA

Fortalece nossa hierarquia iOS. O `Gerente de Projetos` não deve codar, deve chamar o `Especialista` (sub-agente) para tal.

---

## 9. Post-Use Hooks de Formatação

### O Que É

Hooks automáticos que rodam após o Claude gerar código para lidar com os "últimos 10%" de formatação que a IA pode errar.

### Por Que Importa

Garante que o código entregue esteja sempre em conformidade com o linter, evitando quebras de CI. A IA faz o "grosso", o hook dá o polimento final.

---

## 10. NÃO Use `dangerouslySkipPermissions` (Mode YOLO)

### O Que É

Boris aconselha explicitamente **contra** desativar as permissões de segurança, exceto em casos de extrema preguiça local.

### Por Que Importa

"Se você precisar de dar uma permissão a mais, você adiciona no seu arquivo de configurações... e ai ele já fica ali persistido". Configurar permissões explicitamente (`/permissions`) é mais seguro e cria um ambiente de "Low Hallucination".

---

## 11. Integração Total (MCP)

### O Que É

Claude Code não é uma ilha. Ele deve ter acesso a Slack, Sentry, BigQuery, etc.

### Como Aplicar

"Ele usa isso como uma integração para fazer tudo por ele." Se há um bug, o Claude vai no Sentry, pega o log, analisa e propõe a fix.

---

## 12. Background Agents para Tarefas Longas

### O Que É

Para tarefas que demoram (ex: builds longos, testes completos), Boris lança um agente em background.

### Como Aplicar

"I will either prompt Cloud to verify its work with background agent when it's done." Não fique esperando o terminal. Lance a verificação em background e vá fazer outra coisa.

---

## 13. Feedback Loops (A Dica de Ouro)

### O Que É

"Dê ao Cloud Code uma maneira de verificar o próprio trabalho dele." Isso melhora a qualidade do resultado em **2x a 3x**.

### Como Aplicar

Nunca aceite o código "de primeira". O fluxo deve ser:

1. Claude gera código.
2. Claude roda ferramenta de verificação (teste, linter, build).
3. Claude lê o erro.
4. Claude corrige.

Isso é o que chamamos de **Ralph Loop** no nosso sistema. É a diferença entre um código que "parece funcionar" e um código "rock solid".
