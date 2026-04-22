# -*- coding: utf-8 -*-

abas, acoes = map(int,input().split())

for cont in range(acoes):
    re = str(input())
    if re == "fechou":
        abas+=1
    elif re =="clicou":
        abas-=1
print(abas)