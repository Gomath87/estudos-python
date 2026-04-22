# 4. Dada a tupla ("João", 25, "Maria", 30, "Carlos", 28):
#    - Mostre apenas os nomes.
#    - Mostre apenas as idades.
#    - Crie uma nova tupla com os nomes das pessoas que têm mais de 27 anos.

tupla = ("João", 25, "Maria", 30, "Carlos", 28)
print(tupla[0],tupla[2],tupla[4])
print(tupla[1],tupla[3],tupla[5])
nomesmais27 = ("Maria","Carlos")
print(f"O nome das pessoas com mais de 27 anos são: {nomesmais27}")