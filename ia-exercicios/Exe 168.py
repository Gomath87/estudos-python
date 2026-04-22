# 4. Peça ao usuário para digitar 5 palavras.
#    - Armazene em uma lista.
#    - Crie uma segunda lista com o comprimento de cada palavra.
lista = []
lista2 = []
for cont in range (1,6):
    palavra = str(input(f"{cont}° palavra: "))
    lista.append(palavra)

for cont in lista:
    lista2.append(len(cont))
flag = 0
for cont in lista:
    print(f"A palavra {cont} tem {lista2[flag]} letras")
    flag += 1


