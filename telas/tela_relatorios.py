import os, time
from datetime import date
from services.services_relatorios import serviceRelatorioVendasDiario
from rich import print as rprint
from rich.console import Console
from rich.table import Table


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
        # HOJE
        if opcao == "1":
            os.system("clear")
            print("RELATORIO DE VENDAS DIÁRIO")
            print("==========================")
            print("DATA DE HOJE : ")
            hoje = date.today()
            data_escolhida = hoje.strftime("%Y-%m-%d")
            print(f"data de hoje : {data_escolhida} ")

            time.sleep(1.5)
            # Chamada da funcao
            dados = serviceRelatorioVendasDiario(data_escolhida)
            # Chamada da funcao
            imprimirVendasDiario(dados)
        # DATA ESPECIFICA
        elif opcao == "2":
            os.system("clear")
            print("RELATORIO DE VENDAS DIÁRIO")
            print("==========================")
            print("DATA ESPECÍFICA")
            dia = input("> Dia: ").zfill(2)
            mes = input("> Mês: ").zfill(2)
            ano = input("> Ano: ")
            data_escolhida = ano + "-" + mes + "-" + dia

            print(data_escolhida)
            time.sleep(1.5)
            # Chamada da funcao
            dados = serviceRelatorioVendasDiario(data_escolhida)
            # Chamada da funcao
            imprimirVendasDiario(dados)
        elif opcao == "0":
            break
        else:
            print("X ERRO ! OPÇÃO INVÁLIDA")
            time.sleep(2.0)

# Imprimir Relatorio Diario 
def imprimirVendasDiario(dados):
    dados = dados 
    os.system("clear")
 
    # Calculo do valor total do dia
    valor_total = 0  
    for dado in dados:
        valor_total = valor_total + int(dado['totalValue'])
    rprint(f"\nValor total do dia : [green]{(valor_total/100):.2f}[/green]\n")
    # Print dos pedidos
    for dado in dados:
        print("----------------------------------------------\n")
        print(f"Pedido : {dado['idSelling']} - Desconto : {dado['discount']} Total : {dado['totalValue']/100:.2f}")
        detalhes = dado['detalhe']
        table = Table()
        # Codigo produto 
        table.add_column("Codigo", justify="left", style="cyan", no_wrap=True)
        # Nome do Produto 
        table.add_column("Nome do produto", justify="left", style="magenta")
        # Preco 
        table.add_column("Preço", justify="right", style="green")
        # Quantidade 
        table.add_column("Quantidade", justify="right")

        for detalhe in detalhes:
            #print(f"Produto : {detalhe['productCode']} - {detalhe['productName']} Preco: {detalhe['productPrize']/100:.2f} Qte: {detalhe['productQuantity']}")
            varCodigoProduto = f"{detalhe['productCode']}"
            varNomeProduto = f"{detalhe['productName']}"

            varPrecoProduto = f"{detalhe['productPrize']/100:.2f}"
            varQuantidadeProduto = f"{detalhe['productQuantity']}"
            table.add_row(varCodigoProduto, varNomeProduto, varPrecoProduto, varQuantidadeProduto)
        print("")
        console = Console()
        console.print(table)

    input("Continuar ... ")