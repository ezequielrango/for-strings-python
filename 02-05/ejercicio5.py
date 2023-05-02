agenda = {}

# Función para agregar una actividad a una fecha determinada
def agregar_actividad():
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    hora = input("Ingrese la hora de la actividad (HH:MM): ")
    actividad = input("Ingrese la actividad a realizar: ")
    if fecha not in agenda:
        agenda[fecha] = []
    agenda[fecha].append((hora, actividad))
    print("Actividad agregada con éxito!")

# Función para mostrar todas las actividades de la agenda
def mostrar_agenda():
    if not agenda:
        print("No hay actividades cargadas en la agenda")
    else:
        print("Agenda:")
        for fecha, actividades in agenda.items():
            print(fecha + ":")
            for hora, actividad in actividades:
                print("\t" + hora + " - " + actividad)

# Función para buscar actividades en una fecha determinada
def buscar_actividades():
    fecha = input("Ingrese la fecha a buscar (DD/MM/AAAA): ")
    if fecha in agenda:
        print("Actividades para el día", fecha)
        for hora, actividad in agenda[fecha]:
            print(hora, "-", actividad)
    else:
        print("No se encontraron actividades para la fecha ingresada")

# Menú principal del programa
while True:
    print("\nAgenda - Menú principal")
    print("1. Agregar actividad")
    print("2. Mostrar agenda completa")
    print("3. Buscar actividades por fecha")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar_actividad()
    elif opcion == "2":
        mostrar_agenda()
    elif opcion == "3":
        buscar_actividades()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
