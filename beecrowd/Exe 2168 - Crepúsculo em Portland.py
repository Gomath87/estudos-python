# -*- coding: utf-8 -*-
while True:
    multi, xp = map(int,input().split())
    if multi == 0 and xp == 0:
        break
    else:
        print(xp * multi)
