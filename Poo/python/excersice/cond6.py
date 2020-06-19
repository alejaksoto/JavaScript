"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo
 y el nombre. El grupo A esta formado por las mujeres con un nombre anterior
  a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
   Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
    por pantalla el grupo que le corresponde."""
#SE puede hacer pruebas unitarias a este 
nombre = input('ingrese su nombre')
sexo = input('ingrese su sexo M o F')

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "a"
    else:
        grupo = "b"
else:
    if nombre.lower() >= "n":
        grupo = "a "
    else:
        grupo = "b"
print(f'tu grupo es {grupo}')
