def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
print("¿Cuántos nombres desea ingresar?: ")
cantidad = int(input())
estudiantes = []
for i in range (cantidad):
    print(f"Estudiante #{i+1}: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)
resultado = quick_sort(estudiantes)
print(resultado)