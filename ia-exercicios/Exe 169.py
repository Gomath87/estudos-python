# 1. Crie um dicionário com 5 produtos e seus preços.
#    - Mostre o produto mais caro e o mais barato.
#    - Calcule o preço médio dos produtos.

produtos = {
    "Arroz": 22.50,
    "Feijão": 8.90,
    "Macarrão": 4.50,
    "Leite": 5.20,
    "Pão": 9.00
}
maior = nomemaior = menor = nomemenor = soma = media = 0
flag = 0
for produto, valor in produtos.items():
    if flag == 0:
        maior = valor
        nomemaior = produto
        menor = valor
        nomemenor = produto
    else:
        if valor > maior:
            maior = valor
            nomemaior = produto
        if valor < menor:
            menor = valor
            nomemenor = produto
    soma += valor
    flag += 1
media = soma / len(produtos)
print(f"O maior valor foi do produto {nomemaior} custanto R${maior:.2f}")
print(f"O menor valor foi do produto {nomemenor} custando R${menor:.2f}")
print(f"A média dos preços foi R${media:.2f}")
