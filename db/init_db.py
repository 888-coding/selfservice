# Init database 

from db.connection import get_connection

def init_bd():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        code TEXT NOT NULL, 
        nome TEXT NOT NULL, 
        preco INT 
    )
    """)


    conn.commit()
    conn.close()