"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""
Dividendo= int(input('ingrese numero 1'))
divisor = int(input('ingrese numero 2'))

if divisor == 0:
    print('Error controlado, no se puede restar')
else:
    division = Dividendo/divisor
    print(f'el resultado de la division es {division}')
