#Mostrar apenas números positivos
#Peça ao usuário 7 números (podem ser positivos ou negativos) e mostre apenas os positivos.
positivos = []
numeros = 0
for cont in range(1,8):
    num = int(input(f"Digite o {cont}o número: "))
    if num >= 0:
        positivos.append(num)
print (f"Os números positivos são: {positivos}")


