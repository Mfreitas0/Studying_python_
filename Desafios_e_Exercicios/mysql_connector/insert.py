from contextlib import contextmanager
import mysql.connector


@contextmanager
def conecta():
    mydb = mysql.connector.connect(
        user='root', password='minhasenha123',
        host='127.0.0.1',
        database='pycodebr'
        )
    try:
        yield mydb
    finally:
        print('[Conexão fechada]')
        mydb.close()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NULL, idade INT, email VARCHAR(50))')
        conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, idade, email) VALUES (%s, %s, %s)'
        val = [
            ('Marcos', 24, 'marcos@gmail.com'),
            ('Keles', 26, 'taiona@gmail.com'),
        ]
        cursor.executemany(sql, val)
        print(cursor.rowcount, "registro Inseridos")
        conexao.commit()
