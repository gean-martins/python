'''
    Gerador de Senhas
    Crie senhas fortes com opções de tamanho, símbolos, números e letras maiúsculas.
    Bônus: adicione um segundo modo que verifica a força de uma senha usando algumas regras simples.

    ESSE CÓDIGO NÃO FOI FEITO PARA GERAR SENHAS SEGURAS DE FATO, SERVE APENAS PARA ESTUDAR E PRATICAR PROGRAMAÇÃO
'''

import random

MIN_RAND = 5
MAX_RAND = 15

senha = []
tamanhoSenha = random.randint(MIN_RAND, MAX_RAND)
insertMaiusculas = False
insertNumeros = False
invalidOption = True

print("----------------------------------------------")
print("Bem vindo(a) ao gerador de senhas")
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

#cria a senha
for i in range(tamanhoSenha):
    #para inserir letras
    if(insertMaiusculas):
        moeda = random.randint(0, 1)
        if(moeda == 1):
            senha.append(chr(random.randint(ord('A'), ord('Z'))))
        else:
            senha.append(chr(random.randint(ord('a'), ord('z'))))
    else:
        senha.append(chr(random.randint(ord('a'), ord('z'))))

    #para inserir números
    if(insertNumeros):
        senha.append(str(random.randint(0, 9)))
    
#exibe a senha
print("----")
print(f"Senha gerada: {"".join(senha)}")

print("----------------------------------------------")

