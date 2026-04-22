# -*- coding: utf-8 -*-

h1 , minutoinicial, h2, minutoconclusao = map(int,input().split())

inicio = (h1 * 60) + minutoinicial
conclusao = (h2 * 60) + minutoconclusao

if inicio == conclusao:
    duracao = 1440   # 24 horas certinho
else:
    if conclusao < inicio:
        conclusao += 1440
    duracao = conclusao - inicio
hora = duracao // 60
minuto = duracao % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")