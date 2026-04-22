# Peça ao usuário para digitar 7 números e armazene-os em uma lista.
# Depois, mostre a lista em ordem crescente e em ordem decrescente.
numeros = []
for cont in range(1,8):
    numero = int(input(f"Digite o {cont}° número: "))
    numeros.append(numero)
crescente = sorted(numeros)
decrescente = sorted(numeros,reverse=True)
print(f"A lista em ordem crescente é {crescente}")
print(f"A lista em ordem decrescente é {decrescente}")


