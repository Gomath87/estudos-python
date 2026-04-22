# 4. Leia uma matriz 4x4.
#    - Mostre o maior valor presente na matriz e sua posição (linha, coluna).

matriz = []
maior = linha = coluna = 0

for cont in range(4):
    a = []
    for cont2 in range(4):
        n = int(input(f"{cont2+1}° número: "))
        a.append(n)
        if cont == 0 and cont2 == 0:
            maior = n
            linha = cont
            coluna = cont2
        else:
            if n > maior:
                maior = n
                linha = cont
                coluna = cont2
    matriz.append(a)

for cont in matriz:
    for a in cont:
        print(a,end=" ")
    print("")
print("")
print(f"O maior número da matriz é {maior} e está na linha {linha} e coluna {coluna}")
