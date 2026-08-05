from db.get_connection import conectar as conexao
import telas.tela_principal as tela_principal
import telas.tela_produtos as tela_produtos
import telas.tela_vender as tela_vender

def main():
  con = conexao()
  cur = con.cursor()
  sql = "SELECT * FROM products WHERE id = ? "
  cur.execute(sql, (1,))
  cur.close()
  con.close()

main()
