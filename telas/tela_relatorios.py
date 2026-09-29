import os, time

def telaRelatorios():
    while True:
        os.system("clear")
        print("RELATORIOS")
        print("==========")
        print("1. VENDAS DIÁRIO")
        print("2. VENDAS MENSAL")
        print("3. POR PRODUTO")
        print("0. SAIR")

        opcao = input("> Opção : ")
        if opcao == "1":
            telaVendasDiario()
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "0":
            break
        else:
            print("\nX ERRO ! OPÇÃO INVÁLIDA")
            time.sleep(2.0)

def telaVendasDiario():
    while True:
        os.system("clear")
        print("\nRELATÓRIO DE VENDAS DIÁRIO")
        print("==========================")
        print("1. HOJE")
        print("2. DATA ESPECIFICA")
        print("0. SAIR")
        opcao = input("> OPÇÃO : ")

        if opcao == "1":
            pass
        elif opcao == "2":
            os.system("clear")
            print("RELATORIO DE VENDAS DIÁRIO")
            print("==========================")
            time.sleep(1.0)
            print("DATA ESPECÍFICA")
            dia = input("\n> Dia:").zfill(2)
            time.sleep(0.8)
            mes = input("\n> Mês:").zfill(2)
            time.sleep(0.8)
            ano = input("\n> Ano:")
            time.sleep(0.8)
            data_escolhida = ano + "-" + mes + "-" + dia

            print(data_escolhida)
            time.sleep(3.0)
        elif opcao == "0":
            break
        else:
            print("X ERRO ! OPÇÃO INVÁLIDA")
            time.sleep(2.0)
