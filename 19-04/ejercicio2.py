cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

if caracter.isalpha():
    count = cadena.count(caracter)
    print("El caracter '{}' aparece {} veces en la cadena.".format(caracter, count))
else:
    print("El caracter introducido no es alfabético.")

# cadena = input("Introduce una cadena: ")

# if cadena.isdigit():
#     print("La cadena sólo contiene dígitos.")
# else:
#     print("La cadena no contiene sólo dígitos.")