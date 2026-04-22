#🌡️ 2. Temperatura
#Peça uma temperatura em graus Celsius e informe:
#Se está frio (abaixo de 15°C)
#Se está agradável (de 15°C até 25°C)
#Se está quente (acima de 25°C)

temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 15.00:
    print("Está um clima frio!")
elif temperatura >= 15 and temperatura <= 25:
    print("Está um clima agradável!")
else:
    print("Está um clima quente!")