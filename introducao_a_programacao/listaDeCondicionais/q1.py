"""
1. Elabore uma função leia dois números e retorne o maior deles. Ao final mostre o
maior na tela.
"""

def bigNumber():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))

    if(a > b):
        return a
    else:
        return b

print(f"O maior número é: {bigNumber()}")
