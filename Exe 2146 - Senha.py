# -*- coding: utf-8 -*-

while True:
    try:
        a = int(input())
        print(a-1)

    except EOFError:
        break