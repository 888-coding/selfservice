# teste 
import os
from services.services_relatorios import serviceRelatorioVendasDiario
from telas.tela_principal import telaPrincipal
from db.init_db import checkDb

checkDb()

print("teste de relatorio diario\n\n")

dia = input("dia : ")
mes = input("mes : ")
ano = input("ano : ")

data_digitada = ano + "-" + mes + "-" + dia

lista_cabecalho, lista_detalhes = serviceRelatorioVendasDiario(data_digitada)

print("Cabecalho : \n")
for dado in lista_cabecalho:
    print("\n Proximo do cabecalho\n")
    print(dado)

print("\nDetalhes : \n")
for dado in lista_detalhes:
    print("\nProximo do Detalhes\n")
    print(dado)