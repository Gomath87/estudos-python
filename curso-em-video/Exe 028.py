#Escreva um programa que faça o computador "Pensar" emum número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
computador = randint(0,5) # Faz o cotador "PENSAR"
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? ")) #Jogador tenta adivinhar
print("ATUALIZANDO...")
sleep(5)
if jogador == computador:
    print("VOCÊ ACERTOU!!! Venceu o computador")
else:
    print(f"O computador venceu! Boa sorte na próxima, o número escolhido foi {computador}")
print("Foi um prazer jogar com você!")

