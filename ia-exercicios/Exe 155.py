# 1. Crie um dicionário com os dados de uma pessoa (nome, idade, cidade).
#    - Mostre cada chave e valor em uma linha formatada.

dados = {'Nome':'Leancio','Idade':25,'Cidade':'Lagoa do Carro'}

for chave,valor in dados.items():
    print(f"{chave}: {valor}")