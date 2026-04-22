#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

menu = 0
while menu != 5:
    print("-" * 8, "MENU", "-" * 7)
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")
    print("-" * 27)

    menu = int(input("Digite a operação desejada: "))

    if menu == 1:
        soma = n1 + n2
        print(f"O resultado da soma é {soma}")

    elif menu == 2:
        multiplicacao = n1 * n2
        print(f"O resultado da multiplicação é {multiplicacao}")

    elif menu == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n1 < n2:
            print(f"O maior número é {n2}")
        else:
            print("Os números são iguais")

    elif menu == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

    elif menu == 5:
        print("Programa finalizado!")

    else:
        print("Opção inválida. Tente novamente.")
print("Programa finalizado!")


