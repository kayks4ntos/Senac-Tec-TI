import mariadb
from dataclasses import dataclass
from abc import ABC , abstractmethod
'''
try:
    conn = mariadb.connect(
        user="root",
        password=" ",
        host="localhost",
        port= 3306,
        database="agenda"
    )
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO contatos (nome, telefone , email) VALUES (?,?,?)",("KAYK_SANTOS","3299273244","KAYKCOMK@GMAIL.COM")

    )
    conn.commit()
    cur.execute("SELECT id, nome,telefone,email FROM contatos ")
    for (id , nome, telefone , email) in cur:
        print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}, Email: {email}")
except mariadb.Error as e:
    print(f"Erro no MariaDB: {e}")
    '''
try:
    conn = mariadb.connect(
        user="root",
        password=" ",  
        host="localhost",           
        port=3306,
        database="agenda"
        )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contatos (nome, telefone, email) VALUES (?,?,?)",("ARTHUR","(32) 99943-2345","noah@gmail.com")

    )
    conn.commit()
    cur.execute(
        "SELECT id, nome, telefone, email FROM contatos"
    )
    for (id,nome,telefone,email) in cur:
        print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}, Email: {email}")
except mariadb.Error as e:
    print(f"Erro no MariaDB: {e}")





    