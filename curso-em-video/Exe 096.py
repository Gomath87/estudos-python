#Faça um programa que tenha uma função chamada ÁREA(), que
# receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.
def area(a,b):
    result = a*b
    print(f"A área de um terreno {a}x{b} é de {result}m².")

print("Controle de Terrenos")
print("---------------------")

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura,comprimento)

