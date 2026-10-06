def calcConsumo(distancia, combustivel):
	return distancia / combustivel

distancia = float(input("Digite a distância percorrida: "))
combustivel = float(input("Digite a quantidade de combustível: "))

consumo = calcConsumo(distancia, combustivel)
print(f"Consumo de combustível: {consumo} km/l")
