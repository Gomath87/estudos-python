# -*- coding: utf-8 -*-

num = int(input())
bonecos = []
arquitetos = []
musicos = []
desenhistas = []
for cont in range(num):
    nome,setor,horas = map(str,input().split())
    if setor == "bonecos":
        bonecos.append(int(horas))
    elif setor == "arquitetos":
        arquitetos.append(int(horas))
    elif setor == "musicos":
        musicos.append(int(horas))
    elif setor == "desenhistas":
        desenhistas.append(int(horas))

sboneco = sum(bonecos) // 8
sarquiteto = sum(arquitetos) // 4
smusicos = sum(musicos) // 6
sdesenhista = sum(desenhistas) // 12
soma = sdesenhista + sboneco + sarquiteto + smusicos

print(soma)
