'''
    22) Escreva um algoritmo que leia um vetor H[40] de reais e retorna um vetor de índices X. X deve
conter os índices de H dispostos de forma que os valores de H fiquem em ordem crescente.
'''

TAM_VET = 5 #por enquanto...

def organizaPorIndice():
    H = []
    auxVet = []

    #pede números ao usuário
    for i in range(TAM_VET):
        n = float(input("Digite um número: "))
        H.append(n)
        auxVet.append(n)

    #organiza em um vetor auxiliar
    for i in range(TAM_VET):
        houveTroca = False
        for j in range(TAM_VET-i-1):
            if(auxVet[j] > auxVet[j+1]):
                auxNum = auxVet[j]
                auxVet[j] = auxVet[j+1]
                auxVet[j+1] = auxNum
                houveTroca = True
        if(not houveTroca):
            break

    #organiza os índicies
    indices = []
    for i in range(TAM_VET):
        for j in range(TAM_VET):
            if(H[j] == auxVet[i]):
                indices.append(j)
    
    return indices

X = organizaPorIndice()

print("------------------------------")
print(f"Vetor com índices ordenados: {X}")      

