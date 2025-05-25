registro = []
while True:
    u = input('qual e o seu nome: ')
    s = input('senha: ')
    usuarios = {
        'nome':u,
        'senha':s
    }
    registro.append(usuarios)
    print(registro)
