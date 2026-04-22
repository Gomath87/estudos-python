# 2. Dada a tupla (3, 2, 3, 4, 5):
#- Calcule a soma de todos os números.
#- Verifique se o número 3 está na tupla.

tupla = (3, 2, 3, 4, 5)
soma = tres =  0
for cont in tupla:
    soma += cont
print(f"Soma da tupla: {soma}")
if 3 in tupla:
    print("O número 3 está na Tupla")
else:
    print("O número 3 não está na Tupla")

