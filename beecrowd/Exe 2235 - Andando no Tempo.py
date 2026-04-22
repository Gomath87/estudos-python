# -*- coding: utf-8 -*-

entrada = input()
lista = list(map(int, entrada.split()))
maior = max(lista)
if lista[0] == lista[1]:
    print("S")
elif lista[0] == lista[2]:
    print("S")
elif lista[1] == lista[2]:
    print("S")
else:
    lista2 = list()
    for cont in lista:
        if cont != maior:
            lista2.append(cont)
    if sum(lista2) == maior:
        print("S")
    else:
        print("N")




