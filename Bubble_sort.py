
def bubble_sort(lista):
    #aqui detectamos la cantidad de números de la lista
    n = len(lista)

    # Proceso del burbujeo
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista  # devolvemos la lista ordenada