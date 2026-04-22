import math
angulo = float(input("Digite um ângulo em graus: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print (f"O seno é {seno:.2f}")
print (f"O cosseno é {cosseno:.2f}")
print (f"A tangente é {tangente:.2f}")



