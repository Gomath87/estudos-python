# 20. Crie uma tupla com 5 preços de produtos e:
# Mostre o maior e o menor preço.
# Mostre a média dos preços.

precos = (2.50,1.50,5.00,87.00,55.50)
maior = -1000
media = 0
for cont in precos:
    media += cont
    if cont > maior:
        maior = cont
    for cont in precos:   # usei esse aqui apenas para adicionar valor ao menor para garantir que o valor permanecesse no próximo loop da estrutura de repetição
        menor = cont
        break
    if cont < menor:
        menor = cont
print(f"O menor valor é {menor:.2f}")
print(f"O maior valor é {maior:.2f}")
print(f"A média dos preços é {media/5:.2f}")



