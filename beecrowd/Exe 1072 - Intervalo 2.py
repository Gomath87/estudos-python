# -*- coding: utf-8 -*-

quantidade = int(input())
dentro = 0
fora = 0
for cont in range (1,quantidade+1):
    numeros = int(input())
    if numeros >= 10 and numeros <= 20:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} in")
print(f"{fora} out")
