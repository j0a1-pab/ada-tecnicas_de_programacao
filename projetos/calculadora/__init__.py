from funcoes import soma
from funcoes import multiplicacao

def calcula(x, y, operacao):
    if operacao == "+":
        return soma(x, y)
    elif operacao == "*":
        return multiplicacao(x, y)