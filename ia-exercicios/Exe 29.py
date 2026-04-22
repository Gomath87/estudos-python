#Somar apenas os números pares
#Peça ao usuário para digitar 6 números. Some apenas os que forem pares.
somapar = 0
for cont in range(1,7):
    num = int(input(f"Digite o {cont}o número:"))
    if cont % 2 == 0:
        somapar += num
print(f"A soma dos números pares é igual a {somapar}")

