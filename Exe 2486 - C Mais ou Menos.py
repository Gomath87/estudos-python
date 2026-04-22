# -*- coding: utf-8 -*-

alimentos = {"suco de laranja": 120,
             "morango fresco": 85,
             "mamao": 85,
             "goiaba vermelha":70,
             "manga":56,
             "laranja":50,
             "brocolis":34}
soma = 0
while True:
    t = int(input())
    if t == 0:
        break
    else:
        for cont in range(t):
            quantidade, alimento = input().split(maxsplit=1)
            quantidade = int(quantidade)
            vitamina = alimentos[alimento]
            result = quantidade*vitamina
            soma += result

        if soma > 109 and soma < 131:
            print(f"{soma} mg")
        elif soma < 110:
            r  = 110 - soma
            print(f"Mais {r} mg")
        elif soma > 130:
            r = soma - 130
            print(f"Menos {r} mg")
        soma = 0

