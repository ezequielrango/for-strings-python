totalPersonas = int(input('ingrese total personas:'))
counter = 0

while counter <= totalPersonas:
    name = input('Enter name: ').upper()

    if (name[0] in ['A', 'E', 'I', 'O', 'U']):
        print('His name start with vocal:', name)

    counter += 1
