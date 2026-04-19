# Connection 

import sqlite3 as s 
import os 

def get_connection():
    database_name = "panda.db"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, database_name)

    connection = s.connect(db_path)
    return connection