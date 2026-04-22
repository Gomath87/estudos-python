# 3. Crie uma lista com 5 números inteiros.
#    - Mostre o maior, o menor e a média dos valores.

lista = [1,100,0,2,50]

flag = maior = menor = media = soma = 0

for cont in lista:
    flag += 1
    soma += cont
    if flag == 1:
        maior = cont
        menor = cont
    else:
        if cont > maior:
            maior = cont
        if cont < menor:
            menor = cont
media = soma / len(lista)
print(lista)
print(f"O maior número da lista: {maior}")
print(f"O menor número dalista: {menor}")
print(f"A média dos números da lista: {media:.1f}")

