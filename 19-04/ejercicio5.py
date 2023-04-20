numero = input("Introduce un número de teléfono en el formato prefijo-número-extensión: ")

prefijo = "+54"
extension = "00"

if numero.count("-") == 2:  # comprobar que la cadena tiene el formato esperado
    partes = numero.split("-")
    numero = partes[1]
    num_completo = [prefijo, numero, extension]
    num_completo_str = "-".join(num_completo)
    print("El número de teléfono completo es:", num_completo_str)
else:
    print("El número de teléfono no tiene el formato esperado.")
