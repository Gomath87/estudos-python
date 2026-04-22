# 7. Crie um dicionário representando um carrinho de compras.
#    As chaves são os produtos e os valores são as quantidades.
#    Mostre todos os itens do carrinho.

carrinho = {"Sapato":1,"Meia":10,"Cinto":1,"Relogio":3,"Camisa":2}
print(f"{'CARRINHO':^30}")
print("--"*17)
for produto,quantidade in carrinho.items():
    print(f"{produto:<25} {quantidade} Un")