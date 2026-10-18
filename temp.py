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

listaDados = serviceRelatorioVendasDiario(data_digitada)

print("Lista : \n")
for dado in listaDados:
    print(f"idSelling : {dado["idSelling"]}")
