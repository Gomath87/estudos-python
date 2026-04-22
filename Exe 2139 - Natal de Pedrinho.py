# -*- coding: utf-8 -*-

while True:
    try:
        dic = {1:"Janeiro",2:"Fevereiro",3:"Março",4: "Abril",5: "Maio",6: "Junho",7: "Julho",8: "Agosto",
            9: "Setembro",10: "Outubro",11: "Novembro",12: "Dezembro"}

        dic2 = {"Janeiro": 31,"Fevereiro": 29,"Março": 31,"Abril": 30,"Maio": 31,"Junho": 30,"Julho": 31,"Agosto": 31,
        "Setembro": 30,"Outubro": 31,"Novembro": 30,"Dezembro": 25}


        mes,dia = map(int,input().split())

        mes1 = dic[mes]
        mes2 = dic2[mes1]

        total = 0
        somar = False
        for mes, dias in dic2.items():
            if mes == mes1:
                somar = True
            if somar:
                total += dias
        total -= dia

        if total == 1:
            print("E vespera de natal!")
        elif total < 0:
            print("Ja passou!")
        elif total == 0:
            print("E natal!")
        else:
            print(f"Faltam {total} dias para o natal!")

    except EOFError:
        break