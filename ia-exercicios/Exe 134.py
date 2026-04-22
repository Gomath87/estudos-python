#Notas dos alunos
#Peça ao usuário as notas de 5 alunos e armazene em uma lista.
#Mostre a média da turma.
#Mostre quais alunos ficaram acima da média.
nota = []
media = 0
for cont in range(1,6):
    notas = float(input(f"Digite a {cont}° nota: "))
    nota.append(nota)
    media += notas
print(f"A média da turma foi {media / 5}")

for cont in nota:
    if cont > 6.0:
        print(f"Os alunos que ficaram acima da média tiraram as seguintes notas: {cont}",end=" / ")