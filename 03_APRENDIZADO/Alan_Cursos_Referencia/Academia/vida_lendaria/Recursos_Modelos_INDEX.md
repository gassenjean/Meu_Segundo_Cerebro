---
title: INDEX - Mente Lendár[IA] | Alan Nicolas
url: https://mentelendaria.com/Recursos/Modelos/INDEX
downloaded: 2025-11-11T13:03:10.542Z
criado: 2025-11-19T19:06:56-03:00
atualizado: 2025-11-19T19:07:09-03:00
---

📋 Templates - Mentelendaria 

Infraestrutura do vault. Templates reutilizáveis para criar notas consistentes e bem estruturadas.

Última atualização: 2025-11-05 Stage: Infraestrutura

📊 Visão Geral 
Total de templates: 8
Categorias: 4 (Notas Gerais, Conhecimento, Pessoas, Negócios)
Sistema: Templater plugin (variáveis dinâmicas)
🗂️ Templates por Categoria 
📝 Notas Gerais 
Default 

Quando usar: Template universal para qualquer nota nova que não se encaixa em categorias específicas.

Inclui:

YAML metadata (título, datas, aliases, tags)
Templater dinâmico (renomeia automaticamente)
Timestamps (created, last modified)

Melhor para:

Anotações de reuniões
Insights rápidos
Notas de leitura gerais
Reflexões pessoais
5 min (simples) 

Quando usar: Captura rápida de ideias — formato minimalista sem frescura.

Inclui:

Estrutura simplificada
Foco em velocidade de captura
Menos metadata

Melhor para:

Brainstorming sessions
Captura de ideias fugidias
Notas de voz transcritas
Pensamentos durante caminhada
Nota Diária 

Quando usar: Daily notes — diário de trabalho e reflexões do dia.

Inclui:

Data automática
Seções para planejamento/revisão
Links para dias anteriores/posteriores

Melhor para:

Journaling diário
Log de atividades
Planejamento dia a dia
Tracking de hábitos
📚 Conhecimento & Aprendizado 
Livro 

Quando usar: Criar resumo estruturado de um livro (principal template da biblioteca).

Inclui (5 seções obrigatórias):

💡 Ideia Principal — Resumo em 2-3 frases
👤 Para quem é? — Perfil do leitor ideal
👀 Como o Livro me Impactou — Narrativa pessoal primeira pessoa
📒 Sumário — Ideias chave, citações, práticas, críticas
🎙️ Mencionado em Vida Lendária — Cross-reference episódios

YAML metadata:

author, total pages, category, publish date
status (unread/reading/read)
rating (⭐ 1-5)
cover image URL

Dataview query: Lista outros livros do mesmo autor

Melhor para:

Todos os livros em /Livros
Seguir diretrizes do CLAUDE.md (voz pessoal, primeira pessoa)

Ver exemplo: Antifrágil, Essencialismo, Flow

👤 Pessoas & Autores 
Pessoa 

Quando usar: Criar perfil de pessoa importante (mentores, parceiros, clientes, contatos).

Inclui:

Informações básicas
Contexto de relacionamento
Notas de interações
Tags de categorização

Melhor para:

Network tracking
CRM pessoal
Registro de mentores
Clientes/parceiros importantes
Author 

Quando usar: Criar perfil dedicado de autor/pensador (complementa biblioteca de livros).

Inclui:

Bio e background
Principais obras
Ideias centrais
Links para livros no vault

Melhor para:

Autores com múltiplos livros lidos
Pensadores que influenciaram fortemente
Cross-reference com biblioteca

Ver pasta: 38 perfis de autores

💼 Negócios & Conteúdo 
Chamada 

Quando usar: Estruturar chamadas de vendas, webinars, ou apresentações importantes.

Inclui:

Call-to-action framework
Estrutura de apresentação
Objeções e respostas

Melhor para:

Webinars de lançamento
Apresentações de curso
Chamadas de vendas
Lives de conversão
Prep Notes 

Quando usar: Preparação para reuniões, entrevistas, gravações, calls importantes.

Inclui:

Objetivos da reunião
Tópicos a cobrir
Perguntas preparadas
Action items pós-reunião

Melhor para:

Prep para podcast guests
Reuniões estratégicas
Entrevistas
Gravações de aula
🎯 Como Usar Templates 
Método 1: Templater Hotkey 
Criar nova nota (Cmd+N)
Usar comando Templater (Cmd+P → "Templater: Insert Template")
Escolher template desejado
Método 2: Core Templates 
Criar nova nota
Cmd+P → "Templates: Insert template"
Escolher da lista
Método 3: Template Folder (Automático) 
Configurar pasta específica para auto-aplicar template
Exemplo: Notas em /Recursos/Livros/ → auto-aplicar Livro.md
🔧 Customização de Templates 
Variáveis Templater Disponíveis 

Datas:

<% tp.date.now("YYYY-MM-DD") %> — Data atual
<% tp.file.creation_date() %> — Data de criação
<% tp.file.last_modified_date() %> — Última modificação

Arquivo:

<% tp.file.title %> — Título da nota
<% tp.file.folder() %> — Pasta atual
<% tp.file.rename("novo nome") %> — Renomear

Entrada do usuário:

<% tp.system.prompt("Pergunta?") %> — Popup de input
<% tp.system.suggester(options, values) %> — Seletor

Ver documentação: Recursos/Obsidian/Obsidian Templates

📚 Templates Relacionados a MOCs 

Conecte templates com estruturas maiores do vault:

Template	Usado em	MOC Relacionado
Livro	/Recursos/Livros/	MOC - PKM & Segundo Cérebro
Author	/Recursos/Autores & Pensadores/	MOC - PKM & Segundo Cérebro
Nota Diária	/Daily Notes/	MOC - Atenção & Cognição
Default	Geral (/Anotações/)	Todos os MOCs
Chamada	/Cursos/, /Vida Lendária/	MOC - Criação de Conteúdo
🎓 Exemplos de Uso 
Exemplo 1: Processar Livro de ibook 

Situação: Tenho highlights de "Maestria" em /ibook, quero criar entrada completa.

Workflow:

Abrir /Recursos/Livros/
Criar nova nota → usar template Livro
Preencher metadata (autor: Robert Greene, rating, etc.)
Seção 3 "Como me Impactou" → escrever primeira pessoa
Copiar highlights de ibook → organizar em "Ideias Chave"
Adicionar citações preferidas, críticas
Cross-referenciar com MOC - Maestria & Genialidade
Deletar ou arquivar ibook/Maestria.md
Exemplo 2: Preparar Episódio VL 

Situação: Vou gravar episódio sobre "Por que gênios são solitários?"

Workflow:

Criar nota em /Vida Lendária/Episódios VL/
Usar template Prep Notes
Preencher:
Objetivos: "Explorar solidão existencial de gifted people"
Tópicos: Altas habilidadesSuperdotação, Consciência
Referências: The Gifted Adult, A sabedoria da insegurança
Durante gravação: tomar notas inline
Pós-gravação: adicionar timestamps, action items
Exemplo 3: Network Tracking 

Situação: Conheci mentor importante em evento, quero catalogar.

Workflow:

Criar nota em /Recursos/Autores & Pensadores/ ou /Anotações/Pessoas/
Usar template Pessoa
Preencher contexto, área de expertise
Adicionar tag: #mentor #network
Linkar livros que ele recomendou
Atualizar após cada interação
💡 Melhores Práticas 
✅ Faça 
Customize templates para seu workflow específico
Use YAML metadata para queries Dataview
Mantenha consistência — templates garantem padrão
Revise periodicamente — evolua templates conforme necessidade
Cross-reference — conecte com MOCs e outras notas
❌ Evite 
Não crie template para tudo — só para padrões recorrentes
Não sobrecarregue com campos — menos é mais
Não ignore Templater — variáveis dinâmicas economizam tempo
Não duplique templates — consolide similares
Não esqueça de atualizar — templates desatualizados confundem
🔄 Manutenção 
Revisar Templates (Trimestral) 
Auditoria de uso — quais templates são mais usados?
Feedback — quais campos são sempre deletados? (remover)
Gaps — faltam templates para algum padrão recorrente?
Atualizações — incorporar novos plugins ou features
Changelog 

2025-11-05: INDEX criado, 8 templates catalogados [Adicionar futuras atualizações aqui]

🔗 Navegação 

🏠 Voltar para: 📇 Recursos → Vault Principal

Ver também:

📚 Biblioteca (87 livros) — Usa template Livro
👤 Autores & Pensadores (38 perfis) — Usa template Author
📖 Obsidian Templates Guide — Documentação técnica

MOCs Relacionados:

MOC - PKM & Segundo Cérebro
MOC - Criação de Conteúdo

Sistema de conhecimento · Mentelendaria · Alan Nicolas

Tags 

#templates #modelos #infraestrutura #obsidian #templater

LINKS TO THIS PAGE
📇 Index