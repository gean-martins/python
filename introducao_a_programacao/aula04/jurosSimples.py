def calcJurosSimples(juros, capitalInicial, meses):
    jurosEmDinheiro = juros / 100 * capitalInicial
    jurosTotalEmDinheiro = jurosEmDinheiro * meses
    return jurosTotalEmDinheiro

juros = float(input("Digite a taxa de juros em porcentagem: "))
capitalInicial = float(input("Digite o valor do capital inicial: "))
meses = int(input("Digite quantos meses o investimento será aplicado: "))

montanteFinal = calcJurosSimples(juros, capitalInicial, meses) + capitalInicial

print(f"Montante final: {montanteFinal:.2f} reais")

