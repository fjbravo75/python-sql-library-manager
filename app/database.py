import sqlite3
from pathlib import Path

# Ruta del archivo SQLite donde se guardan los datos del proyecto.
DB_PATH = Path("data/library.db")


def get_connection():
    """Devuelve una conexión abierta a la base de datos."""
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