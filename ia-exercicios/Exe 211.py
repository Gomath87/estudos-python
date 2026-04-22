# 4. Crie uma função chamada "filtro_pares" que receba uma lista de números e um parâmetro opcional "par=True".
# Se par=True, retorne apenas os números pares; se par=False, retorne apenas os números ímpares.

def filtro_pares(lista,par=True):
    a = []
    if par:
        for cont in lista:
            if cont % 2 == 0:
                a.append(cont)
    else:
        for cont in lista:
            if cont % 2 != 0:
                a.append(cont)
    return a



#programa principal
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

resultado = filtro_pares(numeros)
if resultado:
    if all(num % 2 == 0 for num in resultado):
        print(f"Números pares: {resultado}")
    else:
        print(f"Números ímpares: {resultado}")
