"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

#n = 10
#for i in range(n):
#   print(n*(i+1))

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")