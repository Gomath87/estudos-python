#O usuário deve digitar um número, e o programa deve exibir a tabuada
# desse número de 1 a 10. Porém, use um formato organizado: 5 x 1 = 5 5 x 2 = 10 ...
# e assim por diante.

#Foco: Uso do laço for e f-strings para formatação.

from time import sleep

num = int(input("Digite um número para saber sua respectiva tabuada: "))

for cont in range (0,11):
    print(f"{num} X {cont} = {num * cont}")
    sleep(0.5)

print(f"Essa é a tabuada do número: {num}")