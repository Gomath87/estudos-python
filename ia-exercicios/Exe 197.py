# 5. Faça um programa que leia uma lista de 10 números e conte quantos são positivos, negativos e zeros.

lista = list()
positivo = negativo = zero = 0

for cont in range(1,11):
    n = int(input(f"Digite o {cont}° número: "))
    lista.append(n)
    if n == 0:
        zero += 1
    elif n > 0:
        positivo += 1
    elif n < 0:
        negativo += 1

print(lista)
print(f"foram informados {positivo} número(s) positivo(s)")
print(f"foram informados {negativo} número(s) negativo(s)")
print(f"foram informados {zero} número(s) zero")