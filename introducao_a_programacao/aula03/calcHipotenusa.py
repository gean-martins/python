def calcHipotenusa(x, y):
    return (x**2 + y**2) ** (1/2)

a = float(input("Digite o cateto oposto: "))
b = float(input("Digite o cateto adjacente: "))

hipotenusa = calcHipotenusa(a, b)

print(f"O valor da hipotenusa é: {hipotenusa}")
