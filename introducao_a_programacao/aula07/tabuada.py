invalidOption = True
n = 0

def calcTabuada(x):
    
    i = 1

    while(i <= 10):
        r = x * i
        print(f"{x} x {i} = {r}")
        i += 1

while(invalidOption):
    
    n = int(input("Digite um número entre 1 a 10: "))

    if(n > 0 and n <= 10):
        invalidOption = False
    else:
        print("Número inválido, tente novamente...")

calcTabuada(n)
