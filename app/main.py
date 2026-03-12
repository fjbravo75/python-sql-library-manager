from database import create_table
from crud import (
    agregar_libro,
    listar_libros,
    actualizar_disponibilidad,
    buscar_libros,
    obtener_libro_por_id,
    editar_libro,
    eliminar_libro
)

ANIO_MINIMO = 1450
ANIO_MAXIMO = 2100


def mostrar_menu():
    """Muestra las opciones disponibles en esta primera versión del programa."""
    print("\nGestor de biblioteca")
    print("1. Añadir libro")
    print("2. Listar libros")
    print("3. Cambiar disponibilidad")
    print("4. Buscar libros")
    print("5. Editar libro")
    print("6. Eliminar libro")
    print("0. Salir")


def pedir_texto_obligatorio(mensaje):
    """Pide un texto obligatorio por teclado hasta que el usuario introduzca uno válido."""
    while True:
        valor = input(mensaje).strip()

        if not valor:
            print("\nEste campo no puede estar vacío.")
            continue

        return valor


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un número entero por teclado hasta que el usuario introduzca uno válido."""
    while True:
        valor = input(mensaje).strip()

        if not valor:
            print("\nDebes introducir un número.")
            continue

        try:
            numero = int(valor)
        except ValueError:
            print("\nEntrada no válida. Introduce un número entero.")
            continue

        if minimo is not None and numero < minimo:
            print(f"\nEl número debe ser mayor o igual que {minimo}.")
            continue

        if maximo is not None and numero > maximo:
            print(f"\nEl número debe ser menor o igual que {maximo}.")
            continue

        return numero


def pedir_texto_con_valor_actual(mensaje, valor_actual):
    """Pide un texto permitiendo conservar el valor actual con Enter."""
    while True:
        nuevo_valor = input(f"{mensaje} [{valor_actual}]: ").strip()

        if not nuevo_valor:
            return valor_actual

        return nuevo_valor


def pedir_entero_con_valor_actual(mensaje, valor_actual, minimo=None, maximo=None):
    """Pide un entero permitiendo conservar el valor actual con Enter."""
    while True:
        entrada = input(f"{mensaje} [{valor_actual}]: ").strip()

        if not entrada:
            return valor_actual

        try:
            numero = int(entrada)
        except ValueError:
            print("\nEntrada no válida. Introduce un número entero.")
            continue

        if minimo is not None and numero < minimo:
            print(f"\nEl número debe ser mayor o igual que {minimo}.")
            continue

        if maximo is not None and numero > maximo:
            print(f"\nEl número debe ser menor o igual que {maximo}.")
            continue

        return numero


def mostrar_libros():
    """Muestra en pantalla los libros guardados en la base de datos."""
    libros = listar_libros()
    mostrar_resultados(libros, "\nLibros guardados en la base de datos:")


def mostrar_resultados(libros, mensaje):
    """Muestra en pantalla una lista de libros con un encabezado."""
    if not libros:
        print("\nNo hay libros para mostrar.")
        return

    print(mensaje)

    for libro in libros:
        id_libro, titulo, autor, genero, anio, disponible = libro
        estado = "Sí" if disponible == 1 else "No"

        print(f"\nID: {id_libro}")
        print(f"Título: {titulo}")
        print(f"Autor: {autor}")
        print(f"Género: {genero}")
        print(f"Año: {anio}")
        print(f"Disponible: {estado}")


def pedir_datos_libro():
    """Pide por teclado los datos de un libro y los devuelve listos para guardar."""
    print("\nIntroduce los datos del libro:")
    titulo = pedir_texto_obligatorio("Título: ")
    autor = pedir_texto_obligatorio("Autor: ")
    genero = pedir_texto_obligatorio("Género: ")
    anio = pedir_entero("Año: ", minimo=ANIO_MINIMO, maximo=ANIO_MAXIMO)

    return titulo, autor, genero, anio


def pedir_cambio_disponibilidad():
    """Pide el ID del libro y su nuevo estado de disponibilidad."""
    libro_id = pedir_entero("\nIntroduce el ID del libro: ", minimo=1)
    print("\nNuevo estado:")
    print("1. Disponible")
    print("2. Prestado")

    opcion_estado = input("Elige una opción: ").strip()

    if opcion_estado == "1":
        return libro_id, 1
    if opcion_estado == "2":
        return libro_id, 0

    return libro_id, None


def ejecutar_busqueda():
    """Pide un texto de búsqueda y muestra los libros encontrados."""
    texto_busqueda = input("\nIntroduce título, autor o género a buscar: ").strip()

    if not texto_busqueda:
        print("\nDebes introducir un texto para buscar.")
        return

    resultados = buscar_libros(texto_busqueda)
    mostrar_resultados(resultados, "\nResultados de la búsqueda:")


def ejecutar_edicion():
    """Pide un ID, comprueba si existe y actualiza sus datos principales."""
    libro_id = pedir_entero("\nIntroduce el ID del libro que quieres editar: ", minimo=1)
    libro = obtener_libro_por_id(libro_id)

    if libro is None:
        print("\nNo existe ningún libro con ese ID.")
        return

    _, titulo_actual, autor_actual, genero_actual, anio_actual, _ = libro

    print("\nPulsa Enter para conservar el valor actual de cada campo.")
    print("\nEdita solo los datos que quieras cambiar:")

    titulo = pedir_texto_con_valor_actual("Título", titulo_actual)
    autor = pedir_texto_con_valor_actual("Autor", autor_actual)
    genero = pedir_texto_con_valor_actual("Género", genero_actual)
    anio = pedir_entero_con_valor_actual(
        "Año",
        anio_actual,
        minimo=ANIO_MINIMO,
        maximo=ANIO_MAXIMO
    )

    filas_actualizadas = editar_libro(libro_id, titulo, autor, genero, anio)

    if filas_actualizadas == 0:
        print("\nNo se pudo actualizar el libro.")
    else:
        print("\nLibro actualizado correctamente.")


def ejecutar_eliminacion_libro():
    """Pide un ID, muestra el libro encontrado y solicita confirmación antes de eliminarlo."""
    libro_id = pedir_entero("\nIntroduce el ID del libro que quieres eliminar: ", minimo=1)
    libro = obtener_libro_por_id(libro_id)

    if libro is None:
        print("\nNo existe ningún libro con ese ID.")
        return

    id_libro, titulo, autor, genero, anio, disponible = libro
    estado = "Sí" if disponible == 1 else "No"

    print("\nLibro encontrado:")
    print(f"\nID: {id_libro}")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Género: {genero}")
    print(f"Año: {anio}")
    print(f"Disponible: {estado}")

    while True:
        confirmacion = input("\n¿Seguro que quieres eliminar este libro? (s = sí, n = volver al menú): ").strip().lower()

        if confirmacion == "s":
            filas_afectadas = eliminar_libro(libro_id)

            if filas_afectadas == 0:
                print("\nNo se pudo eliminar el libro.")
            else:
                print("\nLibro eliminado correctamente.")
            break

        elif confirmacion == "n":
            print("\nEliminación cancelada.")
            break

        else:
            print("\nIntroduce 's' para confirmar o 'n' para volver al menú principal.")


create_table()

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ").strip()

    if opcion == "1":
        titulo, autor, genero, anio = pedir_datos_libro()
        agregar_libro(titulo, autor, genero, anio)
        print("\nLibro añadido correctamente.")

    elif opcion == "2":
        mostrar_libros()

    elif opcion == "3":
        libro_id, disponible = pedir_cambio_disponibilidad()

        if disponible is None:
            print("\nOpción de estado no válida.")
        else:
            filas_actualizadas = actualizar_disponibilidad(libro_id, disponible)

            if filas_actualizadas == 0:
                print("\nNo existe ningún libro con ese ID.")
            else:
                print("\nDisponibilidad actualizada correctamente.")

    elif opcion == "4":
        ejecutar_busqueda()

    elif opcion == "5":
        ejecutar_edicion()

    elif opcion == "6":
        ejecutar_eliminacion_libro()

    elif opcion == "0":
        print("\nHasta luego.")
        break

    else:
        print("\nOpción no válida. Intenta de nuevo.")