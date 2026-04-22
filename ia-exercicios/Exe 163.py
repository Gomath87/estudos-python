# 4. Crie uma lista com as notas de 4 provas de um aluno.
#    - Mostre todas as notas e a média final.

lista = [10,8,7,9]
media = 0
for pos,value in enumerate(lista):
    print(f"{pos+1}° Nota: {value:.1f}")
media = sum(lista) / len(lista)
print(f"A média: {media:.1f}")

