# -*- coding: utf-8 -*-
import math

n = int(input())
raiz5 = math.sqrt(5)
passo1 = ((((1+raiz5)/2)**n)  -  (((1-raiz5)/2)**n)) / raiz5
print(f"{passo1:.1f}")

