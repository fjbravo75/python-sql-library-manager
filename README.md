# Python SQL Library Manager

Aplicación de consola desarrollada en Python para gestionar una biblioteca sencilla usando SQLite como base de datos.

## Tecnologías utilizadas

- Python 3
- SQLite
- SQL
- Git y GitHub

## Funcionalidades

- Añadir libros a la base de datos
- Listar todos los libros guardados
- Buscar libros por título, autor o género
- Editar los datos principales de un libro
- Cambiar la disponibilidad de un libro
- Eliminar libros con confirmación previa

## Estructura del proyecto

```bash
python-sql-library-manager/
├── app/
│   ├── main.py
│   ├── crud.py
│   └── database.py
├── data/
│   └── library.db
├── .gitignore
└── README.md
```

## Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el proyecto.
2. Abre una terminal en la carpeta `app`.
3. Ejecuta el archivo principal con:

```bash
python main.py
```


## Menú principal

Al ejecutar la aplicación, el usuario puede elegir entre estas opciones:

- Añadir libro
- Listar libros
- Cambiar disponibilidad
- Buscar libros
- Editar libro
- Eliminar libro
- Salir

## Qué demuestra este proyecto

Este proyecto demuestra conocimientos básicos de:

- programación en Python
- organización modular del código
- conexión con SQLite
- operaciones CRUD
- validación de entradas por consola
- uso básico de Git y GitHub

## Estado del proyecto

Versión funcional inicial terminada, con operaciones CRUD completas sobre una base de datos SQLite y flujo de interacción por consola.

## Mejoras futuras

- añadir validaciones más avanzadas
- mejorar la gestión de errores
- incorporar pruebas automáticas
- separar mejor responsabilidades en módulos auxiliares
- preparar una versión con interfaz web usando Django o Flask