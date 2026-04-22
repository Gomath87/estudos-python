# 2. Peça ao usuário para digitar 5 nomes e guarde em uma lista.
#    - Mostre os nomes em ordem alfabética.
lista = []
for cont in range(1,6):
    nome = str(input(f"{cont}° nome: "))
    lista.append(nome)
lista.sort()
print("Os nomes organizados em ordem alfabética são: ")
print(lista)