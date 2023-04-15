randomString= input('insert text here: ')
vocals= 0

for letter in randomString:
    if(letter == 'a' or letter == 'e'):
        vocals = vocals + 1
    elif(letter == 'i' or letter == 'o'):
        vocals = vocals + 1
    elif(letter == 'u'):
        vocals = vocals + 1

print('Total vocals: ', vocals)
