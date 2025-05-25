from usu import Usuario
while True:
    nome = input('qual e o seu nome:')
    email = input('qual e o sei email: ')
    user = Usuario(nome,email)
    user.inserir()
