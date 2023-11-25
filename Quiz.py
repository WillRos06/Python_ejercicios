opcion = int(input("Ingrese el número del ejercicio que desea ver: "))

if opcion == 1:
    n = int(input("Ingrese la cantidad de números para la lista: "))
    lista = []

    for i in range(n):
        numero = int(input(f"Ingrese el número para la posición {i}: "))
        lista.append(numero)

    def ordenar_lista(lista):
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
        return lista

    lista_ordenada = ordenar_lista(lista[:])

    print("La lista ordenada: ", lista_ordenada)
    
elif opcion == 2:
    # Ejercicio 2
    def eliminar_duplicados(lista):
        lista_sin_duplicados = []
        for numero in lista:
            if numero not in lista_sin_duplicados:
                lista_sin_duplicados.append(numero)
            return lista_sin_duplicados

    n = int(input("Ingrese la cantidad de números para la lista: "))
    lista = []

    for i in range(n):
        numero = int(input(f"Ingrese el número para la posición {i}: "))
        lista.append(numero)

    lista_sin_duplicados = eliminar_duplicados(lista)

    print("Se han removido los duplicados de la lista suministrada: ", lista_sin_duplicados)




