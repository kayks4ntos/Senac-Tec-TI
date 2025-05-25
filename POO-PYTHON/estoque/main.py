from sql import Produto
while True:
    print(f'{'-'*20}bem vindo{'-'*20}\n [01] Inserir um novo produto ao estoque\n [02] Ver todos os produtos do estoque\n [03] Ver um produto especifico \n [04] Deletar um produto \n [05] atualizar dados de um produto')
    escolha = input('digite aqui: ')
    if escolha == '01':
        nome_produto = input('Nome Produto: ')
        print(nome_produto)
        descricao = input(f'descrição: ')
        catecoria = input(f' catecoria: ')
        data_final = input(f'data de saida ')
        quantidade = int(input('quantidade:' ))
        produto = Produto(nome_produto,descricao,catecoria,quantidade,data_final)
        Produto.inserir_produto_novo(produto)
    if escolha == '02':
        Produto.ver_todos()
    if escolha == '03':
        nome = input(' Nome do protudo que vc quer ver: ')
        Produto.ver_especifico(nome)
    if escolha == '04':
        nome = input(' Nome : ')
        Produto.ver_especifico(nome)
        Produto.deletar(nome)
    if escolha  == '05':
        mudaca = input('qual e o nome do produto que vc quer autualizar: ')
        opcao = input('qual tipo de dado vc quer mudar: ')
        novo = input('coloque o novo dado: ')
        Produto.update(opcao,novo,mudaca)
        if opcao == 'nome_produto':
            Produto.ver_especifico(novo)
        else:
            print(f'{'-'*20}\n{opcao} foi autualizado para {novo}')
            Produto.ver_especifico(nome)
        
        
         
   




               