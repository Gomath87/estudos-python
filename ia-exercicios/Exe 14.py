#Desenhar linha de estrelas
#Peça um número e desenhe na tela uma linha com aquela quantidade de *.
#Exemplo: se digitou 5 → *****

num = int(input("Digite um número: "))
for cont in range(1,num+1):
    print("*",end="")
print("\nPrograma concluído")


