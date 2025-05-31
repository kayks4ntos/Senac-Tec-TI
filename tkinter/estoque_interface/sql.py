from db import banco
class Produto:
    def __init__(self,nome_produto,descricao,catecoria,quantidade,data_saida):
        self.nome_produto = nome_produto
        self.descricao =descricao
        self.catecoria = catecoria
        self.quantidade = quantidade
        self.data_saida = data_saida
    def inserir_produto_novo(self):
        db = banco()
        cur = db.iniciar_cursor()
        sql = 'insert into produto (nome_produto,descricao,catecoria,quantidade,data_saida) values (%s, %s, %s, %s, %s)'
        cur.execute(sql,(self.nome_produto,self.descricao,self.catecoria,self.quantidade,self.data_saida))
        db.commitar()
        db.fechar()
        print('cliente inserido')
    def somar():
        pass
    def menos():
        pass 
    @classmethod
    def ver_todos(cls):
        db = banco()
        cur = db.iniciar_cursor()
        sql = 'select * from produto'
        cur.execute(sql)
        resuldado = cur.fetchall()
        db.fechar()
        return resuldado
        
    @classmethod
    def ver_especifico(cls,nome):
        db = banco()
        cur = db.iniciar_cursor()
        sql = 'select * from produto where nome_produto = ?'
        cur.execute(sql,(nome,))
        resuldado = cur.fetchall()
        for (id,nome_produto,descricao,catecoria,quantidade,data_saida) in resuldado:
            print(f'{'-'*20}')
            print(f'id {id}\n nome: {nome_produto}\n descrição {descricao} \n catecoria: {catecoria} \n quantidade: {quantidade} \n data de saida: {data_saida}')
            id_gerado = cur.lastrowid
            return id_gerado
    @classmethod
    def unico(cls,nome):
        db = banco()
        cur = db.iniciar_cursor()
        sql = 'select * from produto where nome_produto = ?'
        cur.execute(sql,(nome,))
        
    
    @classmethod       
    def deletar(cls,nome):
        db = banco()
        cur = db.iniciar_cursor()
        sql = 'delete from produto where nome_produto = ?'
        cur.execute(sql,(nome,))
        db.commitar()
        print(f'O prroduto {nome} foi deletado')
    @classmethod
    def update(cls,opcao,nova,mudaca):
        db = banco()
        cur = db.iniciar_cursor()
        sql = f'update produto set {opcao} = ? where nome_produto = ?'
        cur.execute(sql,(nova,mudaca,))
        db.commitar()
        


