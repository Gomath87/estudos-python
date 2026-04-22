# Crie um programa que gerencie o aproveitamento de
# um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato

nome = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {nome} jogou? "))

aproveitamento = dict ()
aproveitamento['nome'] = nome
somagols = 0
lista = []

for cont in range(0,partidas):
    gol = int(input(f"Quantos gols na partida {cont}? "))
    lista.append(gol)
    somagols += gol
aproveitamento['gols'] = lista
aproveitamento['total'] = somagols

print("-="*45)
print(aproveitamento)
print("-="*45)

print(f"O campo nome tem valor {aproveitamento['nome']}.")
print(f"O campo gols tem o valor {aproveitamento['gols']}.")
print(f"O campo total tem o valor {aproveitamento['total']}.")
print("-="*45)

print(f"O jogador {nome} jogou 5 partidas.")
for partida,gols in enumerate(aproveitamento['gols']):
    print(f"    ==> Na partida {partida}, fez {gols} gols.")
print(f"Foi um total de {somagols} gols.")

#CONSEGUI GRAÇAS A DEUS!


