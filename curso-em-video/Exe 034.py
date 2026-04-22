#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00. calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Digite o valor do seu salário: "))

if sal < 1250.00:
    porcent = sal * (15/100)
    aumento = sal + porcent
    print(f"Seu salário após aumento será de R${aumento}")
else:
    porcent = sal * (10/100)
    aumento = sal + porcent
    print(f"Seu salário após aumento será de R${aumento}")
