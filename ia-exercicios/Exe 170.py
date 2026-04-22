# 2. Crie um dicionário para armazenar notas de 5 alunos.
#    - Mostre os alunos aprovados (nota >= 7) e reprovados.
#    - Calcule a média geral da turma.
alunos = {}
for cont in range(1,6):
     nome = str(input("Aluno: "))
     nota = float(input("Nota: "))
     alunos[nome] = nota
print("-="*40)
print(f"{"ALUNOS APROVADOS":^15}")
print("-="*40)
print("")
for aluno, notas in alunos.items():
    if notas >= 7:
        print(f"{aluno:<10} nota: {notas}")
print("-="*40)
print(f"{"ALUNOS REPROVADOS":^15}")
print("-="*40)
print("")
for aluno, notas in alunos.items():
    if notas < 7:
        print(f"{aluno:<10} nota: {notas}")
print("-=" * 40)
media = sum(alunos.values()) / len(alunos)
print(f"A média geral da turma foi {media:.2f}")