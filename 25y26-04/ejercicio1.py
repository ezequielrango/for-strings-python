numeros = []

while True:
    num = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
    if num == 0:
        break
    numeros.append(num)

print("La lista contiene", len(numeros), "elementos.")
