# 3. Crie uma função chamada "contador_letras" que receba uma string e uma letra opcional (default="a").
# A função deve retornar quantas vezes a letra aparece na string. Exemplo: contador_letras("banana") → 3.
def contador_letras(msg,l="a"):

    quantidade = msg.count(l)
    return quantidade


#Programa principal
palavra = str(input("Digite uma palavra ou frase: "))
letra = str(input("Digite qual letra quer ver quantas vezes se repete: ")).strip()
if letra == "":
    resposta = contador_letras(palavra)
    letra = "a"
else:
    resposta = contador_letras(palavra,letra)

print(f"A palavra/frase: {palavra} possue {resposta} letras {letra} ")
