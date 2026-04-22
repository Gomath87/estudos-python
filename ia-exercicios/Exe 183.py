# 7. Crie uma função chamada inverter_lista(lista) que receba uma lista e retorne a lista invertida.

def inverter_lista(lista):
    reverso = lista.reverse()
    return lista


# Programa Principal
numeros = [1,2,3,4,5]
resultado = inverter_lista(numeros)
print(f"A lista invertida é: {resultado}")