# -*- coding: utf-8 -*-

num = int(input())

for cont in range(num):
    n = int(input())
    l = list(map(int, input().split()))
    lista = []

    for cont2 in l:              #Aqui adiciona apenas os inpares na lista "lista"
        if cont2 % 2 == 1:
            lista.append(cont2)

    if len(lista) == 0:          #Aqui é pra caso nenhum número seja ímpar
        print()
        lista.clear()

    elif len(lista) == 1:        #
        for cont3 in lista:
            print(cont3)
            lista.clear()
    else:
        newlist = []
        while True:
            maior = max(lista)
            menor = min(lista)
            lista.remove(maior)
            newlist.append(maior)
            if len(lista) == 0:
                break
            else:
                lista.remove(menor)
                newlist.append(menor)
            if len(lista) == 0:
                break

        for posicao, valor in enumerate(newlist):  # Ou usar o desempacotador que é asterisco "*" print(*newlist)
            if posicao == len(newlist) - 1:
                print(valor)
            else:
                print(valor, end=" ")