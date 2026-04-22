# 5. Crie uma função contador() que receba três parâmetros: inicio, fim e passo.
# Todos os parâmetros são opcionais, com valores padrão (inicio=0, fim=10, passo=1).
# A função deve imprimir a contagem de acordo com os parâmetros.
import datetime
from time import sleep


def contador(inicio=0,fim=10,passo=1):
    for cont in range(inicio,fim,passo):
        print(f"{cont}",end=" ")
        sleep(0.5)
#programa principal

entrada_ini = input("Inicio: ")
if entrada_ini.strip() != "":
    ini = int(entrada_ini)
else:
    ini = 0  # valor padrão

entrada_fi = input("fi: ")
if entrada_fi.strip() != "":
    fi = int(entrada_fi)
else:
    fi = 10  # valor padrão

entrada_pas = input("Passo: ")
if entrada_pas.strip() != "":
    pas = int(entrada_pas)
else:
    pas = 1  # valor padrão

contador(ini,fi,pas)