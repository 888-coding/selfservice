from db.get_connection import conectar as connection

def serviceRelatorioVendasDiario(data_escolhida):
    dataConsulta = data_escolhida
    con = connection()
    try:
        with con:
            try:
                listaDados = []
                cur = con.cursor()
                script = "SELECT id, discount, totalValue FROM selling WHERE sellingDate = ? "
                
                cur.execute(script, (dataConsulta,) )
                dados = cur.fetchall()
                for dado in dados :
                    # Dicionario venda
                    # ----------------
                    venda = {"idSelling": dado[0],
                             "discount":dado[1],
                             "totalValue":dado[2],
                             "detalhe":[]}

                    # Dicionario venda > Incluir os detalhes
                    # --------------------------------------
                    idSelling = dado[0] 
                    script = "SELECT id, productId, productCode, productName, productPrice, productQuantity FROM sellingDetails WHERE sellingId = ?"
                    cur.execute(script, (idSelling,) )
                    produtos = cur.fetchall()
                    for produto in produtos :
                        venda["detalhe"].append({
                            "productId": produto[1],
                            "productCode" : produto[2],
                            "productName" : produto[3],
                            "productPrize": produto[4],
                            "productQuantity": produto[5]
                        })
                    # Incluindo dicionario para lista (cada venda)
                    listaDados.append(venda)
            finally:
                cur.close()
            return listaDados
    finally:
        con.close()