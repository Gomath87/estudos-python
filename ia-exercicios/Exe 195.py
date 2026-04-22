# 4. Crie uma função maior() que receba uma lista de números e retorne o maior valor.
# No programa principal, teste chamando a função com diferentes listas.

def maior(l):
    mai = max(l)
    return mai


#Programa Principal
lista = [1,2,3,4,5,6,7,8]
lista1 = [5,10,2,5]
lista2 = [87,50,25,36,40]

resposta = maior(lista)
print(resposta)
resposta = maior(lista1)
print(resposta)
resposta = maior(lista2)
print(resposta)