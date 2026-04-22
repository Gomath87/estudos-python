# -*- coding: utf-8 -*-

colecao = ["PROXYCITY","P.Y.N.G.",
           "DNSUEY!","SERVERS",
           "HOST!","CRIPTONIZE",
           "OFFLINE DAY","SALT",
           "ANSWER!","RAR?","WIFI ANTENNAS"]
n = int(input())
for cont in range(n):
    botaoA,botaoB = map(int,input().split())
    soma = botaoA + botaoB
    print(colecao[soma])
