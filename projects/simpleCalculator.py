def printCalcMenu():
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")

def calc(operation, x, y):
    match operation:
        case 1:
            return x + y
        case 2:
            return x - y
        case 3:
            return x * y
        case 4:
            return x / y

def printContinueMenu():
    print("Você quer continuar calculando?")
    print("[s] - Sim")
    print("[n] - Não")

def printHozintalLine():
    print("----------------------------------------------")

#main -------------------------------------------------------------------------------------
keepCalculating = True

while keepCalculating:
    printHozintalLine()
    n1 = float(input("Digite o primeiro número: "))
    print()

    invalidOptionForCalc = True
    while invalidOptionForCalc:
        printCalcMenu()
        operation = int(input("Escolha a opção desejada: "))
        if (operation >= 1 and operation <= 4):
            invalidOptionForCalc = False

        else:
            print()
            print("[Opção inválida, tente novamente...]")
            print()

    print()
    n2 = float(input("Digite o segundo número: "))
    print()
    
    result = calc(operation, n1, n2)
    print(f"O resultado é: [{result}]")
    print()

    invalidOptionToKeepCalculating = True
    printContinueMenu()
    while invalidOptionToKeepCalculating:
        opt = input("Digite a opção desejada: ")
        if(opt == 's' or opt == 'S'):
            invalidOptionToKeepCalculating = False
        elif(opt == 'n' or opt == 'N'):
            keepCalculating = False
            invalidOptionToKeepCalculating = False
        else:
            print()
            print("[Opção inválida, tente novamente...]")
            print()

print("Obrigado por usar a calculadora!")
printHozintalLine()
