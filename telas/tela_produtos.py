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
            consultar_produtos()
        elif opcao == "3":
            telaAlterarProduto()
        elif opcao == "4":
            inativar_produto()
        elif opcao == "0":
            break
        else:
            input("Opção inválida ... Pressione enter para continuar")

def telaAlterarProduto():
    while True:
        os.system("clear")
        print("ALTERAR PRODUTO")
        print("---------------")
        print("1. ALTERAR NOME")
        print("2. ALTERAR PREÇO")
        print("0. VOLTAR")

        opcao = input("Opção : ")

        if opcao == "1":
            alterar_nome_produto()
        elif opcao == "2":
            alterar_preco_produto()
        elif opcao == "0":
            break
        else:
            input("Digite uma opcao correta!")


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


def consultar_produtos():
        while True:
            os.system("clear")
            print("Consulta de produtos")
            print("--------------------")
            print("Codigo      Produto          Valor")
            print("001         YAKISSOBA        29,90")
            input("Digite algo para continuar ..")
            break

def alterar_nome_produto():
    while True:
        os.system("clear")
        print('Alterar Nome do produto')
        print('-----------------------\n')
        input_codigo = input('Digite o codigo para procurar : ')

        # Aqui precisa procurar codigo
        pesquisa = True
        codigo = '01'
        nome_inicial = 'Pablo'
        valor = 100
        if pesquisa :
            print("\nFoi encontrado o codigo")
            print(f"Codigo: {codigo}")
            print(f"Nome: {nome_inicial}\n\n")

            while True:
                nome_alterado = input("Alterar o nome para : ")
                if nome_alterado == None:
                    input("Erro.. Pressione enter")
                else:
                    break

            print(f"Nome antigo : {nome_inicial} ")
            print(f"Nome alterado : {nome_alterado} ")

            # Aqui atualizar o nome no BD
        else:
            print('Nao foi encontrado valor')
            input('Digite algo para continuar ...')
            break
        break

def alterar_preco_produto():
    while True:
        os.system("clear")
        print("ALTERAR PREÇO DO PRODUTO")
        print("------------------------")
        input_codigo = input("Codigo do produto : (zero para sair)")

        # Aqui vai procurar o codigo se existe

        pesquisa = True
        if input_codigo == '0':
            break
        else:
            # Se existe aqui
            if pesquisa :
                input("Achamos o codigo , cotinue com enter ..")
                break
            # Se não existe aqui
            else:
                input("Não foi encontrado ... \n")

def inativar_produto():
    while True:
        os.system("clear")
        print("INATIVAR PRODUTO")
        print("----------------")
        input_codigo = input("Digite o codigo para inativar (zero para sair) :  ")

        pesquisa = True

        # Aqui precisa procurar o codigo

        if input_codigo == "0":
            break
        else:
            if pesquisa :
                # Aqui Achou o produto
                os.system("clear")
                print(f"Codigo do produto : {input_codigo}")
                print("--------------------------------")
                input("Codigo achado ! ")

                pass
            else:
                # Aqui não achou o produto
                pass
