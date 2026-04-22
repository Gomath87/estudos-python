# 1. Crie uma função chamada "somar_valores" que receba uma quantidade variável de números (*args)
# e retorne a soma de todos eles. Se não receber nenhum número, retorne 0.

def somar_valores(*numeros):
    soma = sum(numeros)
    return soma

#Programa principal

num = [1,2,5,8,8,7,7,8,7,5]
resultado = somar_valores(*num)
print(resultado)



