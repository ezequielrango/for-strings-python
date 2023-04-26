# Función para ordenar la lista utilizando el algoritmo de selección
def ordenar_lista(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Crear y cargar la lista de sueldos
sueldos = []
n = int(input("Ingrese la cantidad de sueldos a ingresar: "))
for i in range(n):
    sueldo = float(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)

# Ordenar la lista de sueldos
ordenar_lista(sueldos)

# Imprimir la lista ordenada
print("Lista ordenada de sueldos:", sueldos)

# Contar cuántos sueldos son mayores a 25000
contador = 0
for sueldo in sueldos:
    if sueldo > 25000:
        contador += 1

print("Hay", contador, "sueldos mayores a $25000.")
