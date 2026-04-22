#🧮 Peça uma frase e mostre quantas palavras ela tem e qual é a maior palavra.
frase = str(input("Digite uma frase: "))
lista = frase.split()
palavras = len(lista)
print(f"A frase informada possue {palavras} palavras")
maior = ""
for palavra in lista:
    if len(palavra) > len(maior):
        maior = palavra
print(f"A maior palavra é '{maior}' com {len(maior)} letras")