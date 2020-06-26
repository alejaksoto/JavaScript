"""pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
word = str(input('ingresa tu palabra'))
x = 0 
while x < 10:
    print(f'la palabra que ingresaste es {word}')
    x=x+1