# Crear dos listas vacías para almacenar los nombres de los países y sus poblaciones
paises = []
poblaciones = []

# Solicitar al usuario que ingrese la cantidad de países a ingresar
n = int(input("Ingrese la cantidad de países a ingresar: "))

# Llenar las listas con los nombres de los países y sus poblaciones ingresados por el usuario
for i in range(n):
    pais = input("Ingrese el nombre del país: ")
    poblacion = int(input("Ingrese la población del país: "))
    paises.append(pais)
    poblaciones.append(poblacion)

# Utilizar el algoritmo de ordenamiento para ordenar las listas de mayor a menor por cantidad de habitantes
for i in range(len(poblaciones)):
    for j in range(i + 1, len(poblaciones)):
        if poblaciones[i] < poblaciones[j]:
            # Intercambiar los elementos de la lista de poblaciones
            poblaciones[i], poblaciones[j] = poblaciones[j], poblaciones[i]
            # Intercambiar los elementos de la lista de países correspondientes
            paises[i], paises[j] = paises[j], paises[i]

# Imprimir la lista de países y sus poblaciones ordenadas de mayor a menor por cantidad de habitantes
print("Países ordenados por cantidad de habitantes (de mayor a menor):")
for i in range(len(paises)):
    print(paises[i], "-", poblaciones[i])
