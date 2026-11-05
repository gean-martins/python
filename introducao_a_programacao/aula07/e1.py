sum = 0
n = float(input("Digite um número: "))

if(n > 0):
    sum = n

while(n >= 0):
        n = float(input("Digite um número: "))

        if(n > 0):
            sum += n

print(f"Resultado da soma: {sum}")
