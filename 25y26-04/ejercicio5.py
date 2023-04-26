# Crear una lista vacía para almacenar los nombres de las ciudades
ciudades = []

# Solicitar al usuario que ingrese la cantidad de ciudades a ingresar
n = int(input("Ingrese la cantidad de ciudades a ingresar: "))

# Llenar la lista con los nombres de las ciudades ingresados por el usuario
for i in range(n):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append(ciudad)

# Solicitar al usuario que ingrese el nombre de una ciudad
busqueda = input("Ingrese el nombre de la ciudad que desea buscar: ")

# Buscar la posición de la ciudad en la lista utilizando el método index()
try:
    posicion = ciudades.index(busqueda)
    print("La ciudad", busqueda, "se encuentra en la posición", posicion, "de la lista.")
except ValueError:
    print("La ciudad", busqueda, "no se encuentra en la lista.")
