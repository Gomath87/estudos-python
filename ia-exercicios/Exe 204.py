# 7. Crie uma função chamada temperatura_c_para_f que converta Celsius para Fahrenheit.
# Fórmula: F = C * 9/5 + 32
# Retorne o valor convertido e adicione docstring explicando a função.

def temperatura_c_para_f(temperatura):
    '''
    -> Função que converte uma temperatrura em Celsius para Fahrenheit
    :param temperatura: Temperatura em Celsius
    :return: Retorna a temperatura convertida para Fahrenheit
    '''

    celsius = (temperatura * 1.8) + 32
    return celsius

#Programa principal
temp = float(input("Informe uma temperatura em Celsius: "))
resposta = temperatura_c_para_f(temp)
print(f"A temperatura {temp}° Celsius convertido para Fahrenheit é {resposta}°")


#Concluido