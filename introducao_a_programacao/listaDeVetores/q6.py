'''
    6) Dados dois vetores A e B com os dados ordenados, construa um algoritmo para intercalar os
vetores A e B de tal modo que o novo vetor C também esteja ordenado. Exemplo: A{1,3,4,7} e
B{2,5,6,8} → C{1,2,3,4,5,6,7,8}
'''

N = 4

A = [1,3,4,7]
B = [2,5,6,8]
C = []

for i in range(N):
    C.append(A[i])
    C.append(B[i])

#ordena
for i in range(N):
    if(C[i] > C[i+1]):
        aux = C[i]
        C[i] = C[i+1]
        C[i+1] = aux

print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)

