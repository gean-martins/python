'''
    26) Elabore uma rotina que leia um vetor K[50] de reais e retorne a quantidade de valores acima da
média aritmética dos valores em K.
'''

TAM_VET = 50

def acimaDaMedia():
    K = []
    media = 0
    cont = 0

    for i in range(TAM_VET):
        K.append(float(input("Digite um número: ")))
        media += K[i]
    media = media / TAM_VET

    for i in range(TAM_VET):
        if(K[i] > media):
            cont += 1

    return cont

c = acimaDaMedia()
print(f"Quantidade de valores acima da média: {c}")

