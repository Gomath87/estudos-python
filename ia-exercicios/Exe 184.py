# 8. Crie uma função chamada fatorial(n) que receba um número e retorne o fatorial dele.

def fatorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Digite um número: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é {resultado}")