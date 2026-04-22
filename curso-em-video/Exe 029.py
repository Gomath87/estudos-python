#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele fou multado>
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite a velocidade do seu carro: "))

if velocidade <= 80:
    print("A sua velocidade está dentro do limite da via que é 80Km/h.")
else:
    m = (velocidade - 80) * 7
    print(f"A sua velocidade excedeu o limite da via que é 80Km/h. Com isso a multa custará R$:{m:.2f}")
