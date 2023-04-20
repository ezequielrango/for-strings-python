randomString = input('Enter string: ')
spaces = 0
for letter in randomString:
    if (letter == ' '):
        spaces = spaces + 1

print('total spaces: ', spaces)
