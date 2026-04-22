# -*- coding: utf-8 -*-

n = int(input())
feminino = masculino = 0
for cont in range(n):
    nome,s = map(str,input().split())
    if s == "F":
        feminino += 1
    elif s == "M":
        masculino += 1
print(f"{masculino} carrinhos")
print(f"{feminino} bonecas")
