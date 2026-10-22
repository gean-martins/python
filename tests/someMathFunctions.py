import math

print("------------------------------------------")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
print("------------------------------------------")

#ceil
print(f"Valor de n1 arredondado pra cima: {math.ceil(n1)}")
print(f"Valor de n2 arredondado pra cima: {math.ceil(n2)}")

#floor
print(f"Valor de n1 arredondado pra baixo: {math.floor(n1)}")
print(f"Valor de n2 arredondado pra baixo: {math.floor(n2)}")

#pow
print(f"Valor de n1 elevado a 2: {math.pow(n1, 2)}")
print(f"Valor de n2 elevado a 2: {math.pow(n2, 2)}")

#max
print(f"Maior número digitado: {max(n1, n2)}")

#min
print(f"Menor número digitado: {min(n1, n2)}")
print("------------------------------------------")
