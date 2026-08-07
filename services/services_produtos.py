import os
import sqlite3
from db.get_connection import conectar as connection

def procurar_todos_produtos():
    with connection() as con:
        cur = con.cursor()
        try:
            script = "SELECT * from products ORDER BY name"
            cur.execute(script)
        finally:
            cur.close()

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
