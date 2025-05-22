import mariadb

try:
    conn = mariadb.connect(
        user='root',
        password='',
        host='localhost',
        port=3306,
        database='Estoque'
    )
    cur = conn.cursor()

    def inserir(nome, quantidade):
        cur.executemany(
            'INSERT INTO Produto (nome,quantidade) VALUES (?,?)',
            [(nome, quantidade)]
        )
        conn.commit()

except mariadb.Error as e:
    print(f'Erro na conexão ou inserção com o banco de dados: {e}')
