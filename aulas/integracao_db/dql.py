import sqlite3
from connection import conn, transactions_manager

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


@transactions_manager
def fetch_by_id(cursor, id):
    return cursor.execute(
        "SELECT * FROM  clientes WHERE id =?", 
        (id,)
        ).fetchone()


@transactions_manager
def fetch_all(cursor):
    results = cursor.execute(
        "SELECT * FROM clientes"
        ).fecthall()
    return [row for row in results]

