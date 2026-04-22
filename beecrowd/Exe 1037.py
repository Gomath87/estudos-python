# -*- coding: utf-8 -*-

a = float(input())
interA = "[0,25]"
interB = "(25,50]"
interC = "(50,75]"
interD = "(75,100]"

if a >= 0 and a <= 25:           #Verifica se está no intervalo entre 0 e 25
    print(f"Intervalo {interA}")
elif a > 25 and a <= 50:         #Verifica se está no intervalo entre 25.1 e 50
    print(f"Intervalo {interB}")
elif a > 50 and a <= 75:         #Verifica se está no intervalo entre 50.1 e 75
    print(f"Intervalo {interC}")
elif a > 75 and a <= 100:        #Verifica se está no intervalo entre 75.1 e 100
    print(f"Intervalo {interD}")
elif a < 0:                      #Verifica se é menor que 0 o que tornará Fora do intervalo
    print("Fora de intervalo")
elif a > 100:                    #Verifica se é maior que 100.1 o que tornará Fora do intervalo
    print("Fora de intervalo")



