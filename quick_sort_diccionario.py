def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
estudiantes = {}
print("¿Cuántos estudiantes desea ingresar? ")
cantidad = int(input())
for i in range(cantidad):
    print(f"Estudiante#{i+1}")
    while True:
        carnet = input("Ingrese el carnet del estudiante: ")
        if carnet in estudiantes:
            print("Error, este estudiante ya existe")
        else:
            break