#crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário
# vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000
# C) qual é o nome do produto mais barato.
print("---" * 10)
print("     LOJA SUPER BARATÃO     ")
print("---" * 10)
valor = 0
maisdemil = 0
maisbaratovalor = 0
nomeprodutobarato = ""
cont = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    cont += 1

    while True:                                                 #Essa estrutura de repetição garante que o usuário digite ou 'S' ou 'N'
        resposta = str(input("Quer continuar? [S/N]")).upper()
        if resposta == "S" or resposta == "N":
            break

    valor += preco

    if cont == 1:
        maisbaratovalor = preco
        nomeprodutobarato = produto
    else:
        if preco < maisbaratovalor:
            maisbaratovalor = preco
            nomeprodutobarato = produto

    if preco > 1000.00:
        maisdemil += 1


    if resposta == "N":
        break


print("---" * 5,"FIM DO PROGRAMA","---" * 5)
print(f"O total da compra foi R${valor:.2f}")

if maisdemil == 0:                                                    #Esse if garante a resposta no plural ou no singular
    print("Nenhum produto custa mais de R$1000.00")
elif maisdemil == 1:
    print("Apenas 1 produto custa mais de R$1000.00")
else:
    print(f"Temos {maisdemil} produtos custando mais de R$1000.00")

print(f"O produto mais barato foi {nomeprodutobarato} que custa R${maisbaratovalor:.2f}")




