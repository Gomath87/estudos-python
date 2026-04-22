# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostar as notas
# de cada aluno individualmente.

lista = []
listatemporaria = []
pos = 0

while True:
    nome = str(input("Nome: "))
    listatemporaria.append(nome)
    nota1 = float(input("Nota 1: "))
    listatemporaria.append(nota1)
    nota2 = float(input("Nota 2: "))
    listatemporaria.append(nota2)

    lista.append(listatemporaria[:])
    listatemporaria.clear()
    resposta = str(input("Quer continuar? [S/N]")).upper()
    if resposta == "N":
        break

print("-="*40)
print(f"{"N°":<4}  {"NOME":<10}          {"MÉDIA":>8}")
print("-"*40)

for cont in lista:
    print(f"{pos:<4}   {cont[0]:<10}       {((cont[1] + cont[2]) / 2):>8.1f}")
    pos += 1

print("-"*30)

while True:
    respostanotas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if respostanotas == 999:
        break
    else:
        print(f"Notas de {lista[respostanotas][0]} são [{lista[respostanotas][1]},{lista[respostanotas][2]}]")



