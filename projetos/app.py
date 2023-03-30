import os, sys
sys.path.insert(0, os.getcwd())

from calculadora import calcula

n1 = float(input("n1: "))
n2 = float(input("n2: "))
op = input("operação (símbolo = [+, -, *, /]): ")
print(calcula(n1, n2, op))