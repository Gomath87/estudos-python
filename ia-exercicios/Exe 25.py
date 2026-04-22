#Mostre os números de trás pra frente
#Peça um número N e mostre uma contagem regressiva de N até 1.

n = int(input("Digite um número: "))
for cont in range(n,0,-1):
    print(cont)
