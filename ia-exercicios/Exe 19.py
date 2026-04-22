numero = int(input("Digite um número: "))

if numero == 0:
    print("O número digitado é zero, não é possível contar até ele.")
elif numero < 0:
    for cont in range(-1,numero - 1,-1):
        print(cont,end=" ")
else:
    for cont in range(1, numero + 1):
        print(cont, end=" ")
