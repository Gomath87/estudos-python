# -*- coding: utf-8 -*-


num = int(input())
lista = []
for cont in range (num):
    a = int(input())
    lista.append(a)
lista2 = lista.copy()
lista2.sort()
dicionario = {}

while True:
    at = lista2[0]
    quantidade = lista2.count(at)
    dicionario[at] = quantidade
    lista2 = [x for x in lista2 if x != at]
    if len(lista2) == 0:
        break

for chave,valor in dicionario.items():
    print(f"{chave} aparece {valor} vez(es)")
