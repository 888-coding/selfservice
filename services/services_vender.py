from db.get_connection import conectar as connection




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
            for produto in produtos :
                productId = produto[0]
                productPrice = produto[4]
                productQuantity = produto[3]
                cur.execute(script, (id_selling, productId, productPrice, productQuantity,) ) 
                con.commit() 

        finally:
            cur.close()

    # Passo 2 Inserir produtos na tabela de selling sellingDetails
    print(f"Id de selling criado é {id_selling} ")
    
# ??
def service_venderAdicionarCabecalho():
    pass


# ??
def service_venderAdicionarProdutos():
    pass


# ??
def service_venderAtualizarCabecalho():
    pass
