#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
#indo de 10 até 0, co uma pausa de 1 segundo entre eles.
import time
print("-==-" * 17)
print("------" * 4, "CONTAGEM REGRESSIVA!", "------" * 4)
print("-==-" * 17)
print(" ")
print(" ")
inicio = 10
fim = -1
passo = -1

for i in range(inicio,fim,passo):
    print(i)
    time.sleep(1)
print("FELIZ ANO NOVO!!!!!! BOOOMMMM")