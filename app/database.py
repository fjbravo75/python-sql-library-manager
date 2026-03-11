import sqlite3
from pathlib import Path

# Carpeta raíz del proyecto: un nivel por encima de /app
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "library.db"


def get_connection():
    """Devuelve una conexión abierta a la base de datos."""
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_table():
    """Garantiza que la tabla libros exista en la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()

    # En esta primera versión usamos 1 para disponible y 0 para prestado.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT,
            anio INTEGER,
            disponible INTEGER NOT NULL DEFAULT 1
        )
    """)

    conn.commit()
    conn.close()