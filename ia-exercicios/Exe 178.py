# 2. Crie uma função chamada soma(a, b) que receba dois números e retorne a soma deles.
#    No programa principal, peça dois números ao usuário e mostre o resultado da função.

def soma(a, b):
    return a + b   # retorna o resultado

# Programa principal
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

resultado = soma(num1, num2)  # guarda o retorno da função
print(f"O resultado da soma é {resultado}")


