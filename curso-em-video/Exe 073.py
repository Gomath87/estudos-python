#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os  times em ordem alfabética>
#D) Em que posição na tabela está o time do Internacional.
from operator import index

Listatimes = ("Flamengo","Cruzeiro","Palmeiras","Bahia","Bragantino","Botafogo","Mirassol",
              "São Paulo","Ceará SC","Internacional","Corinthians","Fluminense","Atlético-MG",
              "Grêmio","EC Vitória","Vasco da Gama","Santos","Fortaleza","Juventude","Sport Recife")
print("-="*20)
print(f"Lista de times do Brasileirão: {Listatimes}")
print("-="*20)
print(f"Os 5 primeiros são {Listatimes [:5]}")
print("-="*20)
print(f"Os 4 últimos são {Listatimes [-4:]}")
print("-="*20)
print(f"Times em ordem alfabética: {sorted(Listatimes)}")
print("-="*20)

posicao = Listatimes.index("Internacional")
print(f"O Internacional está na {posicao+1}ª posição")





