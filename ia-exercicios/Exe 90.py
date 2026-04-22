# 5. Crie uma tupla com os dias da semana e peça ao usuário um número de 1 a 7.
#    - Mostre qual é o dia correspondente ao número digitado.

semana = ("Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado")
dia = int(input("Digite um número de 1 a 7: "))
print(f"O dia da semana correspondente ao número {dia} é: {semana[dia - 1]}")


