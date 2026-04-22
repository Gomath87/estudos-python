# -*- coding: utf-8 -*-

positivo = 0
media = 0
for cont in range(6):                     #Laço para ler 6 números
    numero = float(input())               #Lê um número
    if numero > 0:                        #Verifica se o número é positivo
        positivo += 1                     # Conta mais um número positivo
        media += numero                   # Soma o número positivo a variável da média

media /= positivo                         # Calcula a média apenas se houver ao menos um número positivo
print(f"{positivo} valores positivos")    # Exibe a quantidade de valores positivos
print(f"{media:.1f}")                     # Exibe a média dos valores positivos com uma casa decimal
