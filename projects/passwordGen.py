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
invalidOption = True

print("----------------------------------------------")
print("Bem vindo(a) ao gerador de senhas")
print("Você quer uma senha com letras MAIUSCULAS?")
print("[s/n] - Sim ou Não?") 

#validador
while(invalidOption): 
    optInsertMaiusculas = input("Escolha uma opção: ")

    if(optInsertMaiusculas == 'S' or optInsertMaiusculas == 's'):
        insertMaiusculas = True
        invalidOption = False
    elif(optInsertMaiusculas == 'N' or optInsertMaiusculas == 'n'):
        invalidOption = False
    else:
        invalidOption = True
        print("Opção inválida, tente novamente...")

#cria a senha
if(insertMaiusculas):
    for i in range(tamanhoSenha):
        moeda = random.randint(0, 1)
        if(moeda == 1):
            senha.append(chr(random.randint(ord("A"), ord("Z"))))
        else:
            senha.append(chr(random.randint(ord("a"), ord("z"))))

else:
    for i in range(tamanhoSenha):
        senha.append(chr(random.randint(ord("a"), ord("z"))))

#exibe a senha
print(f"Senha gerada: {"".join(senha)}")

print("----------------------------------------------")

