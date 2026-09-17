#realiza o cálculo de bhaskara e exibe quais são as raízes da função
#caso o delta seja negativo, o tipo de x1 e de x2

#A, B e C de uma função, as raízes deve ser 1 e -0.5
a = 8
b = -4
c = -4

delta = b ** 2 - 4 * a * c

x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

print(f"Valor de X1: {x1}")
print(f"Valor de X2: {x2}")
