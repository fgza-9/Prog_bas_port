def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menos = [x for x in arr[1:] if x <= pivot]
    mayor = [x for x in arr[1:] if x > pivot]
    return quicksort(menos) + [pivot] + quicksort(mayor)

def busqueda_binaria(arr, objetivo):
    bajo, alto = 0, len(arr) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

def generar_aleatorios(n, minimo=1, maximo=100):
    lista = []
    for _ in range(n):
        num = minimo + (hash(str(_)) % (maximo - minimo + 1))
        lista.append(num)
    return lista

n = int(input("Ingresa el tamaño de la lista: "))
lista = generar_aleatorios(n)
print(f"\nLista antes de ordenar: {lista}")
lista_ordenada = quicksort(lista)
print(f"Lista después de ordenar: {lista_ordenada}")
objetivo = int(input("\nIngresa un número para buscar en la lista: "))
indice = busqueda_binaria(lista_ordenada, objetivo)
if indice != -1:
    print(f"El número {objetivo} fue encontrado en el índice {indice}.")
else:
    print(f"El número {objetivo} no se encuentra en la lista.")
