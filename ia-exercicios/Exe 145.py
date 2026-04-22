# 3. Crie um dicionário que guarde o nome de 3 alunos e suas notas.
#    Mostre a média de cada aluno.

dados = {}
soma1 = soma2 = soma3 = 0
for cont in range(1,4):
    nome = str(input(f"Digite o nome do {cont}° aluno: "))
    nota1 = float(input(f"Digite a primeira nota do aluno {nome}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {nome}: "))
    nota3 = float(input(f"Digite a terceira nota do aluno {nome}: "))
    dados[f"aluno {cont}"] = nome
    dados[f"nota {cont}"] = nota1, nota2, nota3
print()
for cont in range(1,4):
    print(f"Aluno: {dados[f"aluno {cont}"]}")
    print(f"Notas: {dados[f"nota {cont}"]}")
    for cont in dados[f"nota {cont}"]:
        soma1 += cont
    print(f"Media: {soma1 / 3:.2f}")
    soma1 = 0
    print("-="*40)










