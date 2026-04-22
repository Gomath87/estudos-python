#Números pares

#Crie uma lista de números de 1 a 20.

#Mostre apenas os números pares.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for cont in lista:
    if cont % 2 == 0:
        print(cont)
print("Os números pares dentro da lista foram estes")
