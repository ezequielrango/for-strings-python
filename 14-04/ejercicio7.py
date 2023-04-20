userName = input("Ingrese un nombre de usuario (entre 6 y 12 caracteres): ")
while len(userName) < 6 or len(userName) > 12:
    userName = input("El nombre de usuario debe contener entre 6 y 12 caracteres. Ingrese otro nombre de usuario: ")

password = input("Ingrese una contraseña (mínimo 8 caracteres, sin espacios en blanco): ")
while len(password) < 8 or " " in password:
    password = input("La contraseña debe contener al menos 8 caracteres y no puede tener espacios en blanco. Ingrese otra contraseña: ")

print("Las credenciales son válidas.")
