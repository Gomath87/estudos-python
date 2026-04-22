#Crie uma tupla com nomes e verifique se um nome digitado pelo usuário está presente.

nomes = ("Alfredo","Patrícia","Cleide","Zazá","Izalick")
nome= str(input("Digite um nome para verificar se ele está na tupla: ")).capitalize()
if nome in nomes:
    print(f"Sim o nome {nome} está na tupla")
else:
    print(f"Não está na tupla")