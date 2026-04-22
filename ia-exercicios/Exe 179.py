# 3. Crie uma função chamada par_ou_impar(n) que receba um número inteiro e diga se ele é par ou ímpar.

def par_ou_impar(n):
    if n % 2 == 0:
        print(f"O número {n} é Par!")
    else:
        print(f"O número {n} é Ímpar!")

# programa principal
num = int(input("Digite um número: "))
par_ou_impar(num)