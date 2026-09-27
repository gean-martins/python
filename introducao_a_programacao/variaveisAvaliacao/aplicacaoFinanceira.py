#calcule o valor que uma aplicação financeira rendeu após seis meses em juros compostos

valor_inicial = 100
juros_mensal = 0.1
rendimento_total = valor_inicial * ((1 + juros_mensal) ** 6) - valor_inicial

#[DEBUG] remover ao enviar no moodle
print(f"Rendimento total: {rendimento_total}")
