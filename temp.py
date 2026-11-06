# teste 
import os
from rich import print as rprint
from rich.console import Console
from rich.table import Table

from services.services_relatorios import serviceRelatorioVendasDiario
from telas.tela_principal import telaPrincipal
from db.init_db import checkDb

checkDb()

print("teste de relatorio diario\n\n")

dia = input("dia : ")
mes = input("mes : ")
ano = input("ano : ")

data_digitada = ano + "-" + mes + "-" + dia

listaDados = serviceRelatorioVendasDiario(data_digitada)

table = Table(title="Star wars movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The rise of Skywalker", "$952,110,690")

console = Console()
console.print(table)


print("Lista : \n")
for dado in listaDados:
    print(f"idSelling : {dado["idSelling"]}")

print("Imprimindo o conteudo completo \n")

print(listaDados)
