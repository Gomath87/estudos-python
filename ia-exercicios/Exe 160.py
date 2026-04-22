# 1. Crie uma lista com 10 números inteiros.
#    - Mostre apenas os números pares.

inteiros = [1,2,3,4,5,6,7,8,9,10]
print("Os números pares: ",end="")
for cont in inteiros:
    if cont % 2 == 0:
        print(f"{cont}",end=" ")