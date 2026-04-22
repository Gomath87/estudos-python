# 5. Crie um dicionário com produtos e seus preços.
#    - Peça ao usuário para digitar um produto.
#    - Mostre o preço se existir no dicionário ou diga que o produto não foi encontrado.

produtos = {
    "arroz": 22.50,
    "feijão": 8.90,
    "macarrão": 4.50,
    "leite": 5.20,
    "pão": 9.00,
    "queijo": 29.90,
    "carne": 45.00,
    "café": 17.50,
    "óleo": 6.80,
    "açúcar": 4.30
}
prod = str(input("Informe um produto: ")).lower()
if prod in produtos:
    print(f"{prod.title()} custa R${produtos[prod]:.2f}")
else:
    print("produto não encontrado!")
