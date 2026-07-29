
# Responsável validar os dados dos incidentes gerados.

def validar_nulo(dado_incidente):

    if dado_incidente is None:
        return False
    else:
        return True

def validar_id(id):

    if not validar_nulo(id):
        return False
    
    if not id.startswith("INC"):
        return False

    if len(id) != 9:
        return False

    return True

def validar_data_abertura(data_abertura):

    if not validar_nulo(data_abertura):
        return False

    return True

def validar_sistema(sistema):

    if not validar_nulo(sistema):
        return False

    if sistema not in ("Portal de Vendas", "API de pagamentos", "Autenticação", "Catálogo de Produtos"):
        return False

    return True

def validar_status(status):

    if not validar_nulo(status):
        return False

    if status not in ("Em andamento","Aberto", "Resolvido","Em espera"):
        return False

    return True

def validar_data_fechamento(data_abertura, data_fechamento, status):


    if status == "Resolvido" and data_fechamento is None:
        return False

    if data_fechamento is not None and data_fechamento < data_abertura:
        return False

    return True

def validar_categoria(categoria):

    if categoria is not None and categoria not in ("Infraestrutura", "Banco de dados","Rede","Aplicação"):
        return False

    return True

def validar_severidade(severidade):

    if severidade is not None and severidade not in ("Baixa","Média","Alta","Crítica"):
        return False

    return True

def validar_responsavel(responsavel):

    if responsavel is not None and responsavel not in ("Maria Silva","Carlos Macedo","Guilherme Silverio","Matheus Ferreira","Nathalia Moreira","Juliana Mendonça"):
        return False

    return True

def validar_descricao(descricao):

    if descricao is not None and descricao not in ("Usuário não consegue acessar o sistema","Erro ao processar pagamento","Banco de dados indisponível","Timeout na API de autenticação","Lentidão no poral de vendas"):
        return False

    return True

def validar_prioridade(prioridade):

    if prioridade is not None and prioridade not in ("Baixa", "Média", "Alta"):
        return False

    return True


## Função que valida os dados dos incidentes

def validar_dados_incidente(incidente):

    if not validar_id(incidente["id_incidente"]):
        return False

    if not validar_data_abertura(incidente["data_abertura"]):
        return False

    if not validar_sistema(incidente["sistema"]):
        return False

    if not validar_status(incidente["status"]):
        return False

    if not validar_data_fechamento(
        incidente["data_abertura"],
        incidente["data_fechamento"],
        incidente["status"]
    ):
        return False

    if not validar_categoria(incidente["categoria"]):
        return False

    if not validar_severidade(incidente["severidade"]):
        return False

    if not validar_responsavel(incidente["responsavel"]):
        return False

    if not validar_descricao(incidente["descricao"]):
        return False

    if not validar_prioridade(incidente["prioridade"]):
        return False

    return True

    



