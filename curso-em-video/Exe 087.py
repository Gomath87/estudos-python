# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
lista = [[],[],[]]
pos = 0
somapares = somalinha3 = 0
while True:
    for cont in range (0,3):
        num = int(input(f"Digite um valor para [{pos},{cont}]: "))
        lista[pos].append(num)
    pos += 1
    if pos == 3:
        break

print("-="*40)
pos = 0

while True:
    for cont in lista[pos]:
        print(f"[  {cont:^5}  ]",end=" ")
        if cont % 2 == 0:
            somapares += cont
    print("")
    if pos == 2:
        break
    pos += 1

somalinha3 = lista[0][2] + lista[1][2] + lista[2][2]
print("-="*40)
print(f"A soma dos valores pares é {somapares}")
print(f"A soma dos valores da terceira coluna é {somalinha3}")
print(f"O maior valor da segunda linha é {max(lista[1])}")