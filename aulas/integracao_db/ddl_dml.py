import sqlite3
from connection import conn

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


def create_table(connection, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    connection.commit()


def insert_one(connection, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (data))
    connection.commit()


def insert_many(connection, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) values (?, ?)", dados)
    connection.commit()


def update_one(connection, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", (data))
    connection.commit()


def delete_one(connection, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", (data))
    connection.commit()
