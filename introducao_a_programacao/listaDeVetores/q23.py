'''
23) Escreva um algoritmo que leia um vetor de inteiros F[34] e retorna-o “compactado”, sem valores
repetidos, nulos (zeros) ou negativos.
'''

TAM_VET = 34

F = []
compact = []

for i in range(TAM_VET):
    F.append(int(input("Digite um número: ")))

for i in range(TAM_VET):
    if(F[i] > 0):
        insertNumber = True
        for j in range(len(compact)):
            if(F[i] == compact[j]):
                insertNumber = False
        
        if(insertNumber):
            compact.append(F[i])

print("-----------------------------------")
print(f"Vetor inserido: {F}")
print(f"Vetor compactado: {compact}")

