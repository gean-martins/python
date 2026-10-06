#recebe o preço de um produto, e mostra o preço com o desconto

precoAntigo = float(input("Digite o preço do produto: "))
taxaDeDesconto = float(input("Digite o desconto em porcentagem a ser aplicado no produto: "))

precoNovo = precoAntigo - taxaDeDesconto/100*precoAntigo

print(f"Preço SEM desconto: {precoAntigo}")
print(f"Preco COM desconto: {precoNovo}")
