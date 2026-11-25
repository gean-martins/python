def ler_lista(nome, tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(float(input(f"Digite o {i+1}º valor de {nome}: ")))

    return lista

def calcular_uniao(lista_x, lista_y):

    uniao = []

    #code here
    for i in range(10):
        insertFromX = True
        insertFromY = True

        for j in range(len(uniao)):
            if(uniao[j] == lista_x[i]):
                insertFromX = False

        if(insertFromX):
            uniao.append(lista_x[i])

        for j in range(len(uniao)):
            if(uniao[j] == lista_y[i]):
                insertFromY = False

        if(insertFromY):
            uniao.append(lista_y[i])

    return uniao

def main():
    X = ler_lista('X', 10)
    Y = ler_lista('Y', 10)
    U = calcular_uniao(X, Y)

    print("----------------------------------")
    print(f"Lista X: {X}")
    print(f"Lista Y: {Y}")
    print("----------------------------------")
    print(f"Lista U: {U}")

if __name__ == "__main__":
    main()