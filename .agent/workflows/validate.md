---
description: Validar Criação de Arquivos e Organização
---

1. **Determinar Modo**
   - Se o usuário descreveu um arquivo para criar -> **Modo Validação**.
   - Se o usuário pediu auditoria/check -> **Modo Auditoria**.

2. **Modo Validação (Criação de Arquivo)**
   - Leia `00_SISTEMA/PADROES/NOMENCLATURA.md` e `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md`.
   - Identifique o tipo de arquivo, localização correta e nomenclatura padrão.
   - Verifique se a pasta de destino existe.
   - **Saída:** Gere um relatório de validação confirmando Tipo, Localização, Nomenclatura e MOC a atualizar.

3. **Modo Auditoria (Organização do Vault)**
   - Liste os arquivos na raiz do vault. Apenas `CLAUDE.md`, `README.md` e `STATUS_VAULT.md` são permitidos.
   - Verifique se os projetos em `02_PROJETOS` seguem a estrutura padrão.
   - Verifique se os arquivos seguem a nomenclatura (CamelCase, sem espaços, prefixos corretos).
   - **Saída:** Gere um relatório de auditoria listando arquivos fora do lugar e ações corretivas.

4. **Executar Correções (Opcional)**
   - Se solicitado, mova os arquivos para os locais corretos e renomeie conforme o padrão.
