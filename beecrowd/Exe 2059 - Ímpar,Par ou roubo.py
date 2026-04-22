# -*- coding: utf-8 -*-

p,j1,j2,r,a = map(int,input().split())

if r == 1 and a == 1:  #se o jogador 1 roubar e o jogador 2 acusar o roubo então o jogador 2 ganha
    print("Jogador 2 ganha!")
elif r == 1 and a == 0:  #caso o jogador 2 não acuse o roubo e o jogador 1 roubar então o jogador 1 ganha
    print("Jogador 1 ganha!")
elif r == 0 and a == 1:  #caso o jogador 2 acuse o roubo, mas o jogador 1 não tiver roubado então o jogador 1 ganha
    print("Jogador 1 ganha!")
elif r == 0 and a == 0:
    if p == 1: #jogador 1 escolheu par
        soma = j1 + j2
        if soma % 2 == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")

    elif p == 0: #jogador escolhei ímpar
        soma = j1 + j2
        if soma % 2 == 0:
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")
