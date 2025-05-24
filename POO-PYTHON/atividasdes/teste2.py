import mariadb
class banco:
    def __init__(self):
        try: 
            self.conn = mariadb.connect(
                user = 'root',
                password='',
                host = 'localhost',
                port= '3306',
                database = 'barbearia'
            )
            self.cur = self.conn.cursor()
            print('CONECTADO')
        except mariadb.Error as e:
            print('erro na conexão com o banco de dados',e) 
    def fechar(self):
        self.conn.close

        
