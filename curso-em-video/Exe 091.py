
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
import random
from time import sleep
from operator import itemgetter
jogo = {}
ranking = list ()

primeiro = random.randint(1,6)
jogo["jogador1"] = primeiro
segundo = random.randint(1,6)
jogo["jogador2"] = segundo
terceiro = random.randint(1,6)
jogo["jogador3"] = terceiro
quarto = random.randint(1,6)
jogo["jogador4"] = quarto

print("Valores sorteados: ")
for k,v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print("-="*30)
print("  == RANKING DOS JOGADORES ==")
for i , v in enumerate(ranking):
    print(f"  {i+1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)




















