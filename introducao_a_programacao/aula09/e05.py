'''
    15) Escreva um algoritmo que leia um vetor X[20] de reais e
    retorna o seu maior e o seu menor valor.
'''

N = 10
vetor = []

for i in range(N):
    vetor.append(float(input("Digite um número: ")))

nMax = vetor[0]
nMin = vetor[0]

for i in range(N):
    if(vetor[i] > nMax):
        nMax = vetor[i]
    elif(vetor[i] < nMin):
        nMin = vetor[i]

print("-----------------------------")
print(f"Vetor: {vetor}")
print(f"Maior valor digitado: {nMax}")
print(f"Menor valor digitado: {nMin}")

