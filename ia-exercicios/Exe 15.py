#Média de notas
#Peça para o usuário digitar quantas notas quiser (ex.: 4 notas).
#No final, mostre a média dessas notas.

num = int(input("Digite quantas notas vai digitar: "))
somanotas = 0
for cont in range(1,num+1):
    nota = float(input(f"Digite a {cont}o nota: "))
    somanotas += nota
media = somanotas/num
print(f"A média das notas informadas é {media:.2f}")