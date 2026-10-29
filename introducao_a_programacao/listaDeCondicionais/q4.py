"""
4. Elabore uma função que receba três números e mostre-os em ordem decrescente
"""

def ordena(x, y, z):
    maior = 0
    meio = 0
    menor = 0

    if(x >= y and x >= z):
        if(y > z):
            maior = x
            meio = y
            menor = z
        else:
            maior = x
            meio = z
            menor = y
    
    elif(y >= x and y >= z):
        if(x > z):
            maior = y
            meio = x
            menor = z
        else:
            maior = y
            meio = z
            menor = x
    
    elif(z >= x and z >= y):
        if(x > y):
            maior = z
            meio = x
            menor = y
        else:
            maior = z
            meio = y
            menor = x

    print("Em ordem decrescente:")
    print(f"{maior}, {meio}, {menor}")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

ordena(n1, n2, n3)
