mensaje = input("Ingrese el mensaje a procesar: ")

# Eliminar espacios en blanco de más
mensaje = " ".join(mensaje.split())

# Cortar palabras de más de cinco letras
palabras = mensaje.split()
for i in range(len(palabras)):
    if len(palabras[i]) > 5:
        palabras[i] = palabras[i][:5] + "@"

mensaje_procesado = " ".join(palabras)

print("Mensaje procesado:")
print(mensaje_procesado)
