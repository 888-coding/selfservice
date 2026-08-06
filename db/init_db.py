import os
import sqlite3

def createDb():
    con = sqlite3.connect("db/panda.db")
    con.executescript("""
    CREATE TABLE IF NOT EXISTS "products" (
        "id" INTEGER NOT NULL,
        "name" TEXT,
        "price" INTEGER,
        "active" BOOLEAN,
        PRIMARY KEY("id")
    );

    CREATE TABLE IF NOT EXISTS "selling" (
        "id" INTEGER NOT NULL,
        "sellingDate" DATE,
        "discount" INTEGER,
        "totalValue" INTEGER,
        PRIMARY KEY("id")
    );

    CREATE TABLE IF NOT EXISTS "sellingDetails" (
        "id" INTEGER NOT NULL,
        "sellingId" INTEGER,
        "productId" INTEGER,
        "productPrice" INTEGER,
        "productQuantity" INTEGER,
        PRIMARY KEY("id")
    );
    """)
    con.commit()
    con.close()

def checkDb():
   file = os.path.join("db","panda.db")
   if not os.path.isfile(file):
        createDb()

