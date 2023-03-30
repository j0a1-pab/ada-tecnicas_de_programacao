from funcoes import *

def calcula(x, y, operacao):
    if operacao == "+":
        return soma(x, y)
    elif operacao == "*":
        return multiplicacao(x, y)
    elif operacao == "-":
        return subtracao(x, y)