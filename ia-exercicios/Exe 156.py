# 4. Crie um dicionário que armazene o nome e idade de várias pessoas (cadastro).
#    - No final, mostre a média de idade das pessoas cadastradas.

cadastro = []
soma = media = 0
while True:
    dicionario = {}
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    soma += idade
    cadastro.append(dicionario)
    resposta = str(input("Deseja continuar? [S/N] ")).upper()
    if resposta == "N":
        break
media = soma / len(cadastro)
print(f"A média de idade é {media:.1f}")
