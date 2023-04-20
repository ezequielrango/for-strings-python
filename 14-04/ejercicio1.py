email = input('enter email: ')
hasArroba = False
for l in email:
    if (l == '@'):
        hasArroba = True
        break

if (hasArroba):
    print('Email valid')
else:
    print('Email invalid')
