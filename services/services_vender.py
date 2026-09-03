from db.get_connection import conectar as connection
import os



def service_venderCadastro(cabecalho, produtos):
    cabecalho = cabecalho
    date = cabecalho[0]
    discount = 0 
    totalValue = 0
    produtos = produtos

    # Passo 1: Inserir cabelho
    with connection() as con:
        cur = con.cursor()
        try:
            # 1. Inserir no cabecalho 
            script = """INSERT INTO selling(
            sellingDate,
            discount,
            totalValue
          )VALUES (?, ?, ?)"""
            cur.execute(script, (date, discount, totalValue,) )

            id_selling = cur.lastrowid

            con.commit()

            # TODO: Tem que fazer Looping para cada produto inserido
            # 2. Inserir no selling details 
            script = """
                INSERT INTO sellingDetails(
                sellingId,
                productId,
                productPrice,
                productQuantity
                ) VALUES(?, ?, ?, ?)
            """
            valor_total = 0 
            for produto in produtos :
                productId = produto[0]
                productPrice = produto[4]
                productQuantity = produto[3]
                cur.execute(script, (id_selling, productId, productPrice, productQuantity,) ) 
                con.commit() 
                valor_total += int(productPrice) * int(productQuantity)

            # Passo 3 : Atualizar a tabela Selling 
            # Precisa atualizar o valor total 

            script = """UPDATE selling
                SET totalValue = ? 
                WHERE id = ? 
            """
            cur.execute(script, (valor_total,id_selling,) )
            con.commit()

        finally:
            cur.close()

    os.system("clear")
    print(f"Número do pedido :  {id_selling} ")
    print(f"Data do pedido : {date}")
    for produto in produtos:
        print(f"{produto}")
    retorno = []
    retorno.append(True)
    retorno.append(id_selling)
    return retorno 


