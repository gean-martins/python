'''
    16) Escreva um algoritmo que leia um vetor Y[25] de inteiros e retorna a posição do seu maior e do
seu menor valor.
'''

N = 25

Y = []

def MaiorMenorPosition(vetor):
    maiorPosition = 0
    menorPosition = 0
    maiorNumero = vetor[0]
    menorNumero = vetor[0]

    for i in range(N):
        if(maiorNumero < vetor[i]):
            maiorNumero = vetor[i]
            maiorPosition = i

        if(menorNumero > vetor[i]):
            menorNumero = vetor[i]
            menorPosition = i

    return maiorPosition, menorPosition

for i in range(N):
    Y.append(int(input("Digite um número: ")))

maior, menor = MaiorMenorPosition(Y)

print(f"O maior valor está na posição {maior}")
print(f"O menor valor está na posição {menor}")

