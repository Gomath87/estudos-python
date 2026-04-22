#Crie um pequeno programa com um menu interativo:Converter de Celsius para Fahrenheit.
# Converter de Fahrenheit para Celsius.Sair.
# O programa deve continuar rodando até que o usuário escolha a opção "Sair".
# Fórmula: $F = C \times 1.8 + 32$


cont = 0

while cont != 3:

    #Menu
    print(f"------------MENU------------")
    print("Digite 1 para transformar C/F")
    print("Digite 2 para transformar F/C")
    print("Digite 3 para sair")
    cont = int(input())
    print("-----------------------------")

    CF = FC = calculo = 0

    #Calculo
    if cont == 1:
        CF = float(input("Digite a temperatura em Celsius: "))
        calculo = CF * 1.8 + 32
        print(f"{CF}° Celsius para Fahrenheit é: {calculo:.2f}")

    elif cont == 2:
        FC = float(input("Digite a temperatura em Fahrenheit: "))
        calculo = (5/9) * (FC - 32)
        print(f"{FC}° Fahrenheit para Celsius é: {calculo:.2f}")

print("Obrigado pela visita seja sempre bem vindo")



