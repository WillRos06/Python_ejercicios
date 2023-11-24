catalogo = {}

while True:
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Mostrar detalles del libro")
    print("4. Listar todos los libros")
    print("5. Listar libros disponibles")
    print("6. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        isbn = input("Introduce el ISBN del libro: ")
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        genero = input("Introduce el género del libro: ")
        año = input("Introduce el año de publicación del libro: ")
        disponible = input("¿Está el libro disponible? (Sí/No): ") == "Sí"
        catalogo[isbn] = {"título": titulo, "autor": autor, "género": genero, "año": año, "disponible": disponible}
    elif opcion == 2:
        isbn = input("Introduce el ISBN del libro a eliminar: ")
        if isbn in catalogo:
            del catalogo[isbn]
        else:
            print("El libro no se encuentra en el catálogo.")
    elif opcion == 3:
        isbn = input("Introduce el ISBN del libro: ")
        if isbn in catalogo:
            detalles = catalogo[isbn]
            print("Título:", detalles["título"])
            print("Autor:", detalles["autor"])
            print("Género:", detalles["género"])
            print("Año de publicación:", detalles["año"])
            print("Disponible:", "Sí" if detalles["disponible"] else "No")
        else:
            print("El libro no se encuentra en el catálogo.")
    elif opcion == 4:
        for isbn, detalles in catalogo.items():
            print("ISBN:", isbn, "- Título:", detalles["título"])
    elif opcion == 5:
        for isbn, detalles in catalogo.items():
            if detalles["disponible"]:
                print("ISBN:", isbn, "- Título:", detalles["título"])
    elif opcion == 6:
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
