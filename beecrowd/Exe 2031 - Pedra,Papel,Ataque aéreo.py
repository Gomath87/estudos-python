# -*- coding: utf-8 -*-

n = int(input())

for cont in range(n):
    lista = []
    jogador1 = str(input())
    jogador2 = str(input())
    lista.append(jogador1)
    lista.append(jogador2)
                                                                                # papel       pedra      ataque
    #Isso aqui da o resultado caso sejam iguais tando jogador 1 e 2            #
    if lista[0] == lista[1]:                                                    # papel x pedra / papel x ataque
        if lista[0] == "ataque":                                                # pedra x ataque
            print("Aniquilacao mutua")
        elif lista[0] == "pedra":
            print("Sem ganhador")
        elif lista[0] == "papel":
            print("Ambos venceram")

    #Esse elif vai pegar todas as possíveis combinações de papel exceto ele com ele mesmo!
    elif "papel" in lista:

        if "papel" and "pedra" in lista:                #Verifica a combinação papel x pedra retonando o vencedor que digitou pedra
            j = 10
            for indice, valor in enumerate(lista):
                if valor == "pedra":
                    j = indice
            if j == 0:
                print("Jogador 1 venceu")
            else:
                print("Jogador 2 venceu")

        elif "papel" and "ataque" in lista:            #Verifica a combinação papel x ataque e retorna o vencedor que digitou ataque
            j = 10
            for indice, valor in enumerate(lista):
                if valor == "ataque":
                    j = indice
            if j == 0:
                print("Jogador 1 venceu")
            else:
                print("Jogador 2 venceu")

    elif "ataque" and "pedra" in lista:          #Verifica a combinação pedra x ataque e retorna o vencedor que digitou ataque
        j = 10
        for indice, valor in enumerate(lista):
            if valor == "ataque":
                j = indice
        if j == 0:
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")