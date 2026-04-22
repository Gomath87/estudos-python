#Tabuada
#Peça um número ao usuário e mostre a tabuada dele de 1 até 10.

num = int(input("Digite um número para saber sua respectiva tabuada:"))

for cont in range(1,11):
    print(num,"x",cont,"=", num*cont)
print(f"Essa foi a tabuada de {num}")

resp = int(input("Deseja ver a tabuada de putro número? DIGITE 1 para SIM e 2 para NÃO"))

if resp == 1:
    num = int(input("Digite um número para saber sua respectiva tabuada:"))
    for cont in range(1, 11):
        print(num, "x", cont, "=", num * cont)
    print(f"Essa foi a tabuada de {num}")
elif resp == 2:
    print("Programa concluído!")
else:
    print("Digite um número entre 1 e 2 ")
    resp = int(input("Deseja ver a tabuada de putro número? DIGITE 1 para SIM e 2 para NÃO"))
    if resp == 1:
        num = int(input("Digite um número para saber sua respectiva tabuada:"))
        for cont in range(1, 11):
            print(num, "x", cont, "=", num * cont)
        print(f"Essa foi a tabuada de {num}")
    elif resp == 2:
        print("Programa concluído!")



