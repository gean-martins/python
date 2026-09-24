#cada degrau de uma escada tem X de altura, faça um algoritmo que receba esta altura e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo, sem se preocuparcom a altura do usuário

from math import ceil

alturaDoDegrau = float(input("Digite a altura do degrau, (em m): "))
alturaDesejada = float(input("Digite a altura que você deseja alcançar, (em m): "))

qtdDeDegragus = ceil(alturaDesejada / alturaDoDegrau)

print(f"Você precisa subir {qtdDeDegragus} degraus.")
