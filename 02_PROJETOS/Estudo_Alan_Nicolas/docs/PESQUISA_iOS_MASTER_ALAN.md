---
created: 2026-01-26T11:55
updated: 2026-01-26T11:55
---
# PESQUISA: iOS Master (Framework Alan Nicolas)

**Contexto:** Estrutura para Projeto Névoa Impecável (T035)
**Researcher:** Gemini Guardian
**Fonte:** Live Lendária 051 + Conceitos Vault
**Data:** 26/Jan/2026

## 1. Resumo Executivo

O **iOS Master** (Intelligence Operating System) não é um software único, mas uma **arquitetura de gestão de agentes**. Ele resolve o problema da "babeira" das IAs (alucinação e falta de foco) através de uma estrutura rígida de **Cargos e Protocolos**.

**A Regra de Ouro:** "Você não gerencia 200 agentes. Você gerencia 1 Orquestrador, que gerencia 5 Líderes, que gerenciam os operários."

## 2. Arquitetura do iOS Master

O iOS Master é o "Coringa" ou "Gerente de Produto". Ele é o único com quem o humano (Gassen) fala diretamente para demandas complexas.

### Os 5 Cargos Fundamentais (Squad Padrão)

1. **iOS Master (Orquestrador):**
    * **Função:** Ponto de contato. Traduz "intenção humana" (caos) em "instrução técnica" (ordem).
    * **Poder:** Decide QUEM chamar. Não executa tarefas especializadas (ex: não coda, não escreve copy final).
    * **Meta:** Reduzir a carga cognitiva do usuário.

2. **Whistle (Arquiteto):**
    * **Função:** Planejamento e Design.
    * **Regra:** "Think before you act". Ele desenha o arquivo, a estrutura do banco, o índice do livro, ANTES de qualquer execução.
    * **Saída:** Um plano MD ou diagrama Mermaid.

3. **James (Dev Sênior / Executor):**
    * **Função:** Execução cega e perfeita.
    * **Regra:** "Faca na caveira". Ele pega o plano do Whistle e implementa. Não questiona a arquitetura (a menos que seja impossível).
    * **Perfil:** Focado, técnico, rápido.

4. **Kim / Queen (QA - Quality Assurance):**
    * **Função:** Crítica e Validação.
    * **Regra:** "A Chata". O trabalho dela é encontrar erros. Se ela aprovar, vai para produção. Se não, volta para o James.
    * **Importante:** Ela protege o usuário de receber lixo.

5. **Dave (DevOps / Infra):**
    * **Função:** O "Zelador" do ambiente.
    * **Regra:** Garante que o arquivo existe, que o git está limpo, que a pasta está organizada.

## 3. Fluxo de Delegação (O Segredo)

O fluxo nunca é linear (A -> B -> C). É um **Ciclo de Refinamento**.

1. **Input:** Gassen diz "Quero um clone do Alex Hormozi".
2. **Triagem (iOS Master):** Entende que é um projeto de *Engenharia*. Chama o Whistle.
3. **Arquitetura (Whistle):** Desenha a estrutura (Extração -> Processamento -> Geração).
4. **Aprovação:** Master mostra o plano para Gassen. Gassen aprova.
5. **Execução (James):** Implementa o script de extração.
6. **Validação (Kim):** Roda o script. Deu erro? Devolve pro James. Funcionou? Libera.

## 4. O "Ralph Loop" (A Camada de Persistência)

IAs são ruins em tarefas longas e repetitivas. O Ralph resolve isso.

* **O que é:** Um script simples (Bash, Python ou n8n) que executa um loop `while`.
* **Lógica:**

    ```python
    while not tarefa_concluida():
        tentar_executar()
        verificar_sucesso()
        if falha:
            log_erro()
            retry() # Tenta de novo sem chorar
        else:
            break
    ```

* **Aplicação na Névoa:**
  * *Pesquisas:* O Ralph tenta abrir a URL. Se der 404, tenta a próxima. Não pergunta para o Gassen.
  * *Code:* O Ralph roda os testes. Se falhar, manda o erro pro James corrigir e roda de novo.

## 5. Sistema de Permissões

Para evitar catástrofes:

* **Nível 1 (Leitura):** Todos os agentes. (Read-only no Vault).
* **Nível 2 (Escrita Local):** James e Dave. Podem criar arquivos em pastas de projeto.
* **Nível 3 (Execução de Sistema):** Apenas via aprovação ou Ralph validado. (Rodar scripts, instalar pacotes).
* **Nível 4 (Deleção/Overwrite):** SOMENTE com confirmação explícita ou em pastas `tmp`/`cache`. **A Kim deve bloquear qualquer deleção de arquivo mestre.**

## 6. Aplicação Imediata na Névoa (Recomendações)

1. **Oficializar os Cargos:** Criar personas no `.cursorrules` ou prompt de sistema do Claude para que ele saiba quem é "James" e quem é "Kim". (Já temos algo similar com Claude Architect/Code, mas o modelo do Alan é mais rígido).
2. **Implementar a Kim:** Antes de me entregar qualquer tarefa concluída, o Claude DEVE invocar uma sub-persona de crítica ("Validando entrega...").
3. **Adotar o Ralph:** Para tarefas de lista (ex: "Pesquisar 50 links"), não fazer uma a uma na mão. Criar um script (ou instrução em lote) e deixar rodar.
