#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#e um atleta e mostre sua categoria, de acordo com a idade:
#até 9 anos: MIRIM
#Até 14 anos:Infantil
#Até 19 anos:Junior
#Até 20 anos:Sênior
#Acima: MASTER
from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    print("A sua categoria é MIRIM")
elif idade > 9 and idade <= 14:
    print("A sua categoria é INFANTIL")
elif idade > 14 and idade <= 19:
    print("A sua categoria é JUNIOR")
elif idade > 19 and idade <= 20:
    print("A sua categoria é SÊNIOR")
else:
    print("A Sua categoria é MASTER")




