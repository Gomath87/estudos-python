# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Informe o primeiro número: "))
razao = int(input("Informe a razão: "))
contador = 1
limite = 10  # quantidade inicial de termos

while True:
    while contador <= limite:
        print(primeiro, end=" → ")
        primeiro += razao
        contador += 1

    print("PAUSA")
    resposta = input("Deseja ver mais alguns termos? [S/N] ").upper()

    if resposta == "S":
        mais = int(input("Quantos termos a mais você deseja ver? "))
        if mais == 0:
            break
        limite += mais
    else:
        break

print("Programa concluído.")