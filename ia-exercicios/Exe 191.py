# 5. Leia uma matriz 3x3.
#    - Mostre a soma dos elementos de cada linha separadamente.

listaprincipal = []
listatemporaria = []
for cont in range(3):
    for tnoc in range(3):
        a = int(input(f"Linha {cont} Coluna {tnoc}: "))
        listatemporaria.append(a)
    listaprincipal.append(listatemporaria.copy())
    listatemporaria.clear()

for cont in listaprincipal:
    soma = sum(cont)
    for tnoc in cont:
        print(f"{tnoc} ",end="")
    print(f" = {soma}")



