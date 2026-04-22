# 1. Peça ao usuário 10 números e armazene em uma lista.
#    - Mostre os números em ordem crescente e decrescente.
#    - Mostre quantos números pares foram digitados.
lista = []
pares = 0
for cont in range (1,11):
    num = int(input(f"{cont}° número: "))
    if num % 2 == 0:
        pares += 1
    lista.append(num)
crescente = sorted(lista)
decrescente = sorted(lista,reverse=True)
print(f"Lista em ordem crescente: {crescente}")
print(f"Lista em ordem decrescente: {decrescente}")
print(f"Quantidade de números pares digitados: {pares}")

