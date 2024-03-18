### 7) Crie um programa que mostra o valor do IMC (indice de massa corporal), fórmula IMC= peso / (altura * altura) ###

altura = float(input("Informe sua altura:  "))
peso = float(input("Informe seu peso"))

def CalcularImc():
    resultado = peso / (altura * altura)
    print("Seu IMC é: ", resultado)

CalcularImc()    