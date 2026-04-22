# 4. Peça ao usuário para digitar o nome de 3 produtos e seus preços.
#    Guarde em um dicionário e depois mostre todos os produtos com seus preços.

produtos = dict()

for cont in range(1,4):
    prod = str(input(f"Informe o nome do {cont}° produto: "))
    valor = float(input("Informe o valor: "))
    produtos[prod] = valor

print()
print(f"{'PRODUTOS':^30}")
print()

for prod,preco in produtos.items():
    print(f"{prod:<20} R$: {preco:.2f}")