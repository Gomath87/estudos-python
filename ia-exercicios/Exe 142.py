#Cadastro simples de alunos

#Crie um dicionário que armazene o nome e a nota de 3 alunos.
#Depois, mostre os nomes dos alunos e suas notas.
dicionario = {}
for cont in range (0,3):
    aluno = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota: "))
    dicionario[aluno] = aluno
    dicionario[nota] = nota
print(dicionario)
