import os
import time
from services.services_produtos import alterar_produto_nome, procurar_todos_produtos, alterar_produto_preco, inativar_produto
from services.services_produtos import adicionar_produto
from services.services_produtos import procurar_codigo

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
            tela_cadastrar_produto()
        elif opcao == "2":
            tela_consultar_produtos()
        elif opcao == "3":
            telaAlterarProduto()
        elif opcao == "4":
            tela_inativar_produto()
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
            tela_alterar_nome_produto()
        elif opcao == "2":
            tela_alterar_preco_produto()
        elif opcao == "0":
            break
        else:
            input("Digite uma opcao correta!")


def tela_cadastrar_produto():
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
        dados = [codigo_produto, nome_produto, preco_produto]
        adicionar_produto(dados)

        print("\nAdicionado com sucesso")
        time.sleep(3)
        break



def tela_consultar_produtos():
        while True:
            os.system("clear")
            print("Consulta de produtos")
            print("--------------------")
            print("Codigo      Produto          Valor")
            print("001         YAKISSOBA        29,90")
            input("Digite algo para continuar ..")
            dados = procurar_todos_produtos()
            if dados is None:
                input("Nao tem dados")
            else:
                for dado in dados :
                    print(dado)
                    input("Continue ...")
            break

def tela_alterar_nome_produto():
    while True:
        os.system("clear")
        print('Alterar Nome do produto')
        print('-----------------------\n')
        input_codigo = input('Digite o codigo para procurar : ')

        # Aqui precisa procurar codigo
        print(f"Você está procurando o codigo : {input_codigo}")
        dados, founded = procurar_codigo(input_codigo)

        if founded :
            id = dados[0]
            codigo = dados[1]
            nome_inicial = dados[2]

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
            resultado = alterar_produto_nome(id, nome_alterado)
            print("Atualizado ! ...")
            time.sleep(2)
        else:
            print('Nao foi encontrado valor')
            input('Digite algo para continuar ...')
            break
        break

def tela_alterar_preco_produto():
    while True:
        os.system("clear")
        print("ALTERAR PREÇO DO PRODUTO")
        print("------------------------")
        input_codigo = input("Codigo do produto : (zero para sair)")

        # Aqui vai procurar o codigo se existe
        dados , founded = procurar_codigo(input_codigo) 
        id = dados[0]
        founded = True
        if input_codigo == '0':
            break
        else:
            # Se existe aqui
            if founded :
                input("Achamos o codigo , cotinue com enter ..")
                preco_novo = input("Digite o valor novo : ")
                # Alterar o preco do produto aqui
                alterar_produto_preco(id, preco_novo)
                print("Atualizado com sucesso ...")
                time.sleep(2)

                break
            # Se não existe aqui
            else:
                input("Não foi encontrado ... \n")

def tela_inativar_produto():
    while True:
        os.system("clear")
        print("INATIVAR PRODUTO")
        print("----------------")
        input_codigo = input("Digite o codigo para inativar (zero para sair) :  ")

        if input_codigo == "0":
            break
        else:
            # Aqui procura o codigo produto
            dados, founded  = procurar_codigo(input_codigo)
            if founded :
                # Aqui Achou o produto
                os.system("clear")
                print(f"Codigo do produto : {input_codigo}")
                print("--------------------------------")
                input("Codigo achado ! ")
                print(dados)

            else:
                # Aqui não achou o produto
                print("Não foi encontrado !")
                print("Retornando ... ")
                time.sleep(3)
