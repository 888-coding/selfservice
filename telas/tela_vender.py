import os
import time
from services.services_produtos import procurar_codigo
from services.services_vender import service_venderCadastro, service_venderConsultaPorData, consultarPorNumeroPedido

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
    while True:
        dia = input("Dia : ")
        if dia.isnumeric():
            break
        else:
            print("Erro na data!")
            time.sleep(1.5)
    while True:
        mes = input("Mês : ")
        if mes.isnumeric():
            break
        else:
            print("Erro na data !")
            time.sleep(1.5)
    while True:
        ano = input("Ano : ")
        if ano.isnumeric():
            break
        else:
            print("Erro na data ! ")
            time.sleep(1.5)

    input_data = ano + "-" + mes.zfill(2) + "-" + dia.zfill(2)
    os.system("clear")
    print("**Pedido \n--------\n\n")
    print(f"\nData Preenchida : {input_data}\n\n")
    lista_produtos = []
    while True:
        while True:
            input_codigo_produto = input("Codigo do produto : ")
            dados , founded = procurar_codigo(input_codigo_produto)
            if founded :
                id = dados[0]
                nome = dados[2]
                preco = dados[3]
                print(f"Codigo achado : {input_codigo_produto} - {nome} - Preço : {preco}")
                break
            else:
                print("ERRO : Codigo nao valido!")

        input_qte_produto = input("Quantidade : ")
        lista_produtos.append((
            id,
            input_codigo_produto,
            nome,
            input_qte_produto,
            preco))
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
    for id, codigo, nome, quantidade, preco in lista_produtos:
        print(f"Codigo do produto {codigo} |  {nome}  | Quantidade : {quantidade} | Preço : {preco}")
    print("guardando dados ...")
    time.sleep(1.5)

    lista_cabecalho = []
    lista_cabecalho.append(input_data)

    resultado, id_selling = service_venderCadastro(lista_cabecalho, lista_produtos)
    if resultado:
        input(f"\n\nPedido {id_selling} cadastrado. Continue ...")

def telaVenderConsultar():
    os.system("clear")
    print("Consultar Pedido")
    print("----------------")
    print("1. Hoje")
    print("2. Por data")
    print("3. Por codigo")
    print("0. Sair")
    while True:
        opcao = input("\n> Opção: ")

        if opcao == "1":
            t = time.localtime()
            dia, mes, ano = t.tm_mday, t.tm_mon, t.tm_year
            hoje = f"{ano}-{mes:02d}-{dia:02d}"
            dados = service_venderConsultaPorData(hoje)
            time.sleep(0.5)
            print("..consultando")
            time.sleep(0.5)
            print("..aguarde ")
            os.system("clear")
            print("\n\nPedidos de Hoje")
            print("===============")
            if dados:
                for dado in dados :
                    print(f"Pedido numero : {dado[0]}")
                    time.sleep(0.5)
                    print(f"Desconto :{dado[1]}")
                    time.sleep(0.5)
                    print(f"Valor total : {dado[2]}")
                    print("\n")
                    time.sleep(0.5)
            else:
                print("\n\nNão existe dados hoje !")
                time.sleep(1.5)
            input("> Pressione enter para continuar ...")
            break
        # Parte 2 : Consultar por data escolhida
        elif opcao == "2":
            print("Você escolheu opção 2 . Consultar por data ")
            dia = input("Dia: ").zfill(2)
            mes = input("Mês: ").zfill(2)
            ano = input("Ano: ")

            data_a_procurar = ano + "-" + mes + "-" + dia

            dados = service_venderConsultaPorData(data_a_procurar)
            time.sleep(0.5)
            print("..consultando")
            time.sleep(0.5)
            print("..aguarde ")
            os.system("clear")
            print("\n\nPedidos de Hoje")
            print("===============")
            if dados:
                for dado in dados :
                    print(f"Pedido numero : {dado[0]}")
                    time.sleep(0.5)
                    print(f"Desconto :{dado[1]}")
                    time.sleep(0.5)
                    print(f"Valor total : {dado[2]}")
                    print("\n")
                    time.sleep(0.5)
            else:
                print("\n\nNão existe dados hoje !")
                time.sleep(1.5)
            input("> Pressione enter para continuar ...")
            break
        # Parte 3 : Consultar por codigo de pedido
        #
        elif opcao == "3":
            print("Procurar por codigo.")
            time.sleep(1.0)
            os.system("clear")
            time.sleep(1.0)
            print("Procurar por Numero de pedido")
            print("-----------------------------")
            numeroPedido = input("Numero do pedido :  ")
            dado = consultarPorNumeroPedido(numeroPedido)
            if dado:
                time.sleep(0.5)
                print(f"\nPedido : {dado[0]}")
                time.sleep(0.7)
                print(f"Data : {dado[3]}")
                time.sleep(0.7)
                print(f"Valor total : {dado[2]}")
                time.sleep(0.7)
                input("\n\nDigite enter para continuar ...")
            else:
                time.sleep(1.5)
                print("Não encontrado !")
                time.sleep(1.0)
                input("Digite enter para continuar ...")
            break
        elif opcao == "0":
            break
        else:
            input("Opcao invalida ! Favor corrigir")
