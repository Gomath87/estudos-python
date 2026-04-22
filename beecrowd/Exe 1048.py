# -*- coding: utf-8 -*-

salario = float(input())

if salario <= 400.00:                             #Verifica se o salário está entre R$0,00 e R$400,00
    reajuste = salario * (15/100)                 #Calcula o reajuste de 15%
    novosalario = salario + reajuste              #Soma o antigo salário com o reajuste de 15%
    print(f"Novo salario: {novosalario:.2f}")     #Mostra o novo salário pós reajuste para o usuário
    print(f"Reajuste ganho: {reajuste:.2f}")      #Mostra o valor do reajuste para o usuário
    print(f"Em percentual: 15 %")                 #Mostra o percentual do reajuste para o usuário

elif salario >= 400.01 and salario <= 800.00:     #Verifica se o salário está entre R$400,01 e R$800,00
    reajuste = salario * (12 / 100)               #Calcula o reajuste de 12%
    novosalario = salario + reajuste              #Soma o antigo salário com o reajuste de 12%
    print(f"Novo salario: {novosalario:.2f}")     #Mostra o novo salário pós reajuste para o usuário
    print(f"Reajuste ganho: {reajuste:.2f}")      #Mostra o valor do reajuste para o usuário
    print(f"Em percentual: 12 %")                 #Mostra o percentual do reajuste para o usuário

elif salario >= 800.01 and salario <= 1200.00:    #Verifica se o salário está entre R$800,01 e R$1200,00
    reajuste = salario * (10 / 100)               #Calcula o reajuste de 10%
    novosalario = salario + reajuste              #Soma o antigo salário com o reajuste de 10%
    print(f"Novo salario: {novosalario:.2f}")     #Mostra o novo salário pós reajuste para o usuário
    print(f"Reajuste ganho: {reajuste:.2f}")      #Mostra o valor do reajuste para o usuário
    print(f"Em percentual: 10 %")                 #Mostra o percentual do reajuste para o usuário

elif salario >= 1200.01 and salario <= 2000.00:   #Verifica se o salário está entre R$1200,01 e R$2000,00
    reajuste = salario * (7 / 100)                #Calcula o reajuste de 7%
    novosalario = salario + reajuste              #Soma o antigo salário com o reajuste de 7%
    print(f"Novo salario: {novosalario:.2f}")     #Mostra o novo salário pós reajuste para o usuário
    print(f"Reajuste ganho: {reajuste:.2f}")      #Mostra o valor do reajuste para o usuário
    print(f"Em percentual: 7 %")                  #Mostra o percentual do reajuste para o usuário

elif salario > 2000.00:                           #Verifica se o salário está acima de R$2000,00
    reajuste = salario * (4 / 100)                #Calcula o reajuste de 4%
    novosalario = salario + reajuste              #Soma o antigo salário com o reajuste de 4%
    print(f"Novo salario: {novosalario:.2f}")     #Mostra o novo salário pós reajuste para o usuário
    print(f"Reajuste ganho: {reajuste:.2f}")      #Mostra o valor do reajuste para o usuário
    print(f"Em percentual: 4 %")                  #Mostra o percentual do reajuste para o usuário

