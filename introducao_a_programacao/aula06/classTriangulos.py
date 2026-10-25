a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))

if(a == b and b == c):
    print("O triângulo é EQUILÁTERO")
elif(a == b or a == c or b == c):
    print("O triângulo é ISÓCELES")
else:
    print("O triângulo é ESCALENO")
