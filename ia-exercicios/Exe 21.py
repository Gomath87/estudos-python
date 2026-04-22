#Contagem dos múltiplos de 3 entre 1 e 100
#Mostre na tela todos os números de 1 até 100 que são múltiplos de 3.

print("Todos o números múltiplos de 3 são: ")
for cont in range(1,101):
    if cont % 3 == 0:
        print(cont,end=" ")

