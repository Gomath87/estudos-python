# 2. Crie uma função chamada eh_par(n) que receba um número como parâmetro.
#    - A função deve retornar True se o número for par e False caso contrário.
#    - No programa principal, peça 5 números ao usuário e mostre se cada um é par ou ímpar.

def eh_par(n):
    if n % 2 == 0:
        print("TRUE")
    else:
        print("FALSE")


for cont in range(1,6):
    num = int(input(f"Digite o {cont}° número: "))
    eh_par(num)