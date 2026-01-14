---
criado: 2024-10-01T10:59:40-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir

## **Destaques do Kindle**

Esse plugin permite que você sincronize (e ressincronize) suas notas e destaques do Kindle diretamente no seu armazém de conhecimento Obsidian. Existem duas maneiras principais de fazer isso:

1. **Usando o Leitor Kindle da Amazon:** Esta opção permite que você sincronize qualquer e-book que tenha comprado diretamente da Amazon. O plugin varrerá suas anotações e destaques do Leitor Kindle da Amazon e os manterá continuamente sincronizados. No entanto, essa opção não funcionará para destaques de livros, artigos, PDFs e documentos pessoais que não foram comprados na Amazon.
2. **Usando o seu dispositivo Kindle (My Clippings):** Esta opção permite que você sincronize suas anotações carregando o arquivo "My Clippings.txt" armazenado em seu dispositivo Kindle. Este arquivo inclui destaques, marcadores e notas para qualquer livro em seu Kindle, independentemente de ter sido comprado na Amazon ou não.

---

## **Como usar**

Para a primeira opção, você precisará fazer login em sua conta da Amazon por meio do Obsidian e permitir que o plugin acesse suas informações de leitura. Para a segunda opção, você precisará conectar seu dispositivo Kindle ao seu computador usando um cabo USB, localizar e carregar o arquivo "My Clippings.txt".

---

## **Recursos**

- **Sincronização contínua e automática:** Após a configuração inicial, o plugin continuará a sincronizar novos destaques sem afetar as edições que você fez em seu arquivo de destaques.
- **Sincronização de livros não comprados na Amazon:** Isso é possível carregando o arquivo "My Clippings.txt" do seu dispositivo Kindle.
- **Metadados enriquecidos:** O plugin pode baixar informações adicionais sobre seus livros da [Amazon.com](http://amazon.com/) para enriquecer suas notas.
- **Modelagem poderosa e flexível com visualização:** Você pode personalizar seus destaques e nomes de arquivos configurando seu próprio modelo usando a linguagem de modelagem Nunjucks com visualização ao vivo.

---

## **Considerações**

- **Segurança:** Se você escolher sincronizar seus destaques através do Leitor Kindle online da Amazon, é importante notar que, ao fazer login em sua conta da Amazon através do Obsidian, sua sessão da Amazon fica disponível para qualquer outro plugin em seus armazéns até que sua sessão expire. Você pode atenuar esse risco fazendo logout após cada sincronização ou usando o método offline de sincronização (opção 2 acima).
- **Limites de exportação:** Por vários motivos, a plataforma Kindle pode às vezes limitar a quantidade de texto destacado que pode ser exportado de um livro específico. Este limite varia de livro para livro, comprado na Amazon ou com proteção DRM. Atualmente, não existe uma alternativa conhecida para contornar isso.

---

## **🎥 Recomendados (Extras)**

Vou deixar abaixo o vídeo oficial da ferramenta, com alguns dos passos demonstrados na aula:

Tivemos uma contribuição bem legal também do Gabriel Silvestri na Biblioteca Obsidian sobre isso, ele mostrou como ele utiliza o Kindle Highlights [» clique aqui para conferir «](https://comunidade.vidalendaria.com.br/c/obsidian/highlights-no-kindle-template-bonitao)

---

## **iBook**

O plugin iBook permite exportar os destaques e anotações do seu iBook no Mac para o seu vault do Obsidian. Seguem algumas informações sobre o plugin:

1. **Requisitos**: O plugin funciona com uma base de dados SQLite3 local que armazena os dados do iBook no Mac. Portanto, é necessário que o SQLite3 esteja instalado no seu sistema. Na seção '**Como instalar o SQLite3'**, você encontrará todas as informações necessárias.
2. **Como usar**: O plugin oferece várias formas de exportar os destaques e anotações do iBook para o Obsidian.
   - Para exportar todas as anotações e destaques, use o atalho **Ctrl/Cmd + P** e digite "ibook export".
   - Para exportar as anotações e destaques de um único livro, use o atalho **Ctrl/Cmd + Shift + B** e procure pelo nome do livro ou do autor.
   - Para exportar informações do livro pesquisando no Goodreads, use o atalho **Ctrl/Cmd + shift + i**. O plugin irá usar o nome do arquivo para pesquisar as informações do livro e inserir na posição atual do cursor.
3. **Recursos**: O plugin iBook oferece vários recursos úteis.
   - Suporta a exportação por nome do livro ou do autor.
   - Exporta os destaques e anotações do iBook para o seu cofre do Obsidian.
   - Permite a criação de um template definido pelo usuário.
   - Pesquisa informações do livro no Goodreads.

---

### **Como instalar o SQLite3**

**MacOS**

SQLite3 vem pré-instalado com Mac OS X (agora macOS). Portanto, você pode ter o SQLite3 no seu sistema e nem saber disso. Para verificar, você pode abrir o Terminal e digitar **sqlite3**, seguido por enter. Se o SQLite3 estiver instalado, você verá uma mensagem com a versão do SQLite e um prompt de comando. Caso contrário, você verá uma mensagem dizendo que o comando sqlite3 não foi encontrado.

Caso o SQLite3 não esteja instalado, você pode instalar usando o **Homebrew**, que é um gerenciador de pacotes para macOS. O gerenciador de pacotes é um programa que automatiza o processo de instalação, atualização e remoção de programas de software.

Aqui estão as etapas para instalar o **SQLite3** no **Mac** usando o **Homebrew**:

1. Abra o terminal:
   - Pressione **Command** + **Space** para abrir a busca Spotlight.
   - Digite "**Terminal**" na busca.
   - Selecione a aplicação "Terminal" que aparecerá nos resultados da busca.
2. **Instalar o Homebrew**: Se você ainda não tem o Homebrew instalado, você pode instalar executando o seguinte comando no Terminal:Este comando baixa um script e o executa. O script explica o que será feito e pedirá sua confirmação antes de prosseguir.`   bashCopy code/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"   `
3. **Instalar o SQLite3**: Uma vez que o Homebrew esteja instalado, você pode instalar o SQLite3 executando o seguinte comando no Terminal:Este comando diz ao Homebrew para baixar e instalar o SQLite3.Após a instalação, você pode verificar se o SQLite3 foi instalado corretamente digitando **sqlite3** no Terminal novamente. Você deverá ver a versão do SQLite e um prompt de comando.`   bashCopy codebrew install sqlite3   `

   ***

## Windows

1. **Baixar o SQLite3**: Acesse a página de download do SQLite: [](https://www.sqlite.org/download.html)**[https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)**. Na seção "Precompiled Binaries for Windows", clique no link "[sqlite-tools-win32-x86-XXXXXXX.zip](http://sqlite-tools-win32-x86-xxxxxxx.zip/)" para baixar o arquivo zip. A parte "XXXXXXX" do link será a versão atual do SQLite.
2. **Extrair os arquivos**: Extraia o arquivo zip em uma pasta no seu computador. Por exemplo, você pode criar uma pasta chamada "SQLite3" no seu diretório C: e extrair os arquivos lá.
3. **Atualizar a variável de ambiente PATH**: Para acessar o SQLite a partir de qualquer diretório no prompt de comando, você precisará adicionar o diretório onde extraiu os arquivos do SQLite à sua variável de ambiente PATH. Aqui estão as etapas:
   - Abra o Painel de Controle e vá para "Sistema e Segurança", então clique em "Sistema".
   - Clique em "Configurações avançadas do sistema".
   - Na janela que se abre, vá para a aba "Avançado" e clique em "Variáveis de ambiente".
   - Na seção "Variáveis do sistema", encontre a variável "Path" e clique em "Editar".
   - Na janela de edição, clique em "Novo" e adicione o caminho da pasta onde você extraiu os arquivos do SQLite.
   - Clique em "OK" em todas as janelas para salvar as alterações.
4. **Verificar a instalação**: Abra o prompt de comando e digite "**sqlite3**". Se a instalação foi bem-sucedida, você verá a versão do SQLite e um prompt de comando.

---

## **🎥 Vídeos Recomendados (Extras)**

Vou deixar abaixo um vídeo que ilustra os passos descritos acima:

[](https://youtu.be/gsZmB_MMKyc)https://youtu.be/gsZmB_MMKyc

---

## **Próximos Passos:**

1. ♾️ Honre o comprometimento com a prática.
2. 🧠 Compartilhe nos comentários o que você aprendeu nesta aula.
3. 👉 Avance para próxima aula.

# ia

O plugin do Kindle para o Obsidian parece ser uma ferramenta útil para sincronizar anotações e destaques de livros lidos no Kindle com o armazém de conhecimento Obsidian. Aqui estão algumas das principais características e recursos do plugin:

**Características principais:**

1. **Sincronização contínua e automática**: O plugin sincroniza as anotações e destaques do Kindle com o Obsidian de forma contínua e automática.
2. **Suporte a diferentes formatos**: O plugin suporta a sincronização de anotações e destaques de diferentes formatos, incluindo livros comprados na Amazon e livros em formato PDF.
3. **Metadados enriquecidos**: O plugin pode baixar informações adicionais sobre os livros da Amazon para enriquecer as anotações.

**Recursos:**

1. **Sincronização de livros não comprados na Amazon**: O plugin permite sincronizar anotações e destaques de livros que não foram comprados na Amazon.
2. **Modelagem poderosa e flexível com visualização**: O plugin permite personalizar as anotações e nomes de arquivos configurando um modelo próprio usando a linguagem de modelagem Nunjucks com visualização ao vivo.

**Considerações:**

1. **Segurança**: É importante notar que, ao fazer login na conta da Amazon através do Obsidian, a sessão da Amazon fica disponível para qualquer outro plugin no armazém até que a sessão expire.
2. **Limites de exportação**: A plataforma Kindle pode limitar a quantidade de texto destacado que pode ser exportado de um livro específico.

**Instalação do SQLite3:**

Para usar o plugin iBook, é necessário instalar o SQLite3 no sistema. Aqui estão as etapas para instalar o SQLite3 no Mac e no Windows:

**Mac:**

1. Abra o Terminal e digite `sqlite3` para verificar se o SQLite3 está instalado.
2. Se o SQLite3 não estiver instalado, instale o Homebrew e, em seguida, instale o SQLite3 usando o comando `brew install sqlite3`.

**Windows:**

1. Baixe o arquivo zip do SQLite3 da página de download oficial.
2. Extraia os ar
