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

def ver(banco):
    try:
        banco.cur.execute(
        'SELECT cpf FROM cliente'
        )
        resultado = banco.cur.fetchall()[0]
        cpf = input('cpf: ')
        if cpf in resultado:
            return resultado
            
    except mariadb.Error as e:
        print('erro no procurar dados ',e)
def agendar(self,banco,cliente_id,data_agendamento):



