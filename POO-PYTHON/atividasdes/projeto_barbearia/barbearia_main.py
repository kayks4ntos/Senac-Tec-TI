from barbearia_inserir import ver, inserir
from barbearia_conexao import banco
banco = banco()
clientes = []

while True:
    print(f'inserir cliente 1\nlogin 2')
    opcao = input('escolha:')
    if  opcao == '1':
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
    elif opcao == '2':
        verificar = ver(banco)
        if verificar == resul:
        

   
    
    

        

    

