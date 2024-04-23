from pathlib import Path
import sqlite3

ROOT = Path(__name__).parent

conn = sqlite3.connect(ROOT / "meubanco.sqlite")
