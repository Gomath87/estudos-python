# 7. Peça ao usuário para digitar uma frase.
#    - Substitua todas as letras "a" por "@".

frase = input("Digite uma frase: ")
frase = frase.replace("a","@").replace("A", "@")
print(frase)
