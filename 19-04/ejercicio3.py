cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if subcadena in cadena:
    print("La subcadena '{}' se encuentra en la cadena.".format(subcadena))
else:
    print("La subcadena '{}' no se encuentra en la cadena.".format(subcadena))