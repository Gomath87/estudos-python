# -*- coding: utf-8 -*-

iniciou , conluio = map(int,input().split())

vinteequatrohoras = 24
meianoite = 0
resultado = 0

if iniciou == conluio:
    print("O JOGO DUROU 24 HORA(S)")
elif iniciou > conluio:
    vinteequatrohoras -= iniciou
    meianoite += conluio
    resultado = vinteequatrohoras + meianoite
    print(f"O JOGO DUROU {resultado} HORA(S)")
else:
    resultado = conluio - iniciou
    print(f"O JOGO DUROU {resultado} HORA(S)")

