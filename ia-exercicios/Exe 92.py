# 8. Faça um programa que leia 5 nomes digitados pelo usuário e guarde em uma tupla.
#    - Mostre os nomes em ordem alfabética.
nomes = []
for cont in range (1,6):
    nome = str(input(f"Digite o {cont}º nome: "))
    nomes.append(nome)
tupla = tuple(nomes)
tupla = sorted(tupla)
print(tupla)
