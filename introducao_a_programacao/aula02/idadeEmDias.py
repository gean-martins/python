#recebe uma idade expressa em anos, meses e dias, imprime a idade da pessoa apenas em dias

anos = int(input("Digite quantos anos você viveu: "))
meses = int(input("Digite quantos meses você viveu: "))
dias = int(input("Digite quantos dias você viveu: "))

diasTotaisDeVida = anos * 365 + meses * 30 + dias

print(f"Você viveu {diasTotaisDeVida} dias até o momento...")
