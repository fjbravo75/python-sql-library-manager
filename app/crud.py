from database import get_connection


def agregar_libro(titulo, autor, genero, anio):
    """Guarda un nuevo libro en la base de datos con estado disponible."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO libros (titulo, autor, genero, anio, disponible)
        VALUES (?, ?, ?, ?, 1)
    """, (titulo, autor, genero, anio))

    conn.commit()
    conn.close()


def listar_libros():
    """Devuelve una lista con todos los libros guardados en la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, autor, genero, anio, disponible
        FROM libros
        ORDER BY id
    """)
    libros = cursor.fetchall()

    conn.close()
    return libros