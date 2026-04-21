# Init database 

from db.connection import get_connection

def init_bd():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        code TEXT NOT NULL, 
        name TEXT NOT NULL, 
        price INT 
    )
    """)


    conn.commit()
    conn.close()