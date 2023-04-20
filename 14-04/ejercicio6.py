totalTriangulos = int(input("Ingrese la cantidad de triángulos: "))
triangulosEquilateros = 0
triangulosIsosceles = 0
triangulosEscaleno = 0

counter = 1
while counter <= totalTriangulos:
    lado1 = int(input(f"Ingrese el lado 1 del triángulo {counter}: "))
    lado2 = int(input(f"Ingrese el lado 2 del triángulo {counter}: "))
    lado3 = int(input(f"Ingrese el lado 3 del triángulo {counter}: "))

    if lado1 == lado2 and lado1 == lado3:
        print(f"El triángulo {counter} es equilátero.")
        triangulosEquilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(f"El triángulo {counter} es isósceles.")
        triangulosIsosceles += 1
    else:
        print(f"El triángulo {counter} es escaleno.")
        triangulosEscaleno += 1
    
    i += 1

print(f"Cantidad de triángulos equiláteros: {triangulosEquilateros}")
print(f"Cantidad de triángulos isósceles: {triangulosIsosceles}")
print(f"Cantidad de triángulos escalenos: {triangulosEscaleno}")