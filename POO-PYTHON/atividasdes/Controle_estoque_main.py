
from atividasdes.controle_estoque_coments import inserir
try:
    while True: 
        produtos = []
        produto_nome = input('nome: ')
        produto_qts = input('Quantidade: ')
        produto = {
            'nome': produto_nome,
            'quantidade': produto_qts
        }
        produtos.append(produto)
        inserir(produto['nome'],produto['quantidade'])
        print(f'protudo {produto_nome} inserido')
        exitt= input('vc deseja sair do menu de inserir produto: ')
        if exitt== 's':
            break
        
finally:
    print('vc saiu do inserir')
print('continue')