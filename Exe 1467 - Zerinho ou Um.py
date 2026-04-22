# -*- coding: utf-8 -*-

while True:
    try:
        alice,beto,clara = map(int,input().split())
        if alice == clara and beto == alice:
            print("*")
        else:
            if alice != beto and alice != clara:
                print("A")
            elif beto != alice and beto != clara:
                print("B")
            elif clara != alice and clara != beto:
                print("C")

    except EOFError:
        break