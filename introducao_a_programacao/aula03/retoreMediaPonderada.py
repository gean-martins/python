def calcMediaPonderada(n1, n2, n3, p1, p2, p3):
    return (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)

print("------------------------------------")
nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))
nota3 = float(input("Digite o valor da nota 3: "))
print("------------------------------------")
peso1 = float(input("Digite o valor do peso 1: "))
peso2 = float(input("Digite o valor do peso 2: "))
peso3 = float(input("Digite o valor do peso 3: "))
print("------------------------------------")

mediaPonderada = calcMediaPonderada(nota1, nota2, nota3, peso1, peso2, peso3)

print(f"O valor da média ponderada é: {mediaPonderada}")
print("------------------------------------")
