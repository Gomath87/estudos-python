#O computador deve "pensar" em um número aleatório entre 1 e 20.
# O usuário tem 5 chances para adivinhar.
#A cada erro, o programa deve dizer se o número secreto é maior ou menor
# que o palpite atual.

#Dica: Use import random e a função random.randint(1, 20).

import random
from time import sleep

cont = 0
contador = 1
ganhou = 0

#Introdução
print("CONSEGUE ADVINHAR O NÚMERO QUE ESTOU PENSANDO???")
sleep(1)

numero = random.randint(1,20)

print()
print("Digite seu melhor palpite (1 / 20), você tem 5 CHANCES!")

while contador < 6:
    cont = int(input())
    contador += 1
    if cont > numero:
        if contador == 6:
            print()
        else:
            print("Analisando...")
            sleep(1)
            print(f"O número secreto é menor do que {cont}, tente novamente:")
    elif cont < numero:
        if contador == 6:
            print()
        else:
            print("Analisando...")
            sleep(1)
            print(f"O número secreto é maior do que {cont}, tente novamente:")
    else:
        print("Analisando...")
        sleep(1)
        print(f"PARABÉNS VOCÊ ACERTOU!")
        ganhou += 1
        break

if ganhou == 1:
    print()
else:
    print("Analisando...")
    sleep(1)
    print("Que pena você perdeu, tente novamente!")
