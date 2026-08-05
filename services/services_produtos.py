import os
import sqlite3
from db.get_connection import conectar

def procurar_todos_produtos():
    con = conectar()
    cur = con.cursor()
    sql = "SELECT * FROM products ORDER BY name "
    dados = cur.execute(sql)
    con.close()
    return dados
