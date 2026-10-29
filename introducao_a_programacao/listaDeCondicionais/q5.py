"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. Uma função
recebe as notas e retorna a média do aluno. O programa ainda deve mostrar a
média alcançada pelo aluno e apresentar:
    • A mensagem "Aprovado com Distinção", se a média for igual a dez.
    • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    • A mensagem "Reprovado", se a média for menor do que sete;
"""

def calcMedia(x, y):

    return (x + y) / 2

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = calcMedia(n1, n2)
print(f"Valor da média: {media}")

if(media == 10):
    print("Aprovado com Distinção")
elif(media >= 7):
    print("Aprovado")
else:
    print("Reprovado")
