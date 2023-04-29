# Ingreso de datos
n = int(input("Ingrese la cantidad de alumnos: "))
nombres = []
notas = []
for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    nombres.append(nombre)
    notas.append(nota)

# Listado de alumnos con su nota y condición
for i in range(n):
    if notas[i] >= 8:
        condicion = "Muy Bueno"
    elif notas[i] >= 4:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    print(f"{nombres[i]} tiene una nota de {notas[i]} y su condición es {condicion}")

# Cálculo de cantidad de alumnos con "Muy Bueno"
muy_buenos = 0
for nota in notas:
    if nota >= 8:
        muy_buenos += 1
print(f"Hay {muy_buenos} alumnos con 'Muy Bueno'")
