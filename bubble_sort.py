def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == "__main__":
    ejemplo = [5, 2, 9, 1, 5]
    print("Antes:", ejemplo)
    print("Ordenado:", bubble_sort(ejemplo.copy()))
