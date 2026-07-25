import os 
from telas.tela_principal import telaPrincipal
from db.init_db import checkDb

def main():
    checkDb()
    telaPrincipal()


if __name__ == "__main__":
    main()
