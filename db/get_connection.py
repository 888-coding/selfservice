import sqlite3
import os

def conectar():
    # nome do arquivo 
    my_database = 'pandaDB.db'
    # Localizar meu diretorio atual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Adicionar a pasta 'db'
    pasta_db = os.path.join(script_dir, "db")
    # Garantir que tenha a pasta (caso nao tem , ele cria)
    os.makedirs(pasta_db, exist_ok=True)

    # Juntar a pasta e o arquivo 
    db_path = os.path.join(pasta_db, my_database)
    # conectar
    con = sqlite3.connect(db_path)
    return con

