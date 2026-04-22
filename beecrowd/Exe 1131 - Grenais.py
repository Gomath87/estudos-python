# -*- coding: utf-8 -*-

vitoriasinter = vitoriasgremio = empates = grenal = 0
while True:
    inter,gremio = map(int,input().split())
    grenal += 1
    if inter > gremio:
        vitoriasinter += 1
    elif inter < gremio:
        vitoriasgremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    resposta = int(input())
    if resposta == 2:
        break
print(f"{grenal} grenais")
print(f"Inter:{vitoriasinter}")
print(f"Gremio:{vitoriasgremio}")
print(f"Empates:{empates}")
if vitoriasgremio < vitoriasinter:
    print("Inter venceu mais")
elif vitoriasinter < vitoriasgremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")





