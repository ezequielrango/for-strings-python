# Creamos un diccionario vacío para almacenar los datos de los empleados
empleados = {}

# Pedimos al usuario que ingrese los datos de cada empleado
for i in range(5):
    nombre = input("Ingrese el nombre del empleado %d: " % (i+1))
    sueldos = []
    for j in range(3):
        sueldo = int(input("Ingrese el sueldo %d del empleado %s: " % (j+1, nombre)))
        sueldos.append(sueldo)
    empleados[nombre] = sueldos

# Pedimos al usuario que ingrese el nombre de un empleado para buscar sus sueldos
nombre_buscar = input("Ingrese el nombre del empleado para buscar sus sueldos: ")

# Buscamos al empleado en el diccionario y mostramos sus sueldos si lo encontramos
if nombre_buscar in empleados:
    sueldos = empleados[nombre_buscar]
    print("Los sueldos de %s son: %s" % (nombre_buscar, str(sueldos)))
else:
    print("El empleado %s no se encuentra en la lista" % nombre_buscar)
