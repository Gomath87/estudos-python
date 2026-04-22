# 3. Crie uma função chamada media(lista) que receba uma lista de números.
#    - A função deve retornar a média da lista.
#    - No programa principal, peça ao usuário para digitar 5 notas, calcule e mostre a média.
def media(lista):
    s = 0
    for cont in lista:
        s += cont
    m = s / len(lista)
    print(f"A média das notas informadas foi: {m:.1f}")


a = []
for cont in range(1,6):
    num = float(input(f"Digite a {cont}° nota: "))
    a.append(num)

media(a)