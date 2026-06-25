# tela principal
import os 
from telas.tela_produtos import telaProdutos

def telaPrincipal():
    while True:
        os.system("clear")
        print("SISTEMA SELFSERVICE --- VERSÃO PRIMEIRO")
        print("---------------------------------------")
        print("1. PRODUTOS ")
        print("2. VENDER")
        print("3. RELATORIOS")
        print("4. SAIR")

        input_value = input("Digite algo : ")

        if input_value == "1":
            telaProdutos()
        elif input_value == "2":
            pass
        elif input_value == "3":
            pass
        elif input_value == "0":
            break
        else: 
            input("Opção invlaida.. Pressione Enter")


