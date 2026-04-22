# Dada uma lista com nomes repetidos:
# nomes = ["Ana", "Pedro", "Maria", "Ana", "João", "Pedro"]
# Crie uma nova lista que contenha apenas nomes únicos, sem repetição, e mostre essa lista.

nomes = ["Ana", "Pedro", "Maria", "Ana", "João", "Pedro"]
nomesunicos = []
for cont in nomes:
    if cont not in nomesunicos:
        nomesunicos.append(cont)
print(f"A lista antiga é {nomes}")
print(f"A nova lista é {nomesunicos}")