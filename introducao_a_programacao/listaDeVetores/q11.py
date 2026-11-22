'''
11) Escreva um algoritmo que leia um vetor X[5] de valores inteiros e não negativos e escreva um
vetor F com o fatorial de cada valor em X.
'''

N = 5

X = []
F = []

#pede os números ao usuário
for i in range(N):
    invalidNumber = True
    while(invalidNumber):
        number = int(input("Digite um número positivo: "))
        if(number >= 0):
            X.append(number)
            invalidNumber = False
        else:
            print("Número negativo é inválido, tente novamente...")

#calcula e faz append em F
for i in range(N):
    fact = X[i]
    for j in range(X[i]-1, 1, -1):
        fact *= j

    F.append(fact)

#imprime a resposta
print("-----------------------------")
print(f"Números digitados: {X}")
print(f"Fatorial dos números: {F}")

