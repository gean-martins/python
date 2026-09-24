#recebe o preço de um produto, e mostra o preço com 10% de desconto

precoAntigo = float(input("Digite o preço do produto: "))
descontoAaplicar = float(input("Digite o desconto a ser aplicado no produto: "))

descontoNoProduto = precoAntigo * descontoAaplicar / 100

precoNovo = precoAntigo - descontoNoProduto

print(f"Preço sem desconto de 10%: {precoAntigo}")
print(f"Preco com desconto de 10%: {precoNovo}")
