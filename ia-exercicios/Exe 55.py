
frase = "Curso em Video Python"
print(len(frase))   # tamanho da string com espaços
print(frase.count("o"))  # conta quantas vezes existe a letra 'o'
print(frase.find("deo")) # indica em qual posição começa a frase "deo" no caso na posição 11 caso não encontre irá mostrar '-1'
print("Curso"in frase)   # se tiver a palavra Curso na string ele vai retornar True, de verdadeiro caso não haja ele vai retornar False
print(frase.replace("Pyhton","Android")) # muda a frase python para android
print(frase.upper()) # torna todos os caracteres da string em maiúsculo, o que estiver em maiúsculo ele deixa o que não estiver ele deixa
print(frase.lower()) # torna todos os caracteres da string em minúsculo, o que estiver em minúsculo ele mantem o que não estiver ele deixa
print(frase.capitalize()) # ele vai jogar todos os caracteres em minúsculo com exceção da primeira letra
print(frase.title()) # Parecido com a capitalize, mas ele analisa a string e onde estiver espaços a próxima palavra ele vai deixar em maiúsculo no caso " Curso Em Video Python"
print(frase.strip()) # vai remover todos os espaços inúteis no início e no fim da string "     APRENDA PYTHON     ", vai ficar, "APRENDA PYTHON"
print(frase.rstrip()) # Vai remover os espaços a direita no caso "     APRENDA PYTHON     ", vai ficar = "      APRENDA PYTHON"
print(frase.lstrip()) # Vai remover os espaços da esquerda no caso "     APRENDA PYTHON     ", vai ficar = "APRENDA PYTHON      "
print(frase.split()) # Vai ocorrer uma divisão basicamente onde tiver espaços," CURSO", "EM", "VIDEO", "PYTHON" ( CURSO na posição 0, EM na posiçao 1, VIDEO na posição 2, PYTHON na posição 3)
print("-".join(frase)) # ao contrário do split o join junta e como coloquei "-" ele vai juntar usando esse separador vai ficar C-U-R-S-O- -E-M- -V-I-D-E-O- -P-Y-T-H-O-N

