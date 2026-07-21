import os
import time

def telaVender():
    while True:
        os.system("clear")
        print("VENDER")
        print("------")
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Alterar")
        print("4. Excluir")
        print("0. Sair")

        input_opcao = input("Opção : ")
        
        if input_opcao  == "1":
            telaVenderCadastrar ()
        elif input_opcao == "2":
            pass
        elif input_opcao == "3":
            pass
        elif input_opcao == "4":
            pass
        elif input_opcao == "0":
            break
        else:
            input("Escolha opção certa ! Continue com enter...")

def telaVenderCadastrar():
    os.system("clear")
    print("Vendas - Cadastro")
    print("-----------------")
    input_data = input("Data do pedido : ")

    lista_produtos = []
    while True:
        input_codigo_produto = input("Codigo do produto : ")
        input_qte_produto = input("Quantidade : ")
        lista_produtos.append((input_codigo_produto, input_qte_produto))
        while True:
            desejaContinuar = input("Deseja adicionar mais (s/n) ? : ").upper()
            if desejaContinuar in ("S", "N"):
                break
            input("Erro. Digite valor correto")

        if desejaContinuar == "N":
            break
            # Se nao deseja adicionar mais, 
            # Continua para proximo passo 
    print("Pedido feito : ")
    print(f"Data : {input_data}")
    for codigo, quantidade in lista_produtos:
        print(f"Codigo do produto {codigo} | Quantidade : {quantidade} ")
    input("guardando dados ...")
    time.sleep(3)
    input("... gravado !  ")

    # TODO : Aqui vai ser gravado dados para banco de dados 

def telaVenderConsultar():
    print("Consultar Pedido")
    print("----------------")
    print("1. Hoje")
    print("2. Por data")
    print("3. Por codigo")
    while True:
        opcao = input("\n> Opção: ")

        if opcao in ("1", "2", "3"):
            break
        else:
            input("Opção inválida! .. Enter para continuar")

    # Parte 1 : Consultar por hoje 

    # Parte 2 : Consultar por data escolhida

    # Parte 3 : Consultar por codigo de pedido

