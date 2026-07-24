# Responsável por gerar dados fictícios de incidentes de TI.

from datetime import datetime
 
def gerar_incidente():

    incidente = {
        "id_incidente": "INC00001",
        "data_abertura": "24/07/2026",
        "sistema": "Portal de Vendas",
        "status": "Aberto"
        }
    return incidente

if __name__ == "__main__":

    resultado = gerar_incidente()
    print(resultado)
