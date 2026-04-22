# 6. Dada a tupla ("Lápis", 1.50, "Caderno", 10.00, "Caneta", 2.00):
#    - Mostre uma listagem com os nomes dos produtos e seus respectivos preços formatados.

tupla = ("Lápis", 1.50, "Caderno", 10.00, "Caneta", 2.00)

print("-="*25)
print(f"{"PRODUTO":^30}{"PREÇO":>10}")
print("-="*25)
preco = 0

for i in range(0, len(tupla), 2):
    nome = tupla[i]
    preco = tupla[i + 1]
    print(f"{nome:<30}R$ {preco:>7.2f}")
