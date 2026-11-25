'''
Desenvolva um programa em Python que leia duas listas de números inteiros (int): a lista X, contendo exatamente 15 elementos, e a lista G, contendo exatamente 10 elementos. O programa deve gerar uma terceira lista chamada Inter, que representa a intersecção entre X e G (apenas os elementos que aparecem simultaneamente em ambas as listas, sem valores repetidos).

Requisitos Obrigatórios
Modularização com funções: Seu programa deve ser estruturado com, no mínimo, as seguintes funções:

ler_lista_inteiros(nome, tamanho): recebe o nome identificador da lista e o seu tamanho, lê os números inteiros fornecidos pelo usuário usando um laço for e retorna a lista preenchida.

calcular_interseccao(lista_x, lista_g): recebe as duas listas como parâmetros e retorna a lista Inter contendo apenas os elementos comuns a ambas, sem repetições.

main(): função principal responsável por invocar a leitura de X (15 elementos) e G (10 elementos), chamar o cálculo da interseção e imprimir o resultado.

Estrutura de repetição: Utilize obrigatoriamente laços for para a leitura das entradas e para a comparação entre os elementos das duas listas.

Restrição pedagógica: Não utilize conjuntos (set) ou operações prontas de intersecção. A lógica de busca de elementos comuns e de prevenção de duplicatas na lista Inter deve ser implementada manualmente com laços for e estruturas condicionais (if).

Entrada e saída:

Indique ao usuário qual lista e qual índice estão sendo solicitados durante a leitura.

Exiba as listas X, G e Inter ao final da execução. Caso não existam elementos em comum entre as duas listas, exiba uma mensagem informando que a interseção é vazia (além ou no lugar da lista vazia []).
'''

TAM_X = 15
TAM_G = 10

def ler_lista_inteiros(nome, tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(int(input(f"Digite o {i+1}° número da lista {nome}: ")))

    return lista

def calcular_interseccao(lista_x, lista_g):
    intersecao = []

    for i in range(TAM_X):
        insertElement = True
        for j in range(TAM_G):
            if(lista_x[i] == lista_g[j]):
                for k in range(len(intersecao)):
                    if(lista_g[j] == intersecao[k]):
                        insertElement = False

                if(insertElement):
                    intersecao.append(lista_g[j])

    return intersecao

def main():
    X = ler_lista_inteiros('X', TAM_X)
    print("-----------------------------")
    G = ler_lista_inteiros('G', TAM_G)
    print("-----------------------------")
    Inter = calcular_interseccao(X, G)

    print(f"Lista X: {X}")
    print(f"Lista G: {G}")
    print("-----------------------------")
    if(len(Inter) == 0):
        print("Não existe nenhum elemento em comum entre a lista X e G")
    else:
        print(f"Lista de Interseções: {Inter}")
    print("-----------------------------")

if __name__ == "__main__":
    main()
