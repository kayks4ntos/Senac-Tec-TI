import mariadb
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host = "localhost",
        port =3306,
        database="login"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO usuario (nome,senha) VALUE(?,?)",("KAYK","123")
    )
    conn.commit()
    cur.execute(
        "SELECT FROM usuario (id,nome,senha)"
    )
    for (id,nome,senha) in cur:
        print(f"id {id}\nnome: {nome}\nsenha:{senha}")
except mariadb.Error as e:
    print(f"Erro no MariaDB: {e}")
