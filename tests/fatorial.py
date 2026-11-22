#Como que calcula o fatorial de um número?

N = 5

fatorial = N

for i in range(N-1, 0, -1):
    fatorial *= i

print(fatorial)

