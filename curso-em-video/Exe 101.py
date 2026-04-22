# Crie um programa que tem uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO,OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(y):
    calculo = 2018 - y
    if calculo < 18:
        return f"Com {calculo} anos: NÃO VOTA."
    elif calculo > 65:
        return f"Com {calculo} anos: VOTO OPCIONAL."
    elif calculo >= 18:
        return f"Com {calculo} anos: VOTO OBRIGATÓRIO."


# programa principal
ano = int(input("Em que ano você nasceu? "))
resp = voto(ano)
print("--"*15)
print(resp)


