"""
7. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M
para Matutino, V para Vespertino ou N para Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("Você estuda em qual turno?")
print("[M] - Matutino")
print("[V] - Vespertino")
print("[N] - Noturno")
turno = input("Digite a opção desejada: ")

match turno:
    case 'M' | 'm':
        print("Bom Dia!")
    case 'V' | 'v':
        print("Boa Tarde!")
    case 'N' | 'n':
        print("Boa Noite!")
    case _:
        print("Valor Inválido!")
