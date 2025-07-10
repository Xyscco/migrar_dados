dados = [
    {
        "NomeTabela": "ACESSOGRUPO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "ACESSOUSUARIO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "ADMINISTRADORACARTAO",
        "WhereSQL": "",
        "Generator": "GEN_ADMINISTRADORACARTAO",
        "GeneratorField": "CODADMINISTRADORACARTAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "ALIQUOTAICMS",
        "WhereSQL": "",
        "Generator": "GEN_ALIQUOTAICMS",
        "GeneratorField": "CODALIQUOTAICMS",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "BAIRRO",
        "WhereSQL": "",
        "Generator": "GEN_BAIRRO",
        "GeneratorField": "CODBAIRRO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "BANCO",
        "WhereSQL": "",
        "Generator": "GEN_BANCO",
        "GeneratorField": "CODBANCO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CAIXA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CAIXA",
        "GeneratorField": "CODCAIXA",
        "CamposFormatados": [
            {
                "CODCAIXA": "'001' || SUBSTRING(a.CODCAIXA FROM 4 FOR 6)"
            },
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 6)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CAIXAMOVAJUSDIFLANCAMENTOS",
        "WhereSQL": "SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            },
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "CAIXAMOVAJUSTEDIFERENCA",
        "WhereSQL": "SUBSTRING(CODCAIXAMOVIMENTACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "CASE a.CODLANCAMENTOCONTAFINANCEIRA WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0') END "
            },
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "CAIXAMOVAJUSTEDIFERENCA",
        "WhereSQL": "SUBSTRING(CODCAIXAMOVIMENTACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "CASE a.CODLANCAMENTOCONTAFINANCEIRA WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0') END"
            },
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "CAIXAMOVIMENTACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CAIXAMOVIMENTACAO",
        "GeneratorField": "CODCAIXAMOVIMENTACAO",
        "CamposFormatados": [
            {
                "CODCAIXA": "'001' || SUBSTRING(a.CODCAIXA FROM 4 FOR 6)"
            },
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 9)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CAIXAMOVIMENTACAOOBS",
        "WhereSQL": "SUBSTRING(CODCAIXAMOVIMENTACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCAIXAMOVIMENTACAO": "'001' || SUBSTRING(CODCAIXAMOVIMENTACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "CAIXARESPONSAVELOPERACAO",
        "WhereSQL": "SUBSTRING(CODCAIXA FROM 1 FOR 3) = :CodOrg ",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCAIXA": "'001' || SUBSTRING(a.CODCAIXA FROM 4 FOR 6)"
            }
        ]
    },
    {
        "NomeTabela": "CARTAOFINANCEIRO",
        "WhereSQL": "",
        "Generator": "GEN_CARTAOFINANCEIRO",
        "GeneratorField": "CODCARTAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CHEQUECLIENTE",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CHEQUECLIENTE",
        "GeneratorField": "CODCHEQUE",
        "CamposFormatados": [
            {
                "CODCHEQUE": "'001' || SUBSTRING(a.CODCHEQUE FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "CIDADE",
        "WhereSQL": "",
        "Generator": "GEN_CIDADE",
        "GeneratorField": "CODCIDADE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CLIENTE",
        "WhereSQL": "",
        "Generator": "GEN_CLIENTE",
        "GeneratorField": "CODCLIENTE",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CLIENTEBLOB",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CLIENTECARTAOCONFIG",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CLIENTECOBRANCA",
        "WhereSQL": "substring(a.CODCLIENTE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CLIENTEDEPENDENTE",
        "WhereSQL": "substring(a.CODCLIENTE FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_DEPENDENTE",
        "GeneratorField": "CODDEPENDENTE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CLIENTEGRUPO",
        "WhereSQL": "",
        "Generator": "GEN_CLIENTEGRUPO",
        "GeneratorField": "CODGRUPOCLIENTE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CLOSEUPCONFIGURACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "COBRANCACARTAATRASO",
        "WhereSQL": "substring(a.CODCARTACOBRANCA FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_COBRANCACARTAATRASO",
        "GeneratorField": "CODCARTACOBRANCA",
        "CamposFormatados": [
            {
                "CODCARTACOBRANCA": "'001' || substring(a.CODCARTACOBRANCA FROM 4 FOR 5)"
            }
        ]
    },
    {
        "NomeTabela": "COMPRA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_COMPRA",
        "GeneratorField": "CODCOMPRA",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODNFE": "case a.CODNFE WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0') END"
            },
            {
                "CODPEDIDO": "case a.CODPEDIDO WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODPEDIDO FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PEDIDO_CODPEDIDO c WHERE C2 < CAST(substring(a.CODPEDIDO FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPEDIDO)-3, '0') END "
            }
        ]
    },
    {
        "NomeTabela": "COMPRAICMS",
        "WhereSQL": "a.CODCOMPRA IN (SELECT b.CODCOMPRA FROM COMPRA b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "GEN_COMPRAICMS",
        "GeneratorField": "CODCOMPRAICMS",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "COMPRALOTE",
        "WhereSQL": "a.CODCOMPRA IN (SELECT b.CODCOMPRA FROM COMPRA b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "COMPRALOTEVENCIMENTO",
        "WhereSQL": "a.CODCOMPRA IN (SELECT b.CODCOMPRA FROM COMPRA b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "COMPRAPRODUTO",
        "WhereSQL": "a.CODCOMPRA IN (SELECT b.CODCOMPRA FROM COMPRA b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "CONCILIARCARTAOCONFIG",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CONFIGURACAOCAIXAVENDAACERTO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTACAIXAVENDACON": "case a.CODCONTACAIXAVENDACON WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAVENDACON FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAACERTOCARTAO": "case a.CODCONTACAIXAACERTOCARTAO WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAACERTOCARTAO FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAVENDACRE": "case a.CODCONTACAIXAVENDACRE WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAVENDACRE FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAACERTOPILLAS": "case a.CODCONTACAIXAACERTOPILLAS WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAACERTOPILLAS FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAVENDADIN": "case a.CODCONTACAIXAVENDADIN WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAVENDADIN FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAACERTOCHEQUE": "case a.CODCONTACAIXAACERTOCHEQUE WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAACERTOCHEQUE FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAVENDACHE": "case a.CODCONTACAIXAVENDACHE WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAVENDACHE FROM 4 FOR 7) END"
            },
            {
                "CODCONTACAIXAACERTOCONVENIO": "case a.CODCONTACAIXAACERTOCONVENIO WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAACERTOCONVENIO FROM 4 FOR 7)  END"
            },
            {
                "CODCONTACAIXAVENDAPIL": "case a.CODCONTACAIXAVENDAPIL WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCONTACAIXAVENDAPIL FROM 4 FOR 7) END"
            }
        ]
    },
    {
        "NomeTabela": "CONFIGURACAOCHEQUEFICTICIO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONFIGURACAOPARCELASCONDPAGTO",
        "WhereSQL": "",
        "Generator": "GEN_CONFIGPARCELASCONDPAGTO",
        "GeneratorField": "CODCONFPARCCONDPAGTO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONFIGURACAOSERASA",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONFIGURACAOTERMINAL",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONTA",
        "WhereSQL": "SUBSTRING(a.CODCONTA FROM 1 FOR 3) = '000' OR SUBSTRING(a.CODCONTA FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_CONTA",
        "GeneratorField": "CODCONTA",
        "CamposFormatados": [
            {
                "CODCAIXA": "case a.CODCAIXA WHEN '' THEN '' ELSE '001' || substring(a.CODCAIXA FROM 4 FOR 6) END"
            },
            {
                "CODCONTA": "iif( SUBSTRING(a.CODCONTA FROM 1 FOR 3) = '000', a.CODCONTA, '001' || SUBSTRING(a.CODCONTA FROM 4 FOR 7))"
            },
            {
                "CODORGANIZACAO": "case a.CODORGANIZACAO WHEN '' THEN '' ELSE '001' END"
            }
        ]
    },
    {
        "NomeTabela": "CONTACORRENTE",
        "WhereSQL": "",
        "Generator": "GEN_CONTACORRENTE",
        "GeneratorField": "CODCONTACORRENTE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONTADOR",
        "WhereSQL": "",
        "Generator": "GEN_CONTADOR",
        "GeneratorField": "CODCONTADOR",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CONTAPAGAR",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CONTAPAGAR",
        "GeneratorField": "CODCONTAPAGAR",
        "CamposFormatados": [
            {
                "CODCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(CODCONTAPAGAR FROM 4 FOR 7) AS integer)+(Iif((SUBSTRING(CODCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODCONTAPAGAR FROM 4 FOR 7) AS integer)) FROM CONTAPAGAR c2), 0)), 7, '0')"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODORGANIZACAOCADASTRO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CONTAPAGARCOMPRA",
        "WhereSQL": "a.CODCOMPRA IN (SELECT b.CODCOMPRA FROM COMPRA b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            },
            {
                "CODCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(CODCONTAPAGAR FROM 4) AS integer)+(Iif((SUBSTRING(CODCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODCONTAPAGAR FROM 4) AS integer)) FROM CONTAPAGAR c2), 0)), 7, '0')"
            }
        ]
    },
    {
        "NomeTabela": "CONTAPAGARDEVOLUCAOCOMPRA",
        "WhereSQL": "a.CODCONTAPAGAR in (SELECT b.CODCONTAPAGAR FROM CONTAPAGAR b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNOTACREDITO": "'001' || substring(a.CODNOTACREDITO FROM 4 FOR 7)"
            },
            {
                "CODCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(CODCONTAPAGAR FROM 4 FOR 7) AS integer)+(Iif((SUBSTRING(CODCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODCONTAPAGAR FROM 4 FOR 7) AS integer)) FROM CONTAPAGAR c2), 0)), 7, '0')"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBER",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CONTARECEBER",
        "GeneratorField": "CODCONTARECEBER",
        "CamposFormatados": [
            {
                "CODCONTARECEBER": "'001' || substring(a.CODCONTARECEBER FROM 4 FOR 12)"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            },
            {
                "CODCONTARECEBERQUITACAO": "case a.CODCONTARECEBERQUITACAO WHEN '' THEN '' ELSE '001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12) END"
            },
            {
                "DTVENCIMENTO": "case DTVENCIMENTO WHEN NULL THEN NULL ELSE EXTRACT(DAY FROM DTVENCIMENTO) || '.' || EXTRACT(MONTH FROM DTVENCIMENTO) || '.' || EXTRACT(YEAR FROM DTVENCIMENTO) END "
            },
            {
                "DTCANCELAMENTO": "case DTCANCELAMENTO WHEN NULL THEN NULL ELSE  EXTRACT(DAY FROM DTCANCELAMENTO) || '.' || EXTRACT(MONTH FROM DTCANCELAMENTO) || '.' || EXTRACT(YEAR FROM DTCANCELAMENTO)  END"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBERCOBRANCAENDERECO",
        "WhereSQL": "substring(a.CODCONTARECEBER FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTARECEBER": "'001' || substring(a.CODCONTARECEBER FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBERQUITACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_CONTARECEBERQUITACAO",
        "GeneratorField": "CODCONTARECEBERQUITACAO",
        "CamposFormatados": [
            {
                "CODCONTARECEBERQUITACAO": "'001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12)"
            },
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBERQUITACAOCARTAO",
        "WhereSQL": "substring(a.CODCONTARECEBERQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTARECEBERQUITACAO": "'001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBERQUITACAOCHEQUE",
        "WhereSQL": "substring(a.CODCONTARECEBERQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTARECEBERQUITACAO": "'001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "CONTARECEBERQUITACAOITEM",
        "WhereSQL": "substring(a.CODCONTARECEBER FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTARECEBERQUITACAO": "'001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12)"
            },
            {
                "CODCONTARECEBER": "'001' || substring(a.CODCONTARECEBER FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "CONVENIO",
        "WhereSQL": "",
        "Generator": "GEN_CONVENIO",
        "GeneratorField": "CODCONVENIO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CURVAABCCLASSIFICACAO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "CURVAABCCONFIGURACAO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "DAVVENDA",
        "WhereSQL": "a.CODORGANIZACAOVENDA = :CodOrg",
        "Generator": "GEN_DAVVENDA",
        "GeneratorField": "CODDAVVENDA",
        "CamposFormatados": [
            {
                "NUMERODAV": "'001' || substring(a.NUMERODAV FROM 4 FOR 13)"
            },
            {
                "CODECF": "CASE a.CODECF WHEN '' THEN '' ELSE '001' || substring(a.CODECF FROM 4 FOR 8) END"
            },
            {
                "CODORGANIZACAOVENDA": "'001'"
            },
            {
                "CODDAVVENDA": "'001' || substring(a.CODDAVVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "DAVVENDAPRODUTO",
        "WhereSQL": "substring(a.CODDAVVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "NUMERODAV": "'001' || substring(a.NUMERODAV FROM 4 FOR 13)"
            },
            {
                "CODDAVVENDA": "'001' || substring(a.CODDAVVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "DESCONTOPROGRESSIVOPRODUTO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "DEVOLUCAOCOMPRALOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODNOTACREDITO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNOTACREDITO": "'001' || substring(a.CODNOTACREDITO FROM 4 FOR 7)"
            }
        ]
    },
    {
        "NomeTabela": "DEVOLUCAOCOMPRANOTACREDITO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_DEVOLUCAOCOMPRA",
        "GeneratorField": "CODNOTACREDITO",
        "CamposFormatados": [
            {
                "CODNOTACREDITO": "'001' || substring(a.CODNOTACREDITO FROM 4 FOR 7)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "DEVOLUCAOCOMPRAPRODUTO",
        "WhereSQL": "substring(a.CODNOTACREDITO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNOTACREDITO": "'001' || substring(a.CODNOTACREDITO FROM 4 FOR 7)"
            },
            {
                "CODCOMPRA": "'001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "DEVOLUCAOPRODUTOVENDIDO",
        "WhereSQL": "a.CODORGANIZACAORESPONSAVEL = :CodOrg",
        "Generator": "GEN_DEVOLUCAOPRODUTOVENDIDO",
        "GeneratorField": "CODDEVOLUCAOPRODUTOVENDIDO",
        "CamposFormatados": [
            {
                "CODORGANIZACAORESPONSAVEL": "'001'"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            },
            {
                "CODDEVOLUCAOPRODUTOVENDIDO": "'001' || substring(a.CODDEVOLUCAOPRODUTOVENDIDO FROM 4 FOR 10)"
            },
            {
                "CODNFE": "case a.CODNFE WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0') END"
            }
        ]
    },
    {
        "NomeTabela": "DEVPRODVENDLOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODDEVOLUCAOPRODUTOVENDIDO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODDEVOLUCAOPRODUTOVENDIDO": "'001' || substring(a.CODDEVOLUCAOPRODUTOVENDIDO FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "ECF",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_ECF",
        "GeneratorField": "CODECF",
        "CamposFormatados": [
            {
                "CODECF": "'001' || SUBSTRING(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "ENTREGA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_ENTREGA",
        "GeneratorField": "CODENTREGA",
        "CamposFormatados": [
            {
                "CODENTREGA": "'001' || SUBSTRING(a.CODENTREGA FROM 4 FOR 12)"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODCAIXAMOVIMENTACAOSAIDA": "CASE a.CODCAIXAMOVIMENTACAOSAIDA WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCAIXAMOVIMENTACAOSAIDA FROM 4 FOR 8) END"
            },
            {
                "CODLANCAMENTOCONTAFINANTROCO": "CASE a.CODLANCAMENTOCONTAFINANTROCO WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODLANCAMENTOCONTAFINANTROCO FROM 4 FOR 8) END"
            },
            {
                "CODCAIXAMOVIMENTACAOCHEGADA": "CASE a.CODCAIXAMOVIMENTACAOCHEGADA WHEN '' THEN '' ELSE '001' || SUBSTRING(a.CODCAIXAMOVIMENTACAOCHEGADA FROM 4 FOR 8) END"
            }
        ]
    },
    {
        "NomeTabela": "ENTREGALANCAMENTOCONTAFINAN",
        "WhereSQL": "substring(a.CODENTREGA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODENTREGA": "'001' || SUBSTRING(a.CODENTREGA FROM 4 FOR 12)"
            },
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "ENTREGAVENDA",
        "WhereSQL": "substring(a.CODENTREGA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODENTREGA": "'001' || SUBSTRING(a.CODENTREGA FROM 4 FOR 12)"
            },
            {
                "CODVENDA": "'001' || SUBSTRING(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "ESTOQUE",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "ESTOQUEECF",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "ESTOQUELOTEVENCIMENTO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_ESTOQUELOTEVENCIMENTO",
        "GeneratorField": "CODESTOQUELOTE",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODESTOQUELOTE": "'001' || lpad(CAST(SUBSTRING(a.CODESTOQUELOTE FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LOTE_CODESTOQUELOTE c WHERE C2 < CAST(substring(a.CODESTOQUELOTE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODESTOQUELOTE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "ESTOQUELOTEVENCIMENTOETIQUETA",
        "WhereSQL": "substring(a.CODESTOQUELOTE from 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODESTOQUELOTE": "'001' || substring(a.CODESTOQUELOTE from 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "ESTOQUEREGULADOR",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "FABRICANTE",
        "WhereSQL": "",
        "Generator": "GEN_FABRICANTE",
        "GeneratorField": "CODFABRICANTE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FARMACIAPOPULARAUTORIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_FARMACIAPOPULARAUTORIZACAO",
        "GeneratorField": "CODFARMPOPAUTORIZACAO",
        "CamposFormatados": [
            {
                "CODFARMPOPAUTORIZACAO": "'001' || substring(a.CODFARMPOPAUTORIZACAO FROM 4 FOR 10)"
            },
            {
                "CODCLIENTE": "case a.CODCLIENTE WHEN '' THEN '' ELSE '001' || substring(a.CODCLIENTE FROM 4 FOR 10) END "
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "FARMACIAPOPULARAUTORIZACAOITEM",
        "WhereSQL": "substring(a.CODFARMPOPAUTORIZACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFARMPOPAUTORIZACAO": "'001' || substring(a.CODFARMPOPAUTORIZACAO FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "FARMACIAPOPULARLOGIN",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "FAVORECIDO",
        "WhereSQL": "",
        "Generator": "GEN_FAVORECIDO",
        "GeneratorField": "CODFAVORECIDO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FISCALCUPOMFISCAL",
        "WhereSQL": " substring(a.CODFISCALCUPOMFISCAL FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALCUPOMFISCAL",
        "GeneratorField": "CODFISCALCUPOMFISCAL",
        "CamposFormatados": [
            {
                "CODFISCALCUPOMFISCAL": "'001' || substring(a.CODFISCALCUPOMFISCAL FROM 4 FOR 12)"
            },
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALDEMAISDOCUMENTOS",
        "WhereSQL": "substring(a.CODFISCALDEMAISDOCUMENTOS FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALDEMAISDOCUMENTOS",
        "GeneratorField": "CODFISCALDEMAISDOCUMENTOS",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODFISCALDEMAISDOCUMENTOS": "'001' || substring(a.CODFISCALDEMAISDOCUMENTOS FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALDETALHECUPOMFISCAL",
        "WhereSQL": "substring(a.CODFISCALDETALHECUPOMFISCAL FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALDETALHECUPOMFISCAL",
        "GeneratorField": "CODFISCALDETALHECUPOMFISCAL",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODFISCALDETALHECUPOMFISCAL": "'001' || substring(a.CODFISCALDETALHECUPOMFISCAL FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALMEIOPAGAMENTO",
        "WhereSQL": "substring(a.CODFISCALMEIOPAGAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALMEIOPAGAMENTO",
        "GeneratorField": "CODFISCALMEIOPAGAMENTO",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODFISCALMEIOPAGAMENTO": "'001' || substring(a.CODFISCALMEIOPAGAMENTO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALMEIOPAGAMENTOCARTAO",
        "WhereSQL": "substring(a.CODFISCALMEIOPAGAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALMEIOPAGAMENTOCARTAO",
        "GeneratorField": "CODFISCALMEIOPAGAMENTOCARTAO",
        "CamposFormatados": [
            {
                "CODFISCALMEIOPAGAMENTO": "'001' || substring(a.CODFISCALMEIOPAGAMENTO FROM 4 FOR 12)"
            },
            {
                "CODFISCALMEIOPAGAMENTOCARTAO": "'001' || substring(a.CODFISCALMEIOPAGAMENTOCARTAO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALMOVIM_ECF_REDUCAOZ",
        "WhereSQL": "substring(a.CODFISCALMOVIMECF FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_FISCALMOVIMECF",
        "GeneratorField": "CODFISCALMOVIMECF",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODFISCALMOVIMECF": "'001' || substring(a.CODFISCALMOVIMECF FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "FISCALMOVIM_ECF_REDUCAOZDETALHE",
        "WhereSQL": "substring(a.CODFISCALMOVIMECF FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODECF": "'001' || substring(a.CODECF FROM 4 FOR 8)"
            },
            {
                "CODFISCALMOVIMECF": "'001' || substring(a.CODFISCALMOVIMECF FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "FORMAPAGAMENTO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FORNECEDOR",
        "WhereSQL": "",
        "Generator": "GEN_FORNECEDOR",
        "GeneratorField": "CODFORNECEDOR",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FORNECEDORFABRICANTE",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FORNECEDORORGANIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "FORNECEDORPRODUTO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FUNCICONTACORRENTELANC",
        "WhereSQL": "A.CODORGANIZACAOLANCAMENTO = :CodOrg",
        "Generator": "GEN_FUNCICONTACORRENTELANC",
        "GeneratorField": "CODFUNCICONTACORRLANC",
        "CamposFormatados": [
            {
                "CODORGANIZACAOLANCAMENTO": "'001'"
            },
            {
                "CODFUNCICONTACORRLANC": "'001' || SUBSTRING(a.CODFUNCICONTACORRLANC FROM 4 FOR 9)"
            },
            {
                "OBSERVACAO": "'VENDA : 001' || SUBSTRING(a.OBSERVACAO FROM 12 FOR 100)"
            }
        ]
    },
    {
        "NomeTabela": "FUNCICONTACORRENTEQUITACAO",
        "WhereSQL": "A.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_FUNCICONTACORRENTEQUITACAO",
        "GeneratorField": "CODFUNCICONTACORRENTEQUITACAO",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODFUNCICONTACORRENTEQUITACAO": "'001' || SUBSTRING(a.CODFUNCICONTACORRENTEQUITACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "FUNCICONTACORRENTEQUITACAOLANC",
        "WhereSQL": "substring(a.CODFUNCICONTACORRENTEQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFUNCICONTACORRLANC": "'001' || SUBSTRING(a.CODFUNCICONTACORRLANC FROM 4 FOR 9)"
            },
            {
                "CODFUNCICONTACORRENTEQUITACAO": "'001' || SUBSTRING(a.CODFUNCICONTACORRENTEQUITACAO FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "FUNCICONTACORRLANCTIPO",
        "WhereSQL": "",
        "Generator": "GEN_FUNCICONTACORRLANCTIPO",
        "GeneratorField": "CODFUNCICONTACORRLANCTIPO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "FUNCICTACORRQUITACAOLANCCTAFIN",
        "WhereSQL": "substring(a.CODFUNCICONTACORRENTEQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFUNCICONTACORRENTEQUITACAO": "'001' || SUBSTRING(a.CODFUNCICONTACORRENTEQUITACAO FROM 4 FOR 9)"
            },
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "FUNCICTACORRQUITAJUSTADIANTAMEN",
        "WhereSQL": "substring(a.CODFUNCICONTACORRENTEQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFUNCICONTACORRENTEQUITACAO": "'001' || SUBSTRING(a.CODFUNCICONTACORRENTEQUITACAO FROM 4 FOR 9)"
            },
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "FUNCICTACORRQUITAJUSTADIANTAMEN",
        "WhereSQL": "substring(a.CODFUNCICONTACORRENTEQUITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFUNCICONTACORRENTEQUITACAO": "'001' || SUBSTRING(a.CODFUNCICONTACORRENTEQUITACAO FROM 4 FOR 9)"
            },
            {
                "CODFUNCICONTACORRLANC": "'001' || SUBSTRING(a.CODFUNCICONTACORRLANC FROM 4 FOR 9)"
            }
        ]
    },
    {
        "NomeTabela": "FUNCIONARIO",
        "WhereSQL": "",
        "Generator": "GEN_FUNCIONARIO",
        "GeneratorField": "CODFUNCIONARIO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPO",
        "WhereSQL": "",
        "Generator": "GEN_GRUPO",
        "GeneratorField": "CODGRUPO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPOCOMISSAO",
        "WhereSQL": "",
        "Generator": "GEN_GRUPOCOMISSAO",
        "GeneratorField": "CODGRUPOCOMISSAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPOICMS",
        "WhereSQL": "",
        "Generator": "GEN_GRUPOICMS",
        "GeneratorField": "CODGRUPOICMS",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPOPRODUTO",
        "WhereSQL": "",
        "Generator": "GEN_GRUPOPRODUTO",
        "GeneratorField": "CODGRUPOPRODUTO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPOREMARCACAOPRECO",
        "WhereSQL": "",
        "Generator": "GEN_GRUPOREMARCACAOPRECO",
        "GeneratorField": "CODGRUPOREMARCACAOPRECO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "GRUPOUSUARIO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "IBPT",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "IFARMACONFIGURACAO",
        "WhereSQL": "A.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "IFARMAMOVIMENTACAO",
        "WhereSQL": "A.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "IMENDESCONFIGURACAO",
        "WhereSQL": "A.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "IMENDESTRIBUTOS",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "INESTRAFTP",
        "WhereSQL": "A.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "INESTRALOG",
        "WhereSQL": "",
        "Generator": "GEN_INESTRALOG",
        "GeneratorField": "CODINESTRALOG",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "INVENTARIO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_INVENTARIO",
        "GeneratorField": "CODINVENTARIO",
        "CamposFormatados": [
            {
                "CODINVENTARIO": "'001' || substring(a.CODINVENTARIO from 4 FOR 8)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "INVENTARIONOVO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_INVENTARIONOVO",
        "GeneratorField": "CODINVENTARIONOVO",
        "CamposFormatados": [
            {
                "CODINVENTARIONOVO": "'001' || substring(a.CODINVENTARIONOVO from 4 FOR 10)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "INVENTARIONOVOLOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODINVENTARIONOVO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODINVENTARIONOVO": "'001' || substring(a.CODINVENTARIONOVO from 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "INVENTARIOPRODUTOSELECIONADO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODINVENTARIO": "'001' || substring(a.CODINVENTARIO from 4 FOR 8)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "LANCAMENTOCONTAFINANCEIRA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_LANCAMENTOCONTAFINANCEIRA",
        "GeneratorField": "CODLANCAMENTOCONTAFINANCEIRA",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            },
            {
                "CODIGOOPERACAOGERADORA": "'001' || substring(a.CODIGOOPERACAOGERADORA FROM 4 FOR 20)"
            },
            {
                "CODCAIXAMOVIMENTACAO": "case a.CODCAIXAMOVIMENTACAO WHEN '' THEN '' ELSE '001' || substring(a.CODCAIXAMOVIMENTACAO FROM 4 FOR 9) END"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODCONTA": "case a.CODCONTA WHEN '' THEN '' ELSE '001' || substring(a.CODCONTA FROM 4 FOR 7) END"
            },
            {
                "CODLANCAMENTOCONTAFINANESTORNO": "case a.CODLANCAMENTOCONTAFINANESTORNO WHEN '' THEN '' ELSE '001' || substring(a.CODLANCAMENTOCONTAFINANESTORNO FROM 4 FOR 10) END"
            }
        ]
    },
    {
        "NomeTabela": "LANCAMENTOCONTAFINANPLANOCONTA",
        "WhereSQL": "substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            },
            {
                "CODPLANOCONTA": "'001' || substring(a.CODPLANOCONTA FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "LANCAMENTODADOSCLIENTE",
        "WhereSQL": "substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "LANCAMENTOUNIFARDOSOPERESPELHO",
        "WhereSQL": "substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "LICITACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_LICITACAO",
        "GeneratorField": "CODLICITACAO",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODLICITACAO": "'001' || substring(a.CODLICITACAO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "LICITACAOPEDIDO",
        "WhereSQL": "substring(a.CODLICITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPEDIDO": "'001' || lpad(CAST(SUBSTRING(a.CODPEDIDO FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PEDIDO_CODPEDIDO c WHERE C2 < CAST(substring(a.CODPEDIDO FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPEDIDO)-3, '0')"
            },
            {
                "CODLICITACAO": "'001' || substring(a.CODLICITACAO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "LICITACAOPRODUTO",
        "WhereSQL": "substring(a.CODLICITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLICITACAO": "'001' || substring(a.CODLICITACAO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "LICITACAORESPOSTA",
        "WhereSQL": "substring(a.CODLICITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLICITACAO": "'001' || substring(a.CODLICITACAO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "LICITACAOVALORTOTAL",
        "WhereSQL": "substring(a.CODLICITACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLICITACAO": "'001' || substring(a.CODLICITACAO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "LINHA",
        "WhereSQL": "",
        "Generator": "GEN_LINHA",
        "GeneratorField": "CODLINHA",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "LIVRO",
        "WhereSQL": "",
        "Generator": "GEN_LIVRO",
        "GeneratorField": "CODLIVRO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "LOGCONSULTA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "LOGINAUTORIZADO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "MARGEMLUCRO",
        "WhereSQL": "",
        "Generator": "GEN_MARGEMLUCRO",
        "GeneratorField": "CODMARGEMLUCRO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "MEDICOCRM",
        "WhereSQL": "",
        "Generator": "GEN_MEDICOCRM",
        "GeneratorField": "CODMEDICO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "MEDICOESPECIALIDADE",
        "WhereSQL": "",
        "Generator": "GEN_MEDICOESPECIALIDADE",
        "GeneratorField": "CODESPECIALIDADE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "NFCECONFIGURACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "NFCEFORMAPAGAMENTO",
        "WhereSQL": "substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFCESERIE",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "NFE",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_NFE",
        "GeneratorField": "CODNFE",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFECONFIGURACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "NFEDESTINATARIO",
        "WhereSQL": "a.CODDESTINATARIO = :CodOrg OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODDESTINATARIO": "iif(a.CODDESTINATARIO = :CodOrg , '001', a.CODDESTINATARIO)"
            },
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEDOCREFERENCIADO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEDUPLICATA",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEEMITENTE",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "case a.CODORGANIZACAO WHEN :CodOrg THEN '001' ELSE a.CODORGANIZACAO END"
            },
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEENDERECO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEINFOADICIONAIS",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEINUTILIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "001"
            },
            {
                "CODINUTILIZACAO": "'001' || substring(a.CODINUTILIZACAO FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "NFEOPERACAOGERADORA",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            },
            {
                "CODOPERACAOGERADORA": "'001' || SUBSTRING(CODOPERACAOGERADORA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "NFEPRODUTO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEPRODUTOMEDICAMENTO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEPRODUTOTRIBUTO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFERESPONSAVELTECNICO",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFESERIE",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "NFETOTAIS",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "NFEXMLRESP",
        "WhereSQL": "(a.CODNFE in (SELECT b.CODNFE FROM NFEDESTINATARIO b WHERE b.CODDESTINATARIO = :CodOrg)) OR substring(a.CODNFE FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODNFE": "'001' || lpad(CAST(SUBSTRING(a.CODNFE FROM 4 FOR 15) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM NFE_CODNFE c WHERE C2 < CAST(substring(a.CODNFE FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODNFE)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "ORGANIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_ORGANIZACAO",
        "GeneratorField": "CODORGANIZACAO",
        "CamposFormatados": [
            {
                "CODTABELAICMS": "'00101'"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PARCEIRO",
        "WhereSQL": "substring(a.CODPARCEIRO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_PARCEIRO",
        "GeneratorField": "CODPARCEIRO",
        "CamposFormatados": [
            {
                "CODPARCEIRO": "'001' || substring(a.CODPARCEIRO FROM 4 FOR 7)"
            }
        ]
    },
    {
        "NomeTabela": "PARCEIROTROCALOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODPARCEIROTROCAPRODUTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPARCEIROTROCAPRODUTO": "'001' || substring(a.CODPARCEIROTROCAPRODUTO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "PARCEIROTROCAPRODUTO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PARCEIROTROCAPRODUTO",
        "GeneratorField": "CODPARCEIROTROCAPRODUTO",
        "CamposFormatados": [
            {
                "CODPARCEIROTROCAPRODUTO": "'001' || substring(a.CODPARCEIROTROCAPRODUTO FROM 4 FOR 8)"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODPARCEIRO": "'001' || substring(a.CODPARCEIRO FROM 4 FOR 7)"
            }
        ]
    },
    {
        "NomeTabela": "PEDIDO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PEDIDOS",
        "GeneratorField": "CODPEDIDO",
        "CamposFormatados": [
            {
                "CODPEDIDO": "'001' || lpad(CAST(SUBSTRING(a.CODPEDIDO FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PEDIDO_CODPEDIDO c WHERE C2 < CAST(substring(a.CODPEDIDO FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPEDIDO)-3, '0')"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PEDIDOPRODUTO",
        "WhereSQL": "substring(a.CODPEDIDO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPEDIDO": "'001' || lpad(CAST(SUBSTRING(a.CODPEDIDO FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PEDIDO_CODPEDIDO c WHERE C2 < CAST(substring(a.CODPEDIDO FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPEDIDO)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "PHARMASYSTEMAUTORIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PHARMASYSTEMAUTORIZACAO",
        "GeneratorField": "CODPHARMASYSTEMAUTORIZACAO",
        "CamposFormatados": [
            {
                "CODPHARMASYSTEMAUTORIZACAO": "'001' || substring(a.CODPHARMASYSTEMAUTORIZACAO FROM 4 FOR 10)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PHARMASYSTEMAUTORIZACAOITEM",
        "WhereSQL": "substring(a.CODPHARMASYSTEMAUTORIZACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPHARMASYSTEMAUTORIZACAO": "'001' || substring(a.CODPHARMASYSTEMAUTORIZACAO FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PHARMASYSTEMIDENTIFICACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PHARMASYSTEMAUTORIZACAO",
        "GeneratorField": "CODPHARMASYSTEMIDENTIFICACAO",
        "CamposFormatados": [
            {
                "CODPHARMASYSTEMIDENTIFICACAO": "'001' || substring(a.CODPHARMASYSTEMIDENTIFICACAO FROM 4 FOR 10)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PILLASCONFIGURACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PLANOCONTA",
        "WhereSQL": "",
        "Generator": "GEN_PLANOCONTA",
        "GeneratorField": "CODPLANOCONTA",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRECONSULTACPFCNPJ",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PREVENDA",
        "WhereSQL": "a.CODORGANIZACAOPREVENDA = :CodOrg",
        "Generator": "GEN_PREVENDA",
        "GeneratorField": "CODPREVENDA",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 15)"
            },
            {
                "CODVENDA": "case a.CODVENDA WHEN '' THEN '' ELSE '001' || substring(a.CODVENDA FROM 4 FOR 15) END"
            },
            {
                "CODSESSAOECFTEF": "case a.CODSESSAOECFTEF WHEN '' THEN '' ELSE '001' || substring(a.CODSESSAOECFTEF FROM 4 FOR 15) END"
            },
            {
                "CODDAVVENDA": "case a.CODDAVVENDA WHEN '' THEN '' ELSE '001' || substring(a.CODDAVVENDA FROM 4 FOR 13) END"
            },
            {
                "CODPREVENDAMESCLADA": "case a.CODPREVENDAMESCLADA WHEN '' THEN '' ELSE '001' || substring(a.CODPREVENDAMESCLADA FROM 4 FOR 15) END"
            },
            {
                "CODORGANIZACAOPREVENDA": "'001'"
            },
            {
                "CODECF": "case a.CODECF WHEN '' THEN '' ELSE '001' || substring(a.CODECF FROM 4 FOR 8) END"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDACARTAOLANCAMENTO",
        "WhereSQL": "substring(a.CODPREVENDALANCAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_PREVENDACARTAOLANCAMENTO",
        "GeneratorField": "CODPREVENDALANCAMENTO",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 15)"
            },
            {
                "CODPREVENDALANCAMENTO": "'001' || substring(a.CODPREVENDALANCAMENTO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDACHEQUELANCAMENTO",
        "WhereSQL": "substring(a.CODPREVENDALANCAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_PREVENDACHEQUELANCAMENTO",
        "GeneratorField": "CODPREVENDALANCAMENTO",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 15)"
            },
            {
                "CODPREVENDALANCAMENTO": "'001' || substring(a.CODPREVENDALANCAMENTO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDACONTARECEBER",
        "WhereSQL": "substring(a.CODPREVENDACONTARECEBER FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_PREVENDACONTARECEBER",
        "GeneratorField": "CODPREVENDACONTARECEBER",
        "CamposFormatados": [
            {
                "CODPREVENDACONTARECEBER": "'001' || substring(a.CODPREVENDACONTARECEBER FROM 4 FOR 10)"
            },
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDACHEQUELANCAMENTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDAFINANCIAMENTOCONDPAGTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDAFORMAPAGAMENTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDALOTE",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDALOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDAMODOUSO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDAMODOUSO": "'001' || substring(a.CODPREVENDAMODOUSO FROM 4 FOR 12)"
            },
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDAPILLASLANCAMENTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDAPRODUTO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDARECEITAPRODCONTROLADO",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_PREVENDARECEITAPRODCONTROL",
        "GeneratorField": "CODRECEITUARIO",
        "CamposFormatados": [
            {
                "CODRECEITUARIO": "'001' || substring(a.CODRECEITUARIO FROM 4 FOR 12)"
            },
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDARECEITAPRODCONTROLITEM",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODRECEITUARIO": "'001' || substring(a.CODRECEITUARIO FROM 4 FOR 12)"
            },
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PREVENDARESTRICOES",
        "WhereSQL": "substring(a.CODPREVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPREVENDA": "'001' || substring(a.CODPREVENDA FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PRINCIPIOATIVO",
        "WhereSQL": "",
        "Generator": "GEN_PRINCIPIOATIVO",
        "GeneratorField": "CODPRINCIPIOATIVO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODPERDADOACAOLOTEVENC",
        "WhereSQL": "substring(a.CODPRODUTOPERDADOACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPRODUTOPERDADOACAO": "'001' || substring(a.CODPRODUTOPERDADOACAO FROM 4 FOR 12)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTO",
        "WhereSQL": "",
        "Generator": "GEN_PRODUTO",
        "GeneratorField": "CODPRODUTO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODUTOALIQICMS",
        "WhereSQL": "a.CODTABELAICMS = (SELECT b.CODTABELAICMS FROM ORGANIZACAO b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODTABELAICMS": "'00101'"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOANVISA",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODUTOBLOB",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODUTOCODIGOBARRA",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOENTRACAB",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOCONTROLADOENTRADA",
        "GeneratorField": "CODPCENTRA",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODPCENTRA": "'001' || lpad(CAST(SUBSTRING(a.CODPCENTRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PCONTRENT_CODPCENTRA c WHERE C2 < CAST(substring(a.CODPCENTRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPCENTRA)-3, '0')"
            },
            {
                "CODCOMPRA": "CASE a.CODCOMPRA WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODCOMPRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM COMPRA_CODCOMPRA c WHERE C2 < CAST(substring(a.CODCOMPRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODCOMPRA)-3, '0') END "
            },
            {
                "CODSNGPC": "case a.CODSNGPC WHEN '' THEN '' ELSE '001' || substring(a.CODSNGPC FROM 4 FOR 10) END"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOENTRAITEM",
        "WhereSQL": "substring(a.CODPCENTRA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPCENTRA": "'001' || lpad(CAST(SUBSTRING(a.CODPCENTRA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PCONTRENT_CODPCENTRA c WHERE C2 < CAST(substring(a.CODPCENTRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPCENTRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOINVENTARIOCAB",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOCONTROLADOINVENTARIO",
        "GeneratorField": "CODPCINVENTARIO",
        "CamposFormatados": [
            {
                "CODSNGPC": "case a.CODSNGPC WHEN '' THEN '' ELSE '001' || substring(a.CODSNGPC FROM 4 FOR 10) END"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODPCINVENTARIO": "'001' || substring(a.CODPCINVENTARIO FROM 4 FOR 7)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOINVENTARIOITEM",
        "WhereSQL": "substring(a.CODPCINVENTARIO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPCINVENTARIO": "'001' || substring(a.CODPCINVENTARIO FROM 4 FOR 7)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOPERDA",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOCONTROLADOPERDA",
        "GeneratorField": "CODPCPERDA",
        "CamposFormatados": [
            {
                "CODPRODUTOPERDADOACAO": "case a.CODPRODUTOPERDADOACAO WHEN '' then '' ELSE '001' || substring(a.CODPRODUTOPERDADOACAO FROM 4 FOR 8) END"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODSNGPC": "case a.CODSNGPC WHEN '' THEN '' ELSE '001' || substring(a.CODSNGPC FROM 4 FOR 10) END"
            },
            {
                "CODPCPERDA": "'001' || substring(a.CODPCPERDA FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOPERDAITEM",
        "WhereSQL": "substring(a.CODPCPERDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPCPERDA": "'001' || substring(a.CODPCPERDA FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOSAICAB",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOCONTROLADOSAIDA",
        "GeneratorField": "CODPCSAIDA",
        "CamposFormatados": [
            {
                "CODVENDA": "case a.CODVENDA WHEN '' THEN '' ELSE '001' || substring(a.CODVENDA FROM 4 FOR 15) END"
            },
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODPCSAIDA": "'001' || lpad(CAST(SUBSTRING(a.CODPCSAIDA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PCONTSAI_CODPCSAIDA c WHERE C2 < CAST(substring(a.CODPCSAIDA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPCSAIDA)-3, '0')"
            },
            {
                "CODSNGPC": "case a.CODSNGPC WHEN '' THEN '' ELSE '001' || substring(a.CODSNGPC FROM 4 FOR 10) END"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOCONTROLADOSAIITEM",
        "WhereSQL": "substring(a.CODPCSAIDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPCSAIDA": "'001' || lpad(CAST(SUBSTRING(a.CODPCSAIDA FROM 4 FOR 7) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM PCONTSAI_CODPCSAIDA c WHERE C2 < CAST(substring(a.CODPCSAIDA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODPCSAIDA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTODEMAISTRIBUTOS",
        "WhereSQL": "a.CODTABELAICMS = (SELECT b.CODTABELAICMS FROM ORGANIZACAO b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODTABELAICMS": "'00101'"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOGERAL",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PRODUTOHISTORICOVENDAS",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOINVENTARIO",
        "WhereSQL": "substring(a.CODINVENTARIO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODINVENTARIO": "'001' || substring(a.CODINVENTARIO FROM 4 FOR 8)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOLIVROLOG",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOLIVROLOG",
        "GeneratorField": "CODPRODUTOLIVROLOG",
        "CamposFormatados": [
            {
                "CODPRODUTOLIVROLOG": "'001' || substring(a.CODPRODUTOLIVROLOG FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOPERDADOACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOPERDADOACAO",
        "GeneratorField": "CODPRODUTOPERDADOACAO",
        "CamposFormatados": [
            {
                "CODPRODUTOPERDADOACAO": "'001' || substring(a.CODPRODUTOPERDADOACAO FROM 4 FOR 5)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOPERDADOACAOITEM",
        "WhereSQL": "substring(a.CODPRODUTOPERDADOACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPRODUTOPERDADOACAO": "'001' || substring(a.CODPRODUTOPERDADOACAO FROM 4 FOR 5)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOPERDADOACAOLOTE",
        "WhereSQL": "substring(a.CODPRODUTOPERDADOACAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODPRODUTOPERDADOACAO": "'001' || substring(a.CODPRODUTOPERDADOACAO FROM 4 FOR 5)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOPRECOVENDALOG",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOPRECOVENDALOG",
        "GeneratorField": "CODPRODUTOPRECOVENDALOG",
        "CamposFormatados": [
            {
                "CODPRODUTOPRECOVENDALOG": "'001' || substring(a.CODPRODUTOPRECOVENDALOG FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PRODUTOREGISTROMSLOG",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_PRODUTOREGISTROMSLOG",
        "GeneratorField": "CODPRODUTOREGISTROMSLOG",
        "CamposFormatados": [
            {
                "CODPRODUTOREGISTROMSLOG": "'001' || substring(a.CODPRODUTOREGISTROMSLOG FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "PROMOCAO",
        "WhereSQL": "",
        "Generator": "GEN_PROMOCAO",
        "GeneratorField": "CODPROMOCAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "PROMOCAOORGANIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "PROMOCAOPRODUTO",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "QUITACAOCONTAPAGAR",
        "WhereSQL": "a.CODQUITACAOCONTAPAGAR IN (SELECT CODQUITACAOCONTAPAGAR FROM QUITACAOCONTAPAGARITEM qcpi WHERE QCPI.CODCONTAPAGAR IN (SELECT cp.CODCONTAPAGAR FROM CONTAPAGAR cp WHERE cp.CODORGANIZACAO = :CodOrg))",
        "Generator": "GEN_QUITACAOCONTAPAGAR",
        "GeneratorField": "CODQUITACAOCONTAPAGAR",
        "CamposFormatados": [
            {
                "CODQUITACAOCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(CODQUITACAOCONTAPAGAR FROM 4 FOR 7) AS integer)+(Iif((SUBSTRING(CODQUITACAOCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODQUITACAOCONTAPAGAR FROM 4 FOR 7) AS integer)) FROM QUITACAOCONTAPAGAR c2), 0)), 7, '0')"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "QUITACAOCONTAPAGARITEM",
        "WhereSQL": "a.CODCONTAPAGAR IN (SELECT cp.CODCONTAPAGAR FROM CONTAPAGAR cp WHERE cp.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(a.CODCONTAPAGAR FROM 4) AS integer)+(Iif((SUBSTRING(a.CODCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODCONTAPAGAR FROM 4) AS integer)) FROM CONTAPAGAR c2), 0)), 7, '0')"
            },
            {
                "CODQUITACAOCONTAPAGAR": "'001' || lpad(CAST(SUBSTRING(a.CODQUITACAOCONTAPAGAR FROM 4 ) AS integer)+(Iif((SUBSTRING(a.CODQUITACAOCONTAPAGAR FROM 1 FOR 3)) <>(SELECT cio.CODORGANIZACAO FROM CONFIGURACAOINSTALACAO cio), (SELECT MAX(CAST(SUBSTRING(c2.CODQUITACAOCONTAPAGAR FROM 4) AS integer)) FROM QUITACAOCONTAPAGAR c2), 0)), 7, '0')"
            }
        ]
    },
    {
        "NomeTabela": "QUITACAOCONTAPAGARLANCCTAFINAN",
        "WhereSQL": "a.CODQUITACAOCONTAPAGAR IN (SELECT CODQUITACAOCONTAPAGAR FROM QUITACAOCONTAPAGARITEM qcpi WHERE QCPI.CODCONTAPAGAR IN (SELECT cp.CODCONTAPAGAR FROM CONTAPAGAR cp WHERE cp.CODORGANIZACAO = :CodOrg))",
        "Generator": "!",
        "GeneratorField": "CODQUITACAOCONTAPAGAR",
        "CamposFormatados": [
            {
                "CODQUITACAOCONTAPAGAR": "'001' || substring(a.CODQUITACAOCONTAPAGAR FROM 4 FOR 10)"
            },
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "'001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0')"
            }
        ]
    },
    {
        "NomeTabela": "RDB$CONTROLLER_P",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "RECEITAPRODUTOCONTROLADO",
        "WhereSQL": "substring(a.CODRECEITUARIO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_RECEITAPRODUTOCONTROLADO",
        "GeneratorField": "CODRECEITUARIO",
        "CamposFormatados": [
            {
                "CODRECEITUARIO": "'001' || substring(a.CODRECEITUARIO FROM 4 FOR 13)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "RECEITAPRODUTOCONTROLADOITEM",
        "WhereSQL": "substring(a.CODRECEITUARIO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODRECEITUARIO": "'001' || substring(a.CODRECEITUARIO FROM 4 FOR 13)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "REGIAO",
        "WhereSQL": "",
        "Generator": "GEN_REGIAO",
        "GeneratorField": "CODREGIAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "SECAO",
        "WhereSQL": "",
        "Generator": "GEN_SECAO",
        "GeneratorField": "CODSECAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "SNGPC",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg AND substring(CODSNGPC FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_SNGPC",
        "GeneratorField": "CODSNGPC",
        "CamposFormatados": [
            {
                "CODSNGPC": "'001' || substring(a.CODSNGPC FROM 4 FOR 12)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "SNGPCPRODUTOTEMP",
        "WhereSQL": "substring(a.CODSNGPC FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODSNGPC": "'001' || substring(a.CODSNGPC FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "SNGPCRESPOSTA",
        "WhereSQL": "substring(a.CODSNGPC FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODSNGPC": "'001' || substring(a.CODSNGPC FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "TABCOMISVENDDESCONTOLIMITE",
        "WhereSQL": "",
        "Generator": "GEN_TABCOMISVENDDESCONTOLIMITE",
        "GeneratorField": "CODCOMISDESCLIMITE",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "TABCOMISVENDPRODMOEDAPERCENTUAL",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "TABELACOMISSAOVENDA",
        "WhereSQL": "",
        "Generator": "GEN_TABELACOMISSAOVENDAS",
        "GeneratorField": "CODTABELACOMISSAO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "TABELAICMS",
        "WhereSQL": "a.CODTABELAICMS = (SELECT b.CODTABELAICMS FROM ORGANIZACAO b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "GEN_TABELAICMS",
        "GeneratorField": "CODTABELAICMS",
        "CamposFormatados": [
            {
                "CODTABELAICMS": "'00101'"
            }
        ]
    },
    {
        "NomeTabela": "TABGRUPOCOMISSAOPERCENTUAL",
        "WhereSQL": "",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "TRANSFERENCIACONTAFINANCEIRA",
        "WhereSQL": "substring(a.CODTRANSFERENCIACONTAFINANCEIRA FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_TRANSFERENCIACONTAFINAN",
        "GeneratorField": "CODTRANSFERENCIACONTAFINANCEIRA",
        "CamposFormatados": [
            {
                "CODTRANSFERENCIACONTAFINANCEIRA": "'001' || substring(a.CODTRANSFERENCIACONTAFINANCEIRA FROM 4 FOR 10)"
            },
            {
                "CODLANCAMENTOORIGEM": "'001' || substring(a.CODLANCAMENTOORIGEM FROM 4 FOR 10)"
            },
            {
                "CODLANCAMENTODESTINO": "'001' || substring(a.CODLANCAMENTODESTINO FROM 4 FOR 10)"
            }
        ]
    },
    {
        "NomeTabela": "USUARIO",
        "WhereSQL": "",
        "Generator": "GEN_USUARIO",
        "GeneratorField": "CODUSUARIO",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "VENDA",
        "WhereSQL": "a.CODORGANIZACAOVENDA = :CodOrg",
        "Generator": "GEN_VENDA",
        "GeneratorField": "CODVENDA",
        "CamposFormatados": [
            {
                "CODPREVENDA": "case a.CODPREVENDA WHEN '' THEN '' ELSE '001' || substring(a.CODPREVENDA FROM 4 FOR 13) END"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            },
            {
                "CODSESSAOECFTEF": "case a.CODSESSAOECFTEF WHEN '' THEN '' ELSE '001' || substring(a.CODSESSAOECFTEF FROM 4 FOR 13) END"
            },
            {
                "CODORGANIZACAOVENDA": "'001'"
            },
            {
                "CODDAVVENDA": "case a.CODDAVVENDA WHEN '' THEN '' ELSE '001' || substring(a.CODDAVVENDA FROM 4 FOR 13) END"
            },
            {
                "CODECF": "case a.CODECF WHEN '' THEN '' ELSE '001' || substring(a.CODECF FROM 4 FOR 5) END"
            },
            {
                "CODORGANIZACAOCAIXA": "case a.CODORGANIZACAOCAIXA when '' then '' ELSE '001' END"
            },
            {
                "CODCAIXA": "case a.CODCAIXA WHEN '' THEN '' ELSE '001' || substring(a.CODCAIXA FROM 4 FOR 5) END"
            }
        ]
    },
    {
        "NomeTabela": "VENDACANCELADAECF",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODORGANIZACAO": "'001'"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "VENDACARTAOLANCAMENTO",
        "WhereSQL": "substring(a.CODVENDALANCAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDACARTAOLANCAMENTO",
        "GeneratorField": "CODVENDALANCAMENTO",
        "CamposFormatados": [
            {
                "CODVENDALANCAMENTO": "'001' || substring(a.CODVENDALANCAMENTO FROM 4 FOR 12)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDACHEQUELANCAMENTO",
        "WhereSQL": "substring(a.CODVENDALANCAMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDACHEQUELANCAMENTO",
        "GeneratorField": "CODVENDALANCAMENTO",
        "CamposFormatados": [
            {
                "CODVENDALANCAMENTO": "'001' || substring(a.CODVENDALANCAMENTO FROM 4 FOR 12)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            },
            {
                "CODCHEQUE": "case a.CODCHEQUE WHEN '' THEN '' ELSE '001' || substring(a.CODCHEQUE FROM 4 FOR 10) END"
            }
        ]
    },
    {
        "NomeTabela": "VENDAENTREGADADOS",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAFINANCIAMENTOCONDPAGAMENTO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAFORMAPAGAMENTO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODLANCAMENTOCONTAFINANCEIRA": "case a.CODLANCAMENTOCONTAFINANCEIRA WHEN '' THEN '' ELSE '001' || lpad(CAST(SUBSTRING(a.CODLANCAMENTOCONTAFINANCEIRA FROM 4 FOR 10) AS integer)+(SELECT COALESCE(SUM(C1),0) FROM LCONTAF_CODLANCAMENTOCFIN c WHERE C2 < CAST(substring(a.CODLANCAMENTOCONTAFINANCEIRA FROM 1 FOR 3) AS integer)), CHAR_LENGTH(a.CODLANCAMENTOCONTAFINANCEIRA)-3, '0') END"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDALOTE",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 13)"
            }
        ]
    },
    {
        "NomeTabela": "VENDALOTEVENCIMENTO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAMODOUSO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDAMODOUSO",
        "GeneratorField": "CODVENDAMODOUSO",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            },
            {
                "CODVENDAMODOUSO": "'001' || substring(a.CODVENDAMODOUSO FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAPBMCOMPROVANTE",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAPERDIDAPRODUTO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "GEN_VENDAPERDIDAPRODUTO",
        "GeneratorField": "CODVENDAPERDIDAPRODUTO",
        "CamposFormatados": [
            {
                "CODVENDAPERDIDAPRODUTO": "'001' || substring(a.CODVENDAPERDIDAPRODUTO FROM 4 FOR 15)"
            },
            {
                "CODORGANIZACAO": "'001'"
            }
        ]
    },
    {
        "NomeTabela": "VENDAPILLASLANCAMENTO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDAPRODUTO",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDARESERVAPRODUTO",
        "WhereSQL": "substring(a.CODRESERVAVENDAPRODUTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDARESERVAPRODUTO",
        "GeneratorField": "CODRESERVAVENDAPRODUTO",
        "CamposFormatados": [
            {
                "CODRESERVAVENDAPRODUTO": "'001' || substring(a.CODRESERVAVENDAPRODUTO FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDARESTRICOES",
        "WhereSQL": "substring(a.CODVENDA FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDCOMISFUNCILANCTOCTACORRENTE",
        "WhereSQL": "substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODFUNCICONTACORRLANC": "'001' || substring(a.CODFUNCICONTACORRLANC FROM 4 FOR 9)"
            },
            {
                "CODVENDEDORCOMISSAOVENCIMENTO": "'001' || substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDEDORCOMISSAO",
        "WhereSQL": "substring(a.CODVENDEDORCOMISSAO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDEDORCOMISSAO",
        "GeneratorField": "CODVENDEDORCOMISSAO",
        "CamposFormatados": [
            {
                "CODDEVOLUCAOPRODUTOVENDIDO": "CASE CODDEVOLUCAOPRODUTOVENDIDO WHEN '' THEN '' ELSE '001' || substring(CODDEVOLUCAOPRODUTOVENDIDO FROM 4 FOR 15) END"
            },
            {
                "CODVENDEDORCOMISSAO": "'001' || substring(a.CODVENDEDORCOMISSAO FROM 4 FOR 20)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDEDORCOMISSAOVENCIMENTO",
        "WhereSQL": "substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "GEN_VENDEDORCOMISSAOVENCIMENTO",
        "GeneratorField": "CODVENDEDORCOMISSAOVENCIMENTO",
        "CamposFormatados": [
            {
                "CODCONTARECEBER": "'001' || substring(a.CODCONTARECEBER FROM 4 FOR 12)"
            },
            {
                "CODVENDEDORCOMISSAOVENCIMENTO": "'001' || substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 4 FOR 15)"
            },
            {
                "CODCONTARECEBERQUITACAO": "'001' || substring(a.CODCONTARECEBERQUITACAO FROM 4 FOR 12)"
            },
            {
                "CODVENDEDORCOMISSAO": "'001' || substring(a.CODVENDEDORCOMISSAO FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "VENDEDORCOMISSAO_INFO",
        "WhereSQL": "substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 1 FOR 3) = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": [
            {
                "CODVENDEDORCOMISSAOVENCIMENTO": "'001' || substring(a.CODVENDEDORCOMISSAOVENCIMENTO FROM 4 FOR 15)"
            },
            {
                "CODVENDA": "'001' || substring(a.CODVENDA FROM 4 FOR 15)"
            }
        ]
    },
    {
        "NomeTabela": "WSAUTORIZACAO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "WSAUTORIZACAOITEM",
        "WhereSQL": "a.TRANSID in (SELECT b.TRANSID FROM WSAUTORIZACAO b WHERE b.CODORGANIZACAO = :CodOrg)",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    },
    {
        "NomeTabela": "WSCREDENCIADO",
        "WhereSQL": "a.CODORGANIZACAO = :CodOrg",
        "Generator": "!",
        "GeneratorField": "",
        "CamposFormatados": []
    }
]