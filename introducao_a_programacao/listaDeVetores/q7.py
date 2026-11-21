'''
    7) Escreva um algoritmo que verifique se um valor X pertence a um vetor Y[10] de reais.
'''

N = 10

Y = [2.0, 7.0, 6.0, 9.0, 38.0, 14.0, 67.0, 3.0, 666.0, 69.0]
X = float(input("Digite um número: "))
nExiste = True

for i in range(N):
    if(X == Y[i]):
        nExiste = False
        break
    
if(nExiste):
    print(f"O número {X} não existe no vetor Y")
else:
    print(f"O número {X} existe no vetor Y")
        
