# Products 
import sqlite3 as s 
import os 

def print_products_menu():
    os.system("cls")
    
    menu_products_list = ['Cadastrar', 'Alterar', 'Mostrar todos']
    for i in range(len(menu_products_list)):
        print(i+1, menu_products_list[i])
    
    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_products_list):
            print("Erro")
        else:
            break

