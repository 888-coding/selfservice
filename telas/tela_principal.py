# tela principal
import os 

def telaPrincipal():
    os.system("clear")
    print("Hello estou na tela")
    while True:
        input_value = input("Digite algo : ")

        if input_value == "hello":
            break

    pass
