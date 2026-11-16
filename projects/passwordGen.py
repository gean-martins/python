'''
    Gerador de Senhas
    Crie senhas fortes com opções de tamanho, símbolos, números e letras maiúsculas.
    Bônus: adicione um segundo modo que verifica a força de uma senha usando algumas regras simples.

    ESSE CÓDIGO NÃO FOI FEITO PARA GERAR SENHAS SEGURAS DE FATO, SERVE APENAS PARA ESTUDAR E PRATICAR PROGRAMAÇÃO
'''

import random

MIN_ASCII_SIMBOL = 33
MAX_ASCII_SIMBOL = 47

MAX_CHAR_OPT = 3

senha = []
insertMaiusculas = False
insertNumeros = False
insertSimbolos = False
invalidOption = True

print("----------------------------------------------")
print("Bem vindo(a) ao gerador de senhas")
tamanhoSenha = int(input("Digite o tamanho da sua senha: "))

print("----")
print("Você quer uma senha com letras MAIUSCULAS?")
print("[s/n] - Sim ou Não?") 

#validador para mauisculas
while(invalidOption): 
    opt = input("Escolha uma opção: ")

    if(opt == 'S' or opt == 's'):
        insertMaiusculas = True
        invalidOption = False
    elif(opt == 'N' or opt == 'n'):
        invalidOption = False
    else:
        invalidOption = True
        print("Opção inválida, tente novamente...")

print("----")
print("Você quer uma senha com números?")
print("[s/n] - Sim ou Não?") 

#validador para numeros
invalidOption = True
while(invalidOption):
    opt = input("Escolha uma opção: ")
    
    if(opt == 'S' or opt == 's'):
        insertNumeros = True
        invalidOption = False
    elif(opt == 'N' or opt == 'n'):
        invalidOption = False
    else:
        invalidOption = True
        print("Opção inválida, tente novamente...")

print("----")
print("Você quer uma senha com símbolos?")
print("[s/n] - Sim ou Não?") 

#validador para símbolos
invalidOption = True
while(invalidOption):
    opt = input("Escolha uma opção: ")
    
    if(opt == 'S' or opt == 's'):
        insertSimbolos = True
        invalidOption = False
    elif(opt == 'N' or opt == 'n'):
        invalidOption = False
    else:
        invalidOption = True
        print("Opção inválida, tente novamente...")

#cria a senha
i = 0
for i in range(tamanhoSenha):
    
    nextChar = random.randint(1, MAX_CHAR_OPT)
    insertMinuscula = False

    match nextChar:
        #para inserir letras
        case 1:
            if(insertMaiusculas):
                senha.append(chr(random.randint(ord('A'), ord('Z'))))
            else:
                insertMinuscula = True

        case 2:
            #para inserir números
            if(insertNumeros):
                senha.append(str(random.randint(0, 9)))
            else: 
                insertMinuscula = True

        case 3:
            #para inserir símbolos
            if(insertSimbolos):
                senha.append(chr(random.randint(MIN_ASCII_SIMBOL, MAX_ASCII_SIMBOL)))
            else:
                insertMinuscula = True
    
    #insere uma letra minúscula de qualquer forma
    if(insertMinuscula):
        senha.append(chr(random.randint(ord('a'), ord('z'))))

#exibe a senha
print("----")
print(f"Senha gerada: {"".join(senha)}")

print("----------------------------------------------")

