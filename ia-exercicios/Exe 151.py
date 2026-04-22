# 1. Crie um dicionário para armazenar informações de um aluno: nome, idade e nota.
#    - Depois, mostre cada informação em uma linha.

nome = str(input("Iforme o nome do aluno: "))
idade = int(input(f"Informe a idade do {nome}: "))
nota = float(input("Informe a nota: "))
dados = {}
dados['nome'] = nome
dados['idade'] = idade
dados['nota'] = nota

for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")
