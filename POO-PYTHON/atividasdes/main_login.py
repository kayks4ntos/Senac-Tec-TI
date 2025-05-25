import mariadb
from dataclasses import dataclass
from abc import ABC , abstractmethod
from interação_login import usuarios, registro

conn = mariadb.connect(
user="root",
password="",
host="localhost",
port=3306,
database="login"
)
print("Conexão estabelecida com sucesso!")
cur = conn.cursor()
def inserir():
    cur.executemany(
        'INSERT INTO usuario (nome,senha) VALUES (?,?)', usuarios
    )
    conn.commit()

'''n = input("digite o seu nome:")
s = input("senha:")
'''
cur.execute(
    'SELECT id, nome FROM usuario;'
    )
for (id,nome) in cur:
    print(f'id {id}\nnome: {nome}\n')            