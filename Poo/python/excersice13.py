"""Ejercicio 13
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
  Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
  introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
   segundo y tercer años. Redondear cada cantidad a dos decimales."""
Ahorro = int(input('ingresa el valor a ahorrar'))
Primer = float(Ahorro+(Ahorro*0.03))
segundo = Primer +(Ahorro*0.03)
tercero = segundo +(Ahorro*0.03)

print(f'se tiene en el primer año {Primer}\n, para el año dos se tiene {segundo}\n, para el año tres')
