"""Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

num = int(input('ingrese un numero'))
interes = int(input('ingrese el interes'))
años = int(input('ingrese el # de años'))
interes = interes/100
total1 = num*interes
for i in range(1, años):
    total2 = (total1+num)*i
    print(f'se encuentra que se tiene una rentabilidad {total2}')