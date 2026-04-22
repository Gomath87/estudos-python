#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
#status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30:Sobrepeso
#30 até 40:Obesidade
#Acima de 40: Obesidade Mórbida
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso: "))
IMC =  peso / (altura ** 2)
if IMC < 18.5:
    print(f"Seu IMC é {IMC:.2f} e você está abaixo do peso")
elif IMC <= 25:
    print(f"Seu IMC é {IMC:.2f} e você está no peso ideal")
elif IMC <= 30:
    print(f"Seu IMC é {IMC:.2f} e você está com sobrepeso")
elif IMC <= 40:
    print(f"Seu IMC é {IMC:.2f} e você está com Obesidade")
else:
    print(f"Seu IMC é {IMC:.2f} e você está com Obesidade Mórbida")



