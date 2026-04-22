# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())  # Digite: 7 14 106
MaiorAB = (A + B + abs(A - B)) // 2
Maior = (MaiorAB + C + abs(MaiorAB - C)) // 2
print(f"{Maior} eh o maior")
