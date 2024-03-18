### 5) Crie uma estrutura condicional capaz de apresentar no console a palavra "Games", se e somente se uma variável do tipo int for igual a 10. ###

valor = int(input("Entre com o Valor"))

def MostrarValor():
    if valor == 10:
        print("Games")

MostrarValor()