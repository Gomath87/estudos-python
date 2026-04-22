# -*- coding: utf-8 -*-

hora = minuto = segundo = total = 0
N = int(input())
if N >= 3600:          #1 hora tem 3.600 segundos    #1 minuto tem 60 segundos # 1 segundo tem 1 segundo
    hora = N // 3600
    N = N - (hora * 3600)
if N <= 3599:
    minuto = N // 60
    N = N - (minuto * 60)
if N <= 59:
    segundo = N // 1

print(f"{hora}:{minuto}:{segundo}")