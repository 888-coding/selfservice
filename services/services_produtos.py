import os
import sqlite3
import time
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
    with connection() as con :
        cur = con.cursor()
        try:
            script = "SELECT * FROM products WHERE code = ? "
            cur.execute(script, (codigo_a_procura,) )
            dados = cur.fetchall()
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

def alterar_produto_nome(dado):
    codigo = dado
    founded = False

    with connection() as con :
        cur = con.cursor()
        try:
            script = "SELECT id, code, name FROM products WHERE code = ? "
            cur.execute(script, (codigo) )
            dados = cur.fetchall()
            if dados :
                founded = True
        finally:
            cur.close()

        if founded : 
            print("Codigo encontrado ... ")
            time.sleep(3)
            for dados in dados :
                print(dado)
                time.sleep(1)
        else:
            print("Codigo nao foi encontrado ... \n Retornaremos para pagina anterior")
            time.sleep(4)
            


