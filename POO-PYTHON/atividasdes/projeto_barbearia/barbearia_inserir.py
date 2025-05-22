from barbearia_conexao import  mariadb 
def inserir(banco,nome,cpf,idade):
    try:
        banco.cur.execute(
        'INSERT INTO cliente (nome,cpf,idade) VALUES (?,?,?)',(nome,cpf,idade)
        )
        banco.conn.commit()
        print('cliente cadastrado')
    except mariadb.Error as e:
        print('erro no inserir usuario',e)
'''
def ver(banco):
    try:
        banco.cur.execute(
        'SELECT FROM cliente (nome,cpf)'
        )
    except mariadb.Error as e:
        print('erro no procurar dados ',e)
'''



