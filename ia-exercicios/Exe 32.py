#Compras acima de 100 reais
#Peça o valor de 5 produtos e diga:
#Quantos produtos custam mais de 100 reais
#O valor total gasto

maisdecem = 0

for cont in range(1,6):
    preco = float(input(f"Digite o valor do {cont} produto: "))
    if preco > 100:
        maisdecem += 1
print(f"São {maisdecem} produtos que passam do valor de R$100,00")
