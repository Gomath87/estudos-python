#Peça ao usuário para digitar as notas de 5 alunos e guarde-as em uma lista.
#Calcule e mostre a maior nota, a menor nota e a média da turma.

notas = []
media = 0
for cont in range(1,6):
    nota = float(input(f"Digite a nota do {cont}° aluno: "))
    media += nota
    notas.append(nota)
print(f"A maior nota foi {max(notas)}")
print(f"A menor nota foi {min(notas)}")
print(f"A média da turma foi {media/5}")
