#Crie uma tupla com os dias da semana.
#Peça um número de 1 a 7 e mostre o dia correspondente.

semana = ("Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado")
dia = int(input("Digite um número entre 1 e 7, para saber o dia correspondente: "))
while True:
    if dia < 1 or dia > 7:
        dia = int(input("Por favor um número entre 1 e 7: "))
    else:
        dia -= 1
        print(f"O dia correspondente ao número {dia + 1} é {semana[dia]}")
        break


