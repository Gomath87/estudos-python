#📊 5. Média Escolar
#Peça duas notas e calcule a média:
#Média 7 ou mais: "Aprovado"
#Média entre 5 e 6.9: "Recuperação"
#Média abaixo de 5: "Reprovado"

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media < 5:
    print(f"Reprovado, nota:{media:.1f}")
elif media <= 6.9:
    print(f"Recuperação, nota:{media:.1f}")
else:
    print(f"Aprovado, nota:{media:.1f}")

