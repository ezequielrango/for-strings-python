# Creamos un diccionario vacío para almacenar las palabras en inglés y sus traducciones al español
diccionario = {}

# Pedimos al usuario que ingrese las palabras en inglés y sus traducciones al español
while True:
    palabra_ingles = input("Ingrese una palabra en inglés (o 'fin' para terminar): ")
    if palabra_ingles == "fin":
        break
    palabra_espanol = input("Ingrese la traducción al español de la palabra '%s': " % palabra_ingles)
    diccionario[palabra_ingles] = palabra_espanol

# Mostramos el diccionario completo
print("Diccionario completo:")
for palabra_ingles, palabra_espanol in diccionario.items():
    print("%s -> %s" % (palabra_ingles, palabra_espanol))

# Pedimos al usuario que ingrese una palabra en inglés para buscar su traducción
palabra_buscar = input("Ingrese una palabra en inglés para buscar su traducción: ")

# Buscamos la palabra en el diccionario y mostramos su traducción si la encontramos
if palabra_buscar in diccionario:
    palabra_espanol = diccionario[palabra_buscar]
    print("La traducción de '%s' es '%s'" % (palabra_buscar, palabra_espanol))
else:
    print("La palabra '%s' no se encuentra en el diccionario" % palabra_buscar)
