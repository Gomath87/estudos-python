# 16. Dada uma tupla com números (10, 20, 30, 40, 50):
#     - Converta-a para uma lista.
#     - Adicione o número 60 à nova lista.
#     - Converta de volta para tupla e exiba o resultado.

numeros = (10, 20, 30, 40, 50)
listanumeros = list(numeros)
listanumeros.append(60)
numeros2 = tuple(listanumeros)
print(numeros2)

