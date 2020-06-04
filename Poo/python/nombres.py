
man1 =input('Cual es tu nombre')
edad1 = int(input('cual es tu edad'))

man2 = input('cual es tu nombre')
edad2 = int(input('cual es tu edad'))

if edad1 > edad2:
    print(f'{man1} es mayor que {man2} por {edad1 - edad2} años')
elif edad2 > edad1:
    print(f'{man2} es mayor que {man1} por {edad2 - edad1} años')
else:
    print('tienen edad iguales')