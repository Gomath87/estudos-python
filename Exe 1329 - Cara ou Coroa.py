# -*- coding: utf-8 -*-

while True:
    a = int(input())
    if a == 0:
        break
    else:
        lista = list(map(int, input().split()))
        mary = lista.count(0)
        john = lista.count(1)
        print(f"Mary won {mary} times and John won {john} times")
