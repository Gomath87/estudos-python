# -*- coding: utf-8 -*-

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

A = str(input())
B = str(input())
cont = 0

tamanhoA = len(A)
tamanhoB = len(B)
lista = [tamanhoA,tamanhoB]
flag = 0

while True:
    primeiraA = A[cont]   #Aqui pega a primeira letra de A
    primeiraB = B[cont]   #Aqui pega a primeira letra de B

    valorA = dicionario[primeiraA]   #Aqui guarda o valor da primeira letra de "A" no dicionário para usar na condicional abaixo
    valorB = dicionario[primeiraB]   #Aqui guarda o valor da primeira letra de "B" no dicionário para usar na condicional abaixo

    if valorA < valorB:   #Se o valor de A for menor significa que a letra atual tradada é menor que a letra de B
        print(A)
        print(B)
        break
    elif valorB < valorA: #Se o valor de B for menor significa que a letra atual tradada é menor que a letra de A
        print(B)
        print(A)
        break
    else:                 #Caso sejam iguais "cont" recebe + 1, para vericar a próxima letra de A e B
        cont += 1

    flag += 1
    if flag == min(lista):

        if tamanhoA < tamanhoB:
            print(A)
            print(B)
            break
        elif tamanhoB < tamanhoA:
            print(B)
            print(A)
            break
        elif tamanhoB == tamanhoA:  #SIM PRINT "A" pq AMBAS SÃO IGUAIS
            print(A)
            print(A)
            break



