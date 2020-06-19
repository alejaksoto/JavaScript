"""Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4,
    0.6 o más, pero no valores intermedios entre las cifras 
    mencionadas. La cantidad de dinero conseguida en cada nivel es
     de 2.400€ multiplicada por la      puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique
 su nivel de rendimiento, así como la cantidad de dinero que recibirá
  el usuario."""
puntaje = float(input('cual es tu puntuación'))

if puntaje == 0:
    cantidad = puntaje
elif puntaje == 0.4:
    cantidad = puntaje* 0.4
elif puntaje == 0.6:
    cantidad = puntaje * 0.6
else:
    print('No ingresaste una puntuación valida')

print(f'nivel de rendimiento{puntaje}\n, cantidad de dinero que va a recibir {cantidad*10000} ')

