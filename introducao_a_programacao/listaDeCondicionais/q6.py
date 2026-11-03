"""
6. Elabore uma função que receba três números e mostre o maior e o menor deles.
"""

def showMaiorMenor(x, y, z):

    #verifica o maior de todos
    if(x > y and x > z):
        maior = x
    elif(y > x and y > z):
        maior = y
    else:
        maior = z

    #verifica o menor de todos
    if(x < y and x < z):
        menor = x
    elif(y < x and y < z):
        menor = y
    else:
        menor = z

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")    

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

showMaiorMenor(n1, n2, n3)
