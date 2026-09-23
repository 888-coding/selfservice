from sqlite3 import Cursor, connect

from db.get_connection import conectar as connection
import os
import time



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
    time.sleep(0.8)
    print(f"Número do pedido :  {id_selling}")
    time.sleep(0.5)
    print(f"\n\nData do pedido : {date}")
    time.sleep(0.5)
    for produto in produtos:
        nome = produto[2]
        qte = produto[3]
        preco = produto[4]

        time.sleep(0.5)
        print(f"\nProduto : {nome} , Quantidade : {qte} , Preço : {preco}")
    retorno = []
    retorno.append(True)
    retorno.append(id_selling)
    return retorno


def service_venderConsultaPorData(data):
    data = data

    t = time.localtime()
    dia, mes, ano = t.tm_mday, t.tm_mon, t.tm_year
    hoje = f"{ano}-{mes:02d}-{dia:02d}"

    if str(data) == str(hoje):
        # Aqui fica o data de Hoje
        # Mostrar somente Cabecalho
        with connection() as con :
            cur = con.cursor()
            try:
                script = "SELECT id, discount, totalValue FROM selling WHERE sellingDate = ?"
                cur.execute(script, (str(data),) )
                dados = cur.fetchall()
                return dados
                time.sleep(2.0)
            finally:
                cur.close()
    else:
        with connection() as con :
            cur = con.cursor()
            try :
                script = "SELECT id, discount, totalValue FROM selling WHERE sellingDate = ?"
                cur.execute(script, (str(data),) )
                dados = cur.fetchall()
                return dados
            finally :
                cur.close()

def consultarPorNumeroPedido(dado):
   numeroPedido = dado
   with connection() as con :
       cur = con.cursor()
       try :
           script = "SELECT id, discount, totalValue, sellingDate FROM selling WHERE id = ?"
           cur.execute(script, (numeroPedido,) )
           dado = cur.fetchone()
           return dado
       finally :
           cur.close()
