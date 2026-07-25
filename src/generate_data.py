# Responsável por gerar dados fictícios de incidentes de TI.

from datetime import datetime, timedelta
import random

# Funções auxialiares

def gerar_sistema():

    lista_sistemas = [
         "Portal de Vendas",
         "API de pagamentos",
         "Autenticação",
         "Catálogo de Produtos"
    ]

    return random.choice(lista_sistemas)

def gerar_status():

    lista_status = [
         "Em andamento",
         "Aberto",
         "Resolvido",
         "Em espera"
    ]

    return random.choice(lista_status)

def gerar_categoria():

    lista_categorias = [
         "Infraestrutura",
         "Banco de dados",
         "Rede",
         "Aplicação"
    ]

    return random.choice(lista_categorias)

def gerar_severridade():

    lista_severidade = [
          "Baixa",
          "Média",
          "Alta",
          "Crítica"
     ]
    
    pesos = [50,30,15,5]

    severidade = random.choices(lista_severidade,weights=pesos)
    return severidade[0]

def gerar_resposnsavel():

    lista_responsavel = [
          "Maria Silva",
          "Carlos Macedo",
          "Guilherme Silverio",
          "Matheus Ferreira",
          "Nathalia Moreira",
          "Juliana Mendonça"
     ]

    return random.choice(lista_responsavel)

def gerar_descricao():

    lista_descricao = [
        "Usuário não consegue acessar o sistema",
        "Erro ao processar pagamento",
        "Banco de dados indisponível",
        "Timeout na API de autenticação",
        "Lentidão no poral de vendas"
    ]

    descricao = random.choice(lista_descricao)
    return descricao

def gerar_prioridade():

    lista_prioridades = [
        "Baixa",
        "Média",
        "Alta"
    ]

    pesos = [60,30,10]

    prioridade = random.choices(lista_prioridades,weights=pesos)

    return prioridade[0]

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
    categoria = gerar_categoria()
    severidade = gerar_severridade()
    resposnavel = gerar_resposnsavel()
    descricao = gerar_descricao()
    prioridade = gerar_prioridade()

    incidente = {
        "id_incidente": id_incidente,
        "data_abertura": data_abertura.isoformat(),
        "sistema": sistema,
        "status": status,
        "data_fechamento": (data_fechamento.isoformat() if data_fechamento else None),
        "categoria": categoria,
        "severidade": severidade,
        "responsavel": resposnavel,
        "descricao": descricao,
        "prioridade": prioridade
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

    resultado = gerar_incidentes(1)
    print(resultado)
