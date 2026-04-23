# Arquivos de Menu 
import os 

def company_title():
    for i in range(30):
        print("*", end="")
        if i == 29 :
            print("\n", end="")
    print("Self Service Easy App")
    for i in range(30):
        print("*", end="")
        if i == 29 :
            print("\n", end="")

def menu_main():
    os.system("cls")
    company_title()
    menu_main_list = ['Vender', 'Produtos', 'Relatorios']
    for i in range(len(menu_main_list)):
        print(i+1, menu_main_list[i])
    print("0 Sair do sistema")

    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_main_list):
            print("Erro")
        else:
            if input_selected == "1":
                menu_vendas()
            elif input_selected == "2":
                menu_products()
            elif input_selected == "3":
                menu_relatorios()
            elif input_selected == "0":
                exit()
            break
def menu_vendas():
    os.system("cls")
    company_title()
    print("<  Vender  >")
    print(" . . . . . . .")
    menu_products_list = ['Vender', 'Alterar', 'Mostrar vendas de hoje']
    for i in range(len(menu_products_list)):
        print(i+1, menu_products_list[i])
    
    print("0 Voltar")
    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_products_list):
            print("Erro")
        else:
            if input_selected == "0":
                menu_main()

            break

def menu_products():
    from services.products import (
        create_product,
        search_all_products,
        change_product_name,
        change_product_price
    )
    os.system("cls")
    company_title()
    print("<  Produtos  >")
    print(" . . . . . . .")
    menu_products_list = ['Cadastrar', 'Alterar Nome', 'Alterar Preço','Mostrar todos']
    for i in range(len(menu_products_list)):
        print(f"{i+1}. {menu_products_list[i]}")
    print("0. Voltar")
    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_products_list):
            print("Erro")
        else:
            if input_selected == "1":
                os.system("cls")
                print("\n\n Cadastro de produto \n")
                code = input("Codigo : ")
                name = input("Nome : ")
                price = input("Preco : ")
                result = create_product(code, name, price)
                if result == True:
                    print("\n\nCadastrado com sucesso!")
                else:
                    print("\n\nERRO! Já existe !!")

                input_selected == input("\n\nDigite algo para continuar...")
                menu_main()
                
            elif input_selected == "2":
                change_product_name()
            elif input_selected == "3":
                change_product_price()
            elif input_selected == "4":
                products = search_all_products()
                for product in products:
                    print(product)
                input("\n\nDigite Algo para continuar...")
                menu_main()
            elif input_selected == "0":
                menu_main()

            break

def menu_relatorios():
    os.system("cls")
    company_title()
    print("<  Relatorios  >")
    print(" . . . . . . .")
    menu_products_list = ['Relatorio 1', 'Relatorio 2', 'Relatorio 3']
    for i in range(len(menu_products_list)):
        print(i+1, menu_products_list[i])
    
    print("0 Voltar")
    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_products_list):
            print("Erro")
        else:
            if input_selected == "0":
                menu_main()

            break

