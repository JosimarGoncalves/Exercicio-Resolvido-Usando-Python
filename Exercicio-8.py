""" 8) Crie um programa que recebe o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 

a. A idade dessa pessoa;
b. Quantos anos ela terá em 2050. """

anoNascimento = int(input("Informe ano de nascimento: "))
anoAtual = int(input("Informe ano atual:"))

def CalcularIdade():
    resultadoIdade = anoAtual - anoNascimento
    resultadoIdadeFutura = 2050 - anoNascimento
    print("Sua idade atual é: ",resultadoIdade)
    print("Sua idade no ano de 2050 será: ",resultadoIdadeFutura)

CalcularIdade()    