from generate_data import gerar_incidentes
from validate_data import validar_dados_incidente

quantidade = 10
lista_incidentes = gerar_incidentes(quantidade)
lista_incidentes_validos = []
lista_incidentes_invalidos = []
lista_incidentes[3]["id_incidente"] = "ACb123"

for incidente in lista_incidentes:
    if validar_dados_incidente(incidente):
        lista_incidentes_validos.append(incidente)
    else:
        lista_incidentes_invalidos.append(incidente)

print(lista_incidentes_validos)
print(lista_incidentes_invalidos)