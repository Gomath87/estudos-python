# 4. Crie uma variável global chamada contador inicializada com 0.
# Crie uma função incrementar() que aumente o valor de contador em 1 a cada chamada.
# Teste chamando a função 3 vezes e depois imprima o valor de contador.

def incrementar():
    global contador
    contador +=1

#Programa principal
contador = 0
incrementar()
incrementar()
incrementar()

print(contador)





#Concluido
