"""El programa debe preguntar al usuario la edad del cliente y mostrar
 el precio de la entrada. Si el cliente es menor de 4 años puede 
 entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es
  mayor de 18 años, 10€."""

edad= int(input('ingrese la edad'))

if edad< 4:
    print('Cliente entra gratis')
elif edad < 18:
    print ('Cliente paga 5 E')
else:
    print ('Cliente paga 10E')
