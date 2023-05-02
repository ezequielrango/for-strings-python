# Creamos un diccionario vacío para almacenar los datos de los candidatos
candidatos = {}

# Pedimos al usuario que ingrese los datos de cada candidato
while True:
    nombre = input("Ingrese el nombre del candidato (o 'q' para salir): ")
    if nombre == 'q':
        break
    
    # Creamos una lista vacía para almacenar las provincias y votos del candidato
    provincias = []
    
    # Pedimos al usuario que ingrese los datos de cada provincia
    while True:
        provincia = input("Ingrese el nombre de la provincia (o 'q' para salir): ")
        if provincia == 'q':
            break
        votos = int(input("Ingrese la cantidad de votos obtenidos en %s: " % provincia))
        # Creamos una tupla con la provincia y la cantidad de votos y la agregamos a la lista de provincias
        provincias.append((provincia, votos))
    
    # Agregamos al candidato al diccionario con su lista de provincias y votos
    candidatos[nombre] = provincias

# Imprimimos el nombre de cada candidato y la cantidad total de votos obtenidos
for nombre, provincias in candidatos.items():
    total_votos = sum(votos for provincia, votos in provincias)
    print("%s obtuvo un total de %d votos" % (nombre, total_votos))
