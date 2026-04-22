# 3. Crie um dicionário vazio.
#    - Peça ao usuário para cadastrar 5 pessoas com idade e sexo.
#    - Mostre quantos homens e quantas mulheres foram cadastrados.
#    - Mostre a média de idade do grupo.
dados = []
quantF = quantM = soma = media = 0
for cont in range(1,6):
    dadostemp = {}
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    soma += idade
    sexo = str(input("Sexo: [M/F] ")).upper()
    if sexo == "M":
        quantM += 1
    elif sexo == "F":
        quantF += 1
    dadostemp['nome'] = nome
    dadostemp['idade'] = idade
    dadostemp['sexo'] = sexo
    dados.append(dadostemp)
media = soma / len(dados)

print(f"Foram cadastradas {quantM} homens")
print(f"Foram cadastradas {quantF} mulheres")
print(f"A média de idades é {media}")



