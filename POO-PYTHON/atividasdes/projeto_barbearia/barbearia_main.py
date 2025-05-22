from barbearia_inserir import inserir
from barbearia_conexao import banco
banco = banco()
clientes = []
while True:
    nome = input('qual e o seu nome: ')
    cpf = input('qual e o seu cpf: ')
    idade = int(input('qual e sua idade: '))
    cliente = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade
    }
    clientes.append(cliente)
    inserir(banco,cliente['nome'],cliente['cpf'],cliente['idade'])

    '''
    ver(banco)
    if (cpf) in banco.cur:
        print('esse usuario ja esta registrado na barbearia')'''
    

        

    

