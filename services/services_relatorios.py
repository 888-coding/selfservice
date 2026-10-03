from db.get_connection import conectar as connection
def serviceRelatorio(dados):
    # DADOS recebido vai ser a data de hoje , ou data especifica
    data_escolhida = dados

    with connection() as con :
        cur = con.cursor()
        try:
            #TODO Criar o script para procurar vendas na tabela selling , e tambem adicionar a lista de 
            script = "SELECT * FROM selling WHERE selling_date = ? "

            cur.execute(script, ( data_escolhida,) )

            dados = cur.fetchall()

            return dados
        finally :
            cur.close()

