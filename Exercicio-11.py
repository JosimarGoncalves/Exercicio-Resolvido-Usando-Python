'''11) Crie um programa que recebe a data de nascimento de uma pessoa e a data de hoje, e calcule aproximadamente, quantos dias ela viveu.Considere um mês com 30 dias e um ano com 365 dias.
Calcule aproximadamente, o tempo em dias , meses e em anos.'''

dataNascimentoAno = int(input("Informe seu ano de nascimento: "))
dataNascimentoMes = int(input("Informe seu mes de nascimento: "))
dataNascimentoDia = int(input("Informe dia do nascimento: "))

dataHojeAno = int(input("Informe o ano atual: "))
dataHojeMes = int(input("Informe o mes atual: "))
dataHojeDia = int(input("Informe o dia atual: "))


def CalcularDiasQueViveu():
    anoAproximado = dataHojeAno - dataNascimentoAno
    print("Anos Vividos é: ",anoAproximado)
    anoAproximado *= 365
    print("Quantidade de dias vividos é: ",anoAproximado)
    anoAproximado /= 30
    print("Quantidade de meses vividos é: ",anoAproximado)


CalcularDiasQueViveu()