from db.get_connection import conectar as connection
def serviceRelatorio(dados):
    # DADOS recebido vai ser a data de hoje , ou data especifica
    # Funciona para data : HOJE, DATA ESPECIFICA
    data_escolhida = dados

    with connection() as con :
        cur = con.cursor()
        try:
            # TODO: 
            # CRIAR O SCRIPT DE SQL PARA BUSCAR:
            # - LISTA DE SELLING CABECALHO
            # - TODOS OS PRODUTOS DENTRO DO SELLING
            # - DETALHES DE TODOS OS PRODUTOS  
            script = "SELECT id, discount, totalValue FROM selling WHERE sellingDate = ? "
            cur.execute(script, ( data_escolhida,) )

            cabecalhos = cur.fetchall()

            while True:
                for cabecalho in cabecalhos:
                    idSelling = cabecalho[0]
                    desconto = cabecalho[1]
                    totalValue = cabecalho[2]

                    # SCRIPT DE PROCURAR COMPLEMENTOS DE SELLING 
                    script = "SELECT id, sellingId, productId, productPrice, productQuantity FROM sellingDetails WHERE sellingId = ?"
                    cur.execute(script, (idSelling,) )
                    complementos = cur.fetchall()

                    for complemento in complementos:
                        idSellingDetail = complemento[0]
                        productId = complemento[2]
                        precoProduto = complemento[3]
                        quantidadeProduto = complemento[4]

                        script = "SELECT code, name FROM products WHERE id = ? "
                        cur.execute(script, (productId,))
                        produto = cur.fetchone()
                        codigoProduto = produto[0]
                        nomeProduto = produto[1]


                break
            return dados
        finally :
            cur.close()

