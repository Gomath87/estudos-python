#🔍 Peça uma frase e mostre a posição
#da primeira letra “e” (ou qualquer letra que quiser).

frase = str(input("Digite uma frase: ")).lower()
letrae = frase.find("e")
if letrae == -1:
    print("Na frase informada não possue nenhuma letra 'e'")
else:
    print(f"Na frase informada a primeira letra 'e' esta na posição {letrae+1}")