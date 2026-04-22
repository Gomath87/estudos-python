# Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
#from unicodedata import numeric


def ficha(n="",g=0):

    if n == "":
        mensagem = "O jogador <desconhecido>"
    else:
        mensagem = f"O jogador {n}"

    mensagem2 = f"fez {g} gol(s) no campeonato."
    print(mensagem,mensagem2)


#Programa Principal
nome = str(input("Nome do Jogador: ")).strip()
gols = str(input("Número de Gols: ")).strip()
if gols.isnumeric():
    gols = int(gols)
    ficha(nome,gols)
else:
    ficha(nome)





