#Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(*a,sit=False):
    """

    -> Função para analisar notas e situações de alunos.
    :param a: uma ou mais notas (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre as notas
    """

    dicionario = {}
    dicionario['total']=len(a)
    dicionario['maior']=max(a)
    dicionario['menor']=min(a)
    dicionario['média']=sum(a) / len(a)
    if sit:
        if dicionario["média"] >= 7:
            dicionario['situação'] = "BOA"
        elif dicionario["média"] >= 5:
            dicionario['situação'] = "RAZOÁVEL"
        else:
            dicionario['situação'] = "RUIM"
    return dicionario


#Programa principal
resp = notas(3.5,2,6.5,2,7,4,5, sit=True)
print(resp)
