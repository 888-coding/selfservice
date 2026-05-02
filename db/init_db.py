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
    );
    """)
    conn.commit()
    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        total_amount INTEGER NOT NULL,
        discount INTEGER DEFAULT 0,
        final_amount INTEGER NOT NULL,
        payment_method TEXT,
        status TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.commit()
    conn.close()