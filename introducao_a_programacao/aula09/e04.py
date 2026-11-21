'''
13) Escreva um algoritmo que leia um vetor Y[10] com valores no intervalo de 1 a 20 e cria um vetor
de contadores C. C deve ao final da rotina conter na posição 1 a quantidade de ocorrências do
valor 1 em Y, na posição 2 a quantidade de ocorrência do valor 2 em Y,...
'''

N = 10
Y = []
C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(N):

    numberOutRange = True
    while(numberOutRange):
        n = int(input("Digite um número entre 1 a 20: "))
        if(n >= 1 and n <= 20):
            Y.append(n)
            numberOutRange = False
        else:
            print("Número inválido, tente novamente...")

print("------------------------------------------")

for i in range(N):
    for j in range(N):
        if(Y[i] == Y[j]):
            C[i] += 1 

for i in range(N):
    print(f"O número {Y[i]} se repete {C[i]}x")

