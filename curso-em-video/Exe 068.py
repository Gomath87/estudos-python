# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
import random
print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)
soma = 0
vitorias = 0
while True:
    n = int(input("Digite um valor: "))
    parouimpar = str(input("Par ou Ímpar? [P/I] ")).upper()
    print("---"* 10)
    computador = random.randint(1,10)
    soma = n + computador
    par = soma % 2
    if parouimpar == "P":
        if par == 0:
            print(f"Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR")
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("-=" * 12)
            vitorias += 1
        else:
            print(f"Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR!")
            print("Você PERDEU!")
            print("-=" * 12)
            break
    else:
        if par == 0:
            print(f"Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR")
            print("Você PERDEU!")
            print("-=" * 12)
            break
        else:
            print(f"Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR!")
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("-=" * 12)
            vitorias += 1
print(f"GAME OVER! Você venceu {vitorias} vezes.")




