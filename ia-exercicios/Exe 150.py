# 10. Crie um dicionário para armazenar login e senha de 3 usuários.
#     Peça ao usuário um login e senha e verifique se estão corretos.

diconario = {"gato12345":"gatinho","cachoro@gmail.com":"cachorro1","peba@gmail.com":"peba12345"}
usuario = str(input("Informe o usuário: "))
senha = str(input("Informe a senha: "))

if usuario in diconario:
    if senha in diconario:
        print("Acesso liberado!")
else:
    print("Acesso negado")