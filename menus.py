# Arquivos de Menu 

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
    menu_main_list = ['Vender', 'Produtos', 'Relatorios']
    for i in range(len(menu_main_list)):
        print(i+1, menu_main_list[i])
    
    print("\n", end="")
    while True:
        input_selected = input("> Escolhe uma opção :  ")
        if int(input_selected) > len(menu_main_list):
            print("Erro")
        else:
            if input_selected == "2":
                from products import print_products_menu
                print_products_menu()
            break

def menu_products():
    pass


