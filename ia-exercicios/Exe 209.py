# 2. Crie uma função chamada "maior_e_menor" que receba uma lista de números
# e retorne uma tupla com o maior e o menor valor da lista.

def maior_e_menor(l):
    tupla = (max(l),min(l))
    return tupla


#Programa principal
lista = [1,2,3,4,5,6,7,8,3]
resultado = maior_e_menor(lista)
print(resultado)