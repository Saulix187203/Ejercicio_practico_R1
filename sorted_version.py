


def sorted_version(lista):
    """
    Ordena una lista usando la función integrada sorted() de Python.
    Esta función usa el algoritmo Timsort, que es mucho más eficiente que Bubble Sort.
    """
    return sorted(lista)

if __name__ == "__main__":
    # Lista de ejemplo para probar el funcionamiento
    ejemplo = [5, 2, 9, 1, 5]
    print("Antes:", ejemplo)
    print("Ordenado con sorted():", sorted_version(ejemplo.copy()))
