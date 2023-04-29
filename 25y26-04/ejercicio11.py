# Punto a
n = int(input("Ingrese la cantidad de países: "))
temperaturas = {}
for i in range(n):
    pais = input("Ingrese el nombre del país: ")
    temps = []
    for j in range(3):
        temp = float(input(f"Ingrese la temperatura media del mes {j+1}: "))
        temps.append(temp)
    temperaturas[pais] = temps

# Punto b
print("Países y temperaturas medias mensuales:")
for pais, temps in temperaturas.items():
    print(f"{pais}: {temps}")

# Punto c
temperaturas_trimestrales = {}
for pais, temps in temperaturas.items():
    temp_trimestral = sum(temps) / 3
    temperaturas_trimestrales[pais] = temp_trimestral

# Punto d
pais_max_temp = max(temperaturas_trimestrales, key=temperaturas_trimestrales.get)

# Punto e
print("Países y temperaturas medias trimestrales:")
for pais, temp_trimestral in temperaturas_trimestrales.items():
    print(f"{pais}: {temp_trimestral}")
    
print(f"El país con la temperatura media trimestral mayor es: {pais_max_temp}")
