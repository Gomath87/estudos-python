# -*- coding: utf-8 -*-

num = int(input())
for cont in range (num):
    valorbonus = int(input())
    Dvalorataque, Dvalordefesa, Dleveltreinador = map(int, input().split())
    Gvalorataque, Gvalordefesa, Gleveltreinador = map(int,input().split())

    D = (Dvalorataque + Dvalordefesa) / 2
    if Dleveltreinador % 2 == 0:
        D += valorbonus
    G = (Gvalorataque + Gvalordefesa) / 2
    if Gleveltreinador % 2 == 0:
        G += valorbonus

    if D > G:
        print("Dabriel")
    elif G > D:
        print("Guarte")
    else:
        print("Empate")
