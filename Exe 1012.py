# -*- coding: utf-8 -*-

pi = 3.14159
A, B, C = map(float, input().split())

calculoTriangulo = (A * C) / 2
calculoCirculo = pi * (C**2)
calculoTrapezio = (A + B) * C / 2
calculoQuadrado = B * B
calculoRetangulo = A * B

print(f"TRIANGULO: {calculoTriangulo:.3f}")
print(f"CIRCULO: {calculoCirculo:.3f}")
print(f"TRAPEZIO: {calculoTrapezio:.3f}")
print(f"QUADRADO: {calculoQuadrado:.3f}")
print(f"RETANGULO: {calculoRetangulo:.3f}")

