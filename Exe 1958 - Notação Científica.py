# -*- coding: utf-8 -*-

caso = 1
while True:
    try:
        num = int(input())

        lista = [0]
        for cont in range(1, num + 1):
            lista += [cont] * cont

        qtd = len(lista)
        if qtd == 1:
            print(f"Caso {caso}: {qtd} numero")
        else:
            print(f"Caso {caso}: {qtd} numeros")

        print(' '.join(str(x) for x in lista))
        print()

        caso += 1

    except EOFError:
        break
