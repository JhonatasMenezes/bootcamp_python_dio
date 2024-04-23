from pathlib import Path
import sqlite3

ROOT = Path(__name__).parent

conn = sqlite3.connect(ROOT / "meubanco.sqlite")

def transactions_manager(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            conn.commit()
        except Exception as exception:
            conn.rollback()
            return f"Erro na transação: {exception}"
        return result if result else None
    return wrapper
