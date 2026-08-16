import os
import time
from services.services_produtos import procurar_codigo
from services.services_vender import service_venderCadastro

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
            telaVenderConsultar()
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
        while True:
            input_codigo_produto = input("Codigo do produto : ")
            dados , founded = procurar_codigo(input_codigo_produto)
            if founded :
                id = dados[0]
                nome = dados[2]
                print(f"Codigo achado : {input_codigo_produto} - {nome}")
                break
            else:
                print("ERRO : Codigo nao valido!")
        
        input_qte_produto = input("Quantidade : ")
        lista_produtos.append((
            id,
            input_codigo_produto, 
            nome,
            input_qte_produto))
        while True:
            desejaContinuar = input("Deseja adicionar mais (s/n) ? : ").upper()
            if desejaContinuar in ("S", "N"):
                break
            input("Erro. Digite valor correto")

        if desejaContinuar == "N":
            break
            # Se nao deseja adicionar mais, 
            # Continua para proximo passo 
    print(f"Data : {input_data}")
    for id, codigo, nome, quantidade in lista_produtos:
        print(f"Codigo do produto {codigo} |  {nome}  | Quantidade : {quantidade} ")
    input("guardando dados ...")
    
    # TODO iniciar gravação 
    # Enviar lista cabecalho, lista produtos 

    lista_cabecalho = []
    
    # Cabecalho : Data 
    lista_cabecalho.append(input_data)
   
    resultado = service_venderCadastro(lista_cabecalho, lista_produtos) 
    input("... gravado !  ")


def telaVenderConsultar():
    os.system("clear")
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
    if opcao == "1":
        input("Você escolheu opção 1 . Consultar hoje ")
        script_sql = ""

        print("Cabecalho")
        print("Pedido numero : 001")
        print("Data : 01/01/2026")
        print("Valor total : 200,00\n")
        print("Detalhe: ")
        print("Codigo produto   |   Quantidade   |   Preco unittario | Preco total ")
        input("continue ...")
    # Parte 2 : Consultar por data escolhida
    elif opcao == "2":
        input("Você escolheu opção 2 . Consultar por data ")
        script_sql = ""
    # Parte 3 : Consultar por codigo de pedido
    elif opcao == "3":
        input("Você escolheu opção 3 . Consultar por codigo de pedido ")
        script_sql = ""

    # TODO: Aqui vai inserir o comando script para procurar pedido


