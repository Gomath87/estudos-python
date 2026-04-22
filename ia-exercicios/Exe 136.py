# 5. Crie uma lista com números repetidos.
#    Mostre a lista original e depois mostre a lista sem duplicatas.

listaoriginal = [1,1,2,2,3,4,5,6,7,8,7,3,3]
listasemduplicatas = []

for numero in listaoriginal:
    if numero not in listasemduplicatas:
        listasemduplicatas.append(numero)
print(f"Lista original {listaoriginal}")
print(f"Lista sem duplicatas {listasemduplicatas}")


