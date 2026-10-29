"""
2. Elabore uma função que receba um valor e mostre na tela se o valor é positivo ou
negativo
"""

def positivoNegativo(a):
    if(a >= 0):
        print(f"O valor {a} é positivo")
    else:
        print(f"O valor {a} é negativo")

n = float(input("Digite um número: "))

positivoNegativo(n)
