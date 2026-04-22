#🆚 Verifique se uma palavra é um palíndromo (ex: “arara”, “radar”).
#💡 Palíndromo: mesma palavra ao contrário.

palavra = str(input("Digite uma palavra: ")).strip().lower()
aocontrário = palavra[::-1]

if palavra == aocontrário:
    print("A palavra informada é um palíndromo")
else:
    print("A palavra informada NÃO é um palíndromo")



