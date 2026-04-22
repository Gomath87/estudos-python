# -*- coding: utf-8 -*-

rep = int(input())
tsaque = tbloqueio = tataque = saque = bloqueio = ataque = 0

for cont in range(rep):
    nome = str(input())
    s, b, a = map(int,input().split())
    s1, b1, a1 = map(int,input().split())
    tsaque += s
    tbloqueio += b
    tataque += a

    saque += s1
    bloqueio += b1
    ataque += a1

calculoSaque = (saque / tsaque) * 100
calculoBloqueio = (bloqueio / tbloqueio) *100
calculoAtaque = (ataque / tataque) * 100

print(f"Pontos de Saque: {calculoSaque:.2f} %.")
print(f"Pontos de Bloqueio: {calculoBloqueio:.2f} %.")
print(f"Pontos de Ataque: {calculoAtaque:.2f} %.")