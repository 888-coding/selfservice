import os 
def telaProdutos():
    while True:
        os.system("clear")
        print("SISTEMA SELFSERVICE -- PRODUTOS")
        print("-------------------------------")
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Alterar")
        print("4. Inativar")
        print("0. Voltar")
        opcao = input("> Opção : ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "0":
            break 
        else:
            input("Opção inválida ... Pressione enter para continuar")


def cadastrar_produto():
    while True:
        os.system("clear")
        print("CADASTRO - PRODUTO")
        print("------------------")
        while True:
            codigo_produto = input("Codigo do produto : ")
            if not codigo_produto:
                input("Erro.. favor digitar correto")
            else:
                print(f"O codigo digitado é : {codigo_produto} ")
                input("Digite enter para continuar ...")
                break
        while True:    
            nome_produto = input("Nome do produto : ")
            if not nome_produto:
                input("Erro .. favor digitar correto")
            else:
                print(f"O nome digitado é : {nome_produto} ")
                input("Digite enter para continuar ...")
                break
        while True:
            preco_produto = input("Preço do produto : ")
            if not preco_produto:
                input("Erro.. favor digitar correto")
            else:
                print(f"O preço digitado é : {preco_produto}")
                input("Digite enter para continuar ...")
                break
        
        print(f"CODIGO : {codigo_produto} - NOME: {nome_produto} - PREÇO : {preco_produto}")
        input("Digite enter para continuar ...")
        break 