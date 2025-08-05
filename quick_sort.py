def quick_sort(lista):
    print("¿Cuántos nombres desea ingresar?: ")
    cantidad = int(input())
    for i in range (cantidad):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
