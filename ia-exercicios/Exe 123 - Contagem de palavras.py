# Peça ao usuário para digitar uma frase.
# Divida a frase em palavras, armazene numa lista e mostre quantas palavras começam com a letra “a”.

frase = str(input("Digite uma frase: "))
partes = frase.split()
iniciaA = 0
for cont in partes:
    if cont[0] == "a" or cont[0] == "A":
        iniciaA += 1
print(f"A frase original é: {frase}")
print(f"{iniciaA} palavras começam com a letra A")