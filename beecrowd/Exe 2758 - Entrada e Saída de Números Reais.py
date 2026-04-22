# -*- coding: utf-8 -*-
import math

a, b = map(float,input().split())
c ,d = map(float,input().split())

print(f"A = {a:.6f}, B = {b:.6f}")
print(f"A = {c:.6f}, B = {d:.6f}")
resultadoA = math.ceil(a*20) / 20
resultadoB = math.ceil(b*20) / 20
resultadoC = math.ceil(c*20) / 20
resultadoD = math.ceil(d*20) / 20
print(f"A = {resultadoA:.1f} B = {resultadoB:.1f}")
print(f"C = {resultadoC:.1f} D = {resultadoD:.1f}")

print(f"A = {a:.2f} B = {b:.2f}")
print(f"C = {c:.2f} D = {d:.2f}")

