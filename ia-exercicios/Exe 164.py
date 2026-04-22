# 5. Peça ao usuário para digitar 10 números.
#    - Coloque em uma lista e mostre apenas os valores sem repetir (remover duplicados).
lista = []

for cont in range (0,10):
    num = int(input(f"{cont}° número: "))
    if num not in lista:
        lista.append(num)
print("Os números únicos digitados foram:", lista)