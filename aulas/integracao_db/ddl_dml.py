import sqlite3
from connection import conn, transactions_manager

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


@transactions_manager
def create_table(cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")



@transactions_manager
def insert_one(cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (data))



@transactions_manager
def insert_many(cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) values (?, ?)", dados)



@transactions_manager
def update_one(cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", (data))



@transactions_manager
def delete_one(cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", (data))

