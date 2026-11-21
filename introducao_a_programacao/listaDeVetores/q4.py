'''
    4) Faça um programa que carregue um vetor de nove elementos numéricos inteiros, calcule e
    mostre os números primos e suas respectivas posições.

    Os Números Primos são números naturais maiores do que 1 que possuem somente dois divisores, ou seja, são
    divisíveis por 1 e por ele mesmo.
'''

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    divCont = 0

    for j in range(vetor[i-1], 1, -1):
        if(vetor[i] == 1 or vetor[i] % j == 0):
            divCont += 1
        
    if(divCont == 0):
        print(f"O número {vetor[i]} é primo, e está na posição {i}")

