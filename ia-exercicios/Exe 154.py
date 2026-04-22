# 4. Crie um programa que peça o nome e a idade de várias pessoas e guarde cada pessoa em um dicionário.
#    - Todos os dicionários devem ficar dentro de uma lista.
#    - No final, mostre quantas pessoas foram cadastradas e a média de idade.
lista = list()
soma = mediaidade = 0
while True:
    dicionario = dict()
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    resposta = str(input("Deseja continuar? [S/N] ")).upper()
    if resposta == "N":
        break
    else:
        continue

print(f"Foram adicionadas {len(lista)} pessoas")

for cont in lista:
    soma += cont['idade']
mediaidade = soma / len(lista)

print(f"A média de idade das pessoas cadastradas é {mediaidade:.1f}")