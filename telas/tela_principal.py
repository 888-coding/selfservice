# tela principal
import os 

def telaPrincipal():
    os.system("clear")
    print("SISTEMA SELFSERVICE --- VERSÃO PRIMEIRO")
    print("---------------------------------------")
    print("1. PRODUTOS ")
    print("2. VENDER")
    print("3. RELATORIOS")
    print("4. SAIR")

    while True:
        input_value = input("Digite algo : ")

        if input_value == "1":
            pass
        elif input_value == "2":
            pass
        elif input_value == "3":
            pass
        elif input_value == "4":
            break

    pass
