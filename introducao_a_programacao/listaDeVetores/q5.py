'''
5)Escreva um algoritmo para ler 8 números inteiros que serão colocados em um vetor chamado
temp. Depois da leitura de todos os números, calcular e imprimir a média deles.
'''

N = 8
temp = []

for i in range(N):
    temp.append(int(input("Digite um número: ")))

print("------------------------------")

soma = 0
for i in range(N):
    soma += temp[i]

media = soma / N

print(f"A média dos números digitados é: {media}")

