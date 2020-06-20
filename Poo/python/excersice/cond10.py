"""sistema de pizza"""

seleccion =int(input('selecciona 1:vegetariana o 2:No vegetarianos'))

if seleccion ==1:
    
    ingredietes = int (input('1:Pimiento ,2: tofu'))
    if ingredietes ==1:
        print('El cliente selecciono Vegetariana con')
        print(' Pimiento')
    else:
        print('El cliente selecciono Vegetariana con')
        print(' Tofu')
else :
    
    ingredietes = int (input('1:Peperoni, 2:Jamón, 3:Salmón.'))
    if ingredietes ==1:
        print('El cliente selecciono Carne con')
        print(' peperoni')
    elif ingredietes ==2:
        print('El cliente selecciono Carne con')
        print(' Jamon')
    else:
        print('El cliente selecciono Carne con')
        print(' salmon')


