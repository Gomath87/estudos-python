# Peça ao usuário para digitar 10 números e armazene-os em uma lista.
# Depois, crie uma nova lista apenas com os números pares e mostre essa lista.
lista = []
listapar = []
for cont in range(1,11):
    numero = int(input("Informe um número: "))
    lista.append(numero)

for cont in lista:
    if cont % 2 == 0:
        listapar.append(cont)
print(f"A lista original é {lista}")
print(f"A lista contendo apenas os númes pares é {listapar}")

