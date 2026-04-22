#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#Se já passoi do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. ####18 a idade de si alistar
from datetime import date
data = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - data

if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda vai se alistar, faltam {tempo} anos para o alistamento")
elif idade > 18:
    tempo = idade - 18
    print(f"Passou do tempo de alistamento {tempo} anos")
else:
    print("É hora de se alistar")

