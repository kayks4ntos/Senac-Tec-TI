import mariadb
class banco:
    def __init__(self):
        try: 
            self.conn = mariadb.connect(
                user='root',
                password='',
                host='localhost',
                port=3306,
                database='Estoque'
            )
        except mariadb.Error as e:
            print('erro na conexão com o banco de dados:', e) 
    def iniciar_cursor(self):
        return self.conn.cursor()
    def commitar(self):
        self.conn.commit()
    def fechar(self):
        self.conn.close()
