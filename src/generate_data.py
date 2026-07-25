# Responsável por gerar dados fictícios de incidentes de TI.

from datetime import datetime

def gerar_incidente(numero_incidente):

    data_abertura = datetime.now().date().isoformat()
    id_incidente = f"INC{numero_incidente:06d}"

    incidente = {
        "id_incidente": id_incidente,
        "data_abertura": data_abertura,
        "sistema": "Portal de Vendas",
        "status": "Aberto"
        }
    return incidente

def gerar_incidentes(quantidade):

    lista_incidentes = []

    for i in range(quantidade):
            lista_incidentes.append(gerar_incidente(i + 1))
    return lista_incidentes

if __name__ == "__main__":

    resultado = gerar_incidentes(2)
    print(resultado)
