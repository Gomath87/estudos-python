#Refaça o DESAFIO 035 do triângulos, acrescentando o recurso de mostrar
#que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
n1 = float(input("Digite o comprimento da primeira reta: "))
n2 = float(input("Digite o comprimento da segunda reta: "))
n3 = float(input("Digite o comprimento da terceira reta: "))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("A medida das 3 retas informadas, pode SIM formar um triângulo!")
    if n1 == n2 and n2 == n3:
        print("E formaria um triângulo EQUILÁTERO, pois todos os lados são iguais")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("E formaria um triângulo ISÓSCELES, pois possue 2 lados iguais")
    else:
        print("E formaria um triângulo ESCALENO, pois todos os lados são diferentes")
else:
    print("A medida das 3 retas informadas, NÃO podem formar um triângulo!")