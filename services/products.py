# Products 
from db.connection import get_connection

def create_product(code, name, price):
    con = get_connection()
    try:
        cursor = con.cursor()
        # First , Search if there is a created code
        sql = "SELECT code, name, price FROM products WHERE code = ?"
        cursor.execute(sql, (code,))
        result = cursor.fetchone()
        if result is None:
            # If Nothing searched, then insert to database 
            sql = "INSERT INTO products (code, name, price) VALUES (?, ?, ?)"
            cursor.execute(sql, (code, name, price,) )
            con.commit()
            return True
        else:
            return False
    finally:
        con.close()

def search_all_products():
    con = get_connection()
    try:
        cursor = con.cursor()
        sql = "SELECT code, name, price FROM products"
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)
    finally:
        con.close()

    pass

def change_product_name(code, new_name):
    con = get_connection()
    try:
        cursor = con.cursor()
        sql = "SELECT id, code, name FROM products WHERE code = ? "
        cursor.execute(sql, (code,) )
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            id = result[0]
            sql = "UPDATE products SET name = ? WHERE id = ?"
            cursor.execute(sql, (new_name,id, ))
            con.commit()
            return True
    finally:
        con.close()
    pass

def change_product_price():
    pass

