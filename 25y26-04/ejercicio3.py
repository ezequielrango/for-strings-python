frase = input("Ingrese una frase: ")

# Eliminar espacios en blanco al principio y al final de la frase
frase = frase.strip()

# Separar la frase en palabras utilizando el método split()
palabras = frase.split()

print("La frase ingresada se ha transformado en la siguiente lista de palabras:", palabras)
