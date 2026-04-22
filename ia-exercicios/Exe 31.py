#Contar quantos são múltiplos de 3
#Peça 8 números e conte quantos deles são múltiplos de 3.
multi = 0
for cont in range(1,9):
    num = int(input(f"Digite o {cont}o número: "))
    if num % 3 == 0:
        multi += 1
print(f"Existem {multi} números múltiplos de 3")