import os

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
    while True:
        input_codigo_produto = input("Codigo do produto : ")
        input_qte_produto = input("Quantidade : ")
        
        while True:
            desejaContinuar = input("Deseja adicionar mais (s/n) ? : ").upper()
            if desejaContinuar != "S" and desejaContinuar != "N":
                input("Erro. Digite valor correto")
            else:
                break

        if desejaContinuar == "N":
            # Se nao deseja adicionar mais, 
            # Continua para proximo passo 




