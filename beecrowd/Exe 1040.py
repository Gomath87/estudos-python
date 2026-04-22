# -*- coding: utf-8 -*-

n1 ,n2 ,n3 ,n4 = map(float,input().split())

# Calcula a média ponderada com pesos: N1*2, N2*3, N3*4, N4*1
media = (n1*2 + n2*3 + n3*4 + n4*1) / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")   # Imprime a média com uma casa decimal

if media >= 7.0:           # Verifica se a média for maior ou igual a 7.0, o aluno está aprovado diretamente
    print("Aluno aprovado.")
elif media < 5.0:          # Se a média for menor que 5.0, o aluno está reprovado diretamente
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:          # Se a média estiver entre 5.0 e 6.9 (inclusive), o aluno vai para o exame
    print("Aluno em exame.")                 # Mensagem de que o aluno fará um exame extra
    examenota = float(input())               # Lê a nota do exame
    print(f"Nota do exame: {examenota:.1f}")    # Mostra a nota do exame com uma casa decimal
    novamedia = (media+examenota) / 2           # Calcula a nova média, considerando o exame
    if novamedia >= 5.0:                             # Se a nova média for maior ou igual a 5.0, o aluno está aprovado
        print("Aluno aprovado.")
        print(f"Media final: {novamedia:.1f}")       # Imprime a média final com uma casa decima
    elif novamedia <= 4.9:                           # Se a nova média for menor ou igual a 4.9, o aluno está reprovado
        print("Aluno reprovado.")
        print(f"Media final: {novamedia:.1f}")       # Imprime a média final com uma casa decima



