# 📝 Peça uma palavra e diga quantas letras ela tem (desconsiderando espaços).
#💡 Dica: use len() e replace(" ", "")
palavra = str(input("Digite uma palavra: "))
semespaços = palavra.replace(" ","")
tamanho = len(semespaços)
print(f"Tem {tamanho} letras")


