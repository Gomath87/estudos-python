#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
#necessários para vencer.

from random import randint
from time import sleep
computador = randint(0,10) # Faz o cotador "PENSAR"
print("-=-"*20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? ")) #Jogador tenta adivinhar
print("ATUALIZANDO...")
sleep(1)
print("")
while jogador != computador:
    print("Nossa passou perto!")
    jogador = int(input("Tente novamente: "))
print("Parabéns você acertou!, foi um prazer jogar com você!")
