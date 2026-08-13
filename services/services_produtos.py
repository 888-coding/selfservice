from db.get_connection import conectar as connection

def procurar_todos_produtos():
    with connection() as con:
        cur = con.cursor()
        try:
            script = "SELECT * from products ORDER BY code"
            cur.execute(script)
            dados = cur.fetchall()
        finally:
            cur.close()
        return dados
def procurar_codigo(dado):
    codigo_a_procura = dado
    founded = False
    with connection() as con :
        cur = con.cursor()
        try:
            script = "SELECT id, code, name FROM products WHERE code = ?"
            cur.execute(script, (codigo_a_procura,))
            dados = cur.fetchone()
            if dados:
                founded = True
            else:
                founded = False
                dados = None

        finally:
            cur.close()
        return (dados, founded)

def adicionar_produto(dados):
    codigo = dados[0]
    nome = dados[1]
    preco = dados[2]
    ativo = True

    with connection() as con :
        cur = con.cursor()
        try:
            script = """
                INSERT INTO products (
                    code, name, price, active
                )
                VALUES (
                    ?, ?, ? , ?
                )"""
            cur.execute(script, (codigo, nome, preco, ativo) )
            con.commit()
        finally:
            cur.close()

def alterar_produto_nome(id, nome_alterado):
    id = id 
    nome_alterado = nome_alterado

    with connection() as con :
        cur = con.cursor()
        try:
            script = "UPDATE products SET name = ? WHERE id = ?"
            cur.execute(script, (nome_alterado, id) )
            con.commit() 
            print(cur.rowcount , "dado(s) atualizado")
        finally:
            cur.close()

def alterar_produto_preco(id, preco):
    id = int(id)
    preco = preco
    with connection() as con : 
        cur = con.cursor()
        try:
            script = "UPDATE products SET price = ? WHERE id = ?"
            cur.execute(script, (preco, id,) )
            con.commit()
            print(cur.rowcount, "dado(s) atualizado")
        finally:
            cur.close()

def inativar_produto(id):
    id = id
    with connection() as con:
        cur = con.cursor()
        try:
            script = "UPDATE products SET active = False WHERE id = ? "
            cur.execute(script, (id,) )
            con.commit()
            print(cur.rowcount, "dado(s) atualizado")
        finally:
            cur.close()

def reativar_produto_listarProdutosInativos():
    dados = []
    with connection() as con:
        cur = con.cursor()
        try:
            script = "SELECT * FROM products WHERE active = ? "
            cur.execute(script, (0,) )
            dados = cur.fetchall()
        finally:
            cur.close()
    return dados

def reativar_produto_inativar(id):
    id = id
    with connection() as con : 
        cur = con.cursor()
        try:
            script = "UPDATE products SET active = True WHERE id = ? " 
            cur.execute(script, (id,))
            con.commit()
            pass
        finally:
            cur.close() 
