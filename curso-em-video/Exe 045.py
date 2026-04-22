#Crie um programa que faça o computador jogar Jokenpô (Pedra, papel e tesoura) com você.
import random
print("-==-" * 12)
print("                   JOKENPÔ         ")
print("-==-" * 12)
resposta = str(input("Preparado para começar? aperte enter para iniciar"))
numero = random.randint(1, 3)
if numero == 1:
    print("Tesoura")
elif numero == 2:
    print("Papel")
else:
    print("Pedra")
