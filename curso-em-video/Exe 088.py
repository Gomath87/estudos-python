# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai
# sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random,time

from pygame.event import clear

print("--" * 14)
print("     JOGA NA MEGA SENA     ")
print("--" * 14)
quantidade = int(input("Quantos jogos você quer que eu sorteie? "))

listatemporaria = []
lista = []
pos = 1

print("-="*3,f"  SORTEANDO {quantidade} JOGOS  ","-="*3)

for cont in range (1,quantidade+1):
    listatemporaria = random.sample(range(1,61),6)
    lista.append(listatemporaria[:])
    listatemporaria.clear()

for cont in lista:
    print(f"Jogo {pos}: {cont}")
    pos += 1
    time.sleep(1)
print("-="*5," < BOA SORTE! > ","-="*5)







