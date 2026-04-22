# -*- coding: utf-8 -*-

num = int(input())
dia = somakg = somapreco = 0
listakg = []
listapreco = []
for cont in range (num):
    real = float(input())
    fruta = input().split()
    qtdfruta = len(fruta)
    dia += 1
    listakg.append(qtdfruta)
    listapreco.append(real)
    print(f"day {dia}: {len(fruta)} kg")





for cont in listakg:
    somakg += cont

for cont in listapreco:
    somapreco += cont

print(f"{(somakg / len(listakg)):.2f} kg by day")
print(f"R$ {(somapreco / len(listapreco)):.2f} by day")
