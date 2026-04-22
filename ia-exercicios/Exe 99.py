# 15. Crie uma tupla com os caracteres da palavra "Python".
#     - Mostre a tupla.
#     - Mostre os caracteres em posições pares.

palavra = ("P","y","t","h","o","n")
print(palavra)
print("Os caracteres em posição par são: ",end="")
for cont in palavra[0::2]:
    print(cont,end=" ")
