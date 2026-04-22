#Faça um programa que mostre a tabuada de vários números, um de cada vez,para cada valor
#digitado pelo usuário. O programa será interrompido quando o número solicidado for negativo.

while True:
    tabuada = int(input("Quer ver a tabuada de qual valor? "))
    print("---"*10)
    if tabuada < 0:
        break
    for cont in range(1,11):
        print(tabuada," x ",cont," = ", tabuada*cont)
    print("---" * 10)
print("Programa filanizado com sucesso!")
