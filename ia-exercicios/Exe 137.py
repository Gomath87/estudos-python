# 6. Peça 8 números ao usuário e armazene em uma lista.
#    Mostre a lista na ordem inversa.

lista = []
for cont in range(1,9):
    num = int(input(f"Digite o {cont} número: "))
    lista.append(num)
print("Lista na ordem inversa:", lista[::-1])