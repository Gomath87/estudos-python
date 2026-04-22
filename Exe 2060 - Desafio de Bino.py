# -*- coding: utf-8 -*-

quantidade = int(input())
lista = list(map(int, input().split()))[:quantidade]

multi2 = multi3 = multi4 = multi5 = 0

for cont in lista:
    if cont % 2 == 0:
        multi2 += 1
    if cont % 3 == 0:
        multi3 += 1
    if cont % 4 == 0:
        multi4 += 1
    if cont % 5 == 0:
        multi5 += 1

print(f"{multi2} Multiplo(s) de 2")
print(f"{multi3} Multiplo(s) de 3")
print(f"{multi4} Multiplo(s) de 4")
print(f"{multi5} Multiplo(s) de 5")
