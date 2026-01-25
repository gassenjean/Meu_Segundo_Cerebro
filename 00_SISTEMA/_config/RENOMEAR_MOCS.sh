#!/bin/bash
# Script de Renomeação de MOCs - Claude Architect
# Data: 28/Nov/2025
# Objetivo: Corrigir nomenclatura de 14 MOCs para conformidade com NOMENCLATURA.md

echo "🏛️ Claude Architect - Renomeação de MOCs"
echo "========================================="
echo ""
echo "⚠️  Este script vai renomear 14 arquivos MOC para padrão correto"
echo ""
echo "Padrão antigo: MOC_-_Palavra_&_Palavra.md (com espaços, acentos, &, -)"
echo "Padrão novo:   MOC_Palavra_Palavra.md (sem espaços, sem acentos, sem &, sem -)"
echo ""
read -p "Continuar? (s/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Ss]$ ]]
then
    echo "❌ Cancelado pelo usuário"
    exit 1
fi

cd "00_SISTEMA/MOCs" || exit

echo ""
echo "🔄 Iniciando renomeação..."
echo ""

# Função para renomear com segurança
rename_file() {
    local old="$1"
    local new="$2"

    if [ -f "$old" ]; then
        mv "$old" "$new"
        echo "✅ $old → $new"
    else
        echo "⚠️  Arquivo não encontrado: $old"
    fi
}

# Renomeações (14 arquivos)
rename_file "MOC_-_Atenção_&_Cognição.md" "MOC_Atencao_Cognicao.md"
rename_file "Moc_-_Ciência_&_Filosofia_Da_Realidade.md" "MOC_Ciencia_Filosofia_Realidade.md"
rename_file "MOC_-_Consciência_&_Desenvolvimento.md" "MOC_Consciencia_Desenvolvimento.md"
rename_file "MOC_-_Criação_De_Conteúdo.md" "MOC_Criacao_Conteudo.md"
rename_file "MOC_-_Decisão_&_Sabedoria.md" "MOC_Decisao_Sabedoria.md"
rename_file "MOC_-_Episódios_Vl.md" "MOC_Episodios_VL.md"
rename_file "MOC_-_Filosofia_&_Espiritualidade.md" "MOC_Filosofia_Espiritualidade.md"
rename_file "Moc_-_Ia_&_Ferramentas_Digitais.md" "MOC_IA_Ferramentas_Digitais.md"
rename_file "MOC_-_Maestria_&_Genialidade.md" "MOC_Maestria_Genialidade.md"
rename_file "MOC_-_Marketing_&_Copy.md" "MOC_Marketing_Copy.md"
rename_file "Moc_-_Negócios_&_Empreendedorismo.md" "MOC_Negocios_Empreendedorismo.md"
rename_file "MOC_-_Pkm_&_Segundo_Cérebro.md" "MOC_PKM_Segundo_Cerebro.md"
rename_file "MOC_-_Psicologia_&_Comportamento.md" "MOC_Psicologia_Comportamento.md"
rename_file "Moc_-_Vida_&_Propósito.md" "MOC_Vida_Proposito.md"

echo ""
echo "✅ Renomeação concluída!"
echo ""
echo "📋 Próximos passos:"
echo "1. Verificar links quebrados nos arquivos"
echo "2. Atualizar referências em outros documentos"
echo "3. Validar MOC_SEGUNDO_CEREBRO_MASTER.md"
echo ""
echo "🏛️ Padrões mantidos. Qualidade > Velocidade."
