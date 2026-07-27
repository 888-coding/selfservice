import os
import sqlite3
from db.get_connection import conectar

def procurar_codigo_produto():
    con = conectar()
    cur = con.cursor()
    sql = "SELECT * FROM produtos"
    cur.execute(sql,)
    con.close()

procurar_codigo_produto()

