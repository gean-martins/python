def calcFatorial(x):
    i = x
    fat = 1

    while(i >= 1):
        fat *= i

        i -= 1

    return fat

a = []
b = []
N = 15
i = 0

while(i < N):
    a.append(int(input("Digite um número: ")))
    i += 1

i = 0

while(i < N):
    b.append(calcFatorial(a[i]))
    i += 1

print(a)
print(b)
