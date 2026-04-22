# Refaça o DESAFIO 051. lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

primeiro = int(input("Informe o primeiro número: "))
razao = int(input("Informe a razão: "))
contador = 1

while contador <= 10:
    print(primeiro, end=" → ")
    contador += 1
    primeiro += razao
print("Programa concluido")

