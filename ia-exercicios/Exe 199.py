# 2. Crie uma função soma que receba dois números como parâmetros e retorne a soma.
# Teste a função e guarde o resultado em uma variável antes de imprimir.

def soma(a,b):
    r = a+b
    return r
#programa principal
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

r = soma(num1,num2)
print(r)