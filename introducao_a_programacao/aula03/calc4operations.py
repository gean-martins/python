def calc4operations(x, y):
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y
    divisao = x / y

    print("----------------------------------")
    print(f"Resultado da soma: {soma}")
    print(f"Resultado da subtracao: {subtracao}")
    print(f"Resultado da multiplicacao: {multiplicacao}")
    print(f"Resultado da divisao: {divisao}")  
    print("----------------------------------")  

print("----------------------------------")
a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))

calc4operations(a, b)
