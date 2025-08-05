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
    nombre = input(f"Ingrese el nombre del estudiante: ")
    while True:
        edad = int(input("Ingrese el edad del estudiante: "))
        if edad > 0:
            break
        else:
            print("Error, ingrese una edad valida")
    carrera = input("Ingrese la carrera del estudiante: ")
    print("¿Cuántos cursos recibirá el estudiante? ")
    cant = int(input())
    for j in range(cant):
        print(f"Curso#{j + 1}")
        while True:
            clave = input("Ingrese la clave del curso: ")
            if clave in estudiantes:
                print("Error, este curso ya se ingresó")
            else:
                break
        nota_tarea = int(input("Ingrese la nota de las tareas: "))
        nota_parcial = int(input("Ingrese la nota del parcial: "))
        nota_proyecto = int(input("Ingrese la nota del proyecto: "))
    estudiantes[carnet] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "curso": {
            "codigo": clave,
            "NotaTarea": nota_tarea,
            "NotaParcial": nota_parcial,
            "NotaProyecto": nota_proyecto
        }
    }