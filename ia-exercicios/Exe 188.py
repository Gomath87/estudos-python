# 2. Leia uma matriz 2x2.
#    - Mostre a soma de todos os elementos.

lista1 = []
lista2 = []

for cont in range(1,5):
    n1= int(input(f"{cont}° número: "))

    if len(lista1) == 2:
        lista2.append(n1)
    else:
        lista1.append(n1)
matriz = [lista1,lista2]
e = 0
for cont,v  in enumerate(matriz):
    for a in v:
        print(a,end=" ")
        e += 1
        if e == 2:
            print(f"= {sum(matriz[cont])}")
            e = 0






