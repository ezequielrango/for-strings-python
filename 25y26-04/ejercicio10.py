n = int(input("Ingrese la cantidad de empleados: "))

nombres = []
ingresos = []

# Carga de los nombres y sueldos de cada empleado
for i in range(n):
    nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
    sueldos = []
    for j in range(3):
        sueldo = float(input(f"Ingrese el sueldo del mes {j+1} de {nombre}: "))
        sueldos.append(sueldo)
    nombres.append(nombre)
    ingresos.append(sueldos)

# Generación de la lista de ingresos acumulados de cada empleado
ingresos_acum = []
for sueldos in ingresos:
    acumulado = sum(sueldos)
    ingresos_acum.append(acumulado)

# Mostrar el total pagado en sueldos a cada empleado en los últimos 3 meses
print("Total pagado en sueldos en los últimos 3 meses:")
for i in range(n):
    print(f"{nombres[i]}: {ingresos_acum[i]}")

# Obtener el nombre del empleado con mayor ingreso acumulado
indice_max = ingresos_acum.index(max(ingresos_acum))
print(f"El empleado con mayor ingreso acumulado es: {nombres[indice_max]}")
