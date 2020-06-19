"""sistema de pizza"""

seleccion =int(input('selecciona 1:vegetariana o 2:No vegetarianos'))

if seleccion ==1:
    print('El cliente selecciono Vegetariana con')
    ingredietes = int (input('1:Pimiento ,2: tofu'))
    if ingredietes ==1:
        print(' con Pimiento')
    else:
        print(' con Tofu')
else :
    print('El cliente selecciono Carne con')
    ingredietes = int (input('1:Peperoni, 2:Jamón, 3:Salmón.'))
     if ingredietes ==1:
        print(' con peperoni')
    elif:
        print(' con Jamon')
    else:
        print(' con salmon')


