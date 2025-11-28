---
criado: 2025-07-23T13:10:33-03:00
atualizado: 2025-07-23T13:10:36-03:00
---
## Guia Completo para Trabalhar com Variáveis no n8n

## Introdução

Bem-vindo ao mundo do n8n! Se você está aqui, provavelmente já teve seu primeiro contato com essa poderosa ferramenta de automação e está pronto para mergulhar mais fundo. Neste ebook, vamos explorar um dos conceitos mais fundamentais para dominar o n8n: as variáveis.

Imagine que você está construindo um fluxo de trabalho que precisa se adaptar a diferentes situações. Em vez de usar dados estáticos, que não mudam, as variáveis permitem que seu fluxo seja dinâmico e flexível. É como a diferença entre um robô que só faz uma coisa e um assistente inteligente que se adapta às suas necessidades.

Vamos começar nossa jornada entendendo por que as variáveis são tão importantes e como elas podem transformar seus fluxos de trabalho.

## Capítulo 1: Introdução ao n8n e Importância das Variáveis

### O que é o n8n?

O n8n é uma ferramenta de automação de fluxos de trabalho que permite conectar diferentes aplicativos e serviços sem a necessidade de codificação. Com o n8n, você pode criar fluxos personalizados para automatizar tarefas repetitivas, sincronizar dados entre diferentes plataformas e muito mais.

### Por que as Variáveis São Importantes?

As variáveis são o coração de qualquer fluxo de trabalho no n8n. Elas permitem que você use dados dinâmicos em seu fluxo, em vez de valores fixos. Isso é especialmente útil quando você está lidando com dados que mudam frequentemente, como nomes de usuários, números de telefone ou horários de envio.

### Um Exemplo Prático

Imagine que você está criando um fluxo para enviar mensagens personalizadas para seus contatos no WhatsApp. Se você usar um número fixo, todas as mensagens serão enviadas para essa pessoa. Mas se você usar uma variável para o número do destinatário, o fluxo pode enviar mensagens para diferentes pessoas com base nos dados que você receber.

## Capítulo 2: Trabalhando com Dados: Estáticos vs. Variáveis

### O que São Dados Estáticos?

Dados estáticos são valores fixos que não mudam. Eles são usados quando você precisa de um valor específico que permanecerá o mesmo em todas as execuções do seu fluxo. Por exemplo, se você sempre quiser enviar mensagens para o número 55928..., você usaria um dado estático.

### O que São Dados Variáveis?

Dados variáveis são valores que podem mudar a cada execução do fluxo. Eles são extraídos de fontes externas, como mensagens recebidas, respostas de APIs ou entradas de usuários. No exemplo anterior, em vez de usar um número fixo, você usaria uma variável para o número do destinatário, que pode ser diferente a cada execução.

### A Diferença Chave

A principal diferença entre dados estáticos e variáveis é a flexibilidade. Dados estáticos são rígidos e não permitem personalização, enquanto dados variáveis permitem que seu fluxo se adapte a diferentes situações.

## Capítulo 3: Tipos de Variáveis no n8n

### Variáveis String

Uma variável string é usada para armazenar texto. Ela é representada pelo símbolo de uma letra "A" azul. Por exemplo, o nome de um usuário é uma variável string.

#### Como Usar Variáveis String

- **Pinning de Dados**: Você pode pinar uma variável string para reutilizá-la em diferentes partes do fluxo.
- **Condições**: Use variáveis string em condições para verificar se um nome existe, está vazio ou contém determinadas palavras.

### Variáveis Number

Uma variável number é usada para armazenar números. Ela é representada pelo símbolo de um "3" verde. Por exemplo, um código de confirmação é uma variável number.

#### Como Usar Variáveis Number

- **Condições Numéricas**: Use variáveis number em condições para verificar se um número existe ou se atende a um critério específico.
- **Transformações**: Você pode transformar uma variável string em uma variável number se necessário.

### Variáveis Object

Uma variável object é usada para armazenar conjuntos de dados relacionados. Ela é representada pelo símbolo de um cubo 3D. Por exemplo, os detalhes de uma conversa são armazenados como um object.

#### Como Usar Variáveis Object

- **Extração de Dados**: Use variáveis object para extrair informações específicas de um conjunto de dados.
- **Transformações**: Você pode transformar um object em outras variáveis para usar em diferentes partes do fluxo.

### Variáveis Boolean

Uma variável boolean é usada para armazenar valores lógicos (verdadeiro ou falso). Ela é representada pelo símbolo de uma setinha preta. Por exemplo, um status de ativo/inativo é uma variável boolean.

#### Como Usar Variáveis Boolean

- **Condições Lógicas**: Use variáveis boolean em condições para verificar se uma ação deve ser executada ou não.
- **Transformações**: Você pode transformar outras variáveis em boolean se necessário.

## Capítulo 4: Configurando Dados com Nodes e IA

### Como Configurar Dados

Configurar dados é o processo de definir quais dados você quer usar em seu fluxo. Isso pode ser feito usando o node "Set" ou o node "Edit Field".

#### Passo a Passo

1. **Adicionar o Node**: Arraste e solte o node "Set" para o seu fluxo.
2. **Definir os Dados**: Selecione quais dados você quer usar e defina seus valores.
3. **Testar**: Clique em "Test Step" para verificar se os dados estão sendo configurados corretamente.

### Usando IA para Corrigir Dados

Às vezes, os dados que recebemos podem estar formatados de forma inadequada. Por exemplo, um número de telefone pode vir com símbolos indesejados. Nesse caso, podemos usar a IA para corrigir esses dados.

#### Como Fazer

1. **Adicionar o Node OpenAI**: Arraste e solte o node "OpenAI" para o seu fluxo.
2. **Configurar o Prompt**: Escreva um prompt instruindo a IA a corrigir o formato do número.
3. **Testar**: Clique em "Test Step" para verificar se a IA está corrigindo os dados corretamente.

## Conclusão

Parabéns! Você completou o Guia Completo para Trabalhar com Variáveis no n8n. Agora você sabe como usar variáveis para criar fluxos de trabalho mais dinâmicos e flexíveis. Lembre-se de que a prática leva à perfeição, então não hesite em experimentar e criar seus próprios fluxos.

### O Que Fazer Agora?

- **Pratique**: Crie fluxos simples usando variáveis para se familiarizar com o conceito.
- **Exploração**: Explore outros nodes e recursos do n8n para expandir suas habilidades.
- **Compartilhe**: Compartilhe seus projetos e dicas com a comunidade n8n.

O mundo da automação está cheio de possibilidades, e agora você tem as ferramentas certas para aproveitá-las. Boa sorte!