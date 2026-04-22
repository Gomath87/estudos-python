# 13. Crie uma tupla com números inteiros e:
#     - Mostre quantos são maiores que 10.
#     - Mostre os valores que estão em posições ímpares.

tupla = (1,2,3,4,5,6,7,8,9,0,12,34,56,7,8,9)

print("Os números maiores que 10 são: ",end="")
for cont in tupla:
    if cont > 10:
        print(cont,end=" ")
print()
print("Os valores que estão em posições ímpares são: ",end="")
for cont in tupla[1::2]:
    print(cont,end=" ")
