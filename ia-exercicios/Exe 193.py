# 2. Crie uma função soma() que receba dois números e retorne a soma.
# Depois, crie uma variável fora da função com outro valor e teste se ela não é alterada pela função.

def soma(a,b):
    return a + b

x = 10
resultado = soma(5,7)
print("Resultado da soma:", resultado)
print("Valor de x:", x)
