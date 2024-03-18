### 2) Crie um código que seja capaz de calcular a soma, subtração, divisão e multiplicação de dois números, depois exiba os valores no console. 
 ###

valorEntrada1 = float(input("Digite o primeiro numero a ser calculado: "))
valorEntrada2 = float(input("Digite o segundo numero a ser calculado: "))

def CalcularValores():
    soma = valorEntrada1 + valorEntrada2
    subtracao = valorEntrada1 - valorEntrada2
    divisao = valorEntrada1 / valorEntrada2
    multiplicacao = valorEntrada1 * valorEntrada2

    print("Valor Somado é: ", soma)
    print("Valor Subtraido é: ",subtracao)
    print("Valor Divisao é:", divisao)
    print("Valor Multiplicacao é: ",multiplicacao)

CalcularValores()    

