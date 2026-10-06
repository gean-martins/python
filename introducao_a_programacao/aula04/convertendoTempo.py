def converteTempo(tempoTotal):
    horas = tempoTotal // 3600
    TempoRestante = tempoTotal % 3600
    minutos = TempoRestante // 60
    segundos = TempoRestante % 60

    print(f"{tempoTotal}seg é igual a {horas}h, {minutos}min e {segundos}seg.")

tempoTotal = int(input("Digite quantos segundos você quer converter: "))
converteTempo(tempoTotal)
