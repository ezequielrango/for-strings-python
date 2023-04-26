# Crear dos listas vacías para almacenar los nombres de los productos y sus precios
productos = []
precios = []

# Solicitar al usuario que ingrese la cantidad de productos a ingresar
n = int(input("Ingrese la cantidad de productos a ingresar: "))

# Llenar las listas con los nombres de los productos y sus precios ingresados por el usuario
for i in range(n):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append(producto)
    precios.append(precio)

# Obtener el precio del primer producto ingresado
primer_precio = precios[0]

# Contar cuantos productos tienen un precio mayor al primer producto ingresado
contador = 0
for i in range(1, len(precios)):
    if precios[i] > primer_precio:
        contador += 1

# Imprimir el resultado
print("Hay", contador, "productos con un precio mayor al primer producto ingresado.")
