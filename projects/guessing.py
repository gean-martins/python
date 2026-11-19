'''
    O funcionamento desse código imita o funcionamento da bola 8 mágica, um brinquedo no qual você faz
    uma pergunta e recebe uma resposta, como se fosse um "vidente", n sei descrever
'''

import random
import time

string = input("Escreva a sua pergunta: ")

n = random.randint(1, 20)
delay = random.randint(1, 5)

print("Pensando", end='', flush=True)

for i in range(delay):
    print('.', end='', flush=True)
    time.sleep(1)

print()

match n:
    case 1:
        print("É certo.")
    case 2:
        print("É decididamente assim.")
    case 3:
        print("Sem dúvida.")
    case 4:
        print("Sim definitivamente.")
    case 5:
        print("Pode contar com isso.")
    case 6:
        print("A meu ver, sim.")
    case 7:
        print("Provavelmente.")
    case 8:
        print("Perspectiva boa.")
    case 9:
        print("Sim.")
    case 10:
        print("Sinais apontam que sim.")
    case 11:
        print("Resposta nebulosa, tente de novo.")
    case 12:
        print("Pergunte novamente mais tarde.")
    case 13:
        print("Melhor não te dizer agora.")
    case 14:
        print("Não é possível prever agora.")
    case 15:
        print("Concentre-se e pergunte novamente.")
    case 16:
        print("Não conte com isso.")
    case 17:
        print("Minha resposta é não.")
    case 18:
        print("Minhas fontes dizem não.")
    case 19:
        print("Perspectiva não é tão boa.")
    case 20:
        print("Muito duvidoso.")

