# Crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

import datetime
dataatual = datetime.date.today()
anoatual = dataatual.year

dados = dict()

nome = str(input("Nome: "))
dados['nome']=nome

nascimento = int(input("Ano de Nascimento: "))
calculoidade = anoatual - nascimento
dados['idade'] = calculoidade

carteira = int(input("Carteira de Trabalho (0 não tem): "))

if carteira != 0:
    dados['ctps'] = carteira
    anocontratacao = int(input("Ano de contratação: "))
    dados['contratação'] = anocontratacao
    salario = float(input("Salário: R$ "))
    dados["salário"] = salario

print("-="*45)
print(dados)

print(f"nome tem valor {dados['nome']}")
print(f"idade tem valor {dados['idade']}")
if carteira != 0:
    print(f"ctps tem o valor {dados['ctps']}")
    print(f"contratação tem o valor {dados['contratação']}")
    print(f"salário tem o valor {dados['salário']}")
    print(f"aposentadoria tem o valor {calculoidade+35}")


