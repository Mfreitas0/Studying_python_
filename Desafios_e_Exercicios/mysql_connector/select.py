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
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
            
        for cliente in clientes:
            print(cliente)
            