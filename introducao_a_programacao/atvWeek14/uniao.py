'''
Desenvolva um programa em Python que leia duas listas de números reais (float), denominadas X e Y, cada uma contendo exatamente 10 elementos, e gere uma terceira lista U representando a união entre X e Y (todos os elementos presentes em X ou em Y, sem valores repetidos).

Requisitos Obrigatórios
Modularização com funções: Seu programa deve conter, no mínimo, as seguintes funções:

ler_lista(nome, tamanho): recebe o nome da lista (para exibição no prompt) e a quantidade de elementos, realiza a leitura dos valores reais via teclado utilizando um laço for e retorna a lista preenchida.

calcular_uniao(lista_x, lista_y): recebe as duas listas como parâmetros, constrói e retorna uma nova lista U contendo todos os elementos de lista_x e lista_y, garantindo que não haja duplicatas (inclusive caso existam valores repetidos dentro da própria lista X ou dentro da própria lista Y).

main(): função principal que coordena as chamadas às funções de leitura, de processamento e de exibição dos resultados.

Estrutura de repetição: Utilize obrigatoriamente a estrutura for tanto para a leitura dos dados quanto para percorrer as listas na construção da união.

Restrição: Não utilize a estrutura de conjuntos (set) nem métodos prontos de união em Python. A verificação de duplicidade deve ser feita explicitamente durante o percurso das listas (por exemplo, verificando se o elemento já pertence à lista U antes de inseri-lo com .append()).

Entrada e saída:

A entrada deve informar ao usuário qual lista e qual posição está sendo lida (ex.: Digite o 1º valor de X:).

Ao final, exiba as listas X, Y e a lista resultante U de forma clara e organizada.
'''

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
