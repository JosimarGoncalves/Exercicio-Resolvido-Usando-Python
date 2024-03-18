''' 9) Crie um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo.
Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que o pelo menos o custo do espetáculo seja alcançado.'''

valorEspetaculo = int(input('Qual Valor Do Espetaculo? ')) 
valorIngresso = int(input('Qual Valor Do Ingresso ? ')) 

def CalcularQuantidadeIngresso():
  resultado = valorEspetaculo / valorIngresso
  print(resultado)

CalcularQuantidadeIngresso()  
