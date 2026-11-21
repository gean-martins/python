'''
    18) Elabore um algoritmo que leia dois vetores X[15] e G[10] de inteiros e cria o vetor Inter. Inter
    (intersecção) deve conter os elementos comuns a X e G, sem repetição de valores.

IS NOT READY
'''

X_N = 15
G_N = 10
N_INTER = G_N

X = []
G = []
inter = []

for i in range(X_N):
    X.append(int(input("Digite um número para X: ")))

for i in range(G_N):
    G.append(int(input("Digite um número para G: ")))

for i in range(N_INTER):
    if(X[i] == G[i]):
        n = X[i]
        for j in range(len(inter)):
            if(inter[j] == n):
                break
    
        inter.append(X[i])

print(inter)

