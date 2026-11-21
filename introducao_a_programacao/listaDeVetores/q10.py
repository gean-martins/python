'''
    10) Escreva um algoritmo que leia um vetor B[15] de inteiros e escreva um vetor C apenas com os
primos de B.
'''

N = 15

B = []
C = []

for i in range(N):
    B.append(int(input("Digite um número: ")))

for i in range(N):
    divPrimo = 0
    for j in range(B[i-1], 1, -1):
        if(B[i] == 1 or B[i] % j == 0):
            divPrimo += 1

    if(divPrimo == 0):
        C.append(B[i])

print("---------------------------")
print(f"Vetor B: {B}")
print(f"Vetor C: {C}")

