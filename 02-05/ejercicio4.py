# Creamos un diccionario vacío para almacenar los datos de los productos
productos = {}

# Pedimos al usuario que ingrese los datos de los productos
while True:
    codigo = input("Ingrese el código del producto (o 'fin' para terminar): ")
    if codigo == "fin":
        break
    nombre = input("Ingrese el nombre del producto con código '%s': " % codigo)
    precio = float(input("Ingrese el precio del producto con código '%s': " % codigo))
    stock = int(input("Ingrese el stock del producto con código '%s': " % codigo))
    productos[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}

# Mostramos el listado completo de productos
print("Listado completo de productos:")
for codigo, datos in productos.items():
    nombre = datos["nombre"]
    precio = datos["precio"]
    stock = datos["stock"]
    print("%s -> %s ($%.2f, %d unidades)" % (codigo, nombre, precio, stock))

# Pedimos al usuario que ingrese el código de un producto para buscar su información
codigo_buscar = input("Ingrese el código de un producto para buscar su información: ")

# Buscamos el producto en el diccionario y mostramos su información si lo encontramos
if codigo_buscar in productos:
    nombre = productos[codigo_buscar]["nombre"]
    precio = productos[codigo_buscar]["precio"]
    stock = productos[codigo_buscar]["stock"]
    print("El producto con código '%s' es '%s' ($%.2f, %d unidades en stock)" % (codigo_buscar, nombre, precio, stock))
else:
    print("El producto con código '%s' no se encuentra en el diccionario" % codigo_buscar)

# Mostramos el listado de productos con stock cero
print("Listado de productos con stock cero:")
for codigo, datos in productos.items():
    if datos["stock"] == 0:
        nombre = datos["nombre"]
        precio = datos["precio"]
        print("%s -> %s ($%.2f)" % (codigo, nombre, precio))
