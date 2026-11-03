"""
8. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
    • salários até R$ 280,00 (incluindo) : aumento de 20%
    • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    • salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
    • o salário antes do reajuste;
    • o percentual de aumento aplicado;
    • o valor do aumento;
    • o novo salário, após o aumento.
"""

salarioOld = float(input("Digite o valor do salário ANTES do reajuste: "))

if(salarioOld <= 280):
    percentual = 20
    
elif(salarioOld > 280 and salarioOld < 700):
    percentual = 15
    
elif(salarioOld >= 700 and salarioOld < 1500):
    percentual = 10
    
else:
    percentual = 5

aumento = percentual/100 * salarioOld
salarioNew = salarioOld + aumento

print(f"Salário ANTES do reajuste: R${salarioOld}")
print(f"Percentual do reajuste: {percentual}%")
print(f"Valor do aumento: R${aumento}")
print(f"Novo salário, com reajuste: R${salarioNew}")
