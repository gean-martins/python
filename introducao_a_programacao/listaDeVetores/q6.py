'''
    6) Dados dois vetores A e B com os dados ordenados, construa um algoritmo para intercalar os
vetores A e B de tal modo que o novo vetor C também esteja ordenado. Exemplo: A{1,3,4,7} e
B{2,5,6,8} → C{1,2,3,4,5,6,7,8}
'''

N = 4

A = [1,3,4,7]
B = [2,5,6,8]
C = []

#esse loop dobra o tamanho do vetor C
for i in range(N):
    C.append(A[i])
    C.append(B[i])

#ordena
for i in range(N*2):
    for j in range(N*2-i-1):
        if(C[j] > C[j+1]):
            aux = C[j]
            C[j] = C[j+1]
            C[j+1] = aux

print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)
