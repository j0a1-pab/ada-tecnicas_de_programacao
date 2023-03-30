def soma(a, b):
    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser uma string, recebido {a}, {type(a)}, {b}, {type(b)}.")
    
def multiplicacao(a, b):
    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        return a * b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser uma string, recebido {a}, {type(a)}, {b}, {type(b)}.")
    
def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print("Divisão inválida (indeteminação)")
        return 0