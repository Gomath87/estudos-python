# 12. Crie uma tupla com nomes de 4 times de futebol.
#     - Mostre os dois primeiros colocados.
#     - Mostre os dois últimos colocados.
#     - Mostre os times em ordem alfabética.

times = ("São Paulo","Santos","Corinthians","Real Sociedad")
print("Os dois primeiros colocados são: ",end="")
for cont in times[0:2]:
    print(cont,end=" ")
print()
print("Os dois ultimos colocados são: ",end="")
for cont in times[-2:]:
    print(cont,end=" ")
print()
ordem = sorted(times)
print("Os times em ordem alfabética são: ", end="")
for cont in ordem:
    print(cont,end=" ")