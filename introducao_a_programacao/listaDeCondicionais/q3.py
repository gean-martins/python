"""
3. Elabore uma função que receba e verifica se uma letra digitada é vogal ou
consoante. Mostre o resultado na tela.
"""

def checkChar(c):
    match c:
        case 'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U': #pipes são portas OR
            print(f"A letra {c} é uma vogal")
        case _:
            print(f"A letra {c} é uma consoante")

letra = str(input("Digite uma letra: "))
checkChar(letra)
