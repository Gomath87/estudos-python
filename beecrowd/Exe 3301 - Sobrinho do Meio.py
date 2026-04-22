# -*- coding: utf-8 -*-

h,z,l = map(int,input().split())

dicionario = {h:"huguinho",z:"zezinho",l:"luisinho"}

maior = max(dicionario.keys())
menor = min(dicionario.keys())
dicionario.pop(maior)
dicionario.pop(menor)
for cont in dicionario.values():
    print(cont)

