# -*- coding: utf-8 -*-

competidores = int(input())
vagas = int(input())
lista = []

for cont in range(competidores):
    nota = int(input())
    lista.append(nota)
lista.sort(reverse=True)
novalista = []


quantasvezesrepete = 0
for cont in range(vagas):
    if cont == vagas - 1:
        quantasvezesrepete = lista.count(lista[0])
    else:
        novalista.append(lista[0])
        lista.pop(0)

for cont in range(quantasvezesrepete):
    novalista.append(lista[0])

print(f"{len(novalista)}")