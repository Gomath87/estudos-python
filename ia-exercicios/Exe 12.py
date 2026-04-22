#Soma de pares
#Peça ao usuário para digitar 6 números inteiros e mostre a soma apenas dos pares.
soma = 0
for cont in range(1,7):
    num = int(input(f"Digite o {cont}o número: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares digitados é {soma}")

