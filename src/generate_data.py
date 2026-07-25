# Responsável por gerar dados fictícios de incidentes de TI.

from datetime import datetime, timedelta
import random

# Funções auxialiares

def gerar_sistema():

    sistemas = [
         "Portal de Vendas",
         "API de pagamentos",
         "Autenticação",
         "Catálogo de Produtos"
    ]

    sistema = random.choice(sistemas)

    return sistema

def gerar_status():

    lista_status = [
         "Em andamento",
         "Aberto",
         "Resolvido",
         "Em espera"
    ]

    status = random.choice(lista_status)
    return status

def gerar_data_abertura():

    aleatorio = random.randint(1,30)
    hoje = datetime.now().date()
    data = hoje - timedelta(days=aleatorio)
    return data    

def gerar_data_fechamento(data_abertura, status):

    hoje = datetime.now().date()
    dias_disponiveis = (hoje - data_abertura).days
    aleatorio = random.randint(0,dias_disponiveis)

    if status in ("Em andamento","Aberto","Em espera"):
          data_fechamento = None
    else:
        data_fechamento = data_abertura + timedelta(days=aleatorio)     
    return data_fechamento

# Função principal de geração de um incidente

def gerar_incidente(numero_incidente):

    data_abertura = gerar_data_abertura()
    id_incidente = f"INC{numero_incidente:06d}"
    sistema = gerar_sistema()
    status = gerar_status()
    data_fechamento = gerar_data_fechamento(data_abertura, status)

    incidente = {
        "id_incidente": id_incidente,
        "data_abertura": data_abertura.isoformat(),
        "sistema": sistema,
        "status": status,
        "data_fechamento": (data_fechamento.isoformat() if data_fechamento else None)
        }
    return incidente

# Função que gera vários incidentes
def gerar_incidentes(quantidade):

    lista_incidentes = []

    for i in range(quantidade):
        lista_incidentes.append(gerar_incidente(i + 1))
    return lista_incidentes

# Ponto de entrada do programa
if __name__ == "__main__":

    resultado = gerar_incidentes(2)
    print(resultado)
