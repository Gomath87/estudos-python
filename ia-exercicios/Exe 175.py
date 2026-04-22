# 4. Crie uma função chamada fatorial(n) que receba um número inteiro.
#    - A função deve retornar o fatorial desse número.
#    - No programa principal, peça ao usuário um número e mostre o resultado.
def fatorial(n):
    fat = n
    for cont in range (1,n):
        fat *= cont
    return fat



# principal
num = int(input("Digite um número: "))
resultado = fatorial(num)
print(f"O fatorial do número {num} é {resultado}")
