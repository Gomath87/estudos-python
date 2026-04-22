# 3. Crie um dicionário com nomes de 5 alunos e suas respectivas notas.
#    - Mostre apenas os alunos que tiveram nota maior ou igual a 7.

dicionario = {"Alejandro":80,"Angelo":75,
              "Anuel": 80, "Sebastian":65
              ,"Matheus":100}
print("Os alunos que tiveram nostas maiores ou iguais a 7 foram: ",end="")
for key,value in dicionario.items():
    if value >= 70:
        print(f"{key} ",end=" ")