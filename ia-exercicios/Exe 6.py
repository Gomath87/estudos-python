#🕒 6. Saudações conforme horário
#Peça a hora atual (apenas a hora, de 0 a 23):
#Até 11: "Bom dia"
#De 12 a 17: "Boa tarde"
#De 18 pra cima: "Boa noite"

hora = int(input("Digite uma hora (0 a 23): "))

if 0 <= hora <= 11:
    print("Bom dia")
elif 12 <= hora <= 17:
    print("Boa tarde")
elif 18 <= hora <= 23:
    print("Boa noite")
else:
    print("Hora inválida! Digite um número de 0 a 23.")



