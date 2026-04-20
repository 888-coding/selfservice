# Selfservice Easy App 

# Imports
import sqlite3 as s
import os

# Modules Imports 
from db.init_db import init_bd
# Main
def main():
    init_bd()
    os.system("cls")
    from menus import company_title
    company_title
    from menus import menu_main
    menu_main()

main()