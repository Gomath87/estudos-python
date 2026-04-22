# 4. Peça 10 números ao usuário e guarde em uma lista.
#    Mostre o maior e o menor valor digitado.

lista = list()
maior = menor = 0
for cont in range (1,11):
    num = int(input(f"Digite o {cont}° número: "))
    lista.append(num)
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f"O maior número {maior}")
print(f"O menor número {menor}")
