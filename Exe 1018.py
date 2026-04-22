# -*- coding: utf-8 -*-

cem = cinquenta = vinte = dez = cinco = dois = um = 0
A = int(input())
print(A)
while True:
    if A >= 100:
        A -= 100
        cem += 1
    else:
        break
while True:
    if A >= 50:
        A -= 50
        cinquenta += 1
    else:
        break
while True:
    if A >= 20:
        A -= 20
        vinte += 1
    else:
        break
while True:
    if A >= 10:
        A -= 10
        dez += 1
    else:
        break
while True:
    if A >= 5:
        A -= 5
        cinco += 1
    else:
        break
while True:
    if A >= 2:
        A -= 2
        dois += 1
    else:
        break
while True:
    if A >= 1:
        A -= 1
        um += 1
    else:
        break

print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")

