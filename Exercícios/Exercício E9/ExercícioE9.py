import sqlite3
import ZODB
import ZODB.FileStorage
import transaction
import os
import timeit

# Conectar ao banco de dados SQLite
conn_sqlite = sqlite3.connect('banco_sqlite.db')
cursor_sqlite = conn_sqlite.cursor()

# Conectar ao banco de dados ZODB
storage = ZODB.FileStorage.FileStorage('banco_zodb.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Obter registros do banco de dados SQLite
cursor_sqlite.execute('SELECT * FROM tabela')
registros_sqlite = cursor_sqlite.fetchall()

# Inserir registros no banco de dados ZODB
root.registros_zodb = registros_sqlite
transaction.commit()

# Fechar conexões
cursor_sqlite.close()
conn_sqlite.close()
connection.close()
db.close()

size_sqlite = os.path.getsize('banco_sqlite.db')
size_zodb = os.path.getsize('banco_zodb.fs')

print(f'Tamanho do banco de dados SQLite: {size_sqlite} bytes')
print(f'Tamanho do banco de dados ZODB: {size_zodb} bytes')

root = connection.root()
registros_zodb = root.registros_zodb

registro_10000 = registros_zodb[9999]
registros_seguintes = registros_zodb[10000:10005]

print(f'Registro 10.000: {registro_10000}')
print('Registros seguintes:')
for registro in registros_seguintes:
    print(registro)

# Tempo de busca no banco de dados SQLite
def busca_sqlite():
    conn_sqlite = sqlite3.connect('banco_sqlite.db')
    cursor_sqlite = conn_sqlite.cursor()

    cursor_sqlite.execute('SELECT * FROM tabela WHERE id = 10000')
    registro = cursor_sqlite.fetchone()
    print(registro)

# Medir tempo de busca no banco de dados SQLite
tempo_busca_sqlite = timeit.timeit(busca_sqlite, number=1)
print(f'Tempo de busca no SQLite: {tempo_busca_sqlite} segundos')
