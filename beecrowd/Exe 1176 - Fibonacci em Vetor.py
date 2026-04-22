# -*- coding: utf-8 -*-
lista = []
primeiro = 0
segundo = 1
lista.append(primeiro)
lista.append(segundo)
cont = 2
while True:
    terceiro = primeiro + segundo
    lista.append(terceiro)
    primeiro = segundo
    segundo = terceiro
    cont += 1
    if cont > 60:
        break
T = int(input())
for cont in range (T):
    num = int(input())
    print(f"Fib({num}) = {lista[num]}")


