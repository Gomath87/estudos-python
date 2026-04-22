# 3. Crie um dicionário com 5 produtos e seus preços.
#    - Calcule e mostre o preço médio dos produtos.
#    - Mostre o produto mais caro e o mais barato.

produtos = {
    "Maçã": 2.50,
    "Banana": 1.80,
    "Leite": 4.20,
    "Pão": 3.00,
    "Queijo": 10.50
}

soma = flag = caro = produtocaro = barato = produtobarato = 0

for cont in produtos.values():
    soma += cont

media = soma / len(produtos)

for key,prod in produtos.items():
    flag += 1
    if flag == 1:
        caro = prod
        produtocaro = key
        barato = prod
        produtobarato = key
    else:
        if prod > caro:
            caro = prod
            produtocaro = key
        if prod < barato:
            barato = prod
            produtobarato = key
print(f"O preço médio dos produtos é R${media:.2f}")
print(f"O produto mais caro foi {produtocaro} custanto R${caro:.2f}")
print(f"O produto mais barato foi {produtobarato} custanto R${barato:.2f}")



