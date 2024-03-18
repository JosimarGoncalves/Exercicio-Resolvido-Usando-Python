''' 10) Elabore um algoritmo que determine o consumo médio de um automóvel sendo fornecida a distancia total percorrida pelo automóvel e o total de combustível gasto. '''

distanciaPercorrida = float(input("Informe distância percorrida: "))
quantidadeCombustivelGasto = float(input("Informe quantidade de combustivel gasto: "))


def CalcularMedia():
    resultado = distanciaPercorrida/quantidadeCombustivelGasto
    print("Consumo médio do automóvel foi de: ",resultado)

CalcularMedia()