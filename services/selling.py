# Selling
from db.connection import get_connection

def selling_action():
    pass
    con = get_connection()
    try:
        cursor = con.cursor()
        sql = ""
        cursor.execute(sql, (,))
    finally:
        con.close()
def selling_alter():
    pass
def selling_show_today():
    pass