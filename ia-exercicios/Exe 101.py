# 17. Peça ao usuário para digitar duas palavras e guarde cada uma em uma tupla.
#     - Junte as duas tuplas em uma só e mostre o resultado.

palavra1 = str(input("Digite a primeira palavra: "))
palavra2 = str(input("Digite a segunda palavra: "))
tupla1 = (palavra1,)
tupla2 = (palavra2,)
tupla3 = (tupla1 + tupla2)

print(tupla3)