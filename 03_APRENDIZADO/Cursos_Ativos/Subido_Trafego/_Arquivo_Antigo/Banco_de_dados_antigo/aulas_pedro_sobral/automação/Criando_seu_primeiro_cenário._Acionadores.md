---
criado: 2024-12-15T13:37:47-03:00
atualizado: 2024-12-15T13:46:25-03:00
tags:
  - consumir
  - trafego
---

## [Criando seu primeiro cenário. Acionadores](https://comunidadesobral.s3.amazonaws.com/automacoes/cst_auto_a5.0_criando_seu_primeiro_cenario_acionadores.pdf)

O documento apresenta um guia prático sobre como criar cenários de automação utilizando a ferramenta Make, com foco nos acionadores. Aqui está um resumo completo e insights extraídos:

---

### **Resumo Completo**

**1. Introdução ao Make e Cenários de Automação**

- **Cenários** são estruturas que conectam ferramentas e permitem automações.
- **Acionadores** são os comandos que coletam os dados para iniciar o processo de automação:
  - **Instantâneos**: Recebem dados assim que estão disponíveis na plataforma fonte.
  - **Agendados**: Requerem configuração de intervalos para receber dados.

**2. Passo a Passo para Configurar Acionadores no Make**

- **Criando um cenário**:
  1. Clique em "Create new a scenario".
  2. Escolha a ferramenta inicial para a automação (ex.: Google Sheets).
- **Configuração com acionadores agendados**:
  - Exemplo: **Google Sheets** com a função "watch new rows".
  - Configuração de intervalo: escolha períodos como "every 15 minutes".
  - Ajuste períodos no painel “schedule setting” (dias específicos, horários, etc.).
- **Configuração com acionadores instantâneos**:
  - Exemplo: **Facebook Lead Ads** com a função "new lead".
  - Conecte a conta ao Make e finalize clicando em "ok".

**3. Conclusão**

- Existem dois tipos principais de acionadores:
  - Instantâneos: Reagem imediatamente.
  - Agendados: Operam em intervalos predefinidos.
- O material enfatiza a prática e revisões contínuas para melhorar as configurações.

---

### **Insights**

1. **Escolha adequada do acionador:** A definição do tipo de acionador é crucial para que a automação seja eficiente e compatível com a frequência desejada dos dados.
2. **Flexibilidade e personalização:** O Make permite configurações avançadas para atender necessidades específicas, como personalização de horários e filtros detalhados.
3. **Praticidade com ferramentas populares:** Exemplo do Google Sheets e Facebook Lead Ads mostra integração fácil com sistemas amplamente utilizados.
4. **Aprendizado contínuo:** Revisitar o material e testar diferentes configurações é importante para aprimorar a compreensão e funcionalidade das automações.
5. **Automação como alavanca de produtividade:** Configurar acionadores corretamente é o primeiro passo para transformar tarefas repetitivas em processos automáticos, economizando tempo e recursos.

Caso precise de mais detalhes ou exemplos sobre os tópicos abordados, posso desenvolver ou adaptar a explicação!
