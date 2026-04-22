# -*- coding: utf-8 -*-
import math

while True:
    try:
        a = int(input())
        result = a / 100
        print(math.ceil(result))

    except EOFError:
        break
