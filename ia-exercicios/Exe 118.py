import random
monstros = ("King-Kong","Godzilla","Fenix")
heroi = 100
batalhas = 0
for cont in monstros :
    print(f"Você vai enfentrar o monstro {cont}")
    decisao = int(input("Digite 1 para Lutar, e 2 para Fugir: "))

    while True:
        if decisao == 1 or decisao == 2:
            break
        else:
            decisao = int(input("Por favor digite um número entre 1 e 2: "))

    if decisao == 1:
        pontos = random.randint(10,30)
        heroi -= pontos
        batalhas += 1
        print(f"Você foi corajoso e enfrentou o Monstro {cont}, mas perdeu {pontos} pontos de vida")
    elif decisao == 2:
        heroi -= 10
        print(f"Você decidiu não lutar, porém esta decisão lhe custou 10 pontos da sua vida")
print()
if heroi > 0:
    print("PARABÉNS VOCÊ SOBREVIVEU A 3 DESAFIOS!")
    print(f"Você sobreviveu com {heroi} pontos de vida")
    print(f"Você enfrentou {batalhas} monstros dos 3 desafiantes")
else:  #Esse else nunca vai ser usado pq o randint vai de 10 a 30 ("Como você me informou"), mesmo que os 3 derem 30 o heroi ainda sai com 10 de vida, mas se futuramente houver mudanças no código ele pode ser utilizado
    print("VOCÊ CHEGOU AO FINAL DO DESAFIO!")
    print(f"Infelizmente você morreu, sua vida ficou {heroi} pontos")
    print(f"Você enfrentou {batalhas} monstros dos 3 desafiantes")



