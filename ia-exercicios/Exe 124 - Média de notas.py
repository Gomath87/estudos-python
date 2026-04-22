# Leia as notas de 5 alunos (uma nota para cada um) e armazene em uma lista.
# Calcule e mostre a média das notas e quantos alunos ficaram acima da média.
lista = []
mediaescolar = float(input("Qual a média mínima para ser aprovado? "))
soma = passaram = 0
for cont in range(1,6):
    nota = float(input(f"Digite a nota do {cont}° aluno: "))
    soma += nota
    if nota >= mediaescolar:
        passaram += 1
    lista.append(nota)
media = soma / len(lista)
print(f"As respectivas notas dos {len(lista)} alunos foi: {lista}")
print(f"A média das notas é: {media:.1f}")
print(f"{passaram} passaram de ano")


