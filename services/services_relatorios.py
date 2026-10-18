from db.get_connection import conectar as connection

def serviceRelatorioVendasDiario(data_escolhida):
    dataConsulta = data_escolhida
    con = connection()
    try:
        with con:
            try:
                listaDados = []
                cur = con.cursor()
                script = "SELECT id FROM selling WHERE sellingDate = ? "
                
                cur.execute(script, (dataConsulta,) )
                dados = cur.fetchall()
                for dado in dados :
                    listaDados.append({"idSelling":dado[0]})
            finally:
                cur.close()
            return listaDados
    finally:
        con.close()