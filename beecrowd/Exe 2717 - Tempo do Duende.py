# -*- coding: utf-8 -*-

num = int(input())
A,B = map(int,input().split())
soma = A + B
if soma <= num:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")
