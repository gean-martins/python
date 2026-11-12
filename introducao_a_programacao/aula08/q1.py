def whatIsImpar(vetor, aux):
    i = 0
    j = 0

    while(i < 6):
        if(vetor[i] % 2 != 0):
            aux.append(vetor[i])
            j += 1

        i += 1

def contImpar(vetor):
    i = 0
    qtdImpar = 0

    while(i < 6):
        if(vetor[i] % 2 != 0):
            qtdImpar += 1

        i += 1

    return qtdImpar

def whatIsPar(vetor, aux):
    i = 0
    j = 0

    while(i < 6):
        if(vetor[i] % 2 == 0):
            aux.append(vetor[i])
            j += 1

        i += 1

def contPar(vetor):

    qtdPar = 0
    i = 0
    while(i < 6):
        if(vetor[i] % 2 == 0):
            qtdPar += 1
        i += 1

    return qtdPar

#main
i = 0
invalidOpt = True
iWantInsertNumbers = True
vetor = []
vetorPar = []
vetorImpar = []

print("-------------------------------------------------")
print("Você quer digitar números manualmente?")
print("[1] - Sim")
print("[2] - Não")

while(invalidOpt):
    opt = int(input("Digite a opção desejada: "))

    if(opt >= 1 and opt <= 2):
        match opt:
            case 1:
                iWantInsertNumbers = True
            case 2:
                iWantInsertNumbers = False
            case _:
                iWantInsertNumbers = False
    
        invalidOpt = False
    else:
        print("Opção inválida, tente novamente...")

#insere números no vetor
if(iWantInsertNumbers):
    while(i < 6):
        vetor.append(int(input("Digite um número: ")))
        i += 1
else: # 2 pares, 4 ímpares
    vetor.append(9)
    vetor.append(7)
    vetor.append(82)
    vetor.append(524)
    vetor.append(3)
    vetor.append(1)    

print("-------------------------------------------------")
print(f"{vetor}")
print("-------------------------------------------------")
print(f"Quantidade de números pares no vetor: {contPar(vetor)}")
whatIsPar(vetor, vetorPar)
print(vetorPar)
print("-------------------------------------------------")
print(f"Quantidade de números impares no vetor: {contImpar(vetor)}")
whatIsImpar(vetor, vetorImpar)
print(vetorImpar)
print("-------------------------------------------------")
