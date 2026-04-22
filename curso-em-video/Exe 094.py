# Crie um programa que leia nome,sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com a idade acima da média.

pessoas = []
somaidade = media = 0

while True:
    nome = str(input("Nome: "))
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper()
        if sexo != "M" and sexo != "F":
            print("ERRO! Por favor, digite apenas M ou F.")
        else:
            break

    idade = int(input("Idade: "))
    pessoa = {}
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()
        if resposta != "S" and resposta != "N":
            print("ERRO! Responda apenas S ou N.")
        else:
            break
    if resposta == "N":
        break
print(pessoas)
print("-="*45)

print(f"- O grupo tem {len(pessoas)} pessoas.")


for cont in pessoas:
    somaidade += cont['idade']    #Somas a idades de todos do grupo
media = somaidade / len(pessoas)
print(f"- A média de idade é de {media:.2f}")


print("- As mulheres cadastradas foram: ",end="")
for cont in pessoas:
    if cont['sexo'] == "F":       #Mostra os nomes das mulheres no grupo
        print(cont['nome'],end=" ")
print()

print("- Lista das pessoas que estão acima da média: ")
for cont in pessoas:
    if cont['idade'] > media:    #Mostra as pessoas que tem idade acima da média
        print()
        for chave,valor in cont.items():
            print(f"{chave} = {valor}",end="; ")
print("<< ENCERRADO >>")





