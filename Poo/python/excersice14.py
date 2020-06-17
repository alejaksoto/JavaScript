"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
 Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
  y el coste final total."""
pan = 3.94
desc =float(pan*0.6)
hoy = pan - desc
vendidas = int(input('ingrese barras vendidas'))

print(f'fueron vendidas ayer {vendidas} por un valor de {pan},que valen {pan*vendidas} las vendidas hoy tienen un descuento de {desc}\n, que hoy un pan vale {hoy} ')
