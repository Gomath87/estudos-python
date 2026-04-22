#Produto do carrinho
#Peça ao usuário o preço de 5 produtos e no final mostre:
#A soma total
#O produto mais caro
#O produto mais barato
maior = 0
menor = 100000
soma = 0
for cont in range(1,6):
    produto = float(input(f"Digite o {cont}º valor: "))
    soma += produto
    if produto > maior:
        maior = produto
    elif produto < menor:
        menor = produto
print(f"O maior valor foi {maior:.1f} e o menor {menor:.1f}")
print(f"E a soma total foi: {soma}")



