# -*- coding: utf-8 -*-

a,b = map(float,input().split())

if a == b:
    print("0.00%")
else:
    subt = b - a
    divi = subt/a
    mult = divi*100
    print(f"{mult:.2f}%")