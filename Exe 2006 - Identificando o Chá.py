# -*- coding: utf-8 -*-

cha = int(input())
palpites = list(map(int, input().split()))
acertos = 0

for cont in palpites:
    if cont == cha:
        acertos += 1
print(acertos)