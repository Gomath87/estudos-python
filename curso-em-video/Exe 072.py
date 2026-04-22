# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extensão, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ("zero","um","dois","três","quatro","cinco","seis","sete","oito",
           "nove","dez","onze","doze","treze","quatorze","quinze",
           "dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while True:
        if num >= 0 and num <= 20:
            break
        else:
            num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {numeros[num]}")
    print()
    resp = int(input("Dejesa continuar? 1[SIM] ou 2[NAO] "))
    if resp == 1:
        continue
    else:
        break



