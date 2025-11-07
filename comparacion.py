import random
import time
from Bubble_sort import bubble_sort   # importamos el algoritmo del otro archivo

# Función para medir el tiempo de ejecución de un algoritmo
def medir_tiempo(funcion, lista):
    inicio = time.perf_counter()
    funcion(lista.copy())  # usamos una copia para no modificar la original
    fin = time.perf_counter()
    return fin - inicio

# Tamaños de listas que se van a probar
tamaños = [100, 500, 1000, 5000]

print("Comparación de tiempos entre Bubble Sort y sorted() en Python:\n")
print(f"{'n':<10} {'BubbleSort (s)':<20} {'sorted() (s)':<20}")

# Ciclo para probar con cada tamaño
for n in tamaños:
    lista = [random.randint(1, 10000) for _ in range(n)]

    tiempo_bubble = medir_tiempo(bubble_sort, lista)
    tiempo_sorted = medir_tiempo(sorted, lista)

    print(f"{n:<10} {tiempo_bubble:<20.5f} {tiempo_sorted:<20.5f}")

# Conclusión final
print("\n✅ Prueba completada. Puedes copiar los resultados al archivo 'analisis.md' o 'resultados.txt'.")
