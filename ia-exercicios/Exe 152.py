# 2. Peça ao usuário para digitar 3 frutas e seus respectivos preços e guarde tudo em um dicionário.
#    - Mostre o dicionário completo e depois cada fruta com seu preço formatado.
lista = []
for cont in range(1, 4):
    dicionario = {}
    fruta = str(input("Nome da fruta: "))
    preco = float(input("Preço: "))
    dicionario['fruta'] = fruta
    dicionario['preço'] = preco
    lista.append(dicionario.copy())

print(lista)
print()
print("-="*40)
print(f"{'TABELA':^40}")
print(f"{'FRUTA':<20} {'PREÇO':>10}")
print()
for cont in lista:
    print(f"{cont['fruta']:<20} {cont['preço']:>10.2f}")
print("-="*40)



