#🏎️ 3. Radar de Velocidade
#Peça a velocidade de um carro:
#Se for maior que 80 km/h, exiba uma mensagem de "Multado!"
#Caso contrário, diga "Velocidade permitida"

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80.00:
    print("Multado por exceder a velocidade da via que é de 80Km/h")
else:
    print("Velocidade permitida")

