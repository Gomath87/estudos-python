# 3. Leia uma matriz 3x3.
#    - Mostre apenas os elementos da diagonal principal.

matriz = []

for cont in range(3):
    linha = []
    for cont2 in range(3):
        n = int(input(f"{cont2}° número: "))
        linha.append(n)
    matriz.append(linha)

print(f"{matriz[0][0]} {matriz[1][1]} {matriz[2][2]}")
