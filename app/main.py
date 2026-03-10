from database import create_table
from crud import agregar_libro, listar_libros


def mostrar_menu():
    """Muestra las opciones disponibles en esta primera versión del programa."""
    print("\nGestor de biblioteca")
    print("1. Añadir libro")
    print("2. Listar libros")
    print("0. Salir")


def mostrar_libros():
    """Muestra en pantalla los libros guardados en la base de datos."""
    libros = listar_libros()

    if not libros:
        print("\nNo hay libros guardados.")
        return

    print("\nLibros guardados en la base de datos:")

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
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    anio = int(input("Año: "))

    return titulo, autor, genero, anio


create_table()

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        titulo, autor, genero, anio = pedir_datos_libro()
        agregar_libro(titulo, autor, genero, anio)
        print("\nLibro añadido correctamente.")

    elif opcion == "2":
        mostrar_libros()

    elif opcion == "0":
        print("\nHasta luego.")
        break

    else:
        print("\nOpción no válida. Intenta de nuevo.")