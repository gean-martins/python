def calcSalarioLiquido(qtdHoras, valorPorHora):
    salarioBruto = qtdHoras * valorPorHora
    imposto = 8 /100 * salarioBruto
    return salarioBruto - imposto

qtdHoras = float(input("Digite a quantidade de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor da hora trabalhada: "))

salarioLiquido = calcSalarioLiquido(qtdHoras, valorPorHora)
print(f"Salário líquido: R${salarioLiquido}")

