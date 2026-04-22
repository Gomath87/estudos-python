#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.

tabuada = int(input("Deseja ver a tabuada de qual número?: "))

for i in range(1,11,1):
    print( tabuada, "X",i,"= ",tabuada*i)
