# 11. Crie uma tupla com os 10 primeiros números inteiros (de 0 a 9).
#     - Mostre os números em ordem inversa.

tupla = (0,1,2,3,4,5,6,7,8,9)

for cont in tupla(::-1):
    print(cont,end=" ")
