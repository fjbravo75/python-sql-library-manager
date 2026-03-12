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


def actualizar_disponibilidad(libro_id, disponible):
    """Actualiza la disponibilidad de un libro a partir de su ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE libros
        SET disponible = ?
        WHERE id = ?
    """, (disponible, libro_id))

    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    return filas_afectadas


def buscar_libros(texto_busqueda):
    """Busca libros por coincidencia parcial en título o autor."""
    conn = get_connection()
    cursor = conn.cursor()

    patron = f"%{texto_busqueda}%"

    cursor.execute("""
        SELECT id, titulo, autor, genero, anio, disponible
        FROM libros
        WHERE titulo LIKE ? OR autor LIKE ?
        ORDER BY id
    """, (patron, patron))

    resultados = cursor.fetchall()
    conn.close()

    return resultados


def obtener_libro_por_id(libro_id):
    """Devuelve un libro por su ID o None si no existe."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, autor, genero, anio, disponible
        FROM libros
        WHERE id = ?
    """, (libro_id,))

    libro = cursor.fetchone()
    conn.close()

    return libro


def editar_libro(libro_id, titulo, autor, genero, anio):
    """Actualiza los datos principales de un libro a partir de su ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE libros
        SET titulo = ?, autor = ?, genero = ?, anio = ?
        WHERE id = ?
    """, (titulo, autor, genero, anio, libro_id))

    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    return filas_afectadas


def eliminar_libro(libro_id):
    """Elimina un libro de la base de datos a partir de su ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM libros
        WHERE id = ?
    """, (libro_id,))

    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    return filas_afectadas